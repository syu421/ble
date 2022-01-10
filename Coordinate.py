import sympy

x, y, z = sympy.symbols("x, y, z")

#RSSI値から距離変換
def RSSItoMetricConversion(rssi):
    TxPower = -66.04316709
    n = 4
    distance = 10 ** ((TxPower - rssi) / (10 * n))
    return round(distance, 2)

# RSSI値代入
rssi_a = -67.41666667
rssi_b = -65.76315789
rssi_c = -72.34567901
rssi_d = -63.83673469
rssi_e = -59.02816901
rssi_f = -54.22972973
rssi_g = -52.8358209
rssi_h = -61.98578199

# 距離変換呼び出し
distance_a = RSSItoMetricConversion(rssi_a)
distance_b = RSSItoMetricConversion(rssi_b)
distance_c = RSSItoMetricConversion(rssi_c)
distance_d = RSSItoMetricConversion(rssi_d)
distance_e = RSSItoMetricConversion(rssi_e)
distance_f = RSSItoMetricConversion(rssi_f)
distance_g = RSSItoMetricConversion(rssi_g)
distance_h = RSSItoMetricConversion(rssi_h)

# 座標
ax, ay, az = 0.0, 0.0, 0.0
bx, by, bz = 0.0, 2.0, 0.0
cx, cy, cz = 2.0, 2.0, 0.0
dx, dy, dz = 2.0, 0.0, 0.0
ex, ey, ez = 0.0, 0.0, 2.0
fx, fy, fz = 0.0, 2.0, 2.0
gx, gy, gz = 2.0, 2.0, 2.0
hx, hy, hz = 2.0, 0.0, 2.0

def AB(ax , ay, az, bx, by, bz, distance_a, distance_b):
    AB_left = 2*(ax - bx)*x + 2*(ay - by)*y + 2*(az - bz)*z
    AB_right = distance_b**2 - distance_a**2 + (ax**2 + ay**2 + az**2) - (bx**2 + by**2 + bz**2)
    AB_y = round(AB_right / (AB_left / y),1)
    return AB_y

def AC(ax, az, cx, cz, distance_a, distance_c):
    AC_left = 2*(ax - cx)*x + 2*(az - cz)*z
    AC_right = distance_c**2 - distance_a**2 + (ax**2 + az**2) - (cx**2 + cz**2)
    AC_x = round(AC_right / (AC_left / x),1)
    return AC_x

def ABC(ax, ay, az, ABC_x, ABC_y, distance_a):
    ABC_left = z**2 - 2*az*z
    ABC_right = distance_a**2 - (ABC_x - ax)**2 - (ABC_y - ay)**2 - az**2
    ABC_func = sympy.solve(ABC_left + ABC_right)
    return round(ABC_func[1],1)

def AD(ax, ay, az, dx, dy, dz, distance_a, distance_d):
    AD_left = 2*(ax - dx)*x + 2*(ay - dy)*y + 2*(az - dz)*z
    AD_right = distance_d**2 - distance_a**2 + (ax**2 + ay**2 + az**2) - (dx**2 + dy**2 + dz**2)
    AD_x = round(AD_right / (AD_left / x),1)
    return AD_x

def ABD(ax, ay, az, ABD_x, ABD_y, distance_a):
    ABD_left = z**2 - 2*az*z
    ABD_right = distance_a**2 - (ABD_x - ax)**2 - (ABD_y - ay)**2 - az**2
    ABD_func = sympy.solve(ABD_left + ABD_right)
    return round(ABD_func[1],1)

def AE(ax, ay, az, ex, ey, ez, distance_a, distance_e):
    AE_left = 2*(ax - ex)*x + 2*(ay - ey)*y + 2*(az - ez)*z
    AE_right = distance_e**2 - distance_a**2 + (ax**2 + ay**2 + az**2) - (ex**2 + ey**2 + ez**2)
    AE_z = round(AE_right / (AE_left / z),1)
    return AE_z

def ABE(ax, ay, az, ABE_y, ABE_z, distance_a):
    ABE_left = x**2 - 2*ax*x
    ABE_right = distance_a**2 - (ABE_y - ay)**2 - (ABE_z - az)**2 - ax**2
    ABE_func = sympy.solve(ABE_left + ABE_right)
    return round(ABE_func[1],1)

def AF(ax, az, fx, fz, distance_a, distance_f):
    AF_left = 2*(ax - fx)*x + 2*(az - fz)*z
    AF_right = distance_f**2 - distance_a**2 + (ax**2 + az**2) - (fx**2 + fz**2)
    AF_z = round(AF_right / (AF_left / z),1)
    return AF_z

def ABF(ax, ay, az, ABF_y, ABF_z, distance_a):
    ABF_left = x**2 - 2*ax*x
    ABF_right = distance_a**2 - (ABF_y - ay)**2 - (ABF_z - az)**2 - ax**2
    ABF_func = sympy.solve(ABF_left + ABF_right)
    return round(ABF_func[1],1)

def ABG(ax, ay, az, gx, gy, ABG_y ,distance_a, distance_g):
    AG_left = 2*(ax - gx)*x
    AG_right = distance_g**2 - distance_a**2 + (ax**2 + ay**2) - (gx**2 + gy**2) - 2*(ay - gy)*ABG_y
    AG_x = round(AG_right / (AG_left / x),1)
    
    ABG_left = z**2 - 2*az*z
    ABG_right = distance_a**2 - (ABG_y - ay)**2 - (AG_x - ax)**2 - az**2
    ABG_func = sympy.solve(ABG_left + ABG_right)
    AB_z = round(ABG_func[1],1)

    return AG_x, AB_z

def AH(ax, ay, hx, hy, distance_a, distance_h):
    AH_left = 2*(ax - hx)*x + 2*(ay - hy)*y
    AH_right = distance_h**2 - distance_a**2 + (ax**2 + ay**2) - (hx**2 + hy**2)
    AH_x = round(AH_right / (AH_left / x),1)
    return AH_x

def ABH(ax, ay, az, ABH_y, ABH_x, distance_a):
    ABH_left = z**2 - 2*az*z
    ABH_right = distance_a**2 - (ABH_y - ay)**2 - (ABH_x - ax)**2 - az**2
    ABH_func = sympy.solve(ABH_left + ABH_right)
    return round(ABH_func[1],1)

