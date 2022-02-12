def s_layer(three_bit_text):
    three_bit_out_text = three_bit_text
    if three_bit_text == "0b000":
        three_bit_out_text = 0
    elif three_bit_text == "0b001":
        three_bit_out_text = 1
    elif three_bit_text == "0b010":
        three_bit_out_text = 3
    elif three_bit_text == "0b011":
        three_bit_out_text = 6
    elif three_bit_text == "0b100":
        three_bit_out_text = 7
    elif three_bit_text == "0b101":
        three_bit_out_text = 4
    elif three_bit_text == "0b110":
        three_bit_out_text = 5
    elif three_bit_text == "0b111":
        three_bit_out_text = 2

    return three_bit_out_text