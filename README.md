# midi2kb

An extremely simple (25 lines, except it uses two lightweight dependencies so it's actually much more than that) way to map any MIDI device to your laptop keyboard. Good for playing rhythm games on real instruments.

## Usage

1. Install the dependencies.

```bash
pip install -r requirements.txt
```

2. Edit the dict at the start to map the MIDI notes to the keys that you want to press. [You can find a list of MIDI notes here.](http://www.inspiredacoustics.com/en/MIDI_note_numbers_and_center_frequencies)

3. Run it.

```bash
python midi2kb.py
```

## Usage Notes

### MacOS

If you're running it from Terminal, be sure to go to `System Preferences > Security and Privacy > Accessibility` and check the box next to Terminal. Otherwise, this won't be allowed to press keys for you.

### Linux

In some cases, this must be run as root. Otherwise, this won't be allowed to press keys for you.

### Windows

Untested.
