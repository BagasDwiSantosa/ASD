from email import message
import timeit
# Impor kelas Timer yang ditentukan dalam modul
from timeit import Timer


# remove_zero = Timer("x.remove(0)", "from __main__ import x")
# remove_end = Timer("x.remove()", "from __main__ import x")
# a = []
# print("\ti\t\t\tremove(0)\t\t\tremove()")
# for i in range(1000000,100000001,1000000):
#     x = list(range(i))
#     pt = remove_end.timeit(number=1000)
#     x = list(range(i))
#     pz = remove_zero.timeit(number=1000)
#     print("%15.5f,\t%15.5f,\t%15.5f" %(i,pz,pt))


# import timeit
# import random
# a = []
# for i in range(10000,1000001,20000):
#     t = timeit.Timer("random.randrange(%d) in x"%i,
#     "from __main__ import random,x")

#     x = list(range(i))
#     lst_time = t.timeit(number=1000)
#     x = {j:None for j in range(i)}
#     d_time = t.timeit(number=1000)
#     # print("%d,%10.3f,%10.3f" % (i, lst_time, d_time))
#     p"%d"%(i))




# import timeit
# import random

# a= []
# remove_end = Timer("x.append(i)","from __main__ import x")
# for i in range(1, 1000, 10):
#     x = list(range(i))
#     h = remove_end.timeit(number=1000)
#     print(h)


import cryptocode
# me = 'halo'
# dec = cryptocode.encrypt(me, "password123")
# print(dec)

# import cryptocode
# me = 'halo'
# dec = cryptocode.decrypt(me, "password123")
# print('hasil : ',dec)


# def decrypt(message):
#     message= message.replace( ':','')
#     message= message.replace(';','')

#     message=message.replace(',','')

#     message= message.replace('.','')

#     message= message.replace('?','')

#     message = message.replace('!','')

#     message = message.upper()

#     decrypted_message = ''

#     for c in message:
#         if c not in ALPHABET :
#             decrypted_message += c
#             continue

#         index_in_alphabet = ALPHABET.find(c)
#         shifted_index = len(ALPHABET) - 1 - index_in_alphabet
#         decrypted_message += ALPHABET[shifted_index]

#     return decrypted_message


# decrypt('halo')
#!/usr/bin/env python

import base64

from Crypto import Random
from Crypto.Cipher import AES

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-ord(s[-1])]


class AESCipher:

    def __init__( self, key ):
        self.key = key

    def encrypt( self, raw ):
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) )

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc[16:] ))


cipher = AESCipher('mysecretpassword')
encrypted = cipher.encrypt('Secret Message A')
decrypted = cipher.decrypt(encrypted)
print (encrypted)
print (decrypted)