#!/usr/bin/env python
# coding: utf-8

# execution time : 20.792 s
"""
PRINTcipher Hafif Blok Şifreleyicisinin Python ile Gerçeklenmesi
Orijinal makaleye https://link.springer.com/chapter/10.1007/978-3-642-15031-9_2
adresinden ulaşabilirsiniz.
"""

"""
"""

import printcipher_round
import printcipher_S_layer
import printcipher_P_layer
import printcipher_RCi
key = 0xC28895BA327B
plaintext = "10011001000010001110101010101011100001101011011"
permkey = 0x69D2CDB6
key_bin = bin(int(str(key), 16))[2:].zfill(48)
plaintext_bin = bin(int(str(plaintext), 16))[2:].zfill(48)
# permkey_bin   = bin(int(str(permkey), 16))[2:].zfill(32)
permkey_bin = format(permkey, "032b")
# print(key_bin, "bin")
# print(key, "perm")
RCi_list = printcipher_RCi.round_counter()
i_round = 0

# 1 round için
# for i_round in range (48):
#     # print(plaintext, "before")
#     plaintext = printcipher_round.round(plaintext, key, permkey_bin, i_round, RCi_list)
# print(plaintext)

f = open("random_numbers_printcipher.txt", "w")
# prng için
for m in range(10000):
    for i_round in range(48):
        # print(plaintext, "before")
        plaintext = printcipher_round.round(
            plaintext, key, permkey_bin, i_round, RCi_list)

    f.write(plaintext + "\n")
f.close()
