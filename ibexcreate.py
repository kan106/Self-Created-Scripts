import re
import string
import datetime
import pandas as pd
import numpy as np
import math
import itertools
import random
from itertools import chain
from random import randrange
inputpath = '/Users/raider/Dropbox/backup/grad school/Lab work/focus particles/ibex itm files/'
outpath = '/Users/raider/Dropbox/backup/grad school/Lab work/focus particles/run lists-new/'

#Name of the file with the texts
TextFileName = "focuspart1"
breakfile = "ibexbreak"
Qfile = "q"
Practice = "PracticeLists"
Fillers = "Fillers"
fillerqs = "fillerq"
infileext = ".itm"

#Name of the file with the questions
numberoflists = range(1,13)
#Do you want a progress bar?
noprogressbar = "false"
#Introduction text
nameofintrofile = "FocusIntro"
#Instructions
instructionfilename = "FocusInstruct"
#Further instruction files
moreinstructions = "FocusQInstruct"
#Demographics collection file
demos = "focusdemos"
#Debriefing file
debrief = "FocusDebrief"
for i in numberoflists:
	outfilename = "focus"
	extension = ".js"
	outfile = open(outpath+outfilename+str(i)+extension, 'w')

	if i in range(1,4):
		x = 1
	elif i in range (4,7):
		x = 2
	elif i in range(7,10):
		x = 3
	elif i in range(10,13):
		x = 4
	stimuli = open(inputpath+TextFileName+str(x)+infileext,'r')
	stimuli = ['\n'.join(stimuli)]
	stimuli = stimuli[0].split("\n\n\n\n")
	random.Random(4).shuffle(stimuli)
	if i in [1,4,7,10]:
		m = 1
	elif i in [2,5,8,11]:
		m = 2
	elif i in [3,6,9,12]:
		m = 3
	probes = open(inputpath+Qfile+str(m)+infileext,'r')
	probes = ['\n'.join(probes)]
	probes = probes[0].split("\n\n\n\n")
	probe1 = probes[0:60]
	probe2 = probes[60:120]
	random.Random(4).shuffle(probe1)
	random.Random(4).shuffle(probe2)
	probes = probe1 + probe2
	
	fillerStim = open(inputpath+Fillers+infileext,'r')
	fillerStim = ['\n'.join(fillerStim)]
	fillerStim = fillerStim[0].split("\n\n\n\n")
	
	fillerQuest = open(inputpath+fillerqs+infileext,'r')
	fillerQuest = ['\n'.join(fillerQuest)]
	fillerQuest = fillerQuest[0].split("\n\n\n\n")
	j = 0

	n = 60
	for item in range(0,30):
		rangefornumber = list(range(0,n))
		randomnumber = random.choice(rangefornumber)
		while stimuli[randomnumber][0] == "F":
			randomnumber = random.choice(rangefornumber)
		stimuli.insert(randomnumber,fillerStim[j])
		stimuli.insert(randomnumber+1,fillerQuest[j])
		j += 1
		n = n+2
	
	PractStim = open(inputpath+Practice+infileext,'r').readlines()
	PractStim = ['\n'.join(PractStim)]
	PractStim = PractStim[0].split("\n\n\n\n")


	#Top file write up
	outfile.write("var shuffleSequence = seq(\"intro\",\"instruct1\",seq(startsWith(\"S_Prac\"), startsWith(\"S_\")), \"instruct2\", sepWith(\"sep\", startsWith(\"Q_\")),\"demos\",\"sr\", \"code\");\n")
	outfile.write("var practiceItemTypes = [\"Practice\"];\n")
	outfile.write("var manualSendResults = true;\n")
	outfile.write("var defaults = [\n")
	outfile.write("\"Question\", {as: [\"True\", \"False\"], randomOrder:false},\n")
	outfile.write("\"DashedSentence\", {mode: \"self-paced reading\"},\n")
	outfile.write("\"Break\", {display:\"in place\"},\n")
	outfile.write("	\"Separator\", {transfer: 1000, normalMessage: \"\"},\n")
	outfile.write("	\"Message\", {hideProgressBar: "+str(noprogressbar)+"},\n")
	outfile.write(" \"Form\", {hideProgressBar: "+str(noprogressbar)+", continueOnReturn: true, saveReactionTime: true}\n")
	outfile.write("];\n")
	outfile.write("var items = [\n")
	outfile.write("[\"sr\", \"__SendResults__\", { }],\n")
	outfile.write("[\"sep\", \"Separator\", {transfer: 500, normalMessage: \"\", ignoreFailure: true}],\n")
	outfile.write("[\"intro\",\"Form\", {html: {include: \""+str(nameofintrofile)+".html\" }, validators: {age: function (s) { if (s.match(/^\d+$/)) return true; else return \"Bad value for \\u2018age\\u2019\"; }}} ],\n")
	outfile.write("[\"instruct1\", \"Message\", {html: { include: \""+str(instructionfilename)+".html\" }}],\n")
	outfile.write("[\"instruct2\", \"Message\", {html: { include: \""+str(moreinstructions)+".html\" }}],\n")
	outfile.write("[\"demos\", \"Form\", {html: { include: \""+str(demos)+".html\" },validators: {age: function (s) { if (s.match(/^\d+$/)) return true; else return \"Bad value for \\u2018age\\u2019\"; }}}],\n")
	outfile.write("[\"code\",\"Form\", {html: {include: \""+str(debrief)+".html\" }, continueMessage: null} ],\n")
	
	#Print the practice lines
	for item in PractStim:
		outfile.write("[\"S__Prac"+str(item)[0:2].replace('\n','')+"\",\n")
		outfile.write("			\"DashedSentence\",{s:\""+str(item)[4:].replace('\n\n\n','').replace('\n\n','\n').replace('\n','\\n')+"\"},\n")
		outfile.write("],")
		outfile.write("\n")
	for item in stimuli:
		n = item.find("\n")
		if item[1] == "Q":
			bar = item.find("|")
			outfile.write("[\"S__"+str(item)[0:n].replace('\n','')+"\",\n")
			outfile.write("			\"Question\", {q: \""+str(item)[n+2:bar].replace('\n\n\n','').replace('\n\n','\n').replace('\n','\\n')+"\", hasCorrect: ")
			if item[bar+2]=="Y":
				outfile.write("1},\n")
			else:
				outfile.write("0},\n")
			outfile.write("],")
			outfile.write("\n")
		else:
			outfile.write("[\"S__"+str(item)[0:n].replace('\n','')+"\",\n")
			outfile.write("			\"DashedSentence\",{s: \""+str(item)[n+2:].replace('\n\n\n','').replace('\n\n','\n').replace('\n','\\n')+"\"},\n")
			outfile.write("],")
			outfile.write("\n")
	for item in probes:
		n = item.find("\n")
		bar = item.find("|")
		outfile.write("[\"Q__"+str(item)[0:n].replace('\n','')+"\",\n")
		outfile.write("			\"Question\", {q: \""+str(item)[n+2:bar].replace('\n\n\n','').replace('\n\n','\n').replace('\n','\\n')+"\", hasCorrect: ")
		if item[bar+2]=="Y":
			outfile.write("1},\n")
		else:
			outfile.write("0},\n")
		outfile.write("],")
		outfile.write("\n")
	outfile.write("];")