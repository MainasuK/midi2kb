# Dependencies
import mido
from pynput.keyboard import Controller

# Use A Major Scale
# Maybe switch to something more interesting...
notes = {
    48: 'z', # C3
    50: 'x', # D3
    52: 'c', # E3
    53: 'v', # F3
    55: 'b', # G3
    57: 'n', # A3
	59: 'm', # B3

	60: 'a', # C4
    62: 's', # D4
    64: 'd', # E4
    65: 'f', # F4
    67: 'g', # G4
    69: 'h', # A4
	71: 'j', # B4

    72: 'q', # C5
    74: 'w', # D5
    76: 'e', # E5
    77: 'r', # F5
    79: 't', # G5
    81: 'y', # A5
	83: 'u', # B5
}

keyboard = Controller()

# Main note processing loop...
with mido.open_input() as inport: # type: ignore
    for msg in inport:
        # Skip if msg not has note
        if not hasattr(msg, "note"):
            continue
        
		# Convert MIDI note to key using dict
        key = notes.get(msg.note, None)
        print(f"{msg.note}: {key}")

		# If the key exists, play it.
        if key != None:
            if msg.type == "note_on":
                keyboard.press(key)
            elif msg.type == "note_off":
                keyboard.release(key)