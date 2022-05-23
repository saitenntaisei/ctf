def babystep_giantstep(G, Y, Q):
    m = int((Q-1) ^ 0.5 + 0.5)
    print(m)
    # Baby step
    table = {}
    YrG = Y  # Y-r*G
    for r in range(m):
        table[YrG] = r
        YrG -= G
    print('babystepdone')
    # Giant step
    mG = m * G  # m*G
    qmG = mG    # qm*G
    for q in range(1, m):
        if qmG in table:  # 左辺と右辺が一致するとき
            return q * m + table[qmG]
        qmG += mG
    return None

# Pohlig–Hellman法


def pohlig_hellman_ECDLP(G, Y, E):
    crt_moduli = []
    crt_remain = []
    for q, e in factor(G.order()):
        print('q =', q)
        beta = (E.order()//(q ^ e))
        res = 0
        z = babystep_giantstep(beta*G, beta*Y, q ^ e)
        #z=discrete_log(Y0*(E.order()//q^(i+1)),G0, operation = '+')
        res = z
        if (res is None) or (res <= 1):
            continue
        crt_moduli.append(q ^ e)
        crt_remain.append(res)
    ans = crt(crt_remain, crt_moduli)
    if ans is None:
        return None
    if G * ans == Y:
        return ans
    return None


p = 310717010502520989590157367261876774703
F = GF(p)
E = EllipticCurve(F, [0, 0, 0, 2, 3])  # Curve25519
g = E(179210853392303317793440285562762725654,
      105268671499942631758568591033409611165)  # E.gen(0)
y = E(280810182131414898730378982766101210916,
      291506490768054478159835604632710368904)
print('E.order=', E.order())
print('factorE=', factor(E.order()))
x = pohlig_hellman_ECDLP(g, y, E)
print(x)
print(y == x*g)
