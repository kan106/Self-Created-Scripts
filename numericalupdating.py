import numpy as np
import random
from itertools import chain
from random import randint
from numpy.random import choice
import csv
from random import randrange
#PID1, 2, etc for file names
def split(word): 
    return [char for char in word] 
iterativefilename = "N1"
outfilename = iterativefilename + '.txt'
outputpath = '/Users/raider/Dropbox/backup/grad school/Lab work/numerical updating/' + outfilename
outfile = open(outputpath, 'w')
#write header
outfile.write("Weight\tNested\tProcedure\tNumber\tLetter\tItem00\tItem01\tItem02\tItem03\tItem04\tItem05\tItem06\tItem07\tItem08\tCondition00\tCondition01\tCondition02\tCondition03\tCondition04\tCondition05\tCondition06\tCondition07\n")
d = {}
fillwhen = [2,8,12]

#FILLER SECTION##################################
firstfillers = ["a","b","c","d","e","f","g","h","i"]
numberfillers = ["1","2","3","4","5","6","7","8","9"]
ff = []
for i in range(0,30):
	g = randrange(1,7)
	if g == 1:
		n = 1
	else:
		n = randrange(1,g)
	lf = random.sample(firstfillers,g-n)
	nf = random.sample(numberfillers,n)
	lfnf = [lf + nf]
	lfnf = list(chain(*lfnf))
	random.shuffle(lfnf)		
	ff.append(lfnf)

probeline = ["probe","noprobe"]
for line in ff:
	probeyn = random.sample(probeline,1)
	numb = 0
	letters = 0
	seq = []
	for i in line:
		if i in numberfillers:
			numb = numb+1
		if i in firstfillers:
			letters = letters + 1
	for i in range(len(line)):
		if line[i] in firstfillers:
			seq.append("flu.")
		elif line[i] in numberfillers:
			seq.append("fnu.")
	seq = [''.join(seq)]
	numb = str(numb)
	letters = str(letters)
	condition = [numb,letters,seq]

	if "noprobe" in probeyn:
		outfile.write(str(1)+'\t'+''+'\t'+str("CompPro")+'\t'+str(numb)+'\t'+str(letters)+'\t'+str(line).replace('[','').replace(']','').replace("'",'').replace(",","\t")+'\t')
		i = len(line)
		while i<9:
			outfile.write('\t')
			i+=1		
		outfile.write(str(seq).replace('[','').replace(']','').replace("'",'').replace(".",'\t')+'\n')
	else:
		outfile.write(str(1)+'\t'+''+'\t'+str("CompPro")+'\t'+str(numb)+'\t'+str(letters)+'\t'+str(line).replace('[','').replace(']','').replace("'",'').replace(",","\t")+'\t'+str("?")+'\t')
		i = len(line)
		while i<8:
			outfile.write('\t')
			i+=1		
		outfile.write(str(seq).replace('[','').replace(']','').replace("'",'').replace(".",'\t')+'\n')

##########################################################################################

