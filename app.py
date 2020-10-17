import math
g = float(input())
m = float(input())
l = float(input())
h0 = float(input())
hf = float(input())
k = float(input())

def sec(i):
    return 1/math.cos(i)

if (l == 0):
    if (hf>h0):
        print("x=100, angulo=90")
    else:
        print("x=0, angulo=0")
else:
    x=100
    angulo= math.atan((hf-h0)/l)
    fAngulo= h0-hf+(l*math.tan(angulo))-((m*g*(l**2))/(2*k)) * (sec(angulo)**2)
    fPrimaAngulo = 2*(sec(angulo)**2)-(m*g*(l**2)*(sec(angulo)**2)*math.tan(angulo))/k
    angulo = angulo - (fAngulo/fPrimaAngulo)
    presenteAngulo = angulo
    anteriorAngulo = angulo +0.5
    while abs(presenteAngulo-anteriorAngulo) >= 0.0005 or abs(anteriorAngulo-presenteAngulo) >= 0.0005:
        anteriorAngulo = presenteAngulo
        angulo= math.atan((hf-h0)/l)
        fAngulo= h0-hf+(l*math.tan(angulo))-((m*g*(l**2))/(2*k)) * (sec(angulo)**2)
        fPrimaAngulo = 2*(sec(angulo)**2)-(m*g*(l**2)*(sec(angulo)**2)*math.tan(angulo))/k
        angulo = angulo - (fAngulo/fPrimaAngulo)
        presenteAngulo= angulo
        print(fAngulo/fPrimaAngulo)

    print("x=100, angulo=", angulo)
