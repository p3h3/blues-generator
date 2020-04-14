import pygame
from pygame import midi
from time import sleep

import music

tempo = 120 # BPM (Beats per Minute)

def init_midi():
    pygame.init()
    midi.init()

def get_target_device(first = True):
    if (first):
        print("If you want to use the default, just press 'Enter'.")
    try:
        device_id_string = input("Please select your output device: ")
        if (device_id_string == ""): # Returning system default output id if user pressed enter
            return midi.get_default_output_id()
        
        return int(device_id_string)
    except ValueError:
        print("This input must be an integer.")
        return get_target_device(False) # Recursively giving the user another chance

def list_devices():
    for i in range(midi.get_count()):
        r = pygame.midi.get_device_info(i)
        (interf, name, input, output, opened) = r

        in_out = ""
        if input:
            in_out = "(input)"
        if output:
            in_out = "(output)"
        
        print("%i: %s %s" % (i, name, in_out))

if __name__ == "__main__":
    init_midi()
    list_devices()

    device_id = get_target_device()
    try:
        midi_out = pygame.midi.Output(device_id, 0)
    except:
        print("Midi Output initialisation went wrong!")

    print("This script will now generate 200 notes worth of blues music..")

    notes = music.generate(200)

    print("Generated!")
    print("Starting playback..")

    try:
        time_unit_duration = (1 / (tempo / 60)) / 16
        for note in notes:
            midi_out.note_on(note.abs_note, note.velocity)
            sleep(time_unit_duration * note.duration)
            midi_out.note_off(note.abs_note, note.velocity)

    except KeyboardInterrupt:
        print("Thanks for using this blues generator. Bye!")

    except:
        print("Something went wrong!")
    
    finally:
        del midi_out
        midi.quit()
