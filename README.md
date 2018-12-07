# Battleship
A text implementation of the classic table top strategy game Battleship. The game runs on the command line and features realistic artificial intelligence and state of the art ASCII animations.

# Installation

Battleship can be installed as a Debian package and comes with a precompiled .deb file. To install, run the .deb file:
```
python3-battleship_1.0-1_all.deb
```

# Building

Battleship can be compiled into a Debian package by running:
```
$ python3 setup.py --command-packages=stdeb.command install_deb
```

# Launching the Game From the Debian Package

Battleship can be launched from the command line after installing the Debian package by running:
```
$ battleship
```

# Launching the Game Without a Debian Package

Battleship can be imported as a python package and launched from command line. From the Battleship root directory:
```
  $ python3
>>> from battleship import Battleship
>>> Battleship.start_game()
```
Note: Some dependancies may need to be installed through pip3

# Animations

Miss:

![Miss](/gifs/miss.gif)

Hit:

![Hit](/gifs/hit.gif)


Sink:

![Sink](/gifs/sink.gif)
