height = int(input('Enter height: '))
print(' '*(height), '*')
counter = 0
for i in range(0,int(height/2)-1):
    print(' '*(height-i), '*', ' '*(i*2+1), '*',sep='')
    counter = i
print(' '*(height-counter-2),'*'*(height))
for i in range(int(height/2), height-1):
    print(' '*(height-i), '*', ' '*(i*2+1), '*',sep='')