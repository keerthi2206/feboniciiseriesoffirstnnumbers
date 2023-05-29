print('THE FEBONICII SERIES')
num = int(input('enter a number: '))
x = 0
y = 1
print(x,y,end=' ')
i = 1

while i<=num:
    z = x + y
    print(z,end=' ')

    x = y
    y = z

    i = i+1
