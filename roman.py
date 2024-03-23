def rtonum(s):
   ref = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    n = 0
    sum = 0
    while n < len(s)-1:
        if ref[s[n]] < ref[s[n+1]]:
            sum += ref[s[n+1]] - ref[s[n]]
            n += 2
        else:
            sum += ref[s[n]]
            n += 1
    if n == len(s)-1:
        sum += ref[ s[n]]

    return sum
print(rtonum("CCCXXIX"))

