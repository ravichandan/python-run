def chocolateFeast(n, c, m):
    total=0
    chocs=int(n/c)
    total+=chocs
    
    while chocs >= m :
        exchange= int(chocs / m)
        remainder = chocs % m    
        total += exchange
        chocs = exchange+remainder

    return total


print(chocolateFeast(6,2,2))
