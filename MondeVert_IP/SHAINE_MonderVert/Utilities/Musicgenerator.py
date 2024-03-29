# import musicpy
#
# import random
#
# input_file = r"A:\Amini Amor\SHAINE\Requests\Beta\AI Tasks\Random Task\random Strays\sample_input.txt"
#
#
# # class MusicGenerator:
# #     def __init__(self, input_file):
# #         self.input_file = input_file
# #         self.notes = []
# #         self.tempo = 120
# #         self.key = "C"
# #
# #     def read_input_file(self):
# #         with open(self.input_file, "r") as f:
# #             for line in f:
# #                 self.notes.append(line.strip())
# #
# #     def generate_music(self):
# #         #music = musicpy.music(tempo=self.tempo, key=self.key)
# #         musicpy.play(guitar, bpm=100, instrument=25)
# #         for note in self.notes:
# #             duration = random.choice([1, 2, 4, 8])
# #             music.add_note(note, duration)
# #         music.write_file("output.mid")
# #         print("Music generated successfully!")
# #
# #     def run_unit_test(self):
# #         self.notes = ["C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5"]
# #         self.tempo = 120
# #         self.key = "C"
# #         self.generate_music()
# #
# # if __name__ == "__main__":
# #     mg = MusicGenerator(input_file)
# #
# #     mg.run_unit_test()
# #     #mg.read_input_file()
# #     #mg.generate_music()
# #
# #
# #
#
#
#
#
# #
# #
# #
# from musicpy import *
# import musicpy as mp
# import midiutil
# from pydub import AudioSegment
# from music21 import *
#
# class MusicComposition:
#     def __init__(self, input_file):
#         self.input_file = input_file
#         self.title = None
#         self.tempo = None
#         self.key = None
#         self.notes = None
#         self.midi_data = None
#         self.composition = None
#
#     def read_input_file(self):
#         with open(self.input_file, 'r') as file:
#             lines = file.readlines()
#             for line in lines:
#                 if line.startswith('Title:'):
#                     self.title = line.split(':')[1].strip()
#                 elif line.startswith('Tempo:'):
#                     self.tempo = int(line.split(':')[1].strip())
#                 elif line.startswith('Key:'):
#                     self.key = line.split(':')[1].strip()
#                 elif line.startswith('Verse') or line.startswith('Chorus'):
#                     notes = line.split(':')[1].strip().split()
#                     if self.notes is None:
#                         self.notes = []
#                     self.notes.extend(notes)
#
#     def convert_to_midi(self):
#         degrees = []
#         for note in self.notes:
#             pitch = note[:-1]
#             octave = int(note[-1])
#             note_obj = note.Note(pitch, octave=octave)
#             degrees.append(note_obj)
#         #scale = scale.MajorScale(self.key)
#         midi_data = midiutil.MIDIFile(1)
#         midi_data.addTempo(0, 0, self.tempo)
#         for i, degree in enumerate(degrees):
#             midi_data.addNote(0, 0, degree.midi, i, 1, 100)
#         self.midi_data = midi_data
#
#     def generate_composition(self):
#         composition = musicpy.Composition()
#         composition.fromMidi(self.midi_data)
#         self.composition = composition
#
#     def export_to_file(self, output_file):
#         self.composition.toMidi(output_file)
#
#     def run(self, test=False):
#         self.read_input_file()
#         self.convert_to_midi()
#         self.generate_composition()
#         self.export_to_file('output.mid')
#         if test:
#             return self.composition
# #
# # Sample input file
#
# # Create an instance of the MusicComposition class
# music = MusicComposition(input_file)
# print(input_file)
# #
# # # # Run the code
# music.run()
#
# # Sample data for unit test
# # test_data = music.run(test=True)
# #
# # #
# #
# # guitar = (C('CM7', 3, 1/8, 1/8)^2 |
# #           C('G7sus', 2, 1/4, 1/8)^2 |
# #           C('A7sus', 2, 1/4, 1/8)^2 |
# #           C('Em7', 2, 1/4, 1/8)^2 |
# #           C('FM7', 2, 1/4, 1/8)^2 |
# #           C('CM7', 3, 1/4, 1/8)@1 |
# #           C('AbM7', 2, 1/4, 1/8)^2 |
# #           C('G7sus', 2, 1/4, 1/8)^2) * 2
# #
# #
# #
# #
# # # guitar = (C('CM7', 3, 1/8, 1/8)^2 |
# # #           C('Em7', 2, 1/4, 1/8)^2 |
# # #           C('FM7', 2, 1/4, 1/8)^2 |
# # #           C('AbM7', 2, 1/4, 1/8)^2 |
# # #           C('G7sus', 2, 1/4, 1/8)^2) * 2
# #
# #
# #
# # #
# # musicpy.play(guitar, bpm=113, instrument='Violin')
# # # #
# # #
# # # #
# # # # a = musicpy.note('D', 6,  volume=100)
# # # # musicpy.play(a, 140, instrument=1, wait = True )
# # # #
# # # # b = musicpy.get_chord('C', 'maj7', intervals=10, duration=20,)
# # # # print(b)
# # # # musicpy.play(b,wait=True,)
# # #
#
#
# print('Done')
#
# #
# # a = C('Dmaj7') % (1/4,1/4) | C('Cmaj7') | C('Fadd9',3) | C('D#maj7',4) | (C('Dmaj7',3)/-2) % (5/4,)
# # b = musicpy.chord('F#5, G5, A5, B5, G5, F5', 1/8, 1/8)
# # musicpy.play(a & b , 120, instrument='Violin')
#

