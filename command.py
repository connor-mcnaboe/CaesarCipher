import argparse
from def_cipher import encrypt, decrypt, rtnTxt, ascii, main
parser = argparse.ArgumentParser() # Define comamand line args
parser.add_argument("-k", type=int, help="Enter a key between 0 and 256")
parser.add_argument("-f", help="Enter filename that will be encrypted") 
parser.add_argument("-e", help="Option to encrypt", action="store_true") 
parser.add_argument("-d", help="Option to decrypt", action="store_true") 
args = parser.parse_args()
key = args.k #agruments to variables 
txt = args.f
ecrpt = args.e
dcrpt = args.d

main(key, txt, ecrpt, dcrpt)
