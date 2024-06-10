from pynput.keyboard import Key

# arturia is the keyboard i used myself, check the readme for how to change it to your own
client_name = "Arturia MiniLab mkII"


# letter only examples:
# midi_to_keyboard = {
# "53," : "f",
# "55," : "g",
# "57," : "h",
# "59," : "j",
# # }

# midi_to_keyboard = {
# "36," : "s",
# "37," : "d",
# "38," : "f",
# "39," : "g",
# "40," : "h",
# "41," : "j",
# "42," : "k",
# }

# midi_to_keyboard = {
# "48," : "s",
# "50," : "d",
# "52," : "f",
# "53," : "g",
# "55," : "h",
# "57," : "j",
# "59," : "k",
# }

#arrow key example:

# }
# midi_to_keyboard = {
# "53," : Key.up,
# "55," : Key.down,
# "57," : Key.left,
# "59," : Key.right,
# }


#mixed example 

midi_to_keyboard = {
"36," : "1",
"37," : "2",
"39," : "4",

"48," : Key.shift,
"53," : Key.space,
"60," : Key.backspace,
"49," : "a",
"50," : "z",
"52," : "x",
"55," : "c",

"41," : Key.page_up,
# "42," : Key.end,
"43," : Key.page_down,
"38," : Key.home,

"69," : Key.left,
"70," : Key.up,
"71," : Key.down,
"72," : Key.right,
}



