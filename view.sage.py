

# This file was *autogenerated* from the file ./cryptoHack/view.sage
from sage.all_cmdline import *   # import sage library

_sage_const_9739 = Integer(9739); _sage_const_497 = Integer(497); _sage_const_1768 = Integer(1768); _sage_const_4726 = Integer(4726); _sage_const_6287 = Integer(6287); _sage_const_6534 = Integer(6534); _sage_const_0 = Integer(0)
# use sagemath 9.3 console

E = EllipticCurve(GF(_sage_const_9739 ), [_sage_const_497 , _sage_const_1768 ])

# in my case, y*y=5507(mod p)
# so, quodrant root modulo p is 5507^((p+1)/4)=6284(mod p)

P = E(_sage_const_4726 , _sage_const_6287 )

# print(shared secret)
print(str((_sage_const_6534 *P)[_sage_const_0 ]))

