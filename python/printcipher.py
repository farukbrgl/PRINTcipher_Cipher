#!/usr/bin/env python
# coding: utf-8
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
key = 0xC28895BA327B
plaintext = 0x4C847555C35B
permkey = 0x69D2CDB6
key_bin = bin(int(str(key), 16))[2:].zfill(48)
plaintext_bin = bin(int(str(plaintext), 16))[2:].zfill(48)
# permkey_bin   = bin(int(str(permkey), 16))[2:].zfill(32)
permkey_bin = format(permkey, "032b")
# print(key_bin, "bin")
# print(key, "perm")


a = printcipher_round.round(plaintext, key, permkey_bin)
