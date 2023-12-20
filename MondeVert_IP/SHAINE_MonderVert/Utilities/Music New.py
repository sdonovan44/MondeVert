import time

from musicpy import *
import shutil
from MondeVert_IP.SHAINE_MonderVert.SHAINE_WIZARD_PROMPTS import User_Prefs as up, Long_User_Prompts as lup
from MondeVert_IP.SHAINE_MonderVert.Utilities import Common_Utilities as cu
from MondeVert_IP.SHAINE_MonderVert import SHAINE as GPT
import musicpy as mp
import datetime
import midiutil
from pydub import AudioSegment
from music21 import *

from pathlib import Path, PureWindowsPath

# piece(tracks,
#       instruments=None,
#       bpm=120,
#       start_times=None,
#       track_names=None,
#       channels=None,
#       name=None,
#       pan=None,
#       volume=None,
#       other_messages=[],
#       daw_channels=None)


import musicpy as mp




import musicpy as mp




C1 = mp.chord('G2, Bb2, C3') % (1/2, 1/2, 1/2) * 4
C2 = mp.chord('G2, Bb2, C3') % (1/2, 1/2, 1/2) * 4
C3 = mp.chord('Bb2, C3, D3, Eb3') % (1/2, 1/2, 1/2, 1/2) * 4
C4 = mp.chord('G2, Bb2, C3') % (1/2, 1/2, 1/2) * 4
C5 = mp.chord('G2, Bb2, C3') % (1/2, 1/2, 1/2) * 4
C6 = mp.chord('Bb2, C3, D3, Eb3') % (1/2, 1/2, 1/2, 1/2) * 4
C7 = mp.chord('G2, Bb2, C3') % (1/2, 1/2, 1/2) * 4
C8 = mp.chord('G2, Bb2, C3') % (1/2, 1/2, 1/2) * 4
C9 = mp.chord('Bb2, C3, D3, Eb3') % (1/2, 1/2, 1/2, 1/2) * 4
C10 = mp.chord('G2, Bb2, C3') % (1/2, 1/2, 1/2) * 4
C11 = mp.chord('G2, Bb2, C3') % (1/2, 1/2, 1/2) * 4
C12 = mp.chord('Bb2, C3, D3, Eb3') % (1/2, 1/2, 1/2, 1/2) * 4
C13 = mp.chord('G2, Bb2, C3') % (1/2, 1/2, 1/2) * 4
C14 = mp.chord('G2, Bb2, C3') % (1/2, 1/2, 1/2) * 4
C15 = mp.chord('Bb2, C3, D3, Eb3') % (1/2, 1/2, 1/2, 1/2) * 4

# Create a new piece with the above chords and notes
new_piece8 = mp.piece(tracks=[C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14, C15],
                  instruments=['Electric Piano 2', 'Electric Bass (finger)', 'Synth Drum', 'Electric Piano 2', 'Electric Piano 2', 'Synth Drum', 'Electric Piano 2', 'Electric Piano 2', 'Synth Drum', 'Electric Piano 2', 'Electric Piano 2', 'Synth Drum', 'Electric Piano 2', 'Electric Piano 2', 'Synth Drum'],
                  bpm=80,
                  start_times=[0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7],
                  track_names=['piano', 'bass', 'drum', 'piano', 'piano', 'drum', 'piano', 'piano', 'drum', 'piano', 'piano', 'drum', 'piano', 'piano', 'drum'])




C1 = mp.chord('C2, G2, C3, F3') % (1, 1/8) * 2
C2 = (mp.chord('C2, C2, G1, G1') % (1,1)) * 2
C3 = (mp.chord('D#4, F4') % (1/8, 1/8) * 8 | mp.chord('G#3, C4','E3') % (1/8, 1/4,1/8) * 8) * 2
C4 = mp.chord('C4, G4, C5, E5') % ([3/8,1/8,1/4,1/4], [3/8,1/8,1/4,1/4]) * 2
C5 = mp.chord('C4, G4, C5, E5') % ([3/8,1/8,1/4,1/4], [3/8,1/8,1/4,1/4]) * 2
C6 = (mp.chord('D#4, F4') % (1/8, 1/8) * 8 | mp.chord('G#3, C4','E3') % (1/8, 1/4,1/8) * 8) * 2
# Create a new piece with the above chords and notes
new_piece7 = mp.piece(tracks=[C1, C2, C3, C4, C5,C6],
                  instruments=['Electric Piano 1', 'Electric Bass (finger)', 'Trumpet', 'Synth Drum', 'Electric Piano 2', 'Trumpet'],
                  bpm=80,
                  start_times=[0, 2, 2, 0, 4,2],
                  track_names=['piano', 'bass', 'trumpet', 'drum', 'electric_piano','test'])

# Chords and notes for the instrumental
C1 = mp.chord('C2, G2, C3, F3') % (1, 1/8) * 4
C2 = (mp.chord('C2, C2, G1, G1') % (1,1)) * 2
C3 = (mp.chord('D#5, F5') % (1/8, 1/8) * 8 | mp.chord('G#4, C5') % (1/8, 1/8) * 8) * 2
C4 = mp.chord('C4, G4, C5, E5') % ([3/8,1/8,1/4,1/4], [3/8,1/8,1/4,1/4]) * 4
C5 = mp.chord('C4, G4, C5, E5') % ([3/8,1/8,1/4,1/4], [3/8,1/8,1/4,1/4]) * 4

# Create a new piece with the above chords and notes
new_piece6 = mp.piece(tracks=[C1, C2, C3, C4, C5],
                  instruments=['Electric Piano 1', 'Electric Bass (finger)', 'Electric Guitar (jazz)', 'Synth Drum', 'Electric Piano 2'],
                  bpm=90,
                  start_times=[0, 2, 2, 0, 4],
                  track_names=['piano', 'bass', 'guitar', 'drum', 'electric_piano'])

C1 = mp.chord('C3, G3, B3, E4') % (1, 1/8) * 4
C2 = (mp.chord('C2, C2, G1, G1') % (1,1)) * 2
C3 = (mp.chord('E5, C5') % (1/8, 1/8) * 8 | mp.chord('C5, D5') % (1/8, 1/4,1/16) * 8) * 2
C4 = mp.chord('C3, C3, C3, C3') % ([3/8,1/8,1/4,1/4], [3/8,1/8,1/4,1/4]) * 4
C5 = mp.chord('C3, C3, C3, C3') % ([3/8,1/8,1/4,1/4], [3/8,1/8,1/4,1/4]) * 4
C6 = (mp.chord('E5, C5') % (1/8, 1/8) * 8 | mp.chord('C5, D5') % (1/8, 1/4,1/16) * 8) * 2


# Piece parameters
new_piece5 = mp.piece(tracks=[C1, C2, C3, C4, C5,C6],
                     instruments=['Acoustic Grand Piano', 'Electric Bass (finger)', 'Electric Guitar (jazz)', 'Synth Drum', 'Trumpet', 'Violin'],
                     bpm=90,
                     start_times=[0, 2, 2, 4, 4, 2],
                     track_names=['piano', 'bass', 'guitar', 'drum','d', 'lead guitar'])