#This code defines a `MusicComposition` class that contains all the functions and methods for the music composition.
# The `read_input_file` function reads the input file and extracts the title, tempo, key, and notes.
# The `convert_to_midi` function converts the notes into MIDI format using the `music21` library.
# The `generate_composition` function generates a music composition using the `musicpy` library.
# The `export_to_file` function exports the music composition to a file.
# The `run` function calls all the required functions in a sequence and exports the music composition to a file named 'output.mid'.
#To run a unit test, you can call the `run` function with the `test` parameter set to `True`.
# This will return the `composition` object, which you can use to test the output of the code.



import musicpy as mp
import random

# Define chords
C1 = mp.chord('C4, E4, G4') % (1, 1/8) * 4
C2 = mp.chord('F4, A4, C5') % (1, 1/8) * 4
C3 = mp.chord('G4, B4, D5') % (1, 1/8) * 4
C4 = mp.chord('A#4, D5, F5') % (1, 1/8) * 4

# Define drum patterns
D1 = mp.drum('x..x..x..x..x..x..x..x..')
D2 = mp.drum('x...x...x...x...x...x...x...x..')
D3 = mp.drum('x...x.x...x...x...x.x...x...x..')
D4 = mp.drum('x..x.x..x..x..x..x.x..x..x..x..x..x..x..x..x..x..x..x..x..x..')

# Define bassline
B1 = mp.bassline('C2', 'C2', 'C2', 'C2', 'F2', 'F2', 'F2', 'F2',
                 'G2', 'G2', 'G2', 'G2', 'A#2', 'A#2', 'A#2', 'A#2') % (1, 1/8) * 4

# Define piano melody
piano_notes = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4']
piano_rhythm = [1/4, 1/4, 1/8, 1/8, 1/8, 1/8, 1/4]

P1 = mp.melody(random.choices(piano_notes, k=8), random.choices(piano_rhythm, k=8)) % (1,1) * 2
P2 = mp.melody(random.choices(piano_notes, k=8), random.choices(piano_rhythm, k=8)) % (1,1) * 2
P3 = mp.melody(random.choices(piano_notes, k=8), random.choices(piano_rhythm, k=8)) % (1,1) * 2

# Define piece
new_piece = mp.piece(tracks=[C1, C2, C3, C4, D1, D2, D3, D4, B1, P1, P2, P3],
                     instruments=['Electric Piano 1', 'Electric Piano 1', 'Electric Piano 1', 'Electric Piano 1',
                                  'Drum Kit', 'Drum Kit', 'Drum Kit', 'Drum Kit', 'Electric Bass (finger)',
                                  'Electric Piano 1', 'Electric Piano 1', 'Electric Piano 1'],
                     bpm=90,
                     start_times=[0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 4, 6],
                     track_names=['piano', 'piano', 'piano', 'piano', 'drums', 'drums', 'drums', 'drums', 'bass', 'melody', 'melody', 'melody'])

# Play piece
mp.play(new_piece, duration=90)