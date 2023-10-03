def convert(number):
    """В возврящаемую строку дописываются:
    'Pling', если число number делится на 3,
    'Plang', если число number делится на 5,
    'Plong', если число number делится на 7,
    само число number, если оно не делится ни на 3, ни на 5, ни на 7."""


    intnum = number
    number = ''
    if int(intnum)%3 == 0: number += 'Pling'
    if int(intnum)%5 == 0: number += 'Plang' 
    if int(intnum)%7 == 0: number += 'Plong'
    if int(intnum)%3 != 0 and int(intnum)%5 != 0 and int(intnum)%7 != 0: number += str(intnum)
    return str(number)