height = int(input('Enter height: '))
for i in range(1,int(height/2)+1):
    print(' '*(int(height/2)-i), '*'*i)
if (height % 2) != 0:
    print('*'*(int(height/2)+1))
for i in range(int(height/2), 0, -1):
    print(' '*(int(height/2)-i), '*'*i)