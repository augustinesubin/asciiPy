def letterSplit(letter):
    letterList = letter.split('*')
    row1.append(letterList[0])
    row1.append(" ")
    row2.append(letterList[1])
    row2.append(" ")
    row3.append(letterList[2])
    row3.append(" ")
record = {' ':'   *   *   ','a':'|---|*|---|*|   |', 'b':'|---\\*|--< *|___/', 'c':'|----*|    *|____', 'd':'|---\\*|   |*|___/'}
row1 = []
row2 = []
row3 = []
inp = input("input: ")
for letter in inp:
    letterSplit(record[letter])
print("".join(row1))
print("".join(row2))
print("".join(row3))