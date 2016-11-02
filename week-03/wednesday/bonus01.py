# 4 Construct given pattern using nested 'for' loop

j = 0

for i in range(1,10):
    if i <= 5:
        j += 1
        print(j*'* ')
    else:
        j -= 1
        print(j*'* ')


