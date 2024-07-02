from pynput.keyboard import Controller as KeyController
import rtmidi

from config import key_config

keyboard = KeyController()
# cmd = "aseqdump", '-p', client_name


def process_midi_input(midi_message):

    try:
        if midi_message[0][2] == 0:
            keyboard.release(key_config[midi_message[0][1]])
        # if midi_message[0][2] > 0:
        else:
            keyboard.press(key_config[midi_message[0][1]])
    except KeyError:
        print(f"key id: {midi_message[0][1]} | acceleration: {midi_message[0][2]}")

midi_in = rtmidi.MidiIn()

ports = range(midi_in.get_port_count())
if ports:
    for i in ports:
        print(f"Port {i}: {midi_in.get_port_name(i)}")
    port = int(input("Select the MIDI input port: "))
    midi_in.open_port(port)
    print(f"Listening on {midi_in.get_port_name(port)}...")

    try:
        while True:
            message = midi_in.get_message()
            if message:
                process_midi_input(message)
    except KeyboardInterrupt:
        print("\nExiting...")
else:
    print("No MIDI input ports available.")

midi_in.close_port()
