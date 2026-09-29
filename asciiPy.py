def letterSplit(letter):
    letterList = letter.split('*')
    row1.append(letterList[0])
    row1.append(" ")
    row2.append(letterList[1])
    row2.append(" ")
    row3.append(letterList[2])
    row3.append(" ")
record = {' ':'   *   *   ','a':' ___ *|___|*|   |', 'b':'|---\\*|--< *|___/', 'c':'/----*|    *\\____', 'd':'|---\\*|   |*|---/', 'e':'|----*|____*|____', 'f':'|----*|----*|    ', 'g':'/----*|  --*\\___|', 'h':'|   |*|---|*|   |', 'i':'_____*  |  *-----', 'j':'_____*  |  *--/  ','k':'|  / *|<   *|  \\ ', 'l':'|    *|    *|____', 'm':' ^ ^ *| | |*| | |', 'n':' ^  |*| \\ |*|  \\|','o':'/---\\*|   |*\\___/', 'p':'/---\\*|___/*|    ','q':' ___ *|   |*\\__\\  '}
row1 = []
row2 = []
row3 = []
inp = input("input: ")
for letter in inp:
    letterSplit(record[letter.lower()])
print("".join(row1))
print("".join(row2))
print("".join(row3))