#do this twice to get 216 trials
for repeatthis in range(1,2):
	numbers = ["1","2","3","4","5","6","7","8","9"]
	stable = ["a","b","c","d","e","f","g","h","i"]
	alpha = ["a","b","c","d","e","f","g","h","i"] 
	allfillers = []
	#Sets up basic lists of each type with n number of items in the list
	SequenceList = []
	sl = 0	#reference for stable letters
	x = 1 #how many numbers to allow in to a sequence
	s = 3 #letter sequence length not being used
	NumSeq = [numbers]
	NumSeq = list(chain(*NumSeq))
	random.shuffle(NumSeq) #actual numbers in the sequence
	duplicated = []
	totalletters = []
	filler = 1
	for j in range(0,len(NumSeq)):
		for i in stable:
			TF = ["True","False"] #Will it be updating or repeating?
			random.shuffle(TF) #Shuffle it so it's random
			d["group" + str(i)] = TF #Create groups a-i with random order of TRUE False using dictionaries
		
		for a in [x for x in range(0,7) if x != s]:
			AlphSeq = [] #create a blank list to have something to append
			letternumber = 0

			while letternumber < a:
				if len(alpha) == 0: #if we run out of letters, renew the list
					alpha = ["a","b","c","d","e","f","g","h","i"] 
					for i in alpha:
						if totalletters.count(i) > 17:
							alpha.remove(i)

				myletter = random.sample(alpha,1) #take a random letter
				if d["group"+str(myletter[0])][0] == "False" or a < 2 or letternumber >= a-1:
					letternumber+=1 #set up conditions for when not to pull a duplicate and to just add one to the letter
					totalletters.append(myletter[0])
				else:
					counter = 0
					while duplicated.count(myletter) >= 12:
					 	myletter = random.sample(alpha,1)
					 	if counter > 20:
					 		letternumber+=1
					 		break
					 	counter +=1
					if duplicated.count(myletter) < 12:
						myletter = myletter*2
						letternumber+=2
						duplicated.append(myletter[0])
						totalletters.append(myletter)
						totalletters = list(chain(*totalletters))
				
				
				d["group"+str(myletter[0])].reverse()
				alpha.remove(myletter[0])
				AlphSeq.append(myletter)
				AlphSeq = list(chain(*AlphSeq))
			
			Sequence = [NumSeq[j]] + AlphSeq #Put the sequence together
			SequenceRepeat = [NumSeq[j]] + AlphSeq + [NumSeq[j]] #Put the repeat sequence together
			SequenceList.append(Sequence)
			SequenceList.append(SequenceRepeat)

	random.shuffle(SequenceList) #Shuffle the sequence so the lines are not in order
	Check = "ERROR"
	z = 1
	while Check == "ERROR" and z < 1000000:
 		for i in range(0,len(SequenceList)):
 			if SequenceList[i][0] == SequenceList[i-1][0]:
 				Check = "ERROR"
 				random.shuffle(SequenceList)
 				break
 			if i > len(SequenceList) - 2:
 				Check = "Good"
 				break
 			elif z == 999999: 
 				print("No good combinations. Rerun this script")
 			else:
 				continue
 		z = 1+z
	fillers = ["a","b","c","d","e","f","g","h","i"]
	for addingfillers in range(1,3):
		if len(fillers) == 0:
			fillers = ["a","b","c","d","e","f","g","h","i"]
		for filler in range(2,5): #number of items for the line
			filleralpha = random.sample(fillers,filler) #get this many letters
			allfillers.append(filleralpha) #create ongoing list
			for each in filleralpha: 
				fillers.remove(each) #get rid of those fillers
		for each in range(0,len(allfillers)):
			randomnumber = randrange(len(SequenceList))
			SequenceList.insert(randomnumber,allfillers[each])
	repeatletter = ""
	probeline = ["probe","noprobe"]