def CD(cx, cy, cz, dx, dy, dz, distance_c, distance_d):
    CD_left = 2*(cx - dx)*x + 2*(cy - dy)*y + 2*(cz - dz)*z
    CD_right = distance_d**2 - distance_c**2 + (cx**2 + cy**2 + cz**2) - (dx**2 + dy**2 + dz**2)
    CD_y = round(CD_right / (CD_left / y),1)
    return CD_y

def ACD(ax, ay, az, ACD_y, ACD_x, distance_a):
    ACD_right = z**2 - 2*az*z
    ACD_left = distance_a**2 - (ACD_y - ay)**2 - (ACD_x - ax)**2 - az**2
    ACD_func = sympy.solve(ACD_right + ACD_left)
    return round(ACD_func[1],1)

def ACE(ax, ay, az, ACE_x, ACE_z, distance_a):
    ACE_left = y**2 - 2*ay*y
    ACE_right = distance_a**2 - (ACE_x - ax)**2 - (ACE_z - az)**2 - ay**2
    ACE_func = sympy.solve(ACE_left + ACE_right)
    return round(ACE_func[1],1)

def ACF(ax, ay, az, ACF_x, ACF_z, distance_a):
    ACF_left = y**2 - 2*ay*y
    ACF_right = distance_a**2 - (ACF_x - ax)**2 - (ACF_z - az)**2 - ay**2
    ACF_func = sympy.solve(ACF_left + ACF_right)
    return round(ACF_func[1],1)

def CG(cx, cy, cz, gx, gy, gz, distance_c, distance_g):
    CG_left = 2*(cx - gx)*x + 2*(cy - gy)*y + 2*(cz - gz)*z
    CG_right = distance_g**2 - distance_c**2 + (cx**2 + cy**2 + cz**2) - (gx**2 + gy**2 + gz**2)
    CG_z = round(CG_right / (CG_left / z),1)
    return CG_z

def ACG(ax, ay, az, ACG_x, ACG_z, distance_a):
    ACG_left = y**2 - 2*ay*y
    ACG_right = distance_a**2 - (ACG_x - ax)**2 - (ACG_z - az)**2 - ay**2
    ACG_func = sympy.solve(ACG_left + ACG_right)
    return round(ACG_func[1],1)

def ACH(cx, cy, hx, hy, ACH_x, distance_c, distance_h):
    CH_left = 2*(cy - hy)*y
    CH_right = distance_h**2 - distance_c**2 + (cx**2 + cy**2) - (hx**2 + hy**2) - 2*(cy - hy)*ACH_x
    CH_y = round(CH_right / (CH_left / y),1)
    
    ACH_left = z**2 - 2*az*z
    ACH_right = distance_a**2 - (ACH_x - ax)**2 - (CH_y - ay)**2 - az**2
    ACH_func = sympy.solve(ACH_left + ACH_right)
    CH_z =  round(ACH_func[1],1)

    return CH_y, CH_z

def ADE(ax, ay, az, ADE_x, ADE_z, distance_a):
    ADE_right = y**2 - 2*ay*y
    ADE_left = distance_a**2 - (ADE_x - ax)**2 - (ADE_z - az)**2 - ay**2
    ADE_func = sympy.solve(ADE_right + ADE_left)
    return round(ADE_func[1],1)

def ADF(ax, ay, az, ADF_x, ADF_z, distance_a):
    ADF_right = y**2 - 2*ay*y
    ADF_left = distance_a**2 - (ADF_x - ax)**2 - (ADF_z - az)**2 - ay**2
    ADF_func = sympy.solve(ADF_right + ADF_left)
    return round(ADF_func[1],1)

def DG(dx, dy, gx, gy, distance_d, distance_g):
    DG_left = 2*(dx - gx)*x + 2*(dy - gy)*y
    DG_right = distance_g**2 - distance_d**2 + (dx**2 + dy**2) - (gx**2 + gy**2)
    DG_y = round(DG_right / (DG_left / y),1)
    return DG_y

def ADG(ax, ay, az, ADG_x, ADG_y, distance_a):
    ADG_left = z**2 - 2*az*z
    ADG_right = distance_a**2 - (ADG_x - ax)**2 - (ADG_y - ay)**2 - az**2
    ADG_func = sympy.solve(ADG_left + ADG_right)
    return round(ADG_func[1],1)

def DH(dx, dy, dz, hx, hy, hz, distance_d, distance_h):
    DH_left = 2*(dx - hx)*x + 2*(dy - hy)*y + 2*(dz - hz)*z
    DH_right = distance_h**2 - distance_d**2 + (dx**2 + dy**2 + dz**2) - (hx**2 + hy**2 + hz**2)
    DH_z = round(DH_right / (DH_left / z),1)
    return DH_z

def ADH(ax, ay, az, ADH_x, ADH_z, distance_a):
    ADH_left = y**2 - 2*ay*y
    ADH_right = distance_a**2 - (ADH_x - ax)**2 - (ADH_z - az)**2 - ay**2
    ADH_func = sympy.solve(ADH_left + ADH_right)
    return round(ADH_func[1],1)

def EF(ex, ey, ez, fx, fy, fz, distance_e, distance_f):
    EF_left = 2*(ex - fx)*x + 2*(ey - fy)*y + 2*(ez - fz)*z
    EF_right = distance_f**2 - distance_e**2 + (ex**2 + ey**2 + ez**2) - (fx**2 + fy**2 + fz**2)
    EF_y = round(EF_right / (EF_left / y) ,1)
    return EF_y

def AEF(ax, ay, az, distance_a, AEF_y, AEF_z):
    AEF_left = x**2 - 2*ax*x
    AEF_right = distance_a**2 - (AEF_y - ay)**2 - (AEF_z - az)**2 - ax**2
    AEF_func = sympy.solve(AEF_left + AEF_right)
    return round(AEF_func[1],1)

def AEG(ax, ay, az, AEG_x, AEG_z, distance_a):
    AEG_left = y**2 - 2*ay*y
    AEG_right = distance_a**2 - (AEG_x - ax)**2 - (AEG_z - az)**2 - ay**2
    AEG_func = sympy.solve(AEG_left + AEG_right)
    return round(AEG_func[1],1)

def AEH(ax, ay, az, AEH_x, AEH_z, distance_a):
    AEH_left = y**2 - 2*ay*y
    AEH_right = distance_a**2 - (AEH_x - ax)**2 - (AEH_z - az)**2 - ay**2
    AEH_func = sympy.solve(AEH_left + AEH_right)
    return round(AEH_func[1],1)

