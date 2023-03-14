#! /bin/bash
#====================================================================
# Instala los paquetes necesarios para funcionamiento del archivo de
# configuracion 

sudo pacman -Syu
sudo pacman -S code firefox rofi which nitrogen pipewire ttf-dejavu
sudo pacman -S ttf-liberation noto-fonts pavucontrol pamixer arandr
sudo pacman -S ntfs-3g network-manager-applet xorg-xinit base-devel
sudo pacman -S git pcmanfm glib2 gvfs lxappearance picom alacritty curl
sudo pacman -S scrot

mkdir Imagenes
curl -O https://r4.wallpaperflare.com/wallpaper/625/89/275/archlinux-digital-art-linux-arch-linux-tech-hd-wallpaper-1f0cb881ced8a6f444c7620593386e99.jpg
mv archlinux-digital-art-linux-arch-linux-tech-hd-wallpaper-1f0cb881ced8a6f444c7620593386e99.jpg Imagenes

git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
