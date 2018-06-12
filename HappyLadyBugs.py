def happyLadybugs(b):
    pre = '\0'
    allSet,underscore,first = True,False,False
    mapCount = [0]*26
    for c in b:
        if(c == '_'):
            underscore=True
        else:
            if allSet :
                if pre != c:
                    if not first:
                        first=True
                    else:
                        allSet=False
                else:
                    first=False
            mapCount[ord(c)-65] += 1
        pre = c
    if (not first) and allSet:
        return "YES"
    for i in mapCount:
        if i==1:
            return 'NO'
    
    return "YES" if underscore else "NO"


print(happyLadybugs("RBY_YBR"));
print(happyLadybugs("X_Y__X"));
print(happyLadybugs("__"));
print(happyLadybugs("B_RRBR"));
print(happyLadybugs("A_A"));
print(happyLadybugs("ABCDEFGHIJKLMNOPQRSTUWXYZABCDEFGHIJKLMNOPQRSTUWXYZABCDEFGHIJKLMNOPQRSTUWXYZABCDEFGHIJKLMNOPQRSTUWXYZABCDEFGHIJKLMNOPQRSTUWXYZABCDEFGHIJKLMNOPQRSTUWXYZABCDEFGHIJKLMNOPQRSTUWXYZ"));
print(happyLadybugs("AAS"));
print(happyLadybugs("KK"))
print(happyLadybugs("FFAA"))