#!	/usr/bin/python
#	-*- coding: iso-8859-1 -*-

#	Developed by w4g. (www.github.com/w4g)
#	Conversion from radians to degrees.

try:
	num1	=	raw_input("(\033[1;37mXπ\033[0m/x)	:	")
	num2	=	raw_input("(%sπ/\033[1;37mX\033[0m)	:	" % num1)

	algorit	=	180 / int(num2) * int(num1)
	print "\n\033[1;37mRadian	:\033[0m	%s°" % algorit
except Exception, e:
	print "\nThe algorithm failed to solve the calculation. Is that correct?\033[01;1m\n %s\033[01;0mπ\n ————\n \033[01;1m%s\033[01;0m" % (num1, num2)
