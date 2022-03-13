WOL Python3
===========

This is a simple Python3 script which is used to remotely wake up computers on the local network.

You can specify the MAC addresses in a configuration fiel and execute the python script.

The script is based on an ActiveState recipe (https://code.activestate.com/recipes/users/2143621/) and was updated for Python3. The ability to define multiple computers in a simple YAML configuration file was added.

Usage
-----

  Create a configuration file with the hosts you want to wake up and save it in the same directory as wol.py . Extecute the wol.py script, no arguments are required.
  Make sure you have PyYAML installed, please see https://pyyaml.org on installation instructions for your system.

Configuration
-------------

  A wol_config.yml file must be saved in the same directory as wol.py. It contains the computer configurations for all the hosts that should be woken up. I have included a wol_config_sample.yml you can rename and moifiy with your hosts. For each host the name and MAC address must be defined. The MAC address can be defined with any kind of seperator.

MacOS Application usage
  -------------

  If you want to create a MacOS Icon to launch the script you can use Script Editor to simply run the command and save it as an application. Once saved you can modify the icon via the Finder properties. Simply modify the path the MacOS Script.scpt file and save it.   

License
-------
  Copyright (c) Hannes Hausegger, released under MIT License, see [LICENSE](LICENSE)
