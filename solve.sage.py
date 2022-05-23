

# This file was *autogenerated* from the file solve.sage
from sage.all_cmdline import *   # import sage library

_sage_const_1 = Integer(1); _sage_const_0p5 = RealNumber('0.5'); _sage_const_0 = Integer(0); _sage_const_310717010502520989590157367261876774703 = Integer(310717010502520989590157367261876774703); _sage_const_2 = Integer(2); _sage_const_3 = Integer(3); _sage_const_179210853392303317793440285562762725654 = Integer(179210853392303317793440285562762725654); _sage_const_105268671499942631758568591033409611165 = Integer(105268671499942631758568591033409611165); _sage_const_280810182131414898730378982766101210916 = Integer(280810182131414898730378982766101210916); _sage_const_291506490768054478159835604632710368904 = Integer(291506490768054478159835604632710368904)
def babystep_giantstep(G, Y, Q):
    m = int((Q-_sage_const_1 ) ** _sage_const_0p5  + _sage_const_0p5 )
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
    for q in range(_sage_const_1 , m):
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
        beta = (E.order()//(q ** e))
        res = _sage_const_0 
        z = babystep_giantstep(beta*G, beta*Y, q ** e)
        #z=discrete_log(Y0*(E.order()//q^(i+1)),G0, operation = '+')
        res = z
        if (res is None) or (res <= _sage_const_1 ):
            continue
        crt_moduli.append(q ** e)
        crt_remain.append(res)
    ans = crt(crt_remain, crt_moduli)
    if ans is None:
        return None
    if G * ans == Y:
        return ans
    return None


p = _sage_const_310717010502520989590157367261876774703 
F = GF(p)
E = EllipticCurve(F, [_sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_2 , _sage_const_3 ])  # Curve25519
g = E(_sage_const_179210853392303317793440285562762725654 ,
      _sage_const_105268671499942631758568591033409611165 )  # E.gen(0)
y = E(_sage_const_280810182131414898730378982766101210916 ,
      _sage_const_291506490768054478159835604632710368904 )
print('E.order=', E.order())
print('factorE=', factor(E.order()))
x = pohlig_hellman_ECDLP(g, y, E)
print(x)
print(y == x*g)
