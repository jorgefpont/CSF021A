"""
Takes a whole number as parameter and returns a string
containing the number spelled out in English.
Number must be a whole number between -999,999,999 and 999,999,999
"""

# ones = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
#       7: 'seven', 8: 'eight', 9: 'nine', 0: 'zero'}

# changed from dict to tupple
ones = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
        'eight', 'nine')

tens = {10: 'ten', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
        60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}

teens = {11: 'eleven', 12: 'twelve', 13: 'thirteen', \
         14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
         18: 'eighteen', 19: 'nineteen'}


def twoDigit(num):
    """spells 2 digit number
    parameter is input integer,
    returns spelled number"""
    un = num % 10  # unit number
    dec = num // 10  # tens number
    # 11 to 19
    if un != 0 and dec == 1:
        result = teens[num]
    # 21, 22, ... , 99 except 20, 30, ... , 90
    elif un != 0 and dec != 1:
        result = f'{tens[dec * 10]} {ones[un]}'
    # 10, 20, ... 90
    elif un == 0:
        result = tens[num]
    else:
        result = 'error'
    return result


def threeDigit(num):
    """spells three digit number
    parameter is input integer,
    returns spelled number"""

    dec = num % 100  # tens number
    cen = num // 100  # hundreds number

    if dec == 0:
        result = f'{ones[cen]} hundred'
    elif dec != 0:
        result = f'{ones[cen]} hundred {twoDigit(dec)}'
    return result


def spell3dn(num):
    """spells a number of 1-3 digits. Returns spelled number.
    Parameter is input integer"""
    global result
    numDigits = len(str(num))
    num = int(num)

    if numDigits == 1:
        result = ones[num]
    elif numDigits == 2:
        result = twoDigit(num)
    elif numDigits == 3:
        result = threeDigit(num)
    else:
        print('error')
    return result


def spell4to6dn(num):
    """Spells the 4th-6th 3 digit number,
    ie the thousands. Returns spelled number.
    Parameter is input integer"""
    lsn = num % 1000  # most significant bit/number
    msn = num // 1000  # least significant bit/number

    if lsn == 0:
        result = f'{spell3dn(msn)} thousand'
    elif lsn != 0:
        result = f'{spell3dn(msn)} thousand {spell3dn(lsn)}'
    return result


def spell7to9dn(num):
    """spells the 7th-9th digit number,
    ie the millions. Returns spelled number.
    Parameter is input integer"""
    # easier to convert to string in order to extract
    # the three 3-digit parts
    numAsString = str(num)
    numDigits = len(numAsString)

    # most significant
    msn = int(numAsString[-9:-6])
    # middle
    middle = int(numAsString[-6:-3])
    # least significant
    lsn = int(numAsString[-3:])

    if lsn == 0 and middle == 0:
        result = f'{spell3dn(msn)} million'

    if lsn == 0 and middle != 0:
        result = f'{spell3dn(msn)} million {spell3dn(middle)} thousand'

    elif middle == 0 and lsn != 0:
        result = f'{spell3dn(msn)} million {spell3dn(lsn)}'

    elif lsn != 0 and middle != 0:
        result = f'{spell3dn(msn)} million {spell3dn(middle)} thousand {spell3dn(lsn)}'

    return result


def spell(num):
    """spell a pos or neg number of up to 9 digits
    parameter is input integer,
    returns spelled number"""

    if num < 0:  # make number positive and set negative flag
        isNegative = True
        num = abs(num)
    else:
        isNegative = False

    numDigits = len(str(num))
    num = int(num)

    if numDigits <= 3:
        result = spell3dn(num)

    elif 4 <= numDigits <= 6:
        result = spell4to6dn(num)

    elif 7 <= numDigits <= 9:
        result = spell7to9dn(num)

    else:
        result = 'number out of input range'

    if isNegative == True:
        return 'negative ' + result
    else:
        return result


######## TESTs function spell()  ###########
print(spell(123456789))
print(spell(456678))
print(spell(66))
print(spell(-123456789))
print(spell(-456678))
print(spell(-418))
print(spell(-13456678))
print(spell(0))
print(spell(10004))

'''
/home/jorge/csf021aWork/bin/python /home/jorge/csf021a/csf021aWork/module4/hwk4redo.py
one hundred twenty three million four hundred fifty six thousand seven hundred eighty nine
four hundred fifty six thousand six hundred seventy eight
sixty six
negative one hundred twenty three million four hundred fifty six thousand seven hundred eighty nine
negative four hundred fifty six thousand six hundred seventy eight
negative four hundred eighteen
negative thirteen million four hundred fifty six thousand six hundred seventy eight
zero
ten thousand four

Process finished with exit code 0
'''