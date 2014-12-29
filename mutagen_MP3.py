#!/usr/bin/python3
# project         :mutagen-tutorial
# title           :mutagen_MP3.py
# description     :Examples using Mutagen's MP3 tagging library.
# author          :ravila
# date            :December 28, 2014
# version         :
# usage           :
# notes           :
# python_version  :3.4
# ==============================================================================

from mutagen.mp3 import MP3

# Print audio attributes
audio = MP3("example.mp3")
print(audio.info.length, audio.info.bitrate)
