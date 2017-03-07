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

class OutOfRangeError(ValueError): pass
class NotIntegerError(ValueError): pass

def to_roman(num):
	''' Convert integer to Roman numeral '''

	if not (0 < num < 4000):
		raise OutOfRangeError('number out of range (must be 1...3999)')
	if not isinstance(num, int):
		raise NotIntegerError('non-integers can not be converted')

	result = ''
	for numeral, integer in roman_numeral_map:
		while num >= integer:
			result += numeral
			num -= integer
	return result
