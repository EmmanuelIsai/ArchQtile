#! /bin/bash
#====================================================================
# Instala los paquetes necesarios para funcionamiento del archivo de
# configuracion 

cd $HOME
sudo pacman -Syu
sudo pacman -S firefox rofi which nitrogen pipewire ttf-dejavu
sudo pacman -S ttf-liberation noto-fonts pavucontrol pamixer arandr
sudo pacman -S ntfs-3g network-manager-applet xorg-xinit base-devel
sudo pacman -S git pcmanfm glib2 gvfs lxappearance picom alacritty curl
sudo pacman -S scrot python-psutil papirus-icon-theme gtk3 arc-gtk-theme
sudo pacman -S lightdm lightdm-gtk-greeter xorg-server-xephyr brightnessctl

mkdir Imagenes
curl -O https://r4.wallpaperflare.com/wallpaper/625/89/275/archlinux-digital-art-linux-arch-linux-tech-hd-wallpaper-1f0cb881ced8a6f444c7620593386e99.jpg
mv archlinux-digital-art-linux-arch-linux-tech-hd-wallpaper-1f0cb881ced8a6f444c7620593386e99.jpg Imagenes
curl -O https://images2.alphacoders.com/122/1224122.png
sudo cp 1224122.png /usr/share/pixmaps/ 
mv 1224122.png Imagenes

mkdir .iconos
curl -O https://img.icons8.com/material/96/FFFFFF/shutdown--v1.png
curl -O https://img.icons8.com/material/96/FFFFFF/reboot.png
curl -O https://img.icons8.com/material/96/FFFFFF/lock--v1.png
mv shutdown--v1.png shutdown.png
mv lock--v1.png lock.png
mv shutdown.png .iconos/
mv lock.png .iconos/
mv reboot.png .iconos/

mkdir ~/.config/alacritty/
curl -O https://gitlab.com/dwt1/dotfiles/-/raw/master/.config/alacritty/alacritty.yml
mv alacritty.yml .config/alacritty/ 

mkdir ~/.config/picom/
cp /etc/xdg/picom.conf ~/.config/picom/

cd $HOME
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si

cd $HOME
# Instala los extras necesarios de AUR y git para el funcionamiento del archivo config.py
sudo pacman -Syu
yay -Syu
# Instala qtile extras para agregar modificaciones visuales a qtile
yay -Sqtile-extras-git ttf-nerd-fonts-symbols-2048-em-mono ttf-ubuntu-mono-nerd ttf-nerd-fonts-symbols-common

cd $HOME
# Instala temas para el menu de aplicaciones rofi
git clone --depth=1 https://github.com/adi1090x/rofi.git
cd rofi
chmod +x setup.sh
./setup.sh

#cd $HOME
# Instala oh my bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/install.sh)"
