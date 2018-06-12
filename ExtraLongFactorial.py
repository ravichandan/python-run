def extraLongFact(n):
    prod =1
    for i in range(2,n+1):
        prod *= i;
    return prod
print(extraLongFact(25))