def AFG(ax, ay, az, AFG_x, AFG_z, distance_a):
    AFG_left = y**2 - 2*ay*y
    AFG_right = distance_a**2 - (AFG_x - ax)**2 - (AFG_z - az)**2 - ay**2
    AFG_func = sympy.solve(AFG_left + AFG_right)
    return round(AFG_func[1],1)

def AFH(ax, ay, az, AFH_x, AFH_z, distance_a):
    AFH_left = y**2 - 2*ay*y
    AFH_right = distance_a**2 - (AFH_x - ax)**2 - (AFH_z - az)**2 - ay**2
    AFH_func = sympy.solve(AFH_left + AFH_right)
    return round(AFH_func[1],1)

def GH(gx, gy, gz, hx, hy, hz, distance_g, distance_h):
    GH_left = 2*(gx - hx)*x + 2*(gy - hy)*y + 2*(gz - hz)*z
    GH_right = distance_h**2 - distance_g**2 + (gx**2 + gy**2 + gz**2) - (hx**2 + hy**2 + hz**2)
    GH_y = round(GH_right / (GH_left / y),1)
    return GH_y

def AGH(ax, ay, az, AGH_x, AGH_y, distance_a):
    AGH_left = z**2 - 2*az*z
    AGH_right = distance_a**2 - (AGH_y - ay)**2 - (AGH_x - ax)**2 - az**2
    AGH_func = sympy.solve(AGH_left + AGH_right)
    return round(AGH_func[1],1)

def BC(bx, by, bz, cx, cy, cz, distance_b, distance_c):
    BC_right = 2*(bx - cx)*x + 2*(by - cy)*y + 2*(bz - cz)*z
    BC_left = distance_c**2 - distance_b**2 + (bx**2 + by**2 + bz**2) - (cx**2 + cy**2 + cz**2)
    BC_x = round(BC_left / (BC_right / x),1)
    return BC_x
 
def BCD(bx, by, bz, BCD_x, BCD_y, distance_b):
    BCD_left = z**2 - 2*bz*z
    BCD_right = distance_b**2 - (BCD_x - bx)**2 - (BCD_y - by)**2 - bz**2
    BCD_func = sympy.solve(BCD_left + BCD_right)
    return round(BCD_func[1],1)

def BE(bx, by, ex, ey, distance_b, distance_e):
    BE_left = 2*(bx - ex)*x + 2*(by - ey)*y
    BE_right = distance_e**2 - distance_b**2 + (bx**2 + by**2) - (ex**2 + ey**2)
    BE_y = round(BE_right / (BE_left / y),1)
    return BE_y

def BCE(bx, by, bz, BCE_x, BCE_y, distance_b):
    BCE_left = (z - bz)**2
    BCE_right = distance_b**2 - (BCE_x - bx)**2 - (BCE_y - by)**2
    BCE_func = sympy.solve(BCE_left + BCE_right)
    return round(BCE_func[1],1)

def BF(bx, by, bz, fx, fy, fz, distance_b, distance_f):
    BF_left = 2*(bx - fx)*x + 2*(by - fy)*y + 2*(bz - fz)*z
    BF_right = distance_f**2 - distance_b**2 + (bx**2 + by**2 + bz**2) - (fx**2 + fy**2 + fz**2)
    BF_z = round(BF_right / (BF_left/z),1)
    return BF_z

def BCF(bx, by, bz, BCF_x, BCF_z, distance_b):
    BCF_right = y**2 - 2*y*by
    BCF_left = distance_b - (BCF_x - bx)**2 - (BCF_z - bz)**2 - by**2
    BCF_func = sympy.solve(BCF_right + BCF_left)
    return round(BCF_func[1],1)

def BCG(bx, by, bz, BCG_x, BCG_z, distance_b):
    BCG_left = y**2 - 2*y*by
    BCG_right = distance_b - (BCG_x - bx)**2 - (BCG_z - bz)**2 - by**2
    BCG_func = sympy.solve(BCG_left + BCG_right)
    return round(BCG_func[1],1)

def BCH(bx, by, bz, hx, hy, BCH_x, distance_b, distance_h):
    BH_left = 2*(by - hy)*y
    BH_right = distance_h**2 - distance_b**2 + (bx**2 + by**2) - (hx**2 + hy**2) - 2*(bx - hx)*BCH_x
    BH_y = round(BH_right / (BH_left / y),1)
    
    BCH_left = z**2 + 2*bz*z
    BCH_right = distance_b - (BCH_x - bx)**2 - (BH_y - by)**2 - bz**2
    BCH_func = sympy.solve(BCH_left + BCH_right)
    BH_z = round(BCH_func[1],1)
    return BH_y, BH_z

def BD(bx, bz, dx, dz, distance_b, distance_d):
    BD_right = 2*(bx - dx)*x + 2*(bz - dz)*z
    BD_left = distance_d - distance_b + (bx**2 + bz**2) - (dx**2 + dz**2)
    BD_x = round(BD_left / (BD_right / x),1)
    return BD_x

def BDE(bx, by, bz, BDE_x, BDE_y, distance_b):
    BDE_left = (z - bz)**2
    BDE_right = distance_b**2 - (BDE_y - by)**2 - (BDE_x - bx)**2
    BDE_func = sympy.solve(BDE_left + BDE_right)
    return round(BDE_func[1],1)

def BDF(bx, by, bz, BDF_x, BDF_z, distance_b):
    BDF_left = y**2 - 2*y*by
    BDF_right = distance_b - (BDF_x - bx)**2 - (BDF_z - bz)**2 - by**2
    BDF_func = sympy.solve(BDF_left + BDF_right)
    return round(BDF_func[1],1)

def BG(by, bz, gy, gz, distance_b, distance_g):
    BG_left = 2*(by - gy)*y + 2*(bz - gz)*z
    BG_right = distance_g**2 - distance_b**2 + (by**2 + bz**2) - (gy**2 + gz**2)
    BG_z = round(BG_right / (BG_left / z),1)
    return BG_z

def BDG(bx, by, bz, BDG_x, BDG_z, distance_b):
    BDG_left = y**2 - 2*y*by
    BDG_right = distance_b - (BDG_x - bx)**2 - (BDG_z - bz)**2 - by**2
    BDG_func = sympy.solve(BDG_left + BDG_right)
    return round(BDG_func[1],1)

