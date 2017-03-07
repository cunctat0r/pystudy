roman_numeral_map = (('M',  1000),
                     ('CM', 900),
                     ('D',  500),
                     ('CD', 400),
                     ('C',  100),
                     ('XC', 90),
                     ('L',  50),
                     ('XL', 40),
                     ('X',  10),
                     ('IX', 9),
                     ('V',  5),
                     ('IV', 4),
                     ('I',  1))

class OutOfRangeError(ValueError):
	pass

def to_roman(num):
	''' Convert integer to Roman numeral '''

	if num > 3999:
		raise OutOfRangeError

	result = ''
	for numeral, integer in roman_numeral_map:
		while num >= integer:
			result += numeral
			num -= integer
	return result
