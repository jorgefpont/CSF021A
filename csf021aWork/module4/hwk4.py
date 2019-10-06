'''
Takes a whole number as parameter and returns a string
containing the number spelled out in English.
Number must be a whole number between -999,999,999 and 999,999,999
'''

ones = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', \
        7: 'seven', 8: 'eight', 9: 'nine', 0: 'zero'}

tens = {10: 'ten', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', \
        60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}

teens = {11: 'eleven', 12: 'twelve', 13: 'thirteen', \
         14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', \
         18: 'eighteen', 19: 'nineteen'}


def twoDigit(num):
    '''spells 2 digit number
    parameter is input integer,
    returns spelled number'''
    un = num % 10  # unit number
    dec = num // 10  # tens number
    # 11 to 19
    if un != 0 and dec == 1:
        result = teens[num]
    # 21, 22, ... , 99 except 20, 30, ... , 90
    elif un != 0 and dec != 1:
        result = f'{tens[(dec) * 10]} {ones[un]}'
    # 10, 20, ... 90
    elif un == 0:
        result = tens[num]
    else:
        result = 'error'
    return result


def threeDigit(num):
    '''spells three digit number
    parameter is input integer,
    returns spelled number'''

    dec = num % 100  # tens number
    cen = num // 100  # hundreds number

    if dec == 0:
        result = f'{ones[cen]} hundred'
    elif dec != 0:
        result = f'{ones[cen]} hundred {twoDigit(dec)}'
    return result


def spell3dn(num):
    '''spells a number of 1-3 digits'''
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
    lsn = num % 1000  # most significan bit/number
    msn = num // 1000  # least significant bit/number

    if lsn == 0:
        result = f'{spell3dn(msn)} thousand'
    elif lsn != 0:
        result = f'{spell3dn(msn)} thousand {spell3dn(lsn)}'
    return(result)

def spell7to9dn(num):
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

    return(result)

def spell(num):
    '''spell a pos or neg number of up to 9 digits
    parameter is input integer,
    returns spelled number'''

    print('number = ', num)

    if num < 0:  # make number positive and set negative flag
        isNegative = True
        num = abs(num)
    else:
        isNegative = False

    numDigits = len(str(num))
    num = int(num)

    if numDigits <= 3:
        result = spell3dn(num)

    elif numDigits >= 4 and numDigits <= 6:
        result = spell4to6dn(num)

    elif numDigits >= 7 and numDigits <= 9:
        result = spell7to9dn(num)

    elif numDigits > 9:
        result = 'number out of input range'



    if isNegative == True:
        print('minus', result)
    else:
        print(result)


# =========
# test list
testList = [0, 3, -9, 10, 13, -19, 23, 40, -90, 99, 110, -123, 200, 256, 999,
            1000, -2000, 5678, -12456, 250456, -250456,
            678956234, 600000000, -600234000, 600000234, 600234001, 999999999,
            1000000000]

for num in testList:
    spell(num)

'''
/home/jorge/csf021aWork/bin/python /home/jorge/csf021a/csf021aWork/module4/hwk4.py
number =  0
zero
number =  3
three
number =  -9
minus nine
number =  10
ten
number =  13
thirteen
number =  -19
minus nineteen
number =  23
twenty three
number =  40
forty
number =  -90
minus ninety
number =  99
ninety nine
number =  110
one hundred ten
number =  -123
minus one hundred twenty three
number =  200
two hundred
number =  256
two hundred fifty six
number =  999
nine hundred ninety nine
number =  1000
one thousand
number =  -2000
minus two thousand
number =  5678
five thousand six hundred seventy eight
number =  -12456
minus twelve thousand four hundred fifty six
number =  250456
two hundred fifty thousand four hundred fifty six
number =  -250456
minus two hundred fifty thousand four hundred fifty six
number =  678956234
six hundred seventy eight million nine hundred fifty six thousand two hundred thirty four
number =  600000000
six hundred million
number =  -600234000
minus six hundred million two hundred thirty four thousand
number =  600000234
six hundred million two hundred thirty four
number =  600234001
six hundred million two hundred thirty four thousand one
number =  999999999
nine hundred ninety nine million nine hundred ninety nine thousand nine hundred ninety nine
number =  1000000000
number out of input range

Process finished with exit code 0
'''
