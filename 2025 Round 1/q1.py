# Q1a

width = int(input('Folded Width: '))
length = int(input('Folded Length: '))
folded_count = int(input('Times folded: '))

if folded_count != 0:
    unfolded_area = folded_count * 2 * length * width
else:
    unfolded_area = length * width
print('Area when unfolded: ' + str(unfolded_area))