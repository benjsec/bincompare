import sys
import os
import binascii

def main(argv=None):
	if argv is None:
		argv = sys.argv

	if len(argv) != 3:
		sys.exit("Requires 2 arguments.")

	for file in argv[1:]:
		checkFileExists(file)
	printhex2(argv[1], argv[2])

def printhex2(A_file, B_file):

	print("     {:^18} |  | {:^18} |  | {:^18}").format(A_file.split('/')[-1], "Difference", B_file.split('/')[-1])
	print("-"*70)

	with open(A_file, 'rb') as fA, open(B_file, 'rb') as fB:
		A_data = list(fA.read())
		B_data = list(fB.read())

	for x in range(0, min(len(A_data)-5, len(B_data))-5, 6):
		print("%3d|" % x),

		for y in range(x, x+6):
			printByte(A_data[y])
		print(" |  |"),
		for y in range(x, x+6):
			if A_data[y] == B_data[y]:
				printByte(A_data[y])
			else:
				print("__"),
		print(" |  |"),
		for y in range(x, x+6):
			printByte(B_data[y])
		print("")

def printByte(bytestring):
	print("{0}".format(binascii.b2a_hex(bytestring))),

def checkFileExists(filepath):
	if not os.path.exists(filepath):
		sys.exit("File not found: %s" % filepath)


if __name__=="__main__":
	main()