# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
    raiz=-b-(b**2-4*a*c) **0,5 /(2*a)
    raiz2=-b+(b**2-4*a*c) **0,5 /(2*a)
    return float(raiz,raiz2)



def value_y(a, b, c, x):
    return a*x**2+b*x+c


def to_string(a, b, c):
    if a==0 and b!= 0 and c!=0:
        return f"f(x) = {b}*x+{c}"
    elif a!=0 and b==0 and c!=0:
        return f"f(x) = {a}*x^2+{c}"
    elif a==0 and b==0 and c!=0:
        return f"{a}*x^2+{b}*x"
    else:
        return f"{a}*x^2{b}*x+{c}"



def derivation(a, b, c):
    return "ANSWER HERE" #no se derivar
