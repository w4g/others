#!	/usr/bin/python
#	-*- coding: iso-8859-1 -*-

#	Developed by w4g. (www.github.com/w4g)
#	Conversion from degrees to radians.

num1	=	raw_input	("\033[1;37mAngle to be converted:	\033[0m")
x		=	180 / int(num1)
x		=	str("π\n——\n%s"	%	x)
print x
