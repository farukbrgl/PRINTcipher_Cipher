import printcipher_P_layer
import printcipher_S_layer

def round(plaintext, key, permkey_bin):
    xored = str(key ^ plaintext)
    # print(xored)
    xored_bin = bin(int(str(xored), 10))[2:].zfill(48)
    before_linear_diff = [int(d) for d in str((xored_bin))]
    after_linear_diff = [None] * 48
    permkey_list = [int(d) for d in str((permkey_bin))]
    # print(permkey_list, "list")
    for i in range(48):
        if (0 <= i < 47):
            a = (((3 * i) % 47))
            after_linear_diff[a] = before_linear_diff[i]
        else:
            after_linear_diff[47] = before_linear_diff[47]
    c = bin(int(''.join(map(str, before_linear_diff)), 2) << 1)[2:-1]
    d = bin(int(''.join(map(str, after_linear_diff)), 2) << 1)[2:-1]
    # print(c, "c")
    # print(d)

    # RCi definition
    # daha sonra yapacağım
    RCi = [0, 0, 0, 0, 0, 1]

    # xor RCi
    after_linear_diff[42:48] = list(
        a ^ b for a, b in zip(after_linear_diff[42:48], RCi))
    print(permkey_list, "fii")

    # p and s layer
    round_final_list = []
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
        print(pk, "pk")
        t = printcipher_P_layer.p_layer(pk, c)
        print(t, "player")
        three_bit_out_text = 0
        z = printcipher_S_layer.s_layer(t)
        print(z, "z", i)
        # print(type(z))
        z_bin = bin(int(str(z), 10))[2:].zfill(3)
        round_final_list.append(z_bin)
        print((z_bin))
        print("***")

    str1 = ''.join(round_final_list)
    print(str1)