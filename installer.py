import bs4 as bs
import urllib.request
import progressbar
import os
import os.path
import json
import zipfile

# Install pv, tar, cgpt, and sgdisk (all dependencies for brunch)
os.system('crew install gptfdisk pv cgpt')

# Variables
latestBrunchReleaseJSON = json.loads(urllib.request.urlopen('https://api.github.com/repos/sebanc/brunch-unstable/releases').read())
version = int(latestBrunchReleaseJSON[0]['assets'][0]['name'].split('_')[1].replace('r', ''))
latestBrunchDownload    = latestBrunchReleaseJSON[0]['assets'][0]['browser_download_url']
board   = input("What is your ChromeOS Board Name? ") # ChromeOS Board Name

# Progress Bar Function for downloading files
pbar = None
def progressBar(block_num, block_size, total_size):
    global pbar
    if pbar is None:
        pbar = progressbar.ProgressBar(maxval=total_size)
        pbar.start()

    downloaded = block_num * block_size
    if downloaded < total_size:
        pbar.update(downloaded)
    else:
        pbar.finish()
        pbar = None

# Download the recovery image if it doesn't exist
if not os.path.exists('recovery.zip'):

    # Firstly, we need to scrape the ChromeOS Recovery Images from the cros-updates-serving page.
    # This is fairly simple because the webpage is just a big table.

    # Convert the page to beautiful soup
    print("Downloading the ChromeOS Recovery Image Webpage...")
    source = urllib.request.urlopen('https://cros-updates-serving.appspot.com/').read()
    soup = bs.BeautifulSoup(source, 'lxml')

    # Get the recovery image (given the CrOS Version and the board name)
    recoveryImageUrl = soup.find(id=board).findChildren('td')[-2].findChildren('a', text=str(version))[0]['href']

    # Download the file
    print("Downloading the recovery. Please wait a few minutes.")
    urllib.request.urlretrieve(recoveryImageUrl, 'recovery.zip', progressBar)

# See the contents of the zip file
zip = zipfile.ZipFile('recovery.zip')
recoveryFilename = zip.namelist()[0]

# Unzip the recovery
print('Unzipping the recovery...')
os.system('unzip recovery.zip')
os.rename(recoveryFilename, 'recovery.bin')

# Download the latest brunch_unstable release (brunch_unstable contains the special kernel needed)
print("Downloading the brunch tarball.")
urllib.request.urlretrieve(latestBrunchDownload, 'brunch.tar.gz', progressBar)

# Unzip the brunch_unstable tarball
print("Unzipping the brunch tarball.")
os.system('tar xvf brunch.tar.gz')

# Now download/extract the MBR Patch
print("Downloading the MBR Patch")
urllib.request.urlretrieve('https://github.com/sebanc/brunch/raw/master/mbr_support.tar.gz', 'brunch_mbr.tar.gz', progressBar)
os.system('tar xvf brunch_mbr.tar.gz')

# Finally, run the script to generate the bootable image
os.system('sudo bash chromeos-install.sh -src recovery.bin -dst BrunchChromeOS.bin')
