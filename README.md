https://user-images.githubusercontent.com/48262994/124794415-9bbb1080-df14-11eb-850e-be174740472b.mp4

# About Campfire2
| Hardware Support    | Campfire2                                           | Crouton                        | Crostini                                       |
|---------------------|-----------------------------------------------------|--------------------------------|------------------------------------------------|
| Internal Display    | Yes                                                 | Yes (sommelier is not working) | Yes                                            |
| External Display    | Yes                                                 | Mostly                         | Yes                                            |
| Touchpad            | Yes                                                 | Mostly                         | Yes                                            |
| Touchscreen         | Yes                                                 | Mostly                         | Yes                                            |
| WiFi                | Yes                                                 | Yes                            | Yes                                            |
| 3D Acceleration     | Yes (Can be used for gaming!)                       | Mostly                         | Yes (but using slower VirGL)                   |
| Audio               | Mostly                                              | Mostly                         | Mostly                                         |
| Camera              | Yes                                                 | Yes                            | Yes                                            |
| Microphone          | No                                                  | Sometimes                      | Yes                                            |
| USB                 | Yes                                                 | Yes                            | No direct USB Access                           |
| Suspending/Resuming | No (sommelier does not persist when suspending)     | Yes                            | Yes                                            |
| KVM Virtualization  | Yes                                                 | Yes                            | No (Not available on all chromebooks and slow) |

## Performance
Campfire2 and Crouton's performance are similar. The only reason to change from Crouton are Quality-of-Life improvements and maintenance. Basically, Campfire2 has the performance of Crouton but the reliability and GUI (known as Sommelier) of Crostini.

Crostini gets around ~17.5 FPS on default Minecraft using the (still very impressive!) VirGL drivers. On the other hand, using `i965` and Mesa gives ~25 fps. Chromebooks released in 2019 can utilize a newer kernel and the new Gallium3d drivers, which would probably offer around ~30 fps.

# Installing Campfire2
1. Install Chromebrew: `curl -Ls git.io/vddgY | bash`
2. Download/extract/configure the Ubuntu (20.04) Chroot:
```
crew install xterm xhost libunwind && echo "Downloading Ubuntu RootFS..." && curl --verbose -o /usr/local/ubuntu.tar.xz "https://cloud-images.ubuntu.com/minimal/releases/focal/release-20210625/ubuntu-20.04-minimal-cloudimg-amd64-root.tar.xz" && sudo rm -rf /usr/local/ubuntu; mkdir /usr/local/ubuntu && sudo tar -xvf /usr/local/ubuntu.tar.xz -C /usr/local/ubuntu && sudo rm /usr/local/ubuntu.tar.xz /usr/local/ubuntu/etc/resolv.conf && sudo mkdir /usr/local/ubuntu/root/Downloads && sudo cp /etc/resolv.conf /usr/local/ubuntu/etc/resolv.conf && sudo curl https://raw.githubusercontent.com/MilkyDeveloper/Campfire2/main/startubuntu -o /usr/local/bin/startubuntu && sudo chmod 755 /usr/local/bin/startubuntu && startsommelier && echo "Done!"
```
Run `sudo startubuntu` to start the chroot.

## Extras
### Audio
1. <kbd><img height="15" width="75" src="https://assets.ubuntu.com/v1/048f7fde-ubuntu_black-orange_hex.jpg"></img></kbd> Install Pulseaudio and Apulse: `apt update && apt upgrade && apt install alsa alsa-tools apulse`
2. Run `speaker-test` (you may need to run it twice for it to work)

PulseAudio is complicated and is often considered bloated. A tool called Apulse is a much better alternative, creating a compatibility layer between PulseAudio libraries and ALSA. 99% of PulseAudio apps will work with Apulse. You can use Apulse by putting `apulse` before your command.
