import re
import string
import textwrap
# get the paths to the files
inputpath = '/Users/raider/Dropbox/backup/grad school/Lab work/text integration/'
outputpath = '/Users/raider/Dropbox/backup/grad school/Lab work/text integration/'

# read file name
fileprefix= 'stimformat'
filesuffix = '.txt'

targetwordlists = ["detour",	"hike",	"eyewear",	"photos",	"writing",	"beetle",	"window",	"acapella",	"Nutcracker",	"magic show",	"portrait",	"accommodations",	"read",	"market stand",	"gate",	"yacht",	"newspaper",	"ghost",	"plant",	"farmland",	"ice cream",	"beast",	"plaything",	"apple pie",	"mountains",	"stage",	"hairstyle",	"train station",	"wood",	"bicycle",	"vehicle",	"dinner",	"hangover",	"destiny",	"rage",	"seamstress",	"street",	"market",	"hedges",	"cash",	"risk",	"picnic",	"envelope",	"airport",	"tourists",	"work",	"crack",	"technology",	"wet",	"recipes",	"angry",	"investment",	"television",	"savings",	"snowfall",	"safe",	"manager",	"mammals",	"expensive",	"emails",	"traffic",	"trail",	"glasses",	"pictures",	"story",	"bug",	"glass",	"vocalists",	"dance",	"trick",	"painting",	"rooms",	"book",	"vegetables",	"flight",	"cruise",	"journals",	"spirit",	"flower",	"barn",	"dessert",	"lion",	"doll",	"picnic",	"peaks",	"actor",	"salon",	"railroad",	"nails",	"brakes",	"insurance",	"meal",	"vodka",	"future",	"anger",	"stitching",	"neighbor",	"store",	"bush",	"loan",	"danger",	"hamburgers",	"mail",	"terminal",	"resort",	"job",	"leak",	"machine",	"storm",	"chef",	"fight",	"savings",	"screen",	"funds",	"cold",	"bank",	"boss",	"animals",	"money",	"job",	"espresso",	"decorations",	"rent",	"garbage",	"celebrate",	"ride",	"snacks",	"galleries",	"work",	"pub",	"sleep",	"pet",	"jacket",	"shop",	"boss",	"National Park",	"spices",	"dirt",	"parents",	"children",	"study",	"library",	"gym",	"home",	"traffic",	"jacket",	"date",	"date",	"conference",	"thirsty",	"groceries",	"fruit",	"cruise",	"food",	"prize",	"paint",	"ball",	"donations",	"Christmas",	"homecoming",	"chopsticks",	"olympic games",	"disease",	"shore",	"jokes",	"celebration",	"trash",	"battlefield",	"rainforest",	"construction",	"astronauts",	"dream",	"journey",	"college",	"poetry",	"power",	"actress",	"movie scene",	"picture frame",	"computer",	"caffeine",	"holiday",	"landlord",	"sewage",	"anniversary",	"rollercoaster",	"popcorn",	"paintings",	"desk",	"beer",	"bed",	"cat",	"sweater",	"store",	"meeting",	"cabin",	"ginger",	"mud",	"father",	"son",	"exam",	"essay",	"workout",	"house",	"car",	"suit",	"kiss",	"boyfriend",	"meeting",	"water",	"produce",	"blueberries",	"boat",	"desserts",	"achievements",	"brush",	"kick",	"charity",	"holidays",	"alumni",	"dumplings",	"athletes",	"nurse",	"beach",	"laugh",	"party",	"landfill",	"soldier",	"jungle",	"bulldozer",	"stars",	"nightmare",	"plane",	"degree",	"rhymes",	"blackout",	"star",	"film",	"canvas",	"website",	"picture",	"fish",	"cure",	"model",	"forest",	"wedding",	"pet",	"crowd",	"letter",	"mall",	"occupation",	"upgrades",	"transcripts",	"siblings",	"mall",	"injury",	"exercise",	"hospital procedures",	"jog",	"blogs",	"tournament",	"audio equipment",	"Super Bowl",	"house",	"data",	"clutter",	"sports",	"documentary",	"sofa",	"eat",	"trouble",	"melody",	"drums",	"lake",	"meals",	"voicemails",	"love",	"holiday",	"travel",	"champion",	"abdomen",	"heading",	"storm",	"vacation",	"cold",	"lost",	"presentation",	"sink",	"woods",	"road",	"bed",	"celebration",	"exam",	"pier",	"clinic",	"dust",	"championship",	"spot",	"patty",	"concert",	"camera",	"trout",	"medication",	"photoshoot",	"hiker",	"bride",	"collar",	"concert",	"mailbox",	"sunglasses",	"job",	"restoration",	"university",	"brother",	"boutique",	"wheelchair",	"gym",	"doctor",	"race",	"website",	"racers",	"microphones",	"touchdown",	"home",	"statistics",	"mess",	"athlete",	"movie",	"couch",	"meal",	"chaos",	"song",	"noise",	"water",	"dinner",	"call",	"romance",	"vacation",	"journey",	"winner",	"stomach",	"title",	"rain",	"trip",	"illness",	"directions",	"talk",	"shower",	"forest",	"street",	"rest",	"party",	"test",	"dock",	"doctor",	"dirt",	"game",	"stain",	"burger",	"music"]
#number of lists
# write file name
testfilepath = outputpath + 'stimformatted' + filesuffix
# open the files for writing and reading
testfile = open(testfilepath, 'w')
txtfilename = inputpath + fileprefix + filesuffix
txtfile = open(txtfilename, 'rU')
with txtfile as infile, testfile as outfile:
    count = 0
    for line in infile:
        count+=1
        if len(line) > 80:
            outfile.write(textwrap.fill(line, 80)+"\n")
        elif count - 1 != 0:
            outfile.write(line.replace('#','#'))
        elif count -1 ==0:
            outfile.write(line)
    txtfile.close()
    testfile.close()


    # write file name
testfilepath = outputpath + 'stimformatted2' + filesuffix
# open the files for writing and reading
testfile = open(testfilepath, 'w')
txtfilename =  outputpath + 'stimformatted' + filesuffix
txtfile = open(txtfilename, 'rU')
    
with txtfile as infile, testfile as outfile:
    for line in infile:
        if line.strip().endswith(tuple(targetwordlists)):
            outfile.write(line.replace('\n','ERROR'))
        elif line.startswith(tuple(targetwordlists)):
            outfile.write(line.replace('\n','ERROR'))
        else:
            outfile.write(line)
    txtfile.close()
    testfile.close()


print('Done!')
