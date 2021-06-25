#!usr/bin/python

import hashlib

hash_qiymat_oldin = input(" <??>:")

print("\n  md5")

hash_qiymat_kegin1 = hashlib.md5()
hash_qiymat_kegin1.update(hash_qiymat_oldin.encode())
print(hash_qiymat_kegin1.hexdigest())
print("\n sha1")

hash_qiymat_kegin2 = hashlib.sha1()
hash_qiymat_kegin2.update(hash_qiymat_oldin.encode())
print(hash_qiymat_kegin2.hexdigest())
print("\n sha224")

hash_qiymat_kegin3 = hashlib.sha224()
hash_qiymat_kegin3.update(hash_qiymat_oldin.encode())
print(hash_qiymat_kegin3.hexdigest())
print("\n sha256")

hash_qiymat_kegin4 = hashlib.sha256()
hash_qiymat_kegin4.update(hash_qiymat_oldin.encode())
print(hash_qiymat_kegin4.hexdigest())
print("\n sha512")

hash_qiymat_kegin5 = hashlib.sha512()
hash_qiymat_kegin5.update(hash_qiymat_oldin.encode())
print(hash_qiymat_kegin5.hexdigest())
