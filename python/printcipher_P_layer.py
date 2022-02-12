# permkey_2_bit : 2 bit binary string
# three_bit_text: 3 bit binary

def p_layer(permkey_2_bit, three_bit_in_text):
    three_bit_in_text = format(three_bit_in_text, '#05b')
    c2 = ((three_bit_in_text))[2:3]
    c1 = ((three_bit_in_text))[3:4]
    c0 = ((three_bit_in_text))[4:5]
    # print((three_bit_text))
    result = 0b000
    if permkey_2_bit == 0b00:
        result = c2 + c1 + c0
        # print(result)
    elif permkey_2_bit == 0b01:
        result = c1 + c2 + c0
        # print(result)
    elif permkey_2_bit == 0b10:
        result = c2 + c0 + c1
        # print(result)
    elif permkey_2_bit == 0b11:
        result = c0 + c1 + c2
        # print(result)
    result = (int(result, 2))
    # print(result, "format öncsi")
    result = format(result, '#05b')
    # print(result, "func içi")
    return result

# x = 0
# y = 6 
# print((x))
# print((y))
# b = p_layer(x,y)
# print(b)