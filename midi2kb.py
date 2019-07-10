# Dependencies
import mido
import keyboard

# Use A Major Scale
# Maybe switch to something more interesting...
notes = {
	57: "d", # A3
	61: "f", # C#4
	64: "j", # E4
	69: "k", # A4
}

# Main note processing loop...
with mido.open_input() as inport:
    for msg in inport:
    	# Convert MIDI note to key using dict.
    	key = notes.get(msg.note, None)
    	
    	# If the key exists, play it.
    	if key != None:
    		if msg.type == "note_on":
    			keyboard.press(key)
    		elif msg.type == "note_off":
    			keyboard.release(key)