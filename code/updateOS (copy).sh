#!/bin/sh
#script for automating the OS updates 

#APT package manager 
update_with_apt() {
echo "updating using apt package manager"
sudo apt update && sudo apt upgrade -y
}

#YUM package manager 
update_with_yum() {
echo "updating using yum package manager"
sudo yum update -y
}

#Zypper package manager 
update_with_zypper() {
echo "updating using zypper package manager"
sudo zypper referesh && sudo zypper update -y 
}

#Ask which package manager we are using 
echo "which packagae manager are you using?"
echo "1. apt"
echo "2. yum"
echo "3. zypper"
read -p "enter your package manager" choice 


#calling the package function based on package manager chosen
case $choice in 
1)
update_with_apt
;;
2)
update_with_yum
;;
3)
update_with_zypper
;;
*)
echo "invalid choice!!"
exit 1
;;

esac
