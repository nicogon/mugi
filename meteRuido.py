import sys
args = sys.argv[1:]
c = bytearray(open(args[0], 'rb').read())
for i in range(len(c)):
	if i%(int(args[1]))==(int(args[1])-1):
		c[i] =0
open(args[0], 'wb').write(c)