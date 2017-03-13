#Programmed by Connor McNaboe 
#Questions or suggestions refer to https://github.com/zerodarkbirdy/CaesarCipher
#
#This program takes a text file and encrypts it using a caesar cipher.

import argparse
import os
import time 
import sys

parser = argparse.ArgumentParser() # Define comamand line args
parser.add_argument("-k", type=int, help="Enter a keyvalue")
parser.add_argument("-f", help="Enter filename that will be encrypted") 
parser.add_argument("-e", help="Option to encrypt", action="store_true") 
parser.add_argument("-d", help="Option to decrypt", action="store_true") 
args = parser.parse_args()
key = args.k #agruments to variables 
txt = args.f
ecrpt = args.e
dcrpt = args.d



def main(k, f, encrpt, dcrpt):
	#Declare variables
	ascii_dict  = create_ascii_dict() #Check all arguments are filled 
	if k is None or f is None: 
		sys.exit("Error: Enter both key and filename")
	if encrpt is False and dcrpt is False:
		sys.exit("Error: Enter an option to encrypt or decrypt a file")
	if k > 255: 
		k = k % 255		 
	createFile(f, k, ascii_dict, encrpt, dcrpt) #Encrypt File 
		 
		
def create_ascii_dict(): # Create ascii dictionary 
	ascii_dict = dict()
	ascii_in_number = range(0,256)
	for i in ascii_in_number:
		ascii_dict[str(i)] = chr(i)
	return ascii_dict

def crypt(txt, key, ascii_dict, dcrpt, encrpt): #Encrypt the file 
	txt2 = []
	for value in txt: 
		txt2 += [k for k, v in ascii_dict.iteritems() if v == value] #Map all values in the txt to value in ascii dict
	txt2 =  [int(i) for i in txt2]# Convert to integer
	if encrpt is True: 
		txt2 = [i + key for i in txt2] #Increment w/ key
	elif dcrpt is True: 
		txt2 = [i - key for i in txt2]
	txt2 = [i + 256 if i < 0 else i - 256 if i > 256 else i for i in txt2] 
	txt2 = [str(i) for i in txt2]
	txt_e = []
	for i in txt2: 		
		txt_e += ascii_dict[i]	#Re-map to ascii 
	return txt_e
	
def rtnTxt(txt): #Put the string back together 
	txt = ''.join(txt)
	return txt

def createFile(txt, key, ascii_dict, encrpt, dcrpt): # Create new encrypted file
	statBar = ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', "100%"]
	status = '' 
	for i  in statBar: 
		sys.stdout.flush()
		time.sleep(0.15)
		sys.stdout.write(i)
	  
	try: 
		with open(os.path.expanduser(txt), 'r+') as f: 
			p = str(f.read())
	except IOError:
		print("Error: Enter filename in current directory")
		exit()
	e = rtnTxt(crypt(p, key, ascii_dict, dcrpt, encrpt))
	if encrpt is True:
		with open("encryptedFile.txt", "w") as eFile:
			eFile.write(e)
			eFile.close()
			print('\nDone Encrypting\n')
	elif dcrpt is True: 
		with open("decyptedFile.txt", "w") as dFile:
			dFile.write(e)
			dFile.close()
			print('\nDone Decrypting\n')



main(key, txt, ecrpt, dcrpt)
