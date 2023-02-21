data=open("D:\my.txt",'w+') 
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                A = 150 + 4 * a + 3 * b + 2 * c + d
                e = (10 - A % 10) % 10
                if (A + e) % 10 == 0:
                    if (A + e) % 10 == 0:
                        print(f"{a}{b}{c}{d}{e}",file=data)

data.close()