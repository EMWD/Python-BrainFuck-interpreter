# BF - next it means braifuck
# My BF interpretator


def main():

	def parseBFcode(BFcode):
		# Clear code from not BF symbols
	    return ''.join(clearCode for clearCode in BFcode if clearCode in '<>[]+-.,')

	def codeBlock(BFcode):
	    opened = []; blocks = {}
	    for i in range(len(BFcode)):
	        if BFcode[i] == '[':
	            opened.append(i)
	        elif BFcode[i] == ']':
	            blocks[i] = opened[-1]
	            blocks[opened.pop()] = i
	    return blocks

	def run(BFcode):
	    BFcode = parseBFcode(BFcode)
	    x = i = 0
	    BF = {0: 0}
	    codeBlocks = codeBlock(BFcode)
	    length = len(BFcode)
	    
	    # Recognizing all characters
	    while i < length:
	        symbol = BFcode[i]
	        if symbol == '>':
	            x += 1
	            BF.setdefault(x, 0)
	        elif symbol == '<':
	            x -= 1
	        elif symbol == '+':
	            BF[x] += 1
	        elif symbol == '-':
	            BF[x] -= 1
	        elif symbol == '.':
	            print(chr(BF[x]), end='')
	        elif symbol == ',':
	            BF[x] = int(input('Input: '))
	        elif symbol == '[':
	            if not BF[x]: i = codeBlocks[i]
	        elif symbol == ']':
	            if BF[x]: i = codeBlocks[i]
	        i += 1

	# Our start BF code which we gonna interpret. This BF code equal "Hello World!"
	BFcode = '++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.' 
	run(BFcode)


if __name__ == '__main__':
	main()