#! /bin/bash
#======================================================================
# Instala los extras necesarios de AUR y git para el funcionamiento del archivo config.py

sudo pacman -Syu
yay -Syu

# Instala qtile extras para agregar modificaciones visuales a qtile
yay qtile-extras-git

# Instala fuentes para los iconos de la barra "Nerd Font"
yay ttf-nerd-fonts-symbols-2048-em-mono
yay ttf-ubuntu-mono-nerd 
yay ttf-nerd-fonts-symbols-common

# Instala temas para el menu de aplicaciones rofi
git clone --depth=1 https://github.com/adi1090x/rofi.git
cd rofi
chmod +x setup.sh
./setup.sh
