import printcipher_P_layer
import printcipher_S_layer
import printcipher_RCi

def round(plaintext, key, permkey_bin, i_round, RCi_list):
    # print(plaintext, "pt", i_round, "adasda")
    # print(type(plaintext), "type")
    plaintext = int(plaintext, 2)
    # print(plaintext, "pt", i_round)
    xored = str(key ^ plaintext)
    # print(xored, "xored", i_round)
    xored_bin = bin(int(str(xored), 10))[2:].zfill(48)
    bef = 0
    af = 0
    before_linear_diff = [int(bef) for bef in str((xored_bin))]
    after_linear_diff = [None] * 48
    permkey_list = [int(af) for af in str((permkey_bin))]
    # print(permkey_list, "list")
    j = 0
    for j in range(48):
        if (0 <= j < 47):
            q = (((3 * j) % 47))
            after_linear_diff[q] = before_linear_diff[j]
        else:
            after_linear_diff[47] = before_linear_diff[47]
    # c = bin(int(''.join(map(str, before_linear_diff)), 2) << 1)[2:-1]
    # d = bin(int(''.join(map(str, after_linear_diff)), 2) << 1)[2:-1]
    # print(c, "c")
    # print(d)
    # RCi definition
    # daha sonra yapacağım
    # RCi = [0, 0, 0, 0, 0, 1]
    # RCi_list = []
    # # RCi_list = printcipher_RCi.round_counter()
    # print(a)
    # print(i_round)
    ## RCi_list listesindeki her bir indisteki
    ## stringi integer sayıya çeviriyor
    x = 0
    RCi = [int(x) for x in RCi_list[i_round]]
    # print(RCi)
    # xor RCi
    a = 0
    b = 0
    after_linear_diff[42:48] = list(
        a ^ b for a, b in zip(after_linear_diff[42:48], RCi))
    # print(permkey_list, "fii")

    # p and s layer
    round_final_list = []
    i = 0
    for i in range(0, 16):
        c = str(after_linear_diff[3 * i + 0]) + str(
            after_linear_diff[3 * i + 1]) + str(after_linear_diff[3 * i + 2])
        c = (int(c, 2))
        # print(type(c))
        # c = format(c, '#05b')
        pk = str(permkey_list[2 * i + 0]) + str(permkey_list[2 * i + 1])
        # print(pk, "ada")
        pk = (int(pk, 2))
        # print(pk)
        # print(type(pk))
        # pk = format(pk, '#04b')
        # print(pk, "pk")
        t = printcipher_P_layer.p_layer(pk, c)
        # print(t, "player")
        three_bit_out_text = 0
        z = printcipher_S_layer.s_layer(t)
        # print(z, "z", i)
        # print(type(z))
        z_bin = bin(int(str(z), 10))[2:].zfill(3)
        round_final_list.append(z_bin)
        # print((z_bin))
        # print("***")

    str1 = ''.join(round_final_list)
    # print(str1, "str1")
    # print(type(str1))
    tttt = (int(str1, 2))
    # print(tttt)
    int_str1 = int(str1, 16)
    # print(type(int_str1), "type str1", i_round)
    # print(int_str1)
    # print("**************")
    return str1


