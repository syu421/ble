import sympy

# RSSI値から距離推定
def RSSItoMetricConversion(rssi):
    TxPower = -66.04316709
    n = 4
    distance = 10 ** ((TxPower - rssi) / (10 * n))
    return round(distance,2)

#def three_point_positioning(X_x, X_y, X_z, Y_x, Y_y, Y_z, X_D, Y_D):
    #x, y, z = symbols("x y z")
    # (2ax - 2bx)x + (2ay - 2by)y + (2az - 2bz)z = distance_b**2 - distance_a**2 + (ax**2 + ay**2 + az**2) - (bx**2 + by**2 + bz**2)
    #return (2*X_x - 2*Y_x)*x + (2*X_y - 2*Y_y)*y + (2*X_z - 2*Y_z)*z


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

print(f"A:{distance_a}\nB:{distance_b}\nC:{distance_c}\nD:{distance_d}\nE:{distance_e}\nF:{distance_f}\nG:{distance_g}\nH:{distance_h}\n")

# 座標
ax, ay, az = 0.0, 0.0, 0.0
bx, by, bz = 0.0, 2.0, 0.0
cx, cy, cz = 2.0, 2.0, 0.0
dx, dy, dz = 2.0, 0.0, 0.0
ex, ey, ez = 0.0, 0.0, 2.0
fx, fy, fz = 0.0, 2.0, 2.0
gx, gy, gz = 2.0, 2.0, 2.0
hx, hy, hz = 2.0, 0.0, 2.0

x, y, z = sympy.symbols("x y z")

AB = (2*ax - 2*bx)*x + (2*ay - 2*by)*y + (2*az - 2*bz)*z - distance_b**2 + distance_a**2 - (ax**2 + ay**2 + az**2) + (bx**2 + by**2 + bz**2)
AB_l = (2*ax - 2*bx)*x + (2*ay - 2*by)*y + (2*az - 2*bz)*z
AB_r = distance_b**2 - distance_a**2 + (ax**2 + ay**2 + az**2) - (bx**2 + by**2 + bz**2)
AC = (2*ax - 2*cx)*x + (2*ay - 2*cy)*y + (2*az - 2*cz)*z - distance_c**2 + distance_a**2 - (ax**2 + ay**2 + az**2) + (cx**2 + cy**2 + cz**2)
BC = (2*bx - 2*cx)*x + (2*by - 2*cy)*y + (2*bz - 2*cz)*z - distance_c**2 + distance_b**2 - (bx**2 + by**2 + bz**2) + (cx**2 + cy**2 + cz**2)

#print(AB_l)
#print(AB_r)
#AB = AB_r/(AB_l/y)
print(AB)
print(AC)
print(BC)
#print(f"AB:{AB}, AC:{AC}, BC:{BC}")
#y = 4.206 / 4.0
#print(y)
#x = 2.8868 / 4.0
#print(x)
#z = 0
#print(f"(x,y,z) = {(x, y, z)}")
a = sympy.solve(AB, AC, BC)
print(a)