# Define chords
C1 = mp.chord('C4, E4, G4') % (1, 1/8) * 4
C2 = mp.chord('F4, A4, C5') % (1, 1/8) * 4
C3 = mp.chord('G4, B4, D5') % (1, 1/8) * 4
C4 = mp.chord('A#4, D5, F5') % (1, 1/8) * 4
# Define the piece with the chords and instruments
new_piece4 = mp.piece(tracks=[C1, C2, C3, C4],
                      instruments=['Electric Bass (finger)', 'Synth Drum', 'Electric Piano 1', 'Steel Drums'],
                      bpm=80,
                      start_times=[0, 2, 2, 0],
                      track_names=['melody', 'bass', 'drums', 'piano'])
new_piece3_name = 'new_piece2'




# Define the chords for the piece
C1 = mp.chord('G3, B3, D4') % (1, 1/8) * 4
C2 = mp.chord('C2, C2, G1, G1') % (1,1) * 2
C3 = mp.chord('C4, E4, G4') % (1/4, 1/4, 1/2) * 4
C4 = mp.chord('D4, F#4, A4') % (1/4, 1/4, 1/2) * 4
C5 = mp.chord('G3, B3, D4') % (1, 1/8) * 4

# Define the piece with the chords and instruments
new_piece3 = mp.piece(tracks=[C1, C2, C3, C4, C5],
                      instruments=['Steel Drums', 'Electric Bass (finger)', 'Synth Drum', 'Electric Piano 1', 'Steel Drums'],
                      bpm=80,
                      start_times=[0, 2, 2, 0, 4],
                      track_names=['melody', 'bass', 'drums', 'piano', 'harmony'])
new_piece3_name = 'new_piece2'

new_pieces = []
# Define the chords for the reggae instrumental
C1 = mp.chord('C4, G4, E4, C4') % (1, 1/8) * 4
C2 = mp.chord('C3, G3, C4, E4') % (1,1) * 2
C3 = (mp.chord('E5, G5') % (1/8, 1/8) * 8 | mp.chord('C5, D5') % (1/8, 1/8) * 8) * 2
C4 = mp.chord('C3, C3, C3, C3') % ([3/8,1/8,1/4,1/4], [3/8,1/8,1/4,1/4]) * 4
C5 = mp.chord('C3, C3, C3, C3') % ([3/8,1/8,1/4,1/4], [3/8,1/8,1/4,1/4]) * 4

# Create a new piece with the defined chords
new_piece2 = mp.piece(tracks=[C1, C2, C3, C4, C5],
                  instruments=['Acoustic Grand Piano', 'Electric Bass (finger)', 'Steel Drums', 'Synth Drum', 'Trumpet'],
                  bpm=120,
                  start_times=[0, 2, 2, 0, 4],
                  track_names=['piano', 'bass', 'steel drums', 'drum', 'trumpet'])

new_piece2_name = 'new_piece2'

C1 = mp.chord('G4, D5, B5, F#5') % (1, 1/8) * 10
C2 = (mp.chord('C2, C2, G1, G1') % (1,1)) * 8
C3 = (mp.chord('F#6, G6') % (1/8, 1/8) * 8 | mp.chord('A5, B5') % (1/8, 1/8) * 8) * 2
C4 = mp.chord('F3, F3, F3, F3') % ([3/8,1/8,1/4,1/4], [3/8,1/8,1/4,1/4]) * 8
C5 = mp.chord('F3, F3, F3, F3') % ([3/8,1/8,1/4,1/4], [3/8,1/8,1/4,1/4]) * 4 #| mp.chord('A5, B5') % (1/8, 1/8) * 8) * 2

new_piece = mp.piece(tracks=[C1, C2, C3, C4,C5],
                  instruments=['Acoustic Grand Piano', 'Electric Bass (finger)', 'Trumpet', 'Synth Drum', 'Trumpet'],
                  bpm=120,
                  start_times=[0, 2, 2, 0,4],
                  track_names=['piano', 'bass', 'violin', 'drum', 'trumpet'])


C1 = mp.chord('E2, G2, A2') % (1, 1/8) * 4
C2 = (mp.chord('E2, G2, A2') % (1,1)) * 2
C3 = (mp.chord('G2, A2, C3') % (1/4, 1/4, 1/2) * 8 | mp.chord('E2, G2, A2') % (1/8, 1/8, 1/4) * 8) * 2
C4 = mp.chord('E2, G2, A2') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C5 = mp.chord('E2, G2, A2') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4

# Create a new piece with the above chords and notes
new_piece9 = mp.piece(tracks=[C1, C2, C3, C4, C5],
                  instruments=['Electric Piano 1', 'Electric Bass (finger)', 'Trumpet', 'Synth Drum', 'Electric Piano 2'],
                  bpm=80,
                  start_times=[0, 2, 2, 0, 4],
                  track_names=['piano', 'bass', 'trumpet', 'drum', 'electric_piano'])



# Chords and notes for the instrumental
C1 = mp.chord('F#2, F#2, F#2, F#2') % (1, 1/8) * 4
C2 = mp.chord('A2, A2, A2, A2') % (1,1) * 2
C3 = mp.chord('C3, C3, C3, C3') % (1, 1/8) * 4
C4 = mp.chord('F#2, F#2, F#2, F#2') % (1, 1/8) * 4
C5 = mp.chord('A2, A2, A2, A2') % (1,1) * 2
C6 = mp.chord('C3, C3, C3, C3') % (1, 1/8) * 4
C7 = mp.chord('F#2, F#2, F#2, F#2') % (1, 1/8) * 4
C8 = mp.chord('G2, G2, G2, G2') % (1,1) * 2
C9 = mp.chord('F#2, F#2, F#2, F#2') % (1, 1/8) * 4
C10 = mp.chord('A2, A2, A2, A2') % (1,1) * 2
C11 = mp.chord('C3, C3, C3, C3') % (1, 1/8) * 4
C12 = mp.chord('F#2, F#2, F#2, F#2') % (1, 1/8) * 4
C13 = mp.chord('A2, A2, A2, A2') % (1,1) * 2
C14 = mp.chord('C3, C3, C3, C3') % (1, 1/8) * 4
C15 = mp.chord('F#2, F#2, F#2, F#2') % (1, 1/8) * 4
C16 = mp.chord('G2, G2, G2, G2') % (1,1) * 2

# Create a new piece with the above chords and notes
new_piece10 = mp.piece(tracks=[C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14, C15, C16],
                      instruments=['Electric Bass (finger)', 'Electric Piano 1', 'Electric Piano 1', 'Electric Piano 1',
                                   'Electric Bass (finger)', 'Electric Piano 1', 'Electric Piano 1', 'Electric Piano 1',
                                   'Electric Bass (finger)', 'Electric Piano 1', 'Electric Piano 1', 'Electric Piano 1',
                                   'Electric Bass (finger)', 'Electric Piano 1', 'Electric Piano 1', 'Electric Piano 1'],
                      bpm=80,
                      start_times=[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],
                      track_names=['bass', 'piano1', 'piano2', 'piano3', 'bass', 'piano1', 'piano2', 'piano3',
                                   'bass', 'piano1', 'piano2', 'piano3', 'bass', 'piano1', 'piano2', 'piano3'])



