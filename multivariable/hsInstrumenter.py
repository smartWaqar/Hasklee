#!/usr/bin/env python3



import os
from pyparsing import *
os.chdir(os.getcwd())




case1 = Word(alphanums) + ZeroOrMore(Word(alphanums) | Literal('-'))

f1 = open('src2.hs', 'r')
f2 = open('factorial_trace2.hs', 'w')
results = ""
newLine = ""


prev_conditions = []


for line in f1:
	if ("=" in line and "main" not in line and "instrxx3567" not in line and "let" not in line):
			print line
			results = case1.parseString( line )
			print results

			newLine = line[0:line.find("=")+1] + ' trace ('

			templine = ""

			for i in prev_conditions:
				templine = templine + "NOT"+ '(' + i + ')' + ','


			templine2 = ""
			count = 0
			for ii in results[1:]:
				count = count + 1
				item = ii

				print "------------------------ ", item

				if count > 1:

					if item.isalpha():
						templine2 = templine2 + 'AND' + '(' + 'x' + str(count) + "==" + "VAR" + ')' 
					else:
						templine2 = templine2 + 'AND' + '(' + 'x' + str(count) + "=="+ item + ')'
				else:

					if item.isalpha():
						templine2 = templine2 + '(' + 'x' + str(count) + "==" + "VAR" + ')' 
					else:
						templine2 = templine2 + '(' + 'x' + str(count) + "=="+ item + ')'


			print type(templine2)

			prev_conditions.append(templine2)

			newLine  = newLine + '"'+templine + templine2 + '"'

			#newLine = newLine + ' val: "'
			#for item in results[1:]:
			#	newLine = newLine + " ++ show " + item + ' ++ " "'

			newLine = newLine + ") "
			newLine = newLine + line[line.find("=")+2:]
			print newLine
			f2.write(line.replace(line, newLine))
	else:
		f2.write(line.replace(line, line))


f1.close()
f2.close()