def BDH(bx, by, bz, BDH_x, BDH_z, distance_b):
    BDH_left = y**2 - 2*y*by
    BDH_right = distance_b - (BDH_x - bx)**2 - (BDH_z - bz)**2 - by**2
    BDH_func = sympy.solve(BDH_left + BDH_right)
    return round(BDH_func[1],1)

def BEF(bx, by, bz, BEF_y, BEF_z, distance_b):
    BEF_left = x**2 - 2*x*bx
    BEF_right = distance_b - (BEF_y - by)**2 - (BEF_z - bz)**2 - bx**2
    BEF_func = sympy.solve(BEF_left + BEF_right)
    return round(BEF_func[1],1)

def BEG(bx, by, bz, BEG_y, BEG_z, distance_b):
    BEG_left = x**2 - 2*x*bx
    BEG_right = distance_b - (BEG_y - by)**2 - (BEG_z - bz)**2 - bx**2
    BEG_func = sympy.solve(BEG_left + BEG_right)
    return round(BEG_func[1],1)

def EH(ex, ey, ez, hx, hy, hz, distance_e, distance_h):
    EH_left = 2*(ex - hx)*x + 2*(ey - hy)*y + 2*(ez - hz)*z
    EH_right = distance_h**2 - distance_e**2 + (ex**2 + ey**2 + ez**2) - (hx**2 + hy**2 + hz**2)
    EH_x = round(EH_right / (EH_left / x),1)
    return EH_x

def BEH(bx, by, bz, BEH_x, BEH_y, distance_b):
    BEH_left = z**2 - 2*z*bz
    BEH_right = distance_b - (BEH_x - bx)**2 - (BEH_y - by)**2 - bz**2
    BEH_func = sympy.solve(BEH_left + BEH_right)
    return round(BEH_func[1],1)

def FG(fx, fy, fz, gx, gy, gz, distance_f, distance_g):
    FG_left = 2*(fx - gx)*x + 2*(fy - gy)*y + 2*(fz - gz)*z
    FG_right = distance_g**2 - distance_f**2 + (fx**2 + fy**2 + fz**2) - (gx**2 + gy**2 + gz**2)
    FG_x = round(FG_right / (FG_left / x),1)
    return FG_x

def BFG(bx, by, bz, BFG_x, BFG_z, distance_b):
    BFG_left = y**2 - 2*y*by
    BFG_right = distance_b - (BFG_x - bx)**2 - (BFG_z - bz)**2 - by**2
    BFG_func = sympy.solve(BFG_left + BFG_right)
    return round(BFG_func[1],1)

def FH(fx, fz, hx, hz, distance_f, distance_h):
    FH_left = 2*(fx - hx)*x + 2*(fz - hz)*z
    FH_right = distance_h**2 - distance_f**2 + (fx**2 + fz**2) - (hx**2 + hz**2)
    FH_x = round(FH_right / (FH_left / x),1)
    return FH_x

def BFH(bx, by, bz, BFH_x, BFH_z, distance_b):
    BFH_left = y**2 - 2*y*by
    BFH_right = distance_b - (BFH_x - bx)**2 - (BFH_z - bz)**2 - by**2
    BFH_func = sympy.solve(BFH_left + BFH_right)
    return round(BFH_func[1],1)

def BGH(bx, by, bz, BGH_y, BGH_z, distance_b):
    BGH_left = x**2 - 2*x*bx
    BGH_right = distance_b - (BGH_y - by)**2 - (BGH_z - bz)**2 - bx**2
    BGH_func = sympy.solve(BGH_left + BGH_right)
    return round(BGH_func[1],1)

def DE(dy, dz, ey, ez, distance_d, distance_e):
    DE_left = 2*(dy - ey)*y + 2*(dz - ez)*z
    DE_right = distance_e**2 - distance_d**2 + (dy**2 + dz**2) - (ey**2 + ez**2)
    DE_z = round(DE_right / (DE_left / z),1)
    return DE_z

def CDE(cx, cy, cz, CDE_y, CDE_z, distance_c):
    CDE_left = x**2 - 2*x*cx
    CDE_right = distance_c - (CDE_y - cy)**2 - (CDE_z - cz)**2 - cx**2
    CDE_func = sympy.solve(CDE_left + CDE_right)
    return round(CDE_func[1],1)

def CF(cy, cz, fy, fz, distance_c, distance_f):
    CF_left = 2*(cy - fy)*y + 2*(cz - fz)*z
    CF_right = distance_f**2 - distance_c**2 + (cy**2 + cz**2) - (fy**2 + fz**2)
    CF_z = round(CF_right / (CF_left / z),1)
    return CF_z

def CDF(cx, cy, cz, CDF_y, CDF_z, distance_c):
    CDF_left = x**2 - 2*x*cx
    CDF_right = distance_c - (CDF_y - cy)**2 - (CDF_z - cz)**2 - cx**2
    CDF_func = sympy.solve(CDF_left + CDF_right)
    return round(CDF_func[1],1)

def CDG(cx, cy, cz, CDG_y, CDG_z, distance_c):
    CDG_left = x**2 - 2*x*cx
    CDG_right = distance_c - (CDG_y - cy)**2 - (CDG_z - cz)**2 - cx**2
    CDG_func = sympy.solve(CDG_left + CDG_right)
    return round(CDG_func[1],1)

def CDH(cx, cy, cz, CDH_y, CDH_z, distance_c):
    CDH_left = x**2 - 2*x*cx
    CDH_right = distance_c - (CDH_y - cy)**2 - (CDH_z - cz)**2 - cx**2
    CDH_func = sympy.solve(CDH_left + CDH_right)
    return round(CDH_func[1],1)

def CEF(cx, cy, cz, CEF_y, CEF_z, distance_c):
    CEF_left = x**2 - 2*x*cx
    CEF_right = distance_c - (CEF_y - cy)**2 - (CEF_z - cz)**2 - cx**2
    CEF_func = sympy.solve(CEF_left + CEF_right)
    return round(CEF_func[1],1)

def EG(ex, ez, gx, gz, distance_e, distance_g):
    EG_left = 2*(ex - gx)*x + 2*(ez - gz)*z
    EG_right = distance_g**2 - distance_e**2 + (ex**2 + ez**2) - (gx**2 + gz**2)
    EG_x = round(EG_right / (EG_left / x),1)
    return EG_x

def CEG(cx, cy, cz, CEG_x, CEG_z, distance_c):
    CEG_left = y**2 - 2*y*cy
    CEG_right = distance_c - (CEG_x - cx)**2 - (CEG_z - cz)**2 - cy**2
    CEG_func = sympy.solve(CEG_left + CEG_right)
    return round(CEG_func[1],1)

