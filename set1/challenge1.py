#Cryptopals Challenge Set 1 Challenge 1

import codecs


'''
This function gives hex to base64 byte conversion 
@Input: Hex String
@Output: Base64 byte array
'''
def hex_to_base64(hex_string):
	
	ba = bytearray.fromhex(hex_string)
	ba_base64 = codecs.encode(ba, 'base64_codec')
	return ba_base64

if __name__ == "__main__":

	hex_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
	print(hex_to_base64(hex_string))


