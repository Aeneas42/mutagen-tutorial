#!/usr/bin/python3
# project         :mutagen-tutorial
# title           :mutagen_EasyMP3.py
# description     :Examples using Mutagen's EasyMP3 tagging library.
# author          :ravila
# date            :December 28, 2014
# version         :
# usage           :
# notes           :EasyID3 is a wrapper around mutagen.id3.ID3 to make ID3 tags appear more like Vorbis or APEv2 tags.
# python_version  :3.4
# ==============================================================================

from mutagen.easyid3 import EasyID3

# EasyID3 uses strings to describe the tags.
# Note, not all ID3 standard tags are supported.

audio = EasyID3("example.mp3")
print("----------------------------------")
print("Example Song Metadata:")
print("----------------------------------")
print(audio.pprint())  # Print all available tags in human readable form.

# Creating a custom tag using a TXXX Key
print("----------------------------------")
print("Valid tags:")
audio.RegisterTXXXKey('valence', 'VALENCE')
print(EasyID3.valid_keys.keys())
print("----------------------------------")

# Assigning tag values
audio["title"] = u"Last Child"
audio.save()
print(audio["title"])

audio["valence"] = u"3.4"
audio.save()
print(audio["valence"])
