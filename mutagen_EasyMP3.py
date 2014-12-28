#!/usr/bin/python3
# project         :mutagen-tutorial
# title           :mutagen_EasyMP3.py
# description     :Examples for using the mutagen API
# author          :ravila
# date            :December 28, 2014
# version         :
# usage           :
# notes           :
# python_version  :3.4
# ==============================================================================

from mutagen.easyid3 import EasyID3

# EasyID3 uses strings to describe the tags.

audio = EasyID3("example.mp3")
print(audio.pprint()) #  Print all tags in human readable form.


# ==============================================================================
# SAMPLE OUTPUT:
#
# album=Aerosmith's Greatest Hits
# artist=Aerosmith
# bpm=82
# date=1993
# genre=Rock
# language=English
# musicbrainz_albumartistid=3d2b98e5-556f-4451-a3ff-c50ea18d57cb
# musicbrainz_albumstatus=bootleg
# musicbrainz_albumtype=album/compilation
# musicbrainz_artistid=3d2b98e5-556f-4451-a3ff-c50ea18d57cb
# musicbrainz_releasegroupid=e2255b98-9ccb-3991-821e-2a3ac6cb44d9
# organization=Sony
# performer=Aerosmith
# title=Last Child
# tracknumber=05 '''
#

