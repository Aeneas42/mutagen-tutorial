#!/usr/bin/python3
# project         :mutagen-tutorial
# title           :mutagen_ID3.py
# description     :Examples for using the mutagen API.
# author          :ravila
# date            :December 28, 2014
# version         :
# usage           :
# notes           :
# python_version  :3.4
# ==============================================================================

from mutagen.id3 import ID3

# Print metadata in human-readable form.
metadata = ID3("example.mp3")
print(metadata.pprint())