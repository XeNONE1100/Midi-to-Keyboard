
# what is this project?

it's a simple python program that allows you to convert midi inputs to keyboard inputs in real-time using the python pynput library

## BIG LATENCY AND COMPATIBILITY UPDATE

should now work on linux, windows and mac!

lowered latency by using a library instead of piping commandline output using subprocess

### setting it up for your own midi keyboard

pip install the dependencies listed in **dependencies.txt**

now sets up automatically!

### if you wanna change / add your own midi buttons:

1. run **start.py** with the key configuration being an empty dict

3. copy the printed **key id**

4. paste it in the `key_config` dict in **config.py** 

reminder: the **key** is the midi input code, while the **value** is the key code thats gonna be pressed