def CEH(cx, cy, cz, ex, ez, CEH_x, distance_c, distance_e):
    CE_left =  2*(cz - ez)*z
    CE_right = distance_e**2 - distance_c**2 + (cx**2 + cz**2) - (ex**2 + ez**2) - 2*(cx - ex)*CEH_x
    CE_z = round(CE_right / (CE_left / z),1)

    CEH_left = y**2 + 2*y*cy
    CEH_right = distance_c - (CEH_x - cx)**2 - (CE_z - cz)**2 - cy**2
    CEH_func = sympy.solve(CEH_left + CEH_right)
    CE_y =  round(CEH_func[1],1)
    
    return CE_z, CE_y 
    
def CFG(cx, cy, cz, CFG_x, CFG_z, distance_c):
    CFG_left = y**2 - 2*y*cy
    CFG_right = distance_c - (CFG_x - cx)**2 - (CFG_z - cz)**2 - cy**2
    CFG_func = sympy.solve(CFG_left + CFG_right)
    return round(CFG_func[1],1)

def CFH(cx, cy, cz, CFH_x, CFH_z, distance_c):
    CFH_left = y**2 - 2*y*cy
    CFH_right = distance_c - (CFH_x - cx)**2 - (CFH_z - cz)**2 - cy**2
    CFH_func = sympy.solve(CFH_left + CFH_right)
    return round(CFH_func[1],1)

def CGH(cx, cy, cz, CGH_y, CGH_z, distance_c):
    CGH_left = x**2 - 2*x*cx
    CGH_right = distance_c - (CGH_y - cy)**2 - (CGH_z - cz)**2 - cx**2
    CGH_func = sympy.solve(CGH_left + CGH_right)
    return round(CGH_func[1],1)

def DEF(dx, dy, dz, DEF_y, DEF_z, distance_d):
    DEF_left = x**2 - 2*x*dx
    DEF_right = distance_d - (DEF_y - dy)**2 - (DEF_z - dz)**2 - dx**2
    DEF_func = sympy.solve(DEF_left + DEF_right)
    return round(DEF_func[1],1)

def DEG(dx, dy, dz, DEG_y, DEG_z, distance_d):
    DEG_left = x**2 - 2*x*dx
    DEG_right = distance_d - (DEG_y - dy)**2 - (DEG_z - dz)**2 - dx**2
    DEG_func = sympy.solve(DEG_left + DEG_right)
    return round(DEG_func[1],1)

def DEH(dx, dy, dz, DEH_x, DEH_z, distance_d):
    DEH_left = y**2 - 2*y*dy
    DEH_right = distance_d - (DEH_x - dx)**2 - (DEH_z - dz)**2 - dy**2
    DEH_func = sympy.solve(DEH_left + DEH_right)
    return round(DEH_func[1],1)

def DFG(dx, dy, dz, DFG_x, DFG_y, distance_d):
    DFG_left = z**2 - 2*z*dz
    DFG_right = distance_d - (DFG_x - dx)**2 - (DFG_y - dy)**2 - dz**2
    DFG_func = sympy.solve(DFG_left + DFG_right)
    return round(DFG_func[1],1)

def DFH(dx, dy, dz, DFH_x, DFH_z, distance_d):
    DFH_left = y**2 - 2*y*dy
    DFH_right = distance_d - (DFH_x - dx)**2 - (DFH_z - dz)**2 - dy**2
    DFH_func = sympy.solve(DFH_left + DFH_right)
    return round(DFH_func[1],1)

def DGH(dx, dy, dz, DGH_y, DGH_z, distance_d):
    DGH_left = x**2 - 2*x*dx
    DGH_right = distance_d - (DGH_y - dy)**2 - (DGH_z - dz)**2 - dx**2
    DGH_func = sympy.solve(DGH_left + DGH_right)
    return round(DGH_func[1],1)

def EFG(ex, ey, ez, EFG_x, EFG_y, distance_e):
    EFG_left = z**2 - 2*z*ez
    EFG_right = distance_e - (EFG_x - ex)**2 - (EFG_y - ey)**2 - ez**2
    EFG_func = sympy.solve(EFG_left + EFG_right)
    return round(EFG_func[1],1)

def EFH(ex, ey, ez, EFH_x, EFH_y, distance_e):
    EFH_left = z**2 - 2*z*ez
    EFH_right = distance_e - (EFH_x - ex)**2 - (EFH_y - ey)**2 - ez**2
    EFH_func = sympy.solve(EFH_left + EFH_right)
    return round(EFH_func[1],1)

def EGH(ex, ey, ez, EGH_x, EGH_y, distance_e):
    EGH_left = z**2 - 2*z*ez
    EGH_right = distance_e - (EGH_x - ex)**2 - (EGH_y - ey)**2 - ez**2
    EGH_func = sympy.solve(EGH_left + EGH_right)
    return round(EGH_func[1],1)

def FGH(fx, fy, fz, FGH_x, FGH_y, distance_f):
    FGH_left = z**2 - 2*z*fz
    FGH_right = distance_f - (FGH_x - fx)**2 - (FGH_y - fy)**2 - fz**2
    FGH_func = sympy.solve(FGH_left + FGH_right)
    return round(FGH_func[1],1)

#ABC
ABC_y = AB(ax , ay, az, bx, by, bz, distance_a, distance_b)
ABC_x = AC(ax, az, cx, cz, distance_a, distance_c)
ABC_z = ABC(ax, ay, az, ABC_x, ABC_y, distance_a)
print(f"ABC(x, y, z) = {ABC_x, ABC_y, ABC_z}")

#ABD
ABD_y = AB(ax , ay, az, bx, by, bz, distance_a, distance_b)
ABD_x = AD(ax, ay, az, dx, dy, dz, distance_a, distance_d)
ABD_z = ABD(ax, ay, az, ABD_x, ABD_y, distance_a)
print(f"ABD(x, y, z) = {ABD_x, ABD_y, ABD_z}")

#ABE
ABE_y = AB(ax , ay, az, bx, by, bz, distance_a, distance_b)
ABE_z = AE(ax, ay, az, ex, ey, ez, distance_a, distance_e)
ABE_x = ABE(ax, ay, az, ABE_y, ABE_z, distance_a)
print(f"ABE(x, y, z) = {ABE_x, ABE_y, ABE_z}")

