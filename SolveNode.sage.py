

# This file was *autogenerated* from the file SolveNode.sage
from sage.all_cmdline import *   # import sage library

_sage_const_4368590184733545720227961182704359358435747188309319510520316493183539079703 = Integer(4368590184733545720227961182704359358435747188309319510520316493183539079703); _sage_const_2582928974243465355371953056699793745022552378548418288211138499777818633265 = Integer(2582928974243465355371953056699793745022552378548418288211138499777818633265); _sage_const_2421683573446497972507172385881793260176370025964652384676141384239699096612 = Integer(2421683573446497972507172385881793260176370025964652384676141384239699096612); _sage_const_8742397231329873984594235438374590234800923467289367269837473862487362482 = Integer(8742397231329873984594235438374590234800923467289367269837473862487362482); _sage_const_225987949353410341392975247044711665782695329311463646299187580326445253608 = Integer(225987949353410341392975247044711665782695329311463646299187580326445253608); _sage_const_2 = Integer(2); _sage_const_3 = Integer(3); _sage_const_0 = Integer(0); _sage_const_1 = Integer(1); _sage_const_64186688762130075872648727143532923412208390610536286437268423112 = Integer(64186688762130075872648727143532923412208390610536286437268423112); _sage_const_32579945572763798990069104934898692239152360555014084068553395172709029894 = Integer(32579945572763798990069104934898692239152360555014084068553395172709029894); _sage_const_1557923326969252180825193218688702224840389936248863823173183835359957757721 = Integer(1557923326969252180825193218688702224840389936248863823173183835359957757721); _sage_const_305179796174210822247618473361747316085422620437271958999235012896334193460 = Integer(305179796174210822247618473361747316085422620437271958999235012896334193460)
p = _sage_const_4368590184733545720227961182704359358435747188309319510520316493183539079703 
fp = GF(p)

x1 = fp(_sage_const_2582928974243465355371953056699793745022552378548418288211138499777818633265 )
y1 = fp(_sage_const_2421683573446497972507172385881793260176370025964652384676141384239699096612 )
x2 = fp(_sage_const_8742397231329873984594235438374590234800923467289367269837473862487362482 )
y2 = fp(_sage_const_225987949353410341392975247044711665782695329311463646299187580326445253608 )

R = PolynomialRing(fp, names=('a', 'b',)); (a, b,) = R._first_ngens(2)
f = y1**_sage_const_2  - (x1**_sage_const_3  + a*x1 + b)
g = y2**_sage_const_2  - (x2**_sage_const_3  + a*x2 + b)
print(f)
print(g)

I = ideal(f, g)
B = I.groebner_basis()
print(B[_sage_const_0 ])
print(-B[_sage_const_0 ])
print(-B[_sage_const_1 ])
R = PolynomialRing(fp, names=('x',)); (x,) = R._first_ngens(1)
a=_sage_const_64186688762130075872648727143532923412208390610536286437268423112 
b=_sage_const_32579945572763798990069104934898692239152360555014084068553395172709029894 
u=-x**_sage_const_3 -a*x-b
print(u.roots())
singular = vector([fp(_sage_const_1557923326969252180825193218688702224840389936248863823173183835359957757721 ),fp(_sage_const_0 )])
# E = EllipticCurve(fp, [a, b])
R = PolynomialRing(fp, names=('x',)); (x,) = R._first_ngens(1)
f = x**_sage_const_3  + a*x + b
f_ = f.subs(x+singular[_sage_const_0 ])
print(f_)

Q = vector([x1, y1])-(singular)
P = vector([x2, y2])-(singular)
k=fp(_sage_const_305179796174210822247618473361747316085422620437271958999235012896334193460 )
t = k.square_root()
# Q=dP->fq=(fp)^d (node) 掛け算のDLP F^*
# Q=dP -> q = dp (cusp) 足し算のDLP F^+
Px, Py = P
Qx, Qy = Q
p = (Py + t*Px) / (Py - t*Px)
q = (Qy + t*Qx) / (Qy - t*Qx)

d = q.log(p)
#d = p.log(q)
#d = q.log(p)
print(d)
from Crypto.Util.number import *
print(long_to_bytes(int(d)))
