
import math

def viralAdvertising(n):
    sum,init = 0,5

    for i in range(0,n):
        f=math.floor(init/2)
        sum += f
        init=f*3
    return sum


result = viralAdvertising(3)
print(result)
print(math.floor(5/2))