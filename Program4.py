def fibonacciFinder(max) :
    i = 0
    j = 1
    k = 0
    while i < 100 : 
        print(k)
        k = i + j
        i = j 
        j = k 
    return("Fibonacci yay!")
'''
for i in range(0, 100) : 
    print(i)
'''
def primeFinder (max) :
    for i in range(2, max):
        for j in range(2, i):
            if i % j == 0 :
                break
        else : 
            print(i)
        return(max)
print(primeFinder(100), primeFinder(15))

def triangleArea(base, height):
    area = base * height/2
    print(area)
    return area


n = 5
m = 5
areaList = [0] * n * m
i = 0
for b in range(0, n):
    for h in range(0, m):
        areaList[i] = triangleArea(b, h)
        i += 1
print(areaList)