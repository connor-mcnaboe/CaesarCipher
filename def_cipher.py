'''Fucntions for caesar cipher encryption/decryption2 program''' 
import os
import time 
import sys

def main(k, f, encrpt, dcrpt):
	#Declare variables
	ascii_dict  = ascii() #Check all arguments are filled 
	if k is None or f is None: 
		sys.exit("Error: Enter both key and filename")
	if encrpt is False and ddcrpt is False:
		sys.exit("Error: Enter an option to encrypt or decrypt a file")
	if k > 255: 
		k = k % 255		 
	createFile(f, k, ascii_dict, encrpt, dcrpt) #Encrypt File 
		 
		
def ascii(): # Create ascii dictionary 
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
		time.sleep(0.25)
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
	


