global RCi
def round_counter(i):
    RCi = bin(i)[2:].zfill(6)
    RCi_list = [int(d) for d in str((RCi))]
    # print(RCi_list)
    t = 1 + RCi_list[0] + RCi_list[1]
    t = t % 2
    RCi_list.append(RCi_list.pop(0))
    # print(RCi_list)
    RCi_list[5] = t
    print(RCi_list, i)
    return RCi

for i in range(16):
    a = round_counter(i)