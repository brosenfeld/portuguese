# -*- coding: latin-1 -*-

import sys

def lookup(letter, predicted):
	if predicted == 0: return letter
	if predicted == 6: return letter.upper()

	accent = int(predicted) % 6

	char = letter

	if letter == 'a': char = unichr(223 + accent)
	if letter == 'e': char = unichr(231 + accent)
	if letter == 'i': char = unichr(235 + accent)
	if letter == 'o': char = unichr(241 + accent)
	if letter == 'u': char = unichr(248 + accent)
	if letter == 'c' and accent == 5: char = unichr(231)

	if int(predicted) > 5: char = char.upper()

	sys.stdout.write(char.encode(sys.stdout.encoding, errors="replace"))

arff = open(sys.argv[1], 'r')
output = open(sys.argv[2], 'r')

for i in range(0, 12): arff.readline()

while (True):
	original = arff.readline()
	fixed = output.readline()

	if original == "": break

	fields = original.split(", ")
	letter = fields[3]

	fields = fixed.split(" ")
	field = fields[2]
	predicted = int(field.split(":")[1])

	if letter == 'SPACE': sys.stdout.write(" "),
	elif letter == 'PERIOD': sys.stdout.write(".")
	elif letter == 'COMMA': sys.stdout.write(',')
	elif predicted == 0: sys.stdout.write(letter)
	elif predicted == 6: sys.stdout.write(letter.upper())
	else: lookup(letter, predicted)

print