# Chords and notes for the instrumental
C1 = mp.chord('G2, B2, D3, F#3') % (1, 1/8) * 4
C2 = (mp.chord('G2, G2, B1, B1') % (1,1)) * 2
C3 = (mp.chord('F2, A2, C3') % (1/4, 1/4, 1/2) * 8 | mp.chord('G2, B2, D3') % (1/8, 1/8, 1/4) * 8) * 2
C4 = mp.chord('G2, B2, D3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C5 = mp.chord('G2, B2, D3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4

# Create a new piece with the above chords and notes
new_piece11 = mp.piece(tracks=[C1, C2, C3, C4, C5],
                  instruments=['Electric Piano 1', 'Electric Bass (finger)', 'Trumpet', 'Synth Drum', 'Electric Piano 2'],
                  bpm=80,
                  start_times=[0, 2, 2, 0, 4],
                  track_names=['piano', 'bass', 'trumpet', 'drum', 'dd'])



# Chords and notes for the instrumental
C1 = mp.chord('D3, G3, Bb3') % (1, 1/8) * 4
C2 = (mp.chord('D3, G3, Bb3') % (1,1)) * 2
C3 = (mp.chord('F4, G4, Bb4') % (1/4, 1/4, 1/2) * 8 | mp.chord('D3, G3, Bb3') % (1/8, 1/8, 1/4) * 8) * 2
C4 = mp.chord('D3, G3, Bb3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C5 = mp.chord('D3, G3, Bb3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4

# Create a new piece with the above chords and notes
new_piece12 = mp.piece(tracks=[C1, C2, C3, C4, C5],
                  instruments=['Electric Bass (finger)', 'Electric Piano 1', 'Electric Piano 1', 'Electric Piano 1', 'Synth Drum'],
                  bpm=80,
                  start_times=[0, 2, 2, 0, 4],
                  track_names=['bass', 'piano1', 'piano2', 'piano3', 'drum'])

# Chords and notes for the instrumental
C1 = mp.chord('G2, B2, D3, F#3') % (1, 1/8) * 4
C2 = (mp.chord('G2, G2, B1, B1') % (1,1)) * 2
C3 = (mp.chord('F2, A2, C3') % (1/4, 1/4, 1/2) * 8 | mp.chord('G2, B2, D3') % (1/8, 1/8, 1/4) * 8) * 2
C4 = mp.chord('G2, B2, D3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C5 = mp.chord('G2, B2, D3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4

# Create a new piece with the above chords and notes
new_piece13 = mp.piece(tracks=[C1, C2, C3, C4, C5],
                  instruments=['Electric Piano 1', 'Electric Bass (finger)', 'Trumpet', 'Synth Drum', 'Electric Piano 2'],
                  bpm=80,
                  start_times=[0, 2, 2, 0, 4],
                  track_names=['piano', 'bass', 'trumpet', 'drum', 'electric_piano'])




# Chords and notes for the song
C1 = mp.chord('G2, B2, D3, F#3') % (1, 1/8) * 4
C2 = (mp.chord('G2, G2, B1, B1') % (1, 1)) * 2
C3 = (mp.chord('F2, A2, C3') % (1/4, 1/4, 1/2) * 8 | mp.chord('G2, B2, D3') % (1/8, 1/8, 1/4) * 8) * 2
C4 = mp.chord('G2, B2, D3') % ([3/8, 1/8, 1/4], [3/8, 1/8, 1/4]) * 4
C5 = mp.chord('G2, B2, D3') % ([3/8, 1/8, 1/4], [3/8, 1/8, 1/4]) * 4
C6 = mp.chord('C3, E3, G3') % (1, 1/8) * 4
C7 = mp.chord('C3, E3, G3') % ([3/8, 1/8, 1/4], [3/8, 1/8, 1/4]) * 4
C8 = mp.chord('C3, E3, G3') % ([3/8, 1/8, 1/4], [3/8, 1/8, 1/4]) * 4

# Create a new piece with the above chords and notes
new_piece14 = mp.piece(tracks=[C1, C2, C3, C4, C5, C6, C7, C8],
                     instruments=['Electric Piano 1', 'Electric Bass (finger)', 'Trumpet', 'Synth Drum', 'Electric Piano 2', 'SynthStrings 1', 'SynthStrings 2', 'Pad 3 (polysynth)'],
                     bpm=80,
                     start_times=[0, 2, 2, 0, 4, 0, 0, 0],
                     track_names=['piano', 'bass', 'trumpet', 'drum', 'electric_piano', 'strings1', 'strings2', 'pad'])

# Chords and notes for the instrumental
C1 = mp.chord('D2, F#2, A2') % (1, 1/8) * 4
C2 = (mp.chord('D2, F#2, A2') % (1,1)) * 2
C3 = (mp.chord('D2, F#2, A2') % (1/4, 1/4, 1/2) * 8 | mp.chord('C2, E2, G2') % (1/8, 1/8, 1/4) * 8) * 2
C4 = mp.chord('D2, F#2, A2') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C5 = mp.chord('D2, F#2, A2') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C6 = mp.chord('C2, E2, G2') % (1, 1/8) * 4
C7 = (mp.chord('C2, E2, G2') % (1,1)) * 2
C8 = (mp.chord('C2, E2, G2') % (1/4, 1/4, 1/2) * 8 | mp.chord('D2, F#2, A2') % (1/8, 1/8, 1/4) * 8) * 2
C9 = mp.chord('C2, E2, G2') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C10 = mp.chord('C2, E2, G2') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4

# Create a new piece with the above chords and notes
new_piece311 = mp.piece(tracks=[C1, C2, C3, C4, C5, C6, C7, C8, C9, C10],
                  instruments=['Electric Piano 1', 'Electric Bass (finger)', 'Trumpet', 'Synth Drum', 'Electric Piano 2', 'Electric Guitar (clean)', 'Acoustic Bass', 'Acoustic Guitar (nylon)', 'Bright Acoustic Piano', 'Electric Guitar (muted)'],
                  bpm=80,
                  start_times=[0, 2, 2, 0, 4, 0, 2, 2, 0, 4],
                  track_names=['piano1', 'bass', 'trumpet', 'drum', 'piano2', 'guitar1', 'bass2', 'guitar2', 'piano3', 'guitar3'])

# Chords and notes for the instrumental
C1 = mp.chord('D2, F#2, A2') % (1, 1/8) * 4
C2 = (mp.chord('D2, F#2, A2') % (1,1)) * 2
C3 = (mp.chord('F#2, A2, C#3') % (1/4, 1/4, 1/2) * 8 | mp.chord('D2, F#2, A2') % (1/8, 1/8, 1/4) * 8) * 2
C4 = mp.chord('D2, F#2, A2') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C5 = mp.chord('D2, F#2, A2') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C6 = mp.chord('A2, C#3, E3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C7 = mp.chord('A2, C#3, E3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C8 = mp.chord('D2, F#2, A2') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C9 = mp.chord('D2, F#2, A2') % (1,1) * 2
C10 = mp.chord('A2, C#3, E3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C11 = mp.chord('A2, C#3, E3') %  (1,1) * 2

# Create a new piece with the above chords and notes
new_piece15 = mp.piece(tracks=[C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11],
                  instruments=['Electric Piano 1', 'Electric Bass (finger)', 'Trumpet', 'Synth Drum', 'Electric Piano 2', 'Acoustic Grand Piano', 'Electric Guitar (jazz)', 'Electric Guitar (clean)', 'SynthBrass 1', 'SynthBrass 2', 'Synth Bass 1'],
                  bpm=80,
                  start_times=[0, 2, 2, 0, 4, 6, 8, 10, 12, 14, 16],
                  track_names=['piano', 'bass', 'trumpet', 'drum', 'electric_piano', 'grand_piano', 'jazz_guitar', 'clean_guitar', 'synth1', 'synth2', 'synth_bass'])

# Chords and notes for the instrumental
C1 = mp.chord('C4, E4, G4') % (1, 1/2) * 2
C2 = mp.chord('F4, A4, C5') % (1, 1/2) * 2
C3 = mp.chord('G4, B4, D5') % (1, 1/2) * 2
C4 = mp.chord('A#4, C5, D#5') % (1, 1/2) * 2
C5 = mp.chord('G4, B4, D5') % (1, 1/2) * 2
C6 = mp.chord('A#4, C5, D#5') % (1, 1/2) * 2

# Create a new piece with the above chords and notes
new_piece16 = mp.piece(tracks=[C1, C2, C3, C4, C5, C6],
                  instruments=['Electric Piano 1', 'Electric Bass (finger)', 'Electric Guitar (clean)', 'Synth Drum', 'Trumpet', 'Synth Bass 1'],
                  bpm=85,
                  start_times=[0, 2, 4, 6, 8, 10],
                  track_names=['piano', 'bass', 'guitar', 'drum', 'trumpet', 'synth'])


# Chords and notes for the instrumental
C1 = mp.chord('F#3, A3, C#4') % (1, 1/8) * 4
C2 = (mp.chord('F#3, A3, C#4') % (1,1)) * 2
C3 = (mp.chord('D3, F#3, A3') % (1/4, 1/4, 1/2) * 8 | mp.chord('F#3, A3, C#4') % (1/8, 1/8, 1/4) * 8) * 2
C4 = mp.chord('F#3, A3, C#4') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C5 = mp.chord('F#3, A3, C#4') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4

# Create a new piece with the above chords and notes
new_piece17 = mp.piece(tracks=[C1, C2, C3, C4, C5],
                  instruments=['Electric Piano 1', 'Electric Bass (finger)', 'Trumpet', 'Synth Drum', 'Electric Piano 2'],
                  bpm=85,
                  start_times=[0, 2, 2, 0, 4],
                  track_names=['piano', 'bass', 'trumpet', 'drum', 'electric_piano'])

# Chords and notes for the instrumental
C1 = mp.chord('G2, B2, D3, F#3') % (1, 1/8) * 4
C2 = (mp.chord('G2, G2, B1, B1') % (1,1)) * 2
C3 = (mp.chord('F2, A2, C3') % (1/4, 1/4, 1/2) * 8 | mp.chord('G2, B2, D3') % (1/8, 1/8, 1/4) * 8) * 2
C4 = mp.chord('G2, B2, D3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C5 = mp.chord('G2, B2, D3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4

# Create a new piece with the above chords and notes
new_piece18 = mp.piece(tracks=[C1, C2, C3, C4, C5],
                  instruments=['Electric Piano 1', 'Electric Bass (finger)', 'Trumpet', 'Synth Drum', 'Electric Piano 2'],
                  bpm=80,
                  start_times=[0, 2, 2, 0, 4],
                  track_names=['piano', 'bass', 'trumpet', 'drum', 'electric_piano'])

# Chords and notes for the instrumental #2
C6 = mp.chord('C4, E4, G4') % (1, 1/8) * 4
C7 = (mp.chord('C4, C4, E3, E3') % (1,1)) * 2
C8 = (mp.chord('D4, F4, A4') % (1/4, 1/4, 1/2) * 8 | mp.chord('C4, E4, G4') % (1/8, 1/8, 1/4) * 8) * 2
C9 = mp.chord('C4, E4, G4') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C10 = mp.chord('C4, E4, G4') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4

# Create a new piece with the above chords and notes
new_piece19 = mp.piece(tracks=[C6, C7, C8, C9, C10],
                  instruments=['Electric Piano 1', 'Electric Bass (finger)', 'Trumpet', 'Synth Drum', 'Electric Piano 2'],
                  bpm=85,
                  start_times=[0, 2, 2, 0, 4],
                  track_names=['piano', 'bass', 'trumpet', 'drum', 'electric_piano'])



# Chords and notes for the instrumental
C1 = mp.chord('D3, F#3, A3') % (1, 1/8) * 4
C2 = (mp.chord('D3, F#3, A3') % (1,1)) * 2
C3 = (mp.chord('F#3, A3, C#4') % (1/4, 1/4, 1/2) * 8 | mp.chord('D3, F#3, A3') % (1/8, 1/8, 1/4) * 8) * 2
C4 = mp.chord('D3, F#3, A3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C5 = mp.chord('D3, F#3, A3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C6 = mp.chord('A3, C#4, E4') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C7 = mp.chord('A3, C#4, E4') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C8 = mp.chord('D3, F#3, A3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C9 = mp.chord('D3, F#3, A3') % (1,1) * 2
C10 = mp.chord('A3, C#4, E4') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C11 = mp.chord('A3, C#4, E4') %  (1,1) * 2

# Create a new piece with the above chords and notes
new_piece_SD = mp.piece(tracks=[C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11],
                  instruments=['Acoustic Guitar (steel)', 'Electric Bass (finger)', 'Trumpet', 'Synth Drum', 'Electric Piano 1', 'Acoustic Grand Piano', 'Electric Guitar (jazz)', 'Electric Guitar (clean)', 'SynthBrass 1', 'SynthBrass 2', 'Synth Bass 1'],
                  bpm=85,
                  start_times=[0, 2, 2, 0, 4, 6, 8, 10, 12, 14, 16],
                  track_names=['guitar', 'bass', 'trumpet', 'drum', 'electric_piano', 'grand_piano', 'jazz_guitar', 'clean_guitar', 'synth1', 'synth2', 'synth_bass'])

# Chords and notes for the instrumental
C1 = mp.chord('E3, G#3, B3') % (1, 1/8) * 6
C2 = (mp.chord('E3, G#3, B3') % (1,1)) * 2
C3 = (mp.chord('C#3, E3, G#3') % (1/4, 1/4, 1/2) * 8 | mp.chord('E3, G#3, B3') % (1/8, 1/8, 1/4) * 8) * 2
C4 = mp.chord('E3, G#3, B3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C5 = mp.chord('E3, G#3, B3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C6 = mp.chord('C#3, E3, G#3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C7 = mp.chord('C#3, E3, G#3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C8 = mp.chord('E3, G#3, B3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C9 = mp.chord('E3, G#3, B3') % (1,1) * 2
C10 = mp.chord('C#3, E3, G#3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C11 = mp.chord('C#3, E3, G#3') %  (1,1) * 2
C12 = mp.chord('B2, D#3, F#3') % (1,1) * 2
C13 = mp.chord('B2, D#3, F#3') % (1/4,1/4,1/2) * 6

# Create a new piece with the above chords and notes
new_piece_SD2 = mp.piece(tracks=[C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13],
                  instruments=['Electric Piano 1', 'Electric Bass (finger)', 'Trumpet', 'Synth Drum', 'Electric Piano 2', 'Acoustic Grand Piano', 'Electric Guitar (jazz)', 'Electric Guitar (clean)', 'SynthBrass 1', 'SynthBrass 2', 'Synth Bass 1', 'Acoustic Guitar (steel)', 'Orchestral Harp'],
                  bpm=95,
                  start_times=[0, 2, 2, 0, 4, 6, 8, 10, 12, 14, 16, 18, 20],
                  track_names=['piano', 'bass', 'trumpet', 'drum', 'electric_piano', 'grand_piano', 'jazz_guitar', 'clean_guitar', 'synth1', 'synth2', 'synth_bass', 'steel_guitar', 'harp'])



# Chords and notes for the instrumental
C1 = mp.chord('E3, G#3, B3') % (1, 1/8) * 4
C2 = (mp.chord('E3, G#3, B3') % (1,1)) * 2
C3 = (mp.chord('C#3, E3, G#3') % (1/4, 1/4, 1/2) * 8 | mp.chord('E3, G#3, B3') % (1/8, 1/8, 1/4) * 8) * 2
C4 = mp.chord('E3, G#3, B3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C5 = mp.chord('E3, G#3, B3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C6 = mp.chord('C#3, E3, G#3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C7 = mp.chord('C#3, E3, G#3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C8 = mp.chord('E3, G#3, B3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C9 = mp.chord('E3, G#3, B3') % (1,1) * 2
C10 = mp.chord('C#3, E3, G#3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C11 = mp.chord('C#3, E3, G#3') %  (1,1) * 2
C12 = mp.chord('F#2, A2, C#3') %  (1,1) * 2
C13 = mp.chord('G#2, C3, D#3') %  (1,1) * 2
C14 = mp.chord('G#2, C3, D#3') % (1/4,1/4,1/2) * 6
C15 = mp.chord('F#2, A2, C#3') %  (1,1) * 2

# Create a new piece with the above chords and notes
Dank_midz = mp.piece(tracks=[C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14, C15],
                      instruments=['Electric Guitar (clean)', 'Electric Bass (finger)', 'Electric Piano 1', 'Synth Drum', 'Electric Piano 2', 'Acoustic Grand Piano', 'Electric Guitar (jazz)', 'Trumpet', 'SynthBrass 1', 'SynthBrass 2', 'Synth Bass 1', 'Distortion Guitar', 'Sitar', 'Kalimba', 'SynthStrings 1'],
                      bpm=100,
                      start_times=[0, 2, 2, 0, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24],
                      track_names=['clean_guitar', 'bass', 'electric_piano', 'drum', 'grand_piano', 'jazz_guitar', 'trumpet', 'synth1', 'synth2', 'synth_bass', 'distortion_guitar', 'sitar', 'kalimba', 'string', 'synthstrings'])



C1 = mp.chord('A2, C#3, E3') % (1, 1/2) * 3
C2 = (mp.chord('A2, C#3, E3') % (1,1)) * 2
C3 = (mp.chord('D2, F#2, A2') % (1/4, 1/4, 1/2) * 8 | mp.chord('A2, C#3, E3') % (1/8, 1/8, 1/4) * 8) * 2
C4 = mp.chord('A2, C#3, E3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C5 = mp.chord('A2, C#3, E3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C6 = mp.chord('D2, F#2, A2') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C7 = mp.chord('D2, F#2, A2') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C8 = mp.chord('A2, C#3, E3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C9 = mp.chord('A2, C#3, E3') % (1,1) * 2
C10 = mp.chord('D2, F#2, A2') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C11 = mp.chord('D2, F#2, A2') %  (1,1) * 2
C12 = mp.chord('C2, E2, G2') % (1,1) * 2
C13 = mp.chord('C2, E2, G2') % (1/4,1/4,1/2) * 6

# Create a new piece with the above chords and notes
Amber = mp.piece(tracks=[C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13],
                  instruments=['Electric Piano 1', 'Electric Bass (finger)', 'Trumpet', 'Synth Drum', 'Electric Piano 2', 'Acoustic Grand Piano', 'Electric Guitar (jazz)', 'Acoustic Guitar (steel)', 'SynthBrass 1', 'SynthBrass 2', 'Synth Bass 1', 'Acoustic Guitar (steel)', 'Orchestral Harp'],
                  bpm=110,
                  start_times=[0, 2, 2, 0, 4, 6, 8, 10, 12, 14, 16, 18, 20],
                  track_names=['piano', 'bass', 'trumpet', 'drum', 'electric_piano', 'grand_piano', 'jazz_guitar', 'clean_guitar', 'synth1', 'synth2', 'synth_bass', 'steel_guitar', 'harp'])




#Chords and notes for the instrumental
C1 = mp.chord('E3, G#3, B3') % (1, 1/8) * 6
C2 = (mp.chord('E3, G#3, B3') % (1,1)) * 2
C3 = (mp.chord('C#3, E3, G#3') % (1/4, 1/4, 1/2) * 8 | mp.chord('E3, G#3, B3') % (1/8, 1/8, 1/4) * 8) * 2
C4 = mp.chord('E3, G#3, B3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C5 = mp.chord('E3, G#3, B3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C6 = mp.chord('C#3, E3, G#3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C7 = mp.chord('C#3, E3, G#3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C8 = mp.chord('E3, G#3, B3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C9 = mp.chord('E3, G#3, B3') % (1,1) * 2
C10 = mp.chord('C#3, E3, G#3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C11 = mp.chord('C#3, E3, G#3') %  (1,1) * 2
C12 = mp.chord('B2, D#3, F#3') % (1,1) * 2
C13 = mp.chord('B2, D#3, F#3') % (1/4,1/4,1/2) * 6

# Create a new piece with the above chords and notes
My_Instrumental = mp.piece(tracks=[C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13],
                  instruments=['Electric Piano 1', 'Electric Bass (finger)', 'Trumpet', 'Synth Drum', 'Electric Piano 2', 'Acoustic Grand Piano', 'Electric Guitar (jazz)', 'Electric Guitar (clean)', 'SynthBrass 1', 'SynthBrass 2', 'Synth Bass 1', 'Acoustic Guitar (steel)', 'Orchestral Harp', 'Muted Trumpet', 'French Horn', 'Brass Section', 'Acoustic Bass', 'Electric Bass (pick)', 'Fretless Bass', 'Slap Bass 1', 'Synth Bass 2', 'Synth Voice', 'Orchestra Hit', 'Alto Sax', 'Tenor Sax', 'Oboe', 'Bassoon', 'Clarinet', 'Flute', 'Recorder', 'Pan Flute', 'Shakuhachi', 'Whistle', 'Lead 1 (square)', 'Lead 2 (sawtooth)', 'Lead 3 (calliope)', 'Lead 4 (chiff)', 'Lead 5 (charang)', 'Lead 6 (voice)', 'Lead 7 (fifths)', 'Lead 8 (bass + lead)', 'Pad 1 (new age)', 'Pad 2 (warm)', 'Pad 3 (polysynth)', 'Pad 4 (choir)', 'Pad 5 (bowed)', 'Pad 6 (metallic)', 'Pad 7 (halo)', 'Pad 8 (sweep)', 'FX 1 (rain)', 'FX 2 (soundtrack)', 'FX 3 (crystal)', 'FX 4 (atmosphere)', 'FX 5 (brightness)', 'FX 6 (goblins)', 'FX 7 (echoes)', 'FX 8 (sci-fi)'],
                  bpm=120,
                  start_times=[0, 2, 2, 0, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118],
                  track_names=['piano', 'bass', 'trumpet', 'drum', 'electric_piano', 'grand_piano', 'jazz_guitar', 'clean_guitar', 'synth1', 'synth2', 'synth_bass', 'steel_guitar', 'harp', 'muted_trumpet', 'french_horn', 'brass_section', 'acoustic_bass', 'electric_bass_pick', 'fretless_bass', 'slap_bass_1', 'synth_bass_2', 'synth_voice', 'orchestra_hit', 'alto_sax', 'tenor_sax', 'oboe', 'bassoon', 'clarinet', 'flute', 'recorder', 'pan_flute', 'shakuhachi', 'whistle', 'lead1', 'lead2', 'lead3', 'lead4', 'lead5', 'lead6', 'lead7', 'lead8', 'pad1', 'pad2', 'pad3', 'pad4', 'pad5', 'pad6', 'pad7', 'pad8', 'fx1', 'fx2', 'fx3', 'fx4', 'fx5', 'fx6', 'fx7', 'fx8'])





# Chords and notes for the instrumental
C1 = mp.chord('E3, G#3, B3') % (1, 1/8) * 16
C2 = (mp.chord('E3, G#3, B3') % (1,1)) * 16
C3 = (mp.chord('C#3, E3, G#3') % (1/4, 1/4, 1/2) * 8 | mp.chord('E3, G#3, B3') % (1/8, 1/8, 1/4) * 8) * 8
C4 = mp.chord('E3, G#3, B3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 16
C5 = mp.chord('E3, G#3, B3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 16
C6 = mp.chord('C#3, E3, G#3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 16
C7 = mp.chord('C#3, E3, G#3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 16
C8 = mp.chord('E3, G#3, B3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 16
C9 = mp.chord('E3, G#3, B3') % (1,1) * 2
C10 = mp.chord('C#3, E3, G#3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 16
C11 = mp.chord('C#3, E3, G#3') %  (1,1) * 8
C12 = mp.chord('F#2, A2, C#3') %  (1,1) * 8
C13 = mp.chord('G#2, C3, D#3') %  (1,1) * 8
C14 = mp.chord('G#2, C3, D#3') % (1/4,1/4,1/2) * 16
C15 = mp.chord('F#2, A2, C#3') %  (1,1) * 8

# Create a new piece with the above chords and notes
Dank_midz_SD = mp.piece(tracks=[C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14, C15],
                      instruments=['Pizzicato Strings', 'Guitar harmonics', 'Bright Acoustic Piano', 'Woodblock', 'Cello',   'Violin', 'Tuba' , 'Harmonica', 'Banjo',  'Alto Sax',  'Slap Bass 1', 'Distortion Guitar', 'Sitar', 'Kalimba', 'Taiko Drum'],
                      bpm=100,
                      start_times=[0, 2, 2, 0, 4, 6, 8, 10,10, 12, 2, 12, 4, 6, 24],
                      track_names=['clean_guitar', 'bass', 'electric_piano', 'drum', 'grand_piano', 'jazz_guitar', 'trumpet', 'synth1', 'synth2', 'synth_bass', 'distortion_guitar', 'sitar', 'kalimba', 'string', 'synthstrings'])


# Chords and notes for the instrumental
C1 = mp.chord('B3, D#4, F#4') % (1, 1/8) * 6
C2 = (mp.chord('B3, D#4, F#4') % (1,1)) * 2
C3 = (mp.chord('B3, D#4, F#4') % (1/4, 1/4, 1/2) * 8 | mp.chord('F#3, A#3, C#4') % (1/8, 1/8, 1/4) * 8) * 2
C4 = mp.chord('B3, D#4, F#4') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C5 = mp.chord('B3, D#4, F#4') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C6 = mp.chord('F#3, A#3, C#4') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C7 = mp.chord('F#3, A#3, C#4') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C8 = mp.chord('B3, D#4, F#4') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C9 = mp.chord('B3, D#4, F#4') % (1,1) * 2
C10 = mp.chord('F#3, A#3, C#4') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C11 = mp.chord('F#3, A#3, C#4') %  (1,1) * 2
C12 = mp.chord('E3, G#3, B3') % (1,1) * 2
C13 = mp.chord('E3, G#3, B3') % (1/4,1/4,1/2) * 6

# Create a new piece with the above chords and notes
My_Instrumental2 = mp.piece(tracks=[C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13],
                  instruments=['Electric Guitar (clean)', 'Electric Bass (pick)', 'Trumpet', 'Synth Drum', 'Electric Piano 1', 'Acoustic Grand Piano', 'Electric Guitar (jazz)', 'SynthBrass 1', 'SynthBrass 2', 'Synth Bass 1', 'Acoustic Guitar (nylon)', 'Orchestral Harp', 'String Ensemble 1'],
                  bpm=110,
                  start_times=[0, 2, 2, 0, 4, 6, 8, 10, 12, 14, 16, 18, 20],
                  track_names=['clean_guitar', 'bass', 'trumpet', 'drum', 'electric_piano', 'grand_piano', 'jazz_guitar', 'synth1', 'synth2', 'synth_bass', 'nylon_guitar', 'harp', 'string_ensemble'])




# Chords and notes for the instrumental
C1 = mp.chord('G3, B3, D4') % (1, 1/8) * 6
C2 = (mp.chord('G3, B3, D4') % (1,1)) * 2
C3 = (mp.chord('G3, B3, D4') % (1/4, 1/4, 1/2) * 8 | mp.chord('A3, C4, E4') % (1/8, 1/8, 1/4) * 8) * 2
C4 = mp.chord('G3, B3, D4') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C5 = mp.chord('G3, B3, D4') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C6 = mp.chord('A3, C4, E4') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C7 = mp.chord('A3, C4, E4') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C8 = mp.chord('G3, B3, D4') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C9 = mp.chord('G3, B3, D4') % (1,1) * 2
C10 = mp.chord('A3, C4, E4') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 4
C11 = mp.chord('A3, C4, E4') %  (1,1) * 2
C12 = mp.chord('C3, E3, G3') % (1,1) * 2
C13 = mp.chord('C3, E3, G3') % (1/4,1/4,1/2) * 6

# Create a new piece with the above chords and notes
My_Instrumental3 = mp.piece(tracks=[C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13],
                  instruments=['Acoustic Grand Piano', 'Electric Bass (finger)', 'Trumpet', 'Synth Drum', 'Electric Piano 2', 'Electric Piano 1', 'Electric Guitar (jazz)', 'Electric Guitar (clean)', 'SynthBrass 1', 'SynthBrass 2', 'Synth Bass 1', 'Acoustic Guitar (steel)', 'Orchestral Harp'],
                  bpm=110,
                  start_times=[0, 2, 2, 0, 4, 6, 8, 10, 12, 14, 16, 18, 20],
                  track_names=['piano', 'bass', 'trumpet', 'drum', 'electric_piano', 'grand_piano', 'jazz_guitar', 'clean_guitar', 'synth1', 'synth2', 'synth_bass', 'steel_guitar', 'harp'])



# Chords and notes for the instrumental
C1 = mp.chord('G2, B2, D3') % (1, 1/8) * 16
C2 = (mp.chord('G2, B2, D3') % (1,1)) * 16
C3 = (mp.chord('A2, C3, E3') % (1/4, 1/4, 1/2) * 8 | mp.chord('G2, B2, D3') % (1/8, 1/8, 1/4) * 8) * 8
C4 = mp.chord('G2, B2, D3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 16
C5 = mp.chord('G2, B2, D3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 16
C6 = mp.chord('A2, C3, E3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 16
C7 = mp.chord('A2, C3, E3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 16
C8 = mp.chord('G2, B2, D3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 16
C9 = mp.chord('G2, B2, D3') % (1,1) * 2
C10 = mp.chord('A2, C3, E3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 16
C11 = mp.chord('A2, C3, E3') %  (1,1) * 8
C12 = mp.chord('D2, F#2, A2') %  (1,1) * 8
C13 = mp.chord('D2, F#2, A2') %  (1,1) * 8
C14 = mp.chord('C2, E2, G2') % (1/4,1/4,1/2) * 16
C15 = mp.chord('D2, F#2, A2') %  (1,1) * 8

# Create a new piece with the above chords and notes
My_new_song = mp.piece(tracks=[C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14, C15],
                      instruments=['Electric Guitar (clean)', 'Acoustic Bass', 'Electric Piano 1', 'Fiddle', 'Piccolo', 'SynthBrass 1', 'Trumpet', 'Synth Voice', 'Shamisen', 'Alto Sax', 'Synth Bass 1', 'Distortion Guitar', 'Sitar', 'Kalimba', 'String Ensemble 1'],
                      bpm=120,
                      start_times=[0, 2, 2, 0, 4, 6, 8, 10,10, 12, 2, 12, 4, 6, 24],
                      track_names=['clean_guitar', 'bass', 'electric_piano', 'drum', 'percussion', 'synth1', 'trumpet', 'synth2', 'shamisen', 'sax', 'synth_bass', 'distortion_guitar', 'sitar', 'kalimba', 'string'])


C1 = mp.chord('F#3, A3, C#4') % (1, 1/8) * 16
C2 = (mp.chord('F#3, A3, C#4') % (1,1)) * 16
C3 = (mp.chord('A3, C#4, E4') % (1/4, 1/4, 1/2) * 8 | mp.chord('F#3, A3, C#4') % (1/8, 1/8, 1/4) * 8) * 8
C4 = mp.chord('F#3, A3, C#4') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 16
C5 = mp.chord('F#3, A3, C#4') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 16
C6 = mp.chord('A3, C#4, E4') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 16
C7 = mp.chord('A3, C#4, E4') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 16
C8 = mp.chord('F#3, A3, C#4') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 16
C9 = mp.chord('F#3, A3, C#4') % (1,1) * 2
C10 = mp.chord('A3, C#4, E4') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 16
C11 = mp.chord('A3, C#4, E4') %  (1,1) * 8
C12 = mp.chord('G#3, B3, D#4') %  (1,1) * 8
C13 = mp.chord('A3, D4, F#4') %  (1,1) * 8
C14 = mp.chord('A3, D4, F#4') % (1/4,1/4,1/2) * 16
C15 = mp.chord('G#3, B3, D#4') %  (1,1) * 8

# Create a new piece with the above chords and notes
Amber_cover = mp.piece(tracks=[C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14, C15],
                      instruments=['Acoustic Bass', 'Electric Guitar (jazz)', 'Electric Grand Piano', 'Steel Drums', 'SynthStrings 1', 'Acoustic Guitar (nylon)', 'Trumpet' , 'SynthBrass 1', 'SynthBrass 2', 'Synth Bass 1', 'Distortion Guitar', 'Sitar', 'Kalimba', 'String Ensemble 1', 'SynthStrings 2'],
                      bpm=120,
                      start_times=[0, 2, 2, 0, 4, 6, 8, 10,10, 12, 2, 12, 4, 6, 24],
                      track_names=['clean_guitar', 'bass', 'electric_piano', 'drum', 'grand_piano', 'jazz_guitar', 'trumpet', 'synth1', 'synth2', 'synth_bass', 'distortion_guitar', 'sitar', 'kalimba', 'string', 'synthstrings'])


new_piece_name = 'original_piece'




# Chords and notes for the instrumental
C1 = mp.chord('B2, D3, G3') % (1, 1/8) * 16
C2 = (mp.chord('B2, D3, G3') % (1,1)) * 16
C3 = (mp.chord('G2, B2, D3') % (1/4, 1/4, 1/2) * 8 | mp.chord('B2, D3, G3') % (1/8, 1/8, 1/4) * 8) * 8
C4 = mp.chord('B2, D3, G3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 16
C5 = mp.chord('B2, D3, G3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 16
C6 = mp.chord('G2, B2, D3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 16
C7 = mp.chord('G2, B2, D3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 16
C8 = mp.chord('B2, D3, G3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 16
C9 = mp.chord('B2, D3, G3') % (1,1) * 2
C10 = mp.chord('G2, B2, D3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 16
C11 = mp.chord('G2, B2, D3') %  (1,1) * 8
C12 = mp.chord('C2, E2, G2') %  (1,1) * 8
C13 = mp.chord('D2, G2, A2') %  (1,1) * 8
C14 = mp.chord('D2, G2, A2') % (1/4,1/4,1/2) * 16
C15 = mp.chord('C2, E2, G2') %  (1,1) * 8

# Create a new piece with the above chords and notes
gravity_instrumental2 = mp.piece(tracks=[C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14, C15],
                               instruments=['Acoustic Guitar (steel)', 'Electric Guitar (clean)', 'Electric Bass (finger)', 'Alto Sax', 'SynthStrings 1', 'Acoustic Grand Piano', 'Trumpet', 'Synth Voice', 'Synth Bass 1', 'Alto Sax', 'Distortion Guitar', 'Sitar', 'Kalimba', 'String Ensemble 1', 'SynthStrings 2'],
                               bpm=80,
                               start_times=[0, 2, 2, 0, 4, 6, 8, 10,10, 12, 2, 12, 4, 6, 24],
                               track_names=['clean_guitar', 'electric_guitar', 'electric_bass', 'drum', 'synth_strings', 'piano', 'trumpet', 'synth1', 'synth2', 'synth_bass', 'distortion_guitar', 'sitar', 'kalimba', 'string', 'synthstrings'])

# Chords and notes for the instrumental
C1 = mp.chord('G2, B2, D3') % (1, 1/8) * 16
C2 = (mp.chord('G2, B2, D3') % (1, 1)) * 16
C3 = (mp.chord('G2, B2, D3') % (1/4, 1/4, 1/2) * 8 | mp.chord('D2, G2, B2') % (1/8, 1/8, 1/4) * 8) * 8
C4 = mp.chord('G2, B2, D3') % ([3/8, 1/8, 1/4], [3/8, 1/8, 1/4]) * 16
C5 = mp.chord('G2, B2, D3') % ([3/8, 1/8, 1/4], [3/8, 1/8, 1/4]) * 16
C6 = mp.chord('D2, G2, B2') % ([3/8, 1/8, 1/4], [3/8, 1/8, 1/4]) * 16
C7 = mp.chord('D2, G2, B2') % ([3/8, 1/8, 1/4], [3/8, 1/8, 1/4]) * 16
C8 = mp.chord('G2, B2, D3') % ([3/8, 1/8, 1/4], [3/8, 1/8, 1/4]) * 16
C9 = mp.chord('G2, B2, D3') % (1, 1) * 2
C10 = mp.chord('D2, G2, B2') % ([3/8, 1/8, 1/4], [3/8, 1/8, 1/4]) * 16
C11 = mp.chord('D2, G2, B2') % (1, 1) * 8
C12 = mp.chord('A1, D2, F#2') % (1, 1) * 8
C13 = mp.chord('B1, E2, G#2') % (1, 1) * 8
C14 = mp.chord('B1, E2, G#2') % (1/4, 1/4, 1/2) * 16
C15 = mp.chord('A1, D2, F#2') % (1, 1) * 8

# Create a new piece with the above chords and notes
gravity_instrumental = mp.piece(tracks=[C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14, C15],
                               instruments=['Electric Guitar (clean)', 'Acoustic Bass', 'Electric Piano 1', 'Woodblock', 'Violin', 'Acoustic Guitar (steel)', 'Trumpet', 'Synth Voice', 'Synth Bass 2', 'Alto Sax', 'Slap Bass 1', 'Distortion Guitar', 'Sitar', 'Kalimba', 'String Ensemble 1'],
                               bpm=80,
                               start_times=[0, 2, 2, 0, 4, 6, 8, 10, 10, 12, 2, 12, 4, 6, 24],
                               track_names=['clean_guitar', 'bass', 'electric_piano', 'drum', 'grand_piano', 'jazz_guitar', 'trumpet', 'synth1', 'synth2', 'synth_bass', 'distortion_guitar', 'sitar', 'kalimba', 'string', 'synthstrings'])




# new_pieces.append(new_piece)
# new_pieces.append(new_piece2)
# new_pieces.append(new_piece3)
# new_pieces.append(new_piece4)
# new_pieces.append(new_piece5)
# new_pieces.append(new_piece6)
# new_pieces.append(new_piece7)
# new_pieces.append(new_piece8)
# new_pieces.append(new_piece9)
# new_pieces.append(new_piece10)
# new_pieces.append(new_piece11)
# new_pieces.append(new_piece12)
# new_pieces.append(new_piece13)
# new_pieces.append(new_piece14)
# new_pieces.append(new_piece311)
# new_pieces.append(new_piece15)
# new_pieces.append(new_piece16)
# new_pieces.append(new_piece17)
# new_pieces.append(My_Instrumental)



#new_pieces.append(new_piece_SD)
# new_pieces.append(new_piece_SD2)
# new_pieces.append(Dank_midz)
# new_pieces.append(Amber)
# new_pieces.append(My_Instrumental)
# new_pieces.append(My_Instrumental2)
# new_pieces.append(Dank_midz_SD)
# new_pieces.append(My_Instrumental3)
# new_pieces.append(My_new_song)
new_pieces.append(gravity_instrumental)


SavePath = up.AI_Music_Path

SavePath = Path(PureWindowsPath(SavePath, 'Raw_Midz'))
cu.Check_Folder_Exists(SavePath)
counter = 0
for m in new_pieces:
    mp.play(m)
    counter +=1

    current_time1 = datetime.datetime.now()
    current_time = current_time1.strftime('%m-%d-%Y_%H.%M')


    fName = 'Dank_Midz_' + str(counter) + '_' + current_time
    tempfile = 'temp.mid'
    fType1 = tempfile.rfind('.')
    fType = tempfile[fType1:]
    fullPath =Path(PureWindowsPath(SavePath,  fName + fType))
    print(fName)
    print(fType)

    print(fullPath)


    FileName2 = fullPath

    FileName2 = cu.CheckFileLength(FileName2, current_time_f = current_time, Title1=fName, FileType=fType)

    shutil.copyfile(tempfile,fullPath)
    time.sleep(13)



#
#
# # Play the new reggae instrumental
# mp.play(new_piece)



x = GPT.MondeVert()
Song = x.Basic_GPT_Query( Line1_System_Rule=lup.MusicPy_System, Line2_Role=lup.MusicPy_Role, Line3_Format=lup.MusicPy_Format, Line4_Task=lup.MusicPy_Task, SaveFile=True, MakeArt=True, SavePath=SavePath)
print(Song)
#
# from midiutil.MidiFile import MIDIFile
#
# # create your MIDI object
# mf = MIDIFile(1)     # only 1 track
# track = 0   # the only track
#
# time = 0    # start at the beginning
# mf.addTrackName(track, time, "Sample Track")
# mf.addTempo(track, time, 120)
#
# # add some notes
# channel = 0
# volume = 100
#
# pitch = 60           # C4 (middle C)
# time = 0             # start on beat 0
# duration = 1         # 1 beat long
# mf.addNote(track, channel, pitch, time, duration, volume)
#
# pitch = 64           # E4
# time = 2             # start on beat 2
# duration = 1         # 1 beat long
# mf.addNote(track, channel, pitch, time, duration, volume)
#
# pitch = 67           # G4
# time = 4             # start on beat 4
# duration = 1         # 1 beat long
# mf.addNote(track, channel, pitch, time, duration, volume)
#
# # write it to disk
# with open( FileName2,'wb') as outf:
#     mf.writeFile(outf)