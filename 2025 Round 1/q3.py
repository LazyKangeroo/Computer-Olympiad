#Q3

# shift letter forward by the same amnt as its pos in word
# all letters lower
# none alp unchanged

alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alp = alp.lower()

decrypted = ''

encrypted = input('Encrypted Word: ')
encrypted = encrypted.lower()

index = 0
for letter in encrypted:
    index += 1
    if not letter in alp:
        decrypted += letter
        index = 0
    else:
        pos = alp.index(letter)
        new_letter = alp[pos - index]
        decrypted += new_letter
print(decrypted)