#ABF
ABF_y = AB(ax , ay, az, bx, by, bz, distance_a, distance_b)
ABF_z = AF(ax, az, fx, fz, distance_a, distance_f)
ABF_x = ABF(ax, ay, az, ABF_y, ABF_z, distance_a)
print(f"ABF(x, y, z) = {ABF_x, ABF_y, ABF_z}")

#ABG
ABG_y = AB(ax , ay, az, bx, by, bz, distance_a, distance_b)
ABG_x, ABG_z = ABG(ax, ay, az, gx, gy, ABG_y ,distance_a, distance_g)
print(f"ABG(x, y, z) = {ABG_x, ABG_y, ABG_z}")

#ABH
ABH_y = AB(ax , ay, az, bx, by, bz, distance_a, distance_b)
ABH_x = AH(ax, ay, hx, hy, distance_a, distance_h)
ABH_z = ABH(ax, ay, az, ABH_y, ABH_x, distance_a)
print(f"ABH(x, y, z) = {ABH_x, ABH_y, ABH_z}")

#ACD
ACD_x = AD(ax, ay, az, dx, dy, dz, distance_a, distance_d)
ACD_y = CD(cx, cy, cz, dx, dy, dz, distance_c, distance_d)
ACD_z = ACD(ax, ay, az, ACD_y, ACD_x, distance_a)
print(f"ACD(x, y, z) = {ACD_x, ACD_y, ACD_z}")

#ACE
ACE_x = AC(ax, az, cx, cz, distance_a, distance_c)
ACE_z = AE(ax, ay, az, ex, ey, ez, distance_a, distance_e)
ACE_y = ACE(ax, ay, az, ACE_x, ACE_z, distance_a)
print(f"ACE(x, y, z) = {ACE_x, ACE_y, ACE_z}")

#ACF
ACF_x = AC(ax, az, cx, cz, distance_a, distance_c)
ACF_z = AF(ax, az, fx, fz, distance_a, distance_f)
ACF_y = ACF(ax, ay, az, ACF_x, ACF_z, distance_a)
print(f"ACF(x, y, z) = {ACF_x, ACF_y, ACF_z}")

#ACG
ACG_x = AC(ax, az, cx, cz, distance_a, distance_c)
ACG_z = CG(cx, cy, cz, gx, gy, gz, distance_c, distance_g)
ACG_y = ACG(ax, ay, az, ACG_x, ACG_z, distance_a)
print(f"ACG(x, y, z) = {ACG_x, ACG_y, ACG_z}")

#ACH
ACH_x = AH(ax, ay, hx, hy, distance_a, distance_h) #AC
ACH_y, ACH_z = ACH(cx, cy, hx, hy, ACH_x, distance_c, distance_h)
print(f"ACH(x, y, z) = {ACH_x, ACH_y, ACH_z}")

#ADE
ADE_x = AC(ax, az, cx, cz, distance_a, distance_c)
ADE_z = AE(ax, ay, az, ex, ey, ez, distance_a, distance_e)
ADE_y = ADE(ax, ay, az, ADE_x, ADE_z, distance_a)
print(f"ADE(x, y, z) = {ADE_x, ADE_y, ADE_z}")

#ADF
ADF_x = AD(ax, ay, az, dx, dy, dz, distance_a, distance_d)
ADF_z = AF(ax, az, fx, fz, distance_a, distance_f)
ADF_y = ADF(ax, ay, az, ADF_x, ADF_z, distance_a)
print(f"ADF(x, y, z) = {ADF_x, ADF_y, ADF_z}")

#ADG
ADG_x = AD(ax, ay, az, dx, dy, dz, distance_a, distance_d)
ADG_y = DG(dx, dy, gx, gy, distance_d, distance_g)
ADG_z = ADG(ax, ay, az, ADG_x, ADG_y, distance_a)
print(f"ADG(x, y, z) = {ADG_x, ADG_y, ADG_z}")

#ADH
ADH_x = AD(ax, ay, az, dx, dy, dz, distance_a, distance_d)
ADH_z = DH(dx, dy, dz, hx, hy, hz, distance_d, distance_h)
ADH_y = ADH(ax, ay, az, ADH_x, ADH_z, distance_a)
print(f"ADH(x, y, z) = {ADH_x, ADH_y, ADH_z}")

#AEF
AEF_z = AE(ax, ay, az, ex, ey, ez, distance_a, distance_e)
AEF_y = EF(ex, ey, ez, fx, fy, fz, distance_e, distance_f)
AEF_x = AEF(ax, ay, az, distance_a, AEF_y, AEF_z)
print(f"AEF(x, y, z) = {AEF_x, AEF_y, AEF_z}")

#AEG
AEG_x = EG(ex, ez, gx, gz, distance_e, distance_g)
AEG_z = AE(ax, ay, az, ex, ey, ez, distance_a, distance_e)
AEG_y = AEG(ax, ay, az, AEG_x, AEG_z, distance_a)
print(f"AEG(x, y, z) = {AEG_x, AEG_y, AEG_z}")

#AEH
AEH_x = AH(ax, ay, hx, hy, distance_a, distance_h)
AEH_z = AE(ax, ay, az, ex, ey, ez, distance_a, distance_e)
AEH_y = AEH(ax, ay, az, AEH_x, AEH_z, distance_a)
print(f"AEH(x, y, z) = {AEH_x, AEH_y, AEH_z}")

#AFG
AFG_x = FG(fx, fy, fz, gx, gy, gz, distance_f, distance_g)
AFG_z = AF(ax, az, fx, fz, distance_a, distance_f)
AFG_y = AFG(ax, ay, az, AFG_x, AFG_z, distance_a)
print(f"AFG(x, y, z) = {AFG_x, AFG_y, AFG_z}")

#AFH
AFH_x = AH(ax, ay, hx, hy, distance_a, distance_h)
AFH_z = AF(ax, az, fx, fz, distance_a, distance_f)
AFH_y = AFH(ax, ay, az, AFH_x, AFH_z, distance_a)
print(f"AFH(x, y, z) = {AFH_x, AFH_y, AFH_z}")

#AGH
AGH_x = AH(ax, ay, hx, hy, distance_a, distance_h)
AGH_y = GH(gx, gy, gz, hx, hy, hz, distance_g, distance_h)
AGH_z = AGH(ax, ay, az, AGH_x, AGH_y, distance_a)
print(f"AGH(x, y, z) = {AGH_x, AGH_y, AGH_z}")

