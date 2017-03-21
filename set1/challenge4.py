#Cryptopals Challenge Set 1 Challenge 3

import collections
import codecs

dictionary = ['a', 'an', 'in', 'on', 'of', 'the']

'''
This function gives XOR of 2 hex strings 
@Input: 2 Hex strings of equal length
@Output: XOR output of 2 strings
'''
def xor_2_strings(hex_string_1, hex_string_2):
	if (len(hex_string_1) == len(hex_string_2)):
		return hex(int(hex_string_1, 16) ^ int(hex_string_2, 16))
	else:
		return 0

'''
1. Iterate from decimal 33 to 126 (ascii chars)
2. Get the hex value of decimal 
3. Encode string of length 34 with the hex value
4. xor original string with generated string
5. Print the string in character format
6. Check for common words like a/the/an/of
@Input: hex string
@Output: prints all decoded strings
'''

def find_key(hex_string):
	
	for dec in range(33, 126):
		generated_hex_string = ""
		for i in range(len(hex_string)//2):
			generated_hex_string += hex(dec)[2:]
		xored_string = xor_2_strings(hex_string, generated_hex_string)[2:]
		key = chr(dec)
		decoded_string = bytearray.fromhex(xored_string).decode("utf-8")
		for word in dictionary:
			if word in decoded_string:
				print("String: ", decoded_string)
				print("Key: ", key, "\n")
		#Character frequency check
#		letters = collections.Counter(decoded_string)
#		print("Character frequency: ", letters, "\n")

if __name__ == "__main__":
	
	in_file = open("input_challenge4.txt", "rt")
	while True:
		hex_string = in_file.readline()
		if not hex_string:
			break
		find_key(hex_string)


