#!/usr/bin/python
#This script downloads the podcast from Critical Hit
#run it with the episode number as the argument
#Use a second argument if you want a range of Episodes
#Example. ./crithit.py 237 
#would download episode 237
#./crithit 8 237
#Would download episodes 8 through 237 to the current dir.
import sys, getopt, urllib
if len(sys.argv) == 3:
	EPISODE=int(sys.argv[1])
	END=int(sys.argv[2])
elif len(sys.argv) == 2:
	EPISODE=int(sys.argv[1])
	END=int(sys.argv[1])
else:
	print "pass the episode number you want to download as the first argument"
        sys.exit(1)

#http://media.libsyn.com/media/majorspoilers/critical_hit008.mp3
mylist1 = range(8, 10)
mylist1.append(25)
#http://media.libsyn.com/media/majorspoilers/critical_hit11.mp3
mylist2 = range(11, 20)
mylist2.extend(range(23, 29))
mylist2.append(43)
mylist2.extend(range(52, 54))
#http://media.libsyn.com/media/majorspoilers/criticalhit_30.mp3
mylist3 = [ 21, 22, 30, 39, 40]
mylist3.extend(range(32, 37))
mylist3.extend(range(42, 50))
mylist3.extend(range(52, 54))
#http://media.libsyn.com/media/majorspoilers/critical_hit_31.mp3
mylist4 = [31, 50, 190, 192, 193, 197, 172, 173]
mylist4.extend(range(37, 42))
mylist4.extend(range(55, 67))
mylist4.extend(range(68, 72))
mylist4.extend(range(73, 93))
mylist4.extend(range(94, 115))
mylist4.extend(range(116, 155))
mylist4.extend(range(156, 159))
mylist4.extend(range(183, 185))
mylist4.extend(range(202, 217))
#http://traffic.libsyn.com/majorspoilers/criticial_hit_51.mp3
mylist5 = [51, 115]
#http://traffic.libsyn.com/majorspoilers/critical_hit54.mp3
mylist6 = [54]
#http://traffic.libsyn.com/majorspoilers/critical-hit-67.mp3
mylist7 = range(159, 167)
mylist7.append(67)
mylist7.append(191)
mylist7.extend(range(169, 172))
mylist7.extend(range(175, 183))
mylist7.extend(range(185, 190))
mylist7.extend(range(194, 200))
mylist7.remove(195)
mylist7.remove(198)
mylist7.remove(164)
mylist7.remove(187)
mylist7.remove(188)
#http://traffic.libsyn.com/majorspoilers/critical_hit-72.mp3
mylist8 = [72]
#http://traffic.libsyn.com/majorspoilers/critical_hit_93fixed.mp3
mylist9 = [93]
#http://traffic.libsyn.com/majorspoilers/criticalhit155_fixed.mp3
mylist10 = [155]
#http://traffic.libsyn.com/majorspoilers/critical-hit-167mp3.mp3
mylist11 = [167]
#http://traffic.libsyn.com/majorspoilers/critical-hit.mp3
mylist12 = [168]
#http://traffic.libsyn.com/majorspoilers/critical-hit-174_mixdown.output-major-spoilers-pod.mp3
mylist13 = [174]
#http://traffic.libsyn.com/majorspoilers/critial-hit-200.mp3
mylist14 = [200]
#http://traffic.libsyn.com/majorspoilers/criticalhit164.mp3
mylist15 = [164, 187, 188, 195, 198, 201]
#http://traffic.libsyn.com/majorspoilers/CriticalHit217.mp3
mylist16 = range(217, 300)