#BCD
BCD_x = BC(bx, by, bz, cx, cy, cz, distance_b, distance_c)
BCD_y = CD(cx, cy, cz, dx, dy, dz, distance_c, distance_d)
BCD_z = BCD(bx, by, bz, BCD_x, BCD_y, distance_b)
print(f"BCD(x, y, z) = {BCD_x, BCD_y, BCD_z}")

#BCE
BCE_x = BC(bx, by, bz, cx, cy, cz, distance_b, distance_c)
BCE_y = BE(bx, by, ex, ey, distance_b, distance_e)
BCE_z = BCE(bx, by, bz, distance_b, BCE_x, BCE_y)
print(f"BCE(x, y, z) = {BCE_x, BCE_y, BCE_z}")

#BCF
BCF_x = BC(bx, by, bz, cx, cy, cz, distance_b, distance_c)
BCF_z = BF(bx, by, bz, fx, fy, fz, distance_b, distance_f)
BCF_y = BCF(bx, by, bz, BCF_x, BCF_z, distance_b)
print(f"BCF(x, y, z) = {BCF_x, BCF_y, BCF_z}")

#BCG
BCG_x = BC(bx, by, bz, cx, cy, cz, distance_b, distance_c)
BCG_z = CG(cx, cy, cz, gx, gy, gz, distance_c, distance_g)
BCG_y = BCG(bx, by, bz, BCG_x, BCG_z, distance_b)
print(f"BCG(x, y, z) = {BCG_x, BCG_y, BCG_z}")

#BCH
BCH_x = BC(bx, by, bz, cx, cy, cz, distance_b, distance_c)
BCH_y, BCH_z = BCH(bx, by, bz, hx, hy, BCH_x, distance_b, distance_h)
print(f"BCH(x, y, z) = {BCH_x, BCH_y, BCH_z}")

#BDE
BDE_x = BD(bx, bz, dx, dz, distance_b, distance_d)
BDE_y = BE(bx, by, ex, ey, distance_b, distance_e)
BDE_z = BDE(bx, by, bz, BDE_x, BDE_y, distance_b)
print(f"BDE(x, y, z) = {BDE_x, BDE_y, BDE_z}")

#BDF
BDF_x = BD(bx, bz, dx, dz, distance_b, distance_d)
BDF_z = BF(bx, by, bz, fx, fy, fz, distance_b, distance_f)
BDF_y = BDF(bx, by, bz, BDF_x, BDF_z, distance_b)
print(f"BDF(x, y, z) = {BDE_x, BDF_y, BDE_z}")

#BDG
BDG_x = BD(bx, bz, dx, dz, distance_b, distance_d)
BDG_z = BG(by, bz, gy, gz, distance_b, distance_g)
BDG_y = BDG(bx, by, bz, BDG_x, BDG_z, distance_b)
print(f"BDG(x, y, z) = {BDG_x, BDG_y, BDG_z}")

#BDH
BDH_x = BD(bx, bz, dx, dz, distance_b, distance_d)
BDH_z = DH(dx, dy, dz, hx, hy, hz, distance_d, distance_h)
BDH_y = BDH(bx, by, bz, BDH_x, BDH_z, distance_b)
print(f"BDH(x, y, z) = {BDH_x, BDH_y, BDH_z}")

#BEF
BEF_y = BE(bx, by, ex, ey, distance_b, distance_e)
BEF_z = BF(bx, by, bz, fx, fy, fz, distance_b, distance_f)
BEF_x = BEF(bx, by, bz, BEF_y, BEF_z, distance_b)
print(f"BEF(x, y, z) = {BEF_x, BEF_y, BEF_z}")

#BEG
BEG_y = BE(bx, by, ex, ey, distance_b, distance_e)
BEG_z = BG(by, bz, gy, gz, distance_b, distance_g)
BEG_x = BEG(bx, by, bz, BEG_y, BEG_z, distance_b)
print(f"BEG(x, y, z) = {BEG_x, BEG_y, BEG_z}")

#BEH
BEH_y = BE(bx, by, ex, ey, distance_b, distance_e)
BEH_x = EH(ex, ey, ez, hx, hy, hz, distance_e, distance_h)
BEH_z = BEH(bx, by, bz, BEH_x, BEH_y, distance_b)
print(f"BEH(x, y, z) = {BEH_x, BEH_y, BEH_z}")

#BFG
BFG_z = BF(bx, by, bz, fx, fy, fz, distance_b, distance_f)
BFG_x = FG(fx, fy, fz, gx, gy, gz, distance_f, distance_g)
BFG_y = BFG(bx, by, bz, BFG_x, BFG_z, distance_b)
print(f"BFG(x, y, z) = {BFG_x, BFG_y, BFG_z}")

#BFH
BFH_z = BF(bx, by, bz, fx, fy, fz, distance_b, distance_f)
BFH_x = FH(fx, fz, hx, hz, distance_f, distance_h)
BFH_y = BFH(bx, by, bz, BFH_x, BFH_z, distance_b)
print(f"BFH(x, y, z) = {BFH_x, BFH_y, BFH_z}")

#BGH
BGH_z = BG(by, bz, gy, gz, distance_b, distance_g)
BGH_y = GH(gx, gy, gz, hx, hy, hz, distance_g, distance_h)
BGH_x = BGH(bx, by, bz, BGH_y, BGH_z, distance_b)
print(f"BGH(x, y, z) = {BGH_x, BGH_y, BGH_z}")

#CDE
CDE_y = CD(cx, cy, cz, dx, dy, dz, distance_c, distance_d)
CDE_z = DE(dy, dz, ey, ez, distance_d, distance_e)
CDE_x = CDE(cx, cy, cz, CDE_y, CDE_z, distance_c)
print(f"CDE(x, y, z) = {CDE_x, CDE_y, CDE_z}")

#CDF
CDF_y = CD(cx, cy, cz, dx, dy, dz, distance_c, distance_d)
CDF_z = CF(cy, cz, fy, fz, distance_c, distance_f)
CDF_x = CDF(cx, cy, cz, CDF_y, CDF_z, distance_c)
print(f"CDF(x, y, z) = {CDF_x, CDF_y, CDF_z}")

#CDG
CDG_y = CD(cx, cy, cz, dx, dy, dz, distance_c, distance_d)
CDG_z = CG(cx, cy, cz, gx, gy, gz, distance_c, distance_g)
CDG_x = CDG(cx, cy, cz, CDG_y, CDG_z, distance_c)
print(f"CDG(x, y, z) = {CDG_x, CDG_y, CDG_z}")

