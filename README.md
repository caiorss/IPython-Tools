# IPython Utilities

Description: This script install icons and desktop files ( icons ) to easily access IPython.

It provides:

    * Desktop Shorcouts to Ipython, IPython QTconsole
    * Launchers Scritps that are installed to the directory /opt/launchers
    * Installation script
    * Icons

The launchers script: termnal.sh can be used to create ~*.desktop files that launch command line applications and
interactives shells like Haskell, Matlab ...

## Create Desktop File and Customize Launchers

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

## Installation

```bash

$ git clone https://github.com/caiorss/IPython-Tools
$ cd IPython-Tools
$ chmod +x install.sh
$ ./install.sh

``` 

## IPython QT Console Customization

Documentation:

    * http://ipython.org/ipython-doc/dev/interactive/qtconsole.html
    * https://github.com/damontallen/IPython-quick-ref-sheets/tree/master/Helpful_projects


```

$ ipython qtconsole --ConsoleWidget.font_size=11 \                 # Set Font Size
--IPythonWidget.gui_completion=ncurses 
--colors=linux  \                                                  # Set Color Scheme
--ConsoleWidget.font_family="Anonymous Pro"                        # Set Font Type          
--ConsoleWidget.font_size=9 \                                      # Set Font Size
--matplotlib inline                                                # Figures embedded in your session,
--no-confirm-exit

--pylab
--pylab inline

```

Possible Colors:

```
  xcode friendly vs monokai rrt igor perldoc paraiso_light native colorful murphy paraiso_dark bw vim fruity 
  borland pastie trac tango emacs autumn manni

```


## Install Extension


See also: 

* [IPython Hello World Magic](http://catherinedevlin.blogspot.com.br/2013/07/ipython-helloworld-magic.html)
* [Ipython Extension Index](https://github.com/ipython/ipython/wiki/Extensions-Index)

```python

%install_ext <path or URL>

%install_ext https://bitbucket.org/birkenfeld/ipython-physics/raw/default/physics.py

%install_ext %install_ext /home/tux/PycharmProjects/Ipython/extension/helloworld.py

```