# 	#get data about conditions for each line and write to file
	for line in SequenceList:
		probeyn = random.sample(probeline,1)
		numb = 0
		letters = 0
		seq = []
		for i in line:
			if i in numbers:
				numb = numb+1 #how many numbers, repeat is 2 and update is 1
			if i in stable:
				letters = letters + 1
		for i in range(len(line)):
			if i == 0 and line[i] not in stable:
				seq.append("nu.")
			elif line[0] in stable:
				seq.append("flu.")
			elif line[i] in numbers:
				seq.append("nr.")
			elif line[i] == line[i-1] and line[i] not in numbers:
				seq.append("lr.")
			elif i == 1 and line[1] == repeatletter:
				seq.append("lr.")
				print("Found a problem.")
				print(repeatletter)
				print(line)
				print("Rerun this script. Don't accept.")
			else:
				seq.append("lu.")

			if i == len(line) and line[i] in stable:
				repeatletter = line[i]

		seq = [''.join(seq)]
		numb = str(numb)
		letters = str(letters)
		condition = [numbers,letters,seq]
		if "noprobe" in probeyn or line[0] in stable:
			outfile.write(str(1)+'\t'+''+'\t'+str("CompPro")+'\t'+str(numb)+'\t'+str(letters)+'\t'+str(line).replace('[','').replace(']','').replace("'",'').replace(",","\t")+'\t')
			i = len(line)
			while i<9:
				outfile.write('\t')
				i+=1		
			outfile.write(str(seq).replace('[','').replace(']','').replace("'",'').replace(".",'\t')+'\n')
		else:
			outfile.write(str(1)+'\t'+''+'\t'+str("CompPro")+'\t'+str(numb)+'\t'+str(letters)+'\t'+str(line).replace('[','').replace(']','').replace("'",'').replace(",","\t")+'\t'+str("?")+'\t')
			i = len(line)
			while i<8:
				outfile.write('\t')
				i+=1		
			outfile.write(str(seq).replace('[','').replace(']','').replace("'",'').replace(".",'\t')+'\n')

	#get counts of everything
	flat_list = [item for sublist in SequenceList for item in sublist]
	numberseparate = [item for sublist in SequenceList for item in sublist if item in numbers]
	alphaseparate = [item for sublist in SequenceList for item in sublist if item in stable]
	alphaseparate = [item.split(' ') for item in alphaseparate]
	alphaseparate = list(chain(*alphaseparate))
#
outfile.close()


infilename = outfilename
inputpath = '/Users/raider/Dropbox/backup/grad school/Lab work/numerical updating/' + infilename
csvfile = open(inputpath, 'r')
csvreader = csv.reader(csvfile,delimiter='\t')
totalnumbers=0
totalletters=0
numbers = ["1","2","3","4","5","6","7","8","9"]
lengths = []
listed = []
filllisted = []
sequencelist = []
duplicatenum = []
duplicatealpha = []
sequencelist = []
fillseq = 0
fillernum = 0
fillalph = 0
next(csvreader)
linenumber=0
for line in csvreader:
	if line[14][0] == "f":
		for i in line[5:13]:
			i = i.replace(' ','').replace('?','')
			if i in stable:
				fillalph +=1
			if i in stable:
				fillernum +=1
			filllisted.append(i)
	else:
		linenumber+=1
		sequencenum=0
		for i in line[5:13]:
			i = i.replace(' ','').replace('?','')
			if i in stable:
				sequencenum +=1
			listed.append(i)
		sequencelist.append(sequencenum)
listed = list(filter(None, listed))
filllisted = list(filter(None,filllisted))
fnumberseparate = [item for line in filllisted for item in line if item in numbers]
falphaseparate = [item for line in filllisted for item in line if item in stable]
numberseparate = [item for line in listed for item in line if item in numbers]
alphaseparate = [item for line in listed for item in line if item in stable]
print("trials: ",linenumber)
print("total elements: ",len(listed))
print("total fillers: ",len(filllisted))
print("total numbers: ",len(numberseparate))
count=0
for i in range(0,len(numberseparate)-1):
 	if(numberseparate[i]==numberseparate[i+1]):
 		count+=1
 		duplicatenum.append(numberseparate[i])
print("Duplicate Numbers: ",count)
print("Updating Numbers: ",len(numberseparate)-count)
print("Total Letters: ",len(alphaseparate))
count=0
for i in range(0,len(alphaseparate)-1):
 	if(alphaseparate[i]==alphaseparate[i+1]):
 		count+=1
 		duplicatealpha.append(alphaseparate[i])

print("Duplicate letters: ",count)
print("Updating letters: ",len(alphaseparate)-count)

for i in range(0,7):
 	print("sequence length ",i,": ",sequencelist.count(i))
for i in numbers:
 	print("updating ",i,": ",numberseparate.count(i)-duplicatenum.count(i), "duplicate ", i,": ",duplicatenum.count(i))
for i in stable:
 	print("updating ",i,": ",alphaseparate.count(i)-duplicatealpha.count(i), "duplicate ", i,": ",duplicatealpha.count(i))
