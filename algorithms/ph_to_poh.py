#! /usr/bin/python
# -*- coding: iso-8859-1 -*-


# Developed by w4g. (www.github.com/w4g)
# Conversion from pH to pOH.


ph  =	raw_input("Insert the pH:\t")
poh	=	14 - int(ph)
solution	=	""

print "[pOH] =\t", poh

if poh < 7:
	solution = "Acid"
elif poh == 7:
	solution	=	"Neutral"
else:
	solution	=	"Basic"
print "Solution (pOH):\t", solution
print "OH- = 1 . 10(-%s) mol/L"	%	(poh)
