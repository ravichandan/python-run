def timeConversion(s):
    hr=s[0:2]
    min=s[3:5]
    sec=s[6:8]
    am=s[8:]
    if(am.upper() == "AM"):
      if(hr == "12"):
        hr="00";
    elif (am.upper() == "PM"):
      if(hr != "12"):
        hr=str((int(hr)+12));
    return hr+":"+min+":"+sec;

def timeConversion2(s):
    pm=s[-2:].lower() == 'pm'
    times=list(map(int,s[0:-2].split(':')))

    print(s[-2:])
    if pm and times[0] != 12:
        times[0] += 12
        
    if not pm and times[0] == 12:
        times[0] = 0
    
    res = ':'.join(list(map(lambda x: str(x).rjust(2,'0'),times)))

    return res
res = timeConversion2("11:01:01PM")
print(res)