from subprocess import Popen, PIPE, CalledProcessError
from pynput.keyboard import Controller as KeyController



from config import *

cmd = "aseqdump", '-p', client_name 


keyboard = KeyController()

with Popen(cmd, stdout=PIPE, bufsize=1, universal_newlines=True) as p:
    for line in p.stdout:
        # print(line[40:43])   # UNCOMMENT THIS LINE FOR DETECTING WHICH KEY IS WHICH NUMBER
        try:
            if line[8:].startswith("Note on"):
                    keyboard.press(midi_to_keyboard[line[40:43]])
            
            elif line[8:].startswith("Note off"):
                    keyboard.release(midi_to_keyboard[line[40:43]])

        except:
            pass

if p.returncode != 0:
    raise CalledProcessError(p.returncode, p.args)