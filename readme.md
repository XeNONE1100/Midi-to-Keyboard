
a simple python program that allows you to convert midi inputs to keyboard inputs in real-time using the pynput library

# this program is linux-only! it wont work on windows / mac!

ive made this because i couldnt find a program that did this for linux and was easy to configure


> setting it up for your own midi keyboard

1. run **aseqdump -l**

2. put the **Client name** for your midi keyboard as the *client_name* variable in *config.py*

3. done! run start.py

> if you wanna change / add your own midi buttons:

1. go to *start.py*

2. uncomment line 15 (thats gonna make it so the program logs the midi presses)

3. copy the printed midi input code

4. paste it as a string in the *midi_to_keyboard* dict in *config.py* 

reminder: the *key* is the midi input code, while the *value* is the key code thats gonna be pressed



