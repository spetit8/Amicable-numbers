import math

AmiNums = []
aDivs = [1]
bDivs = [1]

b = 0
j = 0

for a in range(10000):
    #print(a)
    for i in range(2, math.ceil(math.sqrt(a))+1):
        if a % i == 0:
            j = int(a / i)
            #print(i)
            #print(j)
            aDivs += [i, j]
            #print(aDivs)
            #print(sum(aDivs))
        if i == math.ceil(math.sqrt(a)):
            b = sum(aDivs)
            for x in range(2, math.ceil(math.sqrt(b))+1):
                if b % x == 0:
                    y = int(b / x)
                    bDivs += [x, y]
                if x == math.ceil(math.sqrt(b)) and sum(bDivs) == a and sum(aDivs) == b and a != b and a not in AmiNums:
                    AmiNums += [a, b]
                    print(AmiNums)
    aDivs = [1]
    bDivs = [1]

print(AmiNums)
print(sum(AmiNums))
