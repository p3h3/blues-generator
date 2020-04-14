import random
from math import floor

note_names = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","H"]

minor_blues_scale = [0, 3, 5, 6, 7, 10]

class Note:
    def __init__(self, note, velocity, duration):
        self.abs_note = note              # Midi notes (0-128)
        self.rel_note = note % 12         # Note in it's octave 
        self.octave = floor(note / 12)    # Octave
        self.velocity = velocity          # Midi velocity (0-127)
        self.duration = duration          # Duration in 16th beats
        self.name = note_names[note % 12] # German note names

def generate(length = 0):
    if(not length):
        exit

    notes = []
    notes.append(
        Note(5*12, 100, 16)
        )

    for i in range(1, length):
        pre_octave = notes[i-1].octave     # Previous tone's octave
        pre_rel_note = notes[i-1].rel_note # Previous tone's relative tone
        
        if(pre_rel_note > 7 and pre_octave < 7): 
            octave = pre_octave + random.randint(0,1)

        if(pre_rel_note < 4 and pre_octave > 4): 
            octave = pre_octave - random.randint(0,1)
            
        note = minor_blues_scale[
            (pre_rel_note + random.randint(0,2)) % len(minor_blues_scale)-1
             ]
        
        velocity = random.randint(60, 120)
        duration = 4 * random.randint(1,4)
        
        notes.append(
            Note((octave*12+note), velocity, duration)
            )

    return notes

        
