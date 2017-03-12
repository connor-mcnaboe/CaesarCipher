'''Fucntions for caesar cipher encryption/decryption2 program''' 
import os
import time 
import sys

def main(k, f, e, d):
	#Declare variables
	ascii_dict  = ascii() #Check all arguments are filled 
	if (k  == None) | (f == None): 
		print("Error: Enter both key and filename")
		exit()
	if (e  == None) and (d == None): 
		print("Error: Enter an option to encrypt or decrypt a file")
		exit()
	if k > 255: 
		k = k % 255		
	if e == True: 
		eFile(f, k, ascii_dict) #Encrypt File 
	elif d ==True:
		dFile(f, k, ascii_dict)
		
	return 


def ascii(): # Create ascii dictionary 
	ascii_dict = dict()
	ascii_in_number = range(0,256)
	for i in ascii_in_number:
		ascii_dict[str(i)] = chr(i)
	return ascii_dict

def encrypt(txt, key, ascii_dict): #Encrypt the file 
	txt2 = []
	for value in txt: 
		txt2 += [k for k, v in ascii_dict.iteritems() if v == value] #Map all values in the txt to value in ascii dict
	txt2 =  [int(i) for i in txt2]# Convert to integer
	txt2 = [i + key for i in txt2] #Increment w/ key
	txt2 = [i + 256 if i < 0 else i - 256 if i > 256 else i for i in txt2] 
	txt2 = [str(i) for i in txt2]
	txt_e = []
	for i in txt2: 		
		txt_e += ascii_dict[i]	#Re-map to ascii 
	return txt_e

def decrypt(txt, key, ascii_dict): #Decrypt the file 
	txt2 =[]
	for value in txt: 
		txt2 += [k for k, v in ascii_dict.iteritems() if v == value] #Map all values in the txt to value in ascii dict
	txt2 =  [int(i) for i in txt2]# Convert to integer
	txt2 = [i - key for i in txt2] #Increment w/ key 
	txt2 = [i + 256 if i < 0 else i - 256 if i > 256 else i for i in txt2]
	txt2 = [str(i) for i in txt2]
	txt_e = [] 
	for i in txt2: 
		txt_e += ascii_dict[i]	#Re-map to ascii 
	return txt_e
	
def rtnTxt(txt): #Put the string back together 
	txt = ''.join(txt)
	return txt

def eFile(txt, key, ascii_dict): # Create new encrypted file
	statBar = ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', "100%"]
	status = ''
	for i  in statBar: 
		sys.stdout.flush()
		time.sleep(0.25)
		sys.stdout.write(i)
	print('\nDone Encrypting\n')
	  
	try: 
		with open(os.path.expanduser(txt), 'r+') as f: 
			p = str(f.read())
	except IOError:
		print("Error: Enter filename in current directory")
		exit()
	e = rtnTxt(encrypt(p, key, ascii_dict))
	eFile = open("encryptedFile.txt", "w")
	eFile.write(e)
	eFile.close()
	return 
	
def dFile(txt, key, ascii_dict): # Create new decypted file 
	statBar = ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', "100%"]
	status = ''
	for i  in statBar: 
		sys.stdout.flush()
		time.sleep(0.25)
		sys.stdout.write(i)
	print('\nDone Decrypting\n')
	try:
		with open(os.path.expanduser(txt), 'r+') as f: 
			p = str(f.read())
	except IOError:
		print("Error: Enter filename in current directory")
		exit()
	e = rtnTxt(decrypt(p, key, ascii_dict))
	eFile = open("decyptedFile.txt", "w")
	eFile.write(e)
	eFile.close()
	return  

