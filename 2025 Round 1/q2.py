#Q2
def main():
    list_num = []
    range_begin = int(input('Begin: '))
    range_end = int(input('End: '))
   
    for num in range(range_begin-1,range_end+1):
        sum = count_num(num)
        if sum == num:
            list_num.append(num)
        
    for item in list_num:
        print(item)
    
def count_num(num):
    line = str(num)
    length = len(line)
    sum = 0
    for i in line:
        sum = sum + int(i)**length
    return sum
    
main()