
# use sagemath 9.3 console

E = EllipticCurve(GF(9739), [497, 1768])

# in my case, y*y=5507(mod p)
# so, quodrant root modulo p is 5507^((p+1)/4)=6284(mod p)

P = E(4726, 6287)

# print(shared secret)
print(str((6534*P)[0]))
