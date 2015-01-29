# IPython Utilities

Description: This script install icons and desktop files ( icons ) to easily access IPython
and doesn't need root access.

It provides:

    * Desktop Shorcouts to Ipython, IPython QTconsole
    * Launchers Scritps that are installed to the directory /opt/launchers
    * Installation script
    * Icons

The launchers script: termnal.sh can be used to create ~*.desktop files that launch command line applications and
interactives shells like Haskell, Matlab ...

File: IPython3.desktop

```

[Desktop Entry]
Comment=Enhanced interactive Python shell
Exec=lxterminal -e /opt/launchers/terminal.sh "ipython3c"
GenericName[en_US]=IPython3
GenericName=IPython3
Icon=ipython3
Name[en_US]=ipython3
Name=ipython3
Categories=Development;Utility;
StartupNotify=false
Terminal=false
Type=Application

```