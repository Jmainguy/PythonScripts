#!/usr/bin/python
import sys, getopt, os, re, crithit
EPISODE=str(sys.argv[1])
mp3 = 'CriticalHit' + EPISODE + '.mp3'
file2 = open("index.html.tmp", "w")
with open("index.html", "r") as file:
    for line in file:
        if 'source' in line:
            line = '  <source src="' + mp3 + '" type="audio/mpeg">\n'
        elif 'Episode' in line:
            line = '<h1>Episode ' + EPISODE + '</h1>\n'
        file2.write(line)
file.close
file2.close
os.rename('index.html.tmp','index.html')
