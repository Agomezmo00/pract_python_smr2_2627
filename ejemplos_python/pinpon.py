

c = 1

while c <= 100:
    if c % 3 == 0 and c % 5 == 0:
        print("pinpon")
    elif c % 3 == 0:
        print("pin")
    elif c % 5 == 0:
        print("pon")
    else:
        print(c)
    c = c+1
    
for c in range(101, 202):
    if c % 3 == 0 and c % 5 == 0:
            print("pinpon")
    elif c % 3 == 0:
        print("pin")
    elif c % 5 == 0:
        print("pon")
    else:
        print(c)