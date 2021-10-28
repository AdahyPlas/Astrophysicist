from math import *
from Constants import *

def Jtos(J):
    return J*SinJ.Value

def stoJ(s):
    return s/SinJ.Value
def root(n,x):
    return x**(1/n)
#fonctions
def thirdKeplera(T,M):
    T2 = T**2
    GMs = G.Value*M
    pi24=4*pi**2
    a3=(T2*GMs)/pi24
    a=a3**(1/3)


def thirdKeplerT(a,M):
    a3=a**3
    pi24 = 4*pi**2
    GMa = G.Value*M
    T2=(pi24*a3)/GMa
    T=T2**(1/2)
    return T

def thirdKeplerM(T,a):
    T2=T**2
    a3=a**3
    pi24=4*pi**2
    M=(pi24*a3)/(T2*G.Value)
    return M

def EscapeVelocity(M, R):
    G2M=2*G.Value*M
    v=root(2, G2M/R)
    return v

print(EscapeVelocity(M_t.Value, 6371))





