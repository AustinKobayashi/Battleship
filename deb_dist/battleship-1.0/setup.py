from setuptools import setup
__author__ = 'Austin Kobayashi'
setup(
    name='battleship',
    version='1.0',
    description='Sink your enemy\'s ships!',
    author='Austin Kobayashi',
    author_email='austinkobayashi@gmail.com',
    packages=['battleship'],
    entry_points={
        'console_scripts': [
            'battleship=battleship.Battleship:start_game',
        ]
    },
)

