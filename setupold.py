import os
from setuptools import setup

setup(
    name = "battleship",
    version = "1.0",
    author = "Austin Kobayashi",
    author_email = "austinkobayashi@gmail.com",
    description = "A guessing game where you must destroy the enemy's battleships before yours are destroyed!",
    license = "BSD",
    packages=['battleship'],
    entry_points = {
        'console_scripts' : ['battleship = battleship.battleship:main']
    },
    data_files=[
        ('share/applications/', ['battleship.desktop'])
    ],
    classifiers=[
        "License :: OSI Approved :: BSD License",
    ],
)
