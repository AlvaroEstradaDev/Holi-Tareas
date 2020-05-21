width = int(input('Enter width: '))
height = int(input('Enter height: '))
print('*'*width)
for i in range(height-2):
    print('*', ' '*(width-4), '*')

print('*'*width)