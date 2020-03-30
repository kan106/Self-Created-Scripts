import re
import string
import textwrap
import csv
from collections import Counter
import itertools
path = '/Users/raider/Dropbox/backup/grad school/Lab work/text integration/stimuli/'
FileName = "TILinesBroken.csv"
WriteOut = "TI.IAsAdded.csv"
FileIn = path + FileName
FileOut = path + WriteOut
Opened = open(FileIn, 'r')
csvreader = csv.reader(Opened,escapechar='\\')
outfile = open(FileOut, 'w')
writer = csv.writer(outfile)
header = ("ItemNum,$condition,$Text,$Word1,$Word2,List,$Ante1,$Ante2,$Question,ButtonPress,TitlePresent,$Title\n")
l=0
outfile.write(header)
for line in csvreader:
	if l == 0:
		pass
	else:
		secondarywordlist = [line[6],line[7]] #two columns containing a set of words to look for and to avoid line breaking at
		targetwordlists = [line[3],line[4]] #two columns containing a set of words to look for and to avoid line breaking at
		d = line[2].split('.',2) #Split at periods
		e = ". *" #First word after a period is always an interest area
		f = e.join(d) # Join at period
		f = f.replace("znzn"," znzn") #Make sure that there's a gap before a line break for word count issues
		f = f.replace("  "," ") #Replace any double spaces for word count issues
		f = f.replace(" "," ") #May not help but part of trouble shooting space not read as space
		lastword = f.split()[-1] #get the last word of the passage
		secondtolast = f.split()[-2:-1] #Get the second to last word of the passage
		secondtolast = "".join(secondtolast) #Make the second to last word of the passage a string
		f =  f.rsplit(' ', 2)[0] #Split the whole passage in two with last two words on one side and the rest of the passage on the other
		f = f + " *"+ secondtolast + " *" + lastword #Add the last two words back on but with interest areas marked
	#	f = f.replace(lastword,"*"+lastword) 
		counter = 1 #Start counting, 1 = word from first column, 2 = word from second column
		for word in targetwordlists: #there are two lists of target words for each passage, cycle through them both.
			allwords = re.split(" "+word, f, re.IGNORECASE) #Split the passage in two based on the location of the target word
			fullcount = re.split(f[-1],f,re.IGNORECASE) #Split the passage in two based on the last word
			fullcount = len(re.findall(r' ',fullcount[0]))+1 #Get the full word count by counting the spaces from above and adding one for the removal of the last word.
			wordloc = len(re.findall(r' ', allwords[0]))+1 #Find out where the critical word appears by counting the words that occur before the split. The actual number is one less than the real total and is the space before the critical word
			setup = f.split() #Split the passage up into single words

			if counter == 1: #First critical word action
				word1 = f.split()[wordloc-3:wordloc] #Get the second previous word before the target word
				word1 = " ".join(word1)
				word2 = f.split()[wordloc-2:wordloc-1] #get the word 2 before the target word so we can see if it's the end of the sentence
				word2 = " ".join(word2)
				word3 = f.split()[wordloc-1:wordloc+2] #One word before critical, get more than just the one word though because some words occur more than once in the passage, e.g., "the" 
				word3 = " ".join(word3) #Rejoin so its not list of several words	
				word4 = f.split()[wordloc] #Target word
				word4 = "".join(word4)
				word5 = f.split()[wordloc+1:wordloc+4] #Target word + 1
				word5 = " ".join(word5)
				word6 = f.split()[wordloc+2:wordloc+5] #Target word + 2
				word6 = " ".join(word6)
				word13 = f.split()[wordloc+3:wordloc+6] #Target word +3
				word13 = " ".join(word13)
				word22 = f.split()[wordloc+4:wordloc+7] #Target word +4, needed to end the target word for word +3
				word22 = " ".join(word22)
	#			word24 = f.split()[wordloc+5:wordloc+8]
	#			word24 = " ".join(word24)
				if  len(line) >= fullcount: #Stop the system from going out of range.
					pass
				else:
					word26 = f.split()[wordloc+5:wordloc+8] # If there's more words to be found, get the target word + 5
					word26 = " ".join(word26)
			else:
				word28 = f.split()[wordloc-3:wordloc]
				word28 = " ".join(word1)
				word29 = f.split()[wordloc-2:wordloc-1]
				word29 = " ".join(word29)
				word9 = f.split()[wordloc-1:wordloc+2] #See above notes
				word9 = " ".join(word9)
				word10 = f.split()[wordloc] 
				word10 = "".join(word10)
				word11 = f.split()[wordloc+1:wordloc+4]
				word11 = " ".join(word11)
				word12 = f.split()[wordloc+2:wordloc+5]
				word12 = " ".join(word12)
				word14 = f.split()[wordloc+3:wordloc+6]
				word14 = " ".join(word14)
				word21 = f.split()[wordloc+4:wordloc+7]
				word21 = " ".join(word21)
	#			word23 = f.split()[wordloc+5:wordloc+8]
	#			word23 = " ".join(word23)
				if  len(line) >= fullcount:
					pass
				else:
					word25 = f.split()[wordloc+5:wordloc+8]
					word25 = " ".join(word25)			
			counter = counter+1
		antecount = 1
		for wordAnte in secondarywordlist: #Do this again for the other set of target words but this time check to see if they exist in the passage first
			if wordAnte in f and wordAnte!="":
				if antecount == 1:
					try: 
						n = int(line[12])
					except ValueError:
						n = 1
				else:
					try: 
						n = int(line[13])
					except ValueError:
						n = 1
				if l == 48:
					print(n)
				allwords = re.split(wordAnte, f,n)
				if n == 2:
					allwords = [""+wordAnte.join(allwords[0:2]),allwords[2]]
				if n == 3:
					allwords = [""+wordAnte.join(allwords[0:3]),allwords[3]]
				wordloc = len(re.findall(r' ', allwords[0]))
				wordt = "".join(f.split()[wordloc])
				if l == 48:
					print(wordt)
				if wordt[-1] != "." and antecount == 1:
					word16 = f.split()[wordloc-1:wordloc+2]
					word16 = " ".join(word16)
					word18 = f.split()[wordloc:wordloc+2]
					word18 = " ".join(word18)

					print(word18)
					word19 = f.split()[wordloc+1:wordloc+3]
					word19 = " ".join(word19)
					word20 = f.split()[wordloc+2:wordloc+4]
					word20 = " ".join(word20)
					word27 = f.split()[wordloc+3:wordloc+5]
					word27 = " ".join(word27)
					word30 = f.split()[wordloc+4:wordloc+6]
					word30 = " ".join(word30)
				else:
					pass
				antecount = antecount+1
				newstring = f.replace(" "+word16," *"+word16).replace(" "+word18," *"+word18).replace(" "+word19," *"+word19).replace(" "+word20," *"+word20).replace(" "+word27," *"+word27).replace(" "+word30," *"+word30) #Only replace these if they existed in the passage
				
			else:
				newstring = f
		#print(word24)	

		if word2[-1] == ".":
			newstring = newstring.replace(" "+word1," *"+word1).replace(" "+word2," *"+word2)
		elif word29[-1] == ".":
			newstring = newstring.replace(" "+word28," *"+word28).replace(" "+word29," *"+word29)
		else:
			pass

		newstring = newstring.replace("  "," ").replace("* ","*").replace(" "+word3," *"+word3).replace(" "+word4," *"+word4).replace(" "+word5," *"+word5).replace(" "+word6," *"+word6).replace(" "+word13," *"+word13).replace(" "+word22," *"+word22)

		#.replace(" "+word24," *"+word24)
		try:
			newstring = newstring.replace(" "+word26," *"+word26) #Sometimes words 25 and 26 exceeded the number of words in the passage
		except NameError:
			pass

		newstring = newstring.replace(" "+word9," *"+word9).replace(" "+word10," *"+word10).replace(" "+word11," *"+word11).replace(" "+word12," *"+word12).replace(" "+word14," *"+word14).replace(" "+word21," *"+word21)
		#.replace(" "+word23," *"+word23)

		try:
			newstring = newstring.replace(" "+word25," *"+word25)
		except NameError:
			pass
		newstring = '"*' + newstring.replace("znzn","\\n\\n") + '"'
		newstring = newstring.replace("*\\n\\n","\\n\\n*")
		newstring = newstring.replace("**","jjj")
		newstring = newstring.replace("jjj","*")
		newstring = newstring.replace(" *","*")
		line[1] = '"' + line[1] + '"'
		line[3] = '"' + line[3] + '"'
		line[4] = '"' + line[4] + '"'
		line[8] = '"' + line[8] + '"'
		if line[6] == "":
			line[6] = '"empty"'
			line[7] = '"empty"'
		else:
			line[6] = '"' + line[6] + '"'
			line[7] = '"' + line[7] + '"'
		ListNum = line[5].replace("A","1").replace("B","2").replace("C","3")
		writer.writerow([line[0],line[1],newstring,line[3],line[4],ListNum,line[6],line[7],line[8],line[9],line[10],line[11]])

	#	print(newstring)
	l = l+1