while (EPISODE <= END):
	
	if EPISODE in mylist1:
		GETURL=urllib.urlretrieve ("http://media.libsyn.com/media/majorspoilers/critical_hit" + str(EPISODE).zfill(3) + ".mp3", "CriticalHit" + str(EPISODE).zfill(3) + ".mp3")
	elif EPISODE in mylist2:
		GETURL=urllib.urlretrieve ("http://media.libsyn.com/media/majorspoilers/critical_hit" + str(EPISODE) + ".mp3", "CriticalHit" + str(EPISODE).zfill(3) + ".mp3")
	elif EPISODE in mylist3:
		GETURL=urllib.urlretrieve ("http://media.libsyn.com/media/majorspoilers/criticalhit_" + str(EPISODE) + ".mp3", "CriticalHit" + str(EPISODE).zfill(3) + ".mp3")
	elif EPISODE in mylist4:
		GETURL=urllib.urlretrieve ("http://media.libsyn.com/media/majorspoilers/critical_hit_" + str(EPISODE) + ".mp3", "CriticalHit" + str(EPISODE).zfill(3) + ".mp3")
	elif EPISODE in mylist5:
		GETURL=urllib.urlretrieve ("http://media.libsyn.com/media/majorspoilers/criticial_hit_" + str(EPISODE) + ".mp3", "CriticalHit" + str(EPISODE).zfill(3) + ".mp3")
	elif EPISODE in mylist6:
		GETURL=urllib.urlretrieve ("http://traffic.libsyn.com/majorspoilers/critical_hit" + str(EPISODE) + ".mp3", "CriticalHit" + str(EPISODE).zfill(3) + ".mp3")
	elif EPISODE in mylist7:
		GETURL=urllib.urlretrieve ("http://traffic.libsyn.com/majorspoilers/critical-hit-" + str(EPISODE) + ".mp3", "CriticalHit" + str(EPISODE).zfill(3) + ".mp3")
	elif EPISODE in mylist8:
		GETURL=urllib.urlretrieve ("http://traffic.libsyn.com/majorspoilers/critical_hit-" + str(EPISODE) + ".mp3", "CriticalHit" + str(EPISODE).zfill(3) + ".mp3")
	elif EPISODE in mylist9:
		GETURL=urllib.urlretrieve ("http://traffic.libsyn.com/majorspoilers/critical_hit_" + str(EPISODE) + "fixed.mp3", "CriticalHit" + str(EPISODE).zfill(3) + ".mp3")
	elif EPISODE in mylist10:
		GETURL=urllib.urlretrieve ("http://traffic.libsyn.com/majorspoilers/criticalhit" + str(EPISODE) + "_fixed.mp3", "CriticalHit" + str(EPISODE).zfill(3) + ".mp3")
	elif EPISODE in mylist11:
		GETURL=urllib.urlretrieve ("http://traffic.libsyn.com/majorspoilers/critical-hit-" + str(EPISODE) + "mp3.mp3", "CriticalHit" + str(EPISODE).zfill(3) + ".mp3")
	elif EPISODE in mylist12:
		GETURL=urllib.urlretrieve ("http://traffic.libsyn.com/majorspoilers/critical-hit" + ".mp3", "CriticalHit" + str(EPISODE).zfill(3) + ".mp3")
	elif EPISODE in mylist13:
		GETURL=urllib.urlretrieve ("http://traffic.libsyn.com/majorspoilers/critical-hit-" + str(EPISODE) + "_mixdown.output-major-spoilers-pod.mp3", "CriticalHit" + str(EPISODE).zfill(3) + ".mp3")
	if EPISODE in mylist14:
		GETURL=urllib.urlretrieve ("http://traffic.libsyn.com/majorspoilers/critial-hit-" + str(EPISODE) + ".mp3", "CriticalHit" + str(EPISODE).zfill(3) + ".mp3")
	if EPISODE in mylist15:
		GETURL=urllib.urlretrieve ("http://traffic.libsyn.com/majorspoilers/criticalhit" + str(EPISODE) + ".mp3", "CriticalHit" + str(EPISODE).zfill(3) + ".mp3")
	if EPISODE in mylist16:
		GETURL=urllib.urlretrieve ("http://traffic.libsyn.com/majorspoilers/CriticalHit" + str(EPISODE) + ".mp3", "CriticalHit" + str(EPISODE).zfill(3) + ".mp3")
	GETURL
	EPISODE += 1
