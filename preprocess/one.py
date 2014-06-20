import sys, string
from unidecode import unidecode

# Table of accented-characters and their accent codes
accent_code = {
	224: 1, 225: 2, 226: 3, 227: 4, 	
	232: 1, 233: 2, 234: 3,				
	236: 1, 237: 2, 238: 3,				
	242: 1, 243: 2, 244: 3, 245: 4,		
	249: 1, 250: 2, 251: 3, 			
	231: 5,								
}

alphabet = '0123456789abcdefghijklmnopqrstuvwxyz., '

def clean_char(c):
	c = unidecode(c).lower()
	return convert(c)

def convert(c):
	if c == ',': return "COMMA"
	if c == ' ': return "SPACE"
	if c == '.': return "PERIOD"
	if c not in alphabet: return "OTHER"
	return c

#ARFF formatting
print "@RELATION\tportuguese"
print
print "@ATTRIBUTE\tprev\t{a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, SPACE, PERIOD, COMMA, OTHER, BOS, EOS}"
print "@ATTRIBUTE\tletter\t{a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, SPACE, PERIOD, COMMA, OTHER, BOS, EOS}"
print "@ATTRIBUTE\tnext\t{a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, SPACE, PERIOD, COMMA, OTHER, BOS, EOS}"
print "@ATTRIBUTE\ttarget\t{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}"
print
print "@data"

# Read in the file and get rid of all of the newline characters
text = sys.stdin.read()
text = text.decode('utf-8').replace('\n', '')

# Initialize the character variables
prev, next, char = "BOS", "BOS", "BOS"

# Convert the corpus to an array of characters
text = list(text)

# Iterate over the corpus
for i in range(0, len(text)):

	prev = char # Update the prev character

	# Try to get the next character
	try: next = clean_char(text[i+1])
	except Exception, e: next = "EOS"

	c = text[i] # The current character

	clean = unidecode(c) # ascii
	upper = clean.isupper() # boolean indicating upper or lower
	clean = clean.lower() # lower-case ascii

	# If the letter is a valid letter
	try:
		char = convert(clean) # Get the numeric value of the letter

		# Set the code (see README for list of possibilities)
		code = (accent_code[ord(c.lower())] if ord(c.lower()) in accent_code else 0)
		code += (6 if upper else 0)

		print "{0}, {1}, {2}, {3}".format(prev, char, next, code)
		#print "{0}, {1}, {2}, {3}".format(chr(prev), chr(num), chr(next), code)

	except Exception, e: pass