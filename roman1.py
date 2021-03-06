import re

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

roman_numeral_pattern = re.compile('''
    ^                   # beginning of string
    M{0,3}              # thousands - 0 to 3 Ms
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 Cs),
                        #            or 500-800 (D, followed by 0 to 3 Cs)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 Xs),
                        #        or 50-80 (L, followed by 0 to 3 Xs)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 Is),
                        #        or 5-8 (V, followed by 0 to 3 Is)
    $                   # end of string
    ''', re.VERBOSE)

class OutOfRangeError(ValueError): pass
class NotIntegerError(ValueError): pass
class InvalidRomanNumeralError(ValueError): pass

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

def from_roman(str):
	''' Convert roman numeral to integer '''
	if not roman_numeral_pattern.search(str):
		raise InvalidRomanNumeralError('Invalid roman numeral: {0}'.format(str))

	result = 0
	index = 0
	for numeral, integer in roman_numeral_map:
		while str[index:index+len(numeral)] == numeral:
			result += integer
			index += len(numeral)
	return result