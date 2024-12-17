
import sys

input_number = int(sys.argv[1])

for i in range(1, 21):
    #print(f'{input_number} * {i} = {input_number * i}')
    print('%d * %02d = %03d'%(input_number, i, input_number*i))
