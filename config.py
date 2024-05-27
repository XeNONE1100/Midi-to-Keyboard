from pynput.keyboard import Key

# arturia is the keyboard i used myself, check the readme for how to change it to your own
client_name = "Arturia MiniLab mkII"


# letter only examples:
# midi_to_keyboard = {
# "53," : "f",
# "55," : "g",
# "57," : "h",
# "59," : "j",
# }
# 
# midi_to_keyboard = {
# "36," : "f",
# "37," : "g",
# "38," : "h",
# "39," : "j",
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



