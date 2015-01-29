#!/bin/bash
#
# Install Icons and Desktop Shortcouts to the User Directory
#
#

# Load the User XDG directories Desktop, Downloads, Documents in local language
source ~/.config/user-dirs.dirs

sudo mkdir -p /opt/launchers
sudo cp -r scripts/* /opt/launchers
#sudo find /opt/launchers -name "*.sh" | xargs chmod +x
sudo chmod +x /opt/launchers/ipython.sh
sudo chmod +x /opt/launchers/terminal.sh

echo "Launchers scripts:"
ls /opt/launchers


cp -r icons/* ~/.local/share/icons/
cp -r desktop/* ~/.local/share/applications
cp -r desktop/* $XDG_DESKTOP_DIR



echo "Installation Finished"