#CDH
CDH_y = CD(cx, cy, cz, dx, dy, dz, distance_c, distance_d)
CDH_z = DH(dx, dy, dz, hx, hy, hz, distance_d, distance_h)
CDH_x = CDH(cx, cy, cz, CDH_y, CDH_z, distance_c)
print(f"CDH(x, y, z) = {CDH_x, CDH_y, CDH_z}")

#CEF
CEF_z = CF(cy, cz, fy, fz, distance_c, distance_f)
CEF_y = EF(ex, ey, ez, fx, fy, fz, distance_e, distance_f)
CEF_x = CEF(cx, cy, cz, CEF_y, CEF_z, distance_c)
print(f"CEF(x, y, z) = {CEF_x, CEF_y, CEF_z}")

#CEG
CEG_z = CG(cx, cy, cz, gx, gy, gz, distance_c, distance_g)
CEG_x = EG(ex, ez, gx, gz, distance_e, distance_g)
CEG_y = CEG(cx, cy, cz, CEG_x, CEG_z, distance_c)
print(f"CEG(x, y, z) = {CEG_x, CEG_y, CEG_z}")

#CEH
CEH_x = EH(ex, ey, ez, hx, hy, hz, distance_e, distance_h)
CEH_z, CEH_y = CEH(cx, cy, cz, ex, ez, CEH_x, distance_c, distance_e)
print(f"CEH(x, y, z) = {CEH_x, CEH_y, CEH_z}")

#CFG
CFG_z = CF(cy, cz, fy, fz, distance_c, distance_f)
CFG_x = FG(fx, fy, fz, gx, gy, gz, distance_f, distance_g)
CFG_y = CFG(cx, cy, cz, CFG_x, CFG_z, distance_c)
print(f"CFG(x, y, z) = {CFG_x, CFG_y, CFG_z}")

#CFH
CFH_z = CF(cy, cz, fy, fz, distance_c, distance_f)
CFH_x = FH(fx, fz, hx, hz, distance_f, distance_h)
CFH_y = CFH(cx, cy, cz, CFH_x, CFH_z, distance_c)
print(f"CFH(x, y, z) = {CFH_x, CFH_y, CFH_z}")

#CGH
CGH_z = CG(cx, cy, cz, gx, gy, gz, distance_c, distance_g)
CGH_y = GH(gx, gy, gz, hx, hy, hz, distance_g, distance_h)
CGH_x = CGH(cx, cy, cz, CGH_y, CGH_z, distance_c)
print(f"CGH(x, y, z) = {CGH_x, CGH_y, CGH_z}")

#DEF
DEF_z = DE(dy, dz, ey, ez, distance_d, distance_e)
DEF_y = EF(ex, ey, ez, fx, fy, fz, distance_e, distance_f)
DEF_x = DEF(dx, dy, dz, DEF_y, DEF_z, distance_d)
print(f"DEF(x, y, z) = {DEF_x, DEF_y, DEF_z}")

#DEG
DEG_z = DE(dy, dz, ey, ez, distance_d, distance_e)
DEG_y = DG(dx, dy, gx, gy, distance_d, distance_g)
DEG_x = DEG(dx, dy, dz, DEG_y, DEG_z, distance_d)
print(f"DEG(x, y, z) = {DEG_x, DEG_y, DEG_z}")

#DEH
DEH_z = DE(dy, dz, ey, ez, distance_d, distance_e)
DEH_x = EH(ex, ey, ez, hx, hy, hz, distance_e, distance_h)
DEH_y = DEH(dx, dy, dz, DEH_x, DEH_z, distance_d)
print(f"DEH(x, y, z) = {DEH_x, DEH_y, DEH_z}")

#DFG
DFG_y = DG(dx, dy, gx, gy, distance_d, distance_g)
DFG_x = FG(fx, fy, fz, gx, gy, gz, distance_f, distance_g)
DFG_z = DFG(dx, dy, dz, DFG_x, DFG_y, distance_d)
print(f"DFG(x, y, z) = {DFG_x, DFG_y, DFG_z}")

#DFH
DFH_z = DH(dx, dy, dz, hx, hy, hz, distance_d, distance_h)
DFH_x = FH(fx, fz, hx, hz, distance_f, distance_h)
DFH_y = DFH(dx, dy, dz, DFH_x, DFH_z, distance_d)
print(f"DFH(x, y, z) = {DFH_x, DFH_y, DFH_z}")

#DGH
DGH_y = DG(dx, dy, gx, gy, distance_d, distance_g)
DGH_z = DH(dx, dy, dz, hx, hy, hz, distance_d, distance_h)
DGH_x = DGH(dx, dy, dz, DGH_y, DGH_z, distance_d)
print(f"DGH(x, y, z) = {DGH_x, DGH_y, DGH_z}")

#EFG
EFG_y = EF(ex, ey, ez, fx, fy, fz, distance_e, distance_f)
EFG_x = EG(ex, ez, gx, gz, distance_e, distance_g)
EFG_z = EFG(ex, ey, ez, EFG_x, EFG_y, distance_e)
print(f"EFG(x, y, z) = {EFG_x, EFG_y, EFG_z}")

#EFH
EFH_y = EF(ex, ey, ez, fx, fy, fz, distance_e, distance_f)
EFH_x = FH(fx, fz, hx, hz, distance_f, distance_h)
EFH_z = EFH(ex, ey, ez, EFH_x, EFH_y, distance_e)
print(f"EFH(x, y, z) = {EFH_x, EFH_y, EFH_z}")

#EGH
EGH_x = EG(ex, ez, gx, gz, distance_e, distance_g)
EGH_y = GH(gx, gy, gz, hx, hy, hz, distance_g, distance_h)
EGH_z = EGH(ex, ey, ez, EGH_x, EGH_y, distance_e)
print(f"EGH(x, y, z) = {EGH_x, EGH_y, EGH_z}")

#FGH
FGH_x = FG(fx, fy, fz, gx, gy, gz, distance_f, distance_g)
FGH_y = GH(gx, gy, gz, hx, hy, hz, distance_g, distance_h)
FGH_z = FGH(fx, fy, fz, FGH_x, FGH_y, distance_f)
print(f"FGH(x, y, z) = {FGH_x, FGH_y, FGH_z}")