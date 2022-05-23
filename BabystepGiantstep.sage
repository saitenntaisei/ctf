def babystep_giantstep(G, Y, E):
    m = int((E.order()-1)**0.5 + 0.5)
    # Baby step
    table = {}
    YrG = Y  # Y-r*G
    for r in range(m):
        table[YrG] = r
        YrG -= G
    # Giant step
    mG = m * G  # m*G
    qmG = mG    # qm*G
    for q in range(1, m):
        if qmG in table:  # 左辺と右辺が一致するとき
            return q * m + table[qmG]
        qmG += mG
    return None

p = 240556067
F = GF(p)
E = EllipticCurve(F, [0, 486662, 0, 1, 0])  # Curve25519
G = E(103666880, 133544401)
Y = E(220898463, 208070124)

x = babystep_giantstep(G, Y, E)
print(x)
print(Y == x*G)