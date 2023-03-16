#! /bin/bash
#====================================================================
# Instala los paquetes necesarios para funcionamiento del archivo de
# configuracion 

cd /home/*

sudo pacman -Syu
sudo pacman -S firefox rofi which nitrogen pipewire ttf-dejavu
sudo pacman -S ttf-liberation noto-fonts pavucontrol pamixer arandr
sudo pacman -S ntfs-3g network-manager-applet xorg-xinit base-devel
sudo pacman -S git pcmanfm glib2 gvfs lxappearance picom alacritty curl
sudo pacman -S scrot python-psutil papirus-icon-theme

mkdir Imagenes
curl -O https://r4.wallpaperflare.com/wallpaper/625/89/275/archlinux-digital-art-linux-arch-linux-tech-hd-wallpaper-1f0cb881ced8a6f444c7620593386e99.jpg
mv archlinux-digital-art-linux-arch-linux-tech-hd-wallpaper-1f0cb881ced8a6f444c7620593386e99.jpg Imagenes

cd /home/*

git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si

cd /home/*

# Instala los extras necesarios de AUR y git para el funcionamiento del arc>

sudo pacman -Syu
yay -Syu

# Instala qtile extras para agregar modificaciones visuales a qtile
yay qtile-extras-git

# Instala fuentes para los iconos de la barra "Nerd Font"
yay ttf-nerd-fonts-symbols-2048-em-mono
yay ttf-ubuntu-mono-nerd
yay ttf-nerd-fonts-symbols-common

cd /home/*

# Instala temas para el menu de aplicaciones rofi
git clone --depth=1 https://github.com/adi1090x/rofi.git
cd rofi
chmod +x setup.sh
./setup.sh
