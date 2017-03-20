#Cryptopals Challenge Set 1 Challenge 2

import codecs


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

if __name__ == "__main__":

	hex_string_1 = '1c0111001f010100061a024b53535009181c'
	hex_string_2 = '686974207468652062756c6c277320657965'
	print(xor_2_strings(hex_string_1, hex_string_2))


