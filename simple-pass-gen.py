# Simple Password Generator
# Fixed length password with a mix of uppercase, lowercase and numbers

import random, argparse

parser = argparse.ArgumentParser(description='Generates a password using a mix of upperase, lowercase, numbers and optionally, symbols')
parser.add_argument('-l','--length', type=int, default=8, help='Specify the desired length of the password. Default = 8')
# parser.add_argument('-s','--symbols', type=bool, default=False, help='Specify whether the password should include symbols. Default = False')
args = vars(parser.parse_args())

# Set 1 - Numers
numChars = ['1','2','3','4','5','6','7','8','9']
# Set 2 - Lowercase Charaters
lowerChars = ['a','b','c','d','e','f','g','h','i','j','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# Set 3 - Uppercase Characters
upperChars = ['A','B','C','D','E','F','G','H','I','J','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# Set 4 (Optional) - Symbols
symbolChars = ['#','!','?','@','%','$','%','&','*','^']


tempPassLength = 0
maxPassLength = args['length']
generatedPass = ""


def getPassChar(charSet):
	# Return character from the given list of characters
	setLength = len(charSet)
	char = charSet[random.randint(1,setLength - 1)]
	return char

def getCharSet(charSetNum = 0):
	# Return list of characters based on given number

	numCharSets = 3
	# if args['symbols'] == True:
	#	numCharSets = 4

	# If no number given, return a random list
	if charSetNum == 0:
		charSetNum = random.randint(1,numCharSets)

	if charSetNum == 1:
		return numChars
	elif charSetNum == 2:
		return lowerChars
	# elif charSetNum == 4:
	#	return symbolChars
	else:
		return upperChars

while tempPassLength < maxPassLength:
	generatedPass += getPassChar(getCharSet())
	tempPassLength += 1

print(generatedPass)