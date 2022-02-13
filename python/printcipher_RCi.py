def round_counter():
    RCi = 0
    RCi_list = []
    # print(type(RCi))
    l = 0
    for l in range (48):
        # print(type(RCi))
        RCi = bin(RCi)[2:].zfill(6)
        RCi_one_list = [int(d) for d in str((RCi))]
        # print(RCi_one_list)
        t = 1 + RCi_one_list[0] + RCi_one_list[1]
        t = t % 2
        RCi_one_list.append(RCi_one_list.pop(0))
        # print(RCi_one_list)
        RCi_one_list[5] = t
        RCi = ''.join((str(e) for e in  RCi_one_list))
        RCi_list.append(RCi)
        # print(RCi, i, "bin")
        RCi = int(RCi, 2)
        # print(RCi, i, "dec")
        
    return RCi_list

# RCi = 0
# # print(type(RCi))
# # for i in range(16):
# a = round_counter()
# print(a)