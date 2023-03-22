t = float(input('판재 두께 입력 : '))

if t == 1.6:
    r = 1.4
    e = 2.6
elif t == 2:
    r = 2
    e = 3.5

a = (2*(2*t-e))
b = r*0.86
c = 3.14*t
d = (a+b)/c
print ('K-Factor = ' ,d)
