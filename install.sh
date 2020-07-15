#!/bin/bash
cd _build/
meson --reconfigure
meson install

while true; do
 read -p 'Do you wish you enable scale-to-fit? [Y/n]: ' response
 echo
 case $response in
  [Yy]* ) scale-to-fit musik on; break;;
  [Nn]* ) exit;;
  * ) echo "Please answer \"Y\", \"y\", \"N\", or \"n\"."
 esac
done
