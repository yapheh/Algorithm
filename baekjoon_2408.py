dice_3 = input()

a = int(dice_3.split()[0])
b = int(dice_3.split()[1])
c = int(dice_3.split()[2])
num_dice = [a, b, c]

if a == b & b == c & c ==a:
    print(10000+a*1000)
elif a == b:
    print(1000+a*100)
elif b == c:
    print(1000+b*100)
elif c == a:
    print(1000+c*100)
else:
    print(max(a, b, c)*100)


