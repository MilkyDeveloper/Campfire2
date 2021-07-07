Welcome to the Campfire2 Project! Campfire2 is more modern than Crouton, more flexible than Crostini, and uses Chromebrew, a wonderful package manager for ChromeOS.


https://user-images.githubusercontent.com/48262994/124794415-9bbb1080-df14-11eb-850e-be174740472b.mp4

# Installing Campfire2
1. Install Chromebrew: `curl -Ls git.io/vddgY | bash`
2. Download/extract/configure the Ubuntu (20.04) Chroot:
```
crew install micro xterm xhost libunwind && echo "Downloading Ubuntu RootFS..." && curl --verbose -o /usr/local/ubuntu.tar.xz "https://cloud-images.ubuntu.com/minimal/releases/focal/release-20210625/ubuntu-20.04-minimal-cloudimg-amd64-root.tar.xz" && sudo rm -rf /usr/local/ubuntu; mkdir /usr/local/ubuntu && sudo tar -xvf /usr/local/ubuntu.tar.xz -C /usr/local/ubuntu && sudo rm /usr/local/ubuntu.tar.xz /usr/local/ubuntu/etc/resolv.conf && sudo mkdir /usr/local/ubuntu/root/Downloads && sudo cp /etc/resolv.conf /usr/local/ubuntu/etc/resolv.conf && startsommelier && echo "Done!"
```
3. Make a command to start Ubuntu: `sudo micro /usr/local/bin/startubuntu` and paste in (<kbd>CTRL</kbd> <kbd>SHIFT</kbd> <kbd>V</kbd>):
```
#!/bin/bash
xhost + > /dev/null
mount -t proc /proc /usr/local/ubuntu/proc/
mount --rbind /sys /usr/local/ubuntu/sys/
mount --rbind /dev /usr/local/ubuntu/dev/
if [ -z "$1" ]
then
      DISPLAY=:0 chroot /usr/local/ubuntu /bin/bash
else
      DISPLAY=:0 chroot /usr/local/ubuntu /bin/bash “$@”
fi
umount -lf /usr/local/ubuntu/proc/
umount -lf /usr/local/ubuntu/sys/
umount -lf /usr/local/ubuntu/dev/
```  
Save it with <kbd>CTRL</kbd> <kbd>Q</kbd> and make it executable by running: `sudo chmod +x /usr/local/bin/startubuntu`. Run `sudo startubuntu` to start the chroot.

## Extras
### Audio
1. <kbd><img height="15" width="75" src="https://assets.ubuntu.com/v1/048f7fde-ubuntu_black-orange_hex.jpg"></img></kbd> Install Pulseaudio and Apulse: `apt update && apt upgrade && apt install alsa alsa-tools apulse`
2. Run `speaker-test` (you may need to run it twice for it to work)

PulseAudio is complicated and is often considered bloated. A tool called Apulse is a much better alternative, creating a compatibility layer between PulseAudio libraries and ALSA. 99% of PulseAudio apps will work with Apulse. You can use Apulse by putting `apulse` before your command.
