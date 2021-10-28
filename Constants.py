class Constant():
    def __init__(self, Symbol, Value, Unity):
        self.Symbol = Symbol
        self.Value = Value
        self.Unity = Unity
#Temps
SinJ = Constant("SinJ", 86400, "s")
R_t = Constant("r_t",365.256363, "J")
#Constante gravitationnel
G = Constant("G", 6.6742*10**(-11), "N")
#Masses
M_s = Constant("Ms", 1,9884*10**30, "Kg")
M_t = Constant("Mt", 5,9722*10**24, "Kg")
l_by_t = Constant("M_M/M_E", 1.23000371*10**(-2), "Kg")
s_by_me = Constant("M_s/M_m", 6.023657330*10**6, "Kg")
s_by_ve = Constant("M_s/M_ve", 4.08523719*10**5, "Kg")
s_by_ma = Constant("M_s/M_ma", 3.09870359*10**6, "Kg")
s_by_j = Constant("M_s/M_j", 1.047348644*10**3, "Kg")
s_by_sa = Constant("M_s/M_sa", 3.4979018*10**3, "Kg")
s_by_u = Constant("M_s/M_u", 2.2902951*10**4, "Kg")
s_by_n = Constant("M_s/M_n", 1.941226*10**4, "Kg")
s_by_p = Constant("M_s/M_p", 1.3605*10**8, "Kg")
#Longueurs
au = Constant("au", 1.49597870700*10**11, "m")
L_e = Constant("Equateur", 40075, "Km")
L_R_t = Constant("Radius earth", 6378.1366)
L_R_s = Constant("Radius Sun", 696000, "Km")
#Vitesse
V_lum = Constant("c", 299792458, "m/s")

