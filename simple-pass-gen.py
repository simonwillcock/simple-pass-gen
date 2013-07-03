# Title: Simple Password Generator
# Description: Generate a password with a mix of uppercase, lowercase and 
# numbers, with the option to specify the desired length.
# Author: Simon Willcock
# Author Email: github@willcock.com.au

import random, argparse

parser = argparse.ArgumentParser(description='Generates a password using a mix of upperase, lowercase, numbers and optionally, symbols')
parser.add_argument('-l','--length', type=int, default=8, help='Specify the desired length of the password. Default = 8')
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
	
	# Set number of lists defined above
	numCharSets = 3

	# If no number given, return a random list
	if charSetNum == 0:
		charSetNum = random.randint(1,numCharSets)

	if charSetNum == 1:
		return numChars
	elif charSetNum == 2:
		return lowerChars
	else:
		return upperChars

while tempPassLength < maxPassLength:
	generatedPass += getPassChar(getCharSet())
	tempPassLength += 1

print(generatedPass)