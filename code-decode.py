def encoding():
    start = -8192
    end = 8191
    # Getting integer value from user
    raw_value = int(input("Enter signed integer: "))
    print(type(raw_value))
    print(raw_value)
    # validating user given input range
    if raw_value < start or raw_value > end:
        print("signed integer should be in the 14-bit range [-8192..+8191]")
    else:
        print("good")
        # Adding 8192 to raw-value so its range is translated to [0..16383]
        number = raw_value + 8192
        print(type(number))
        # Separate L bits with bitwise AND using bit mask 0x007f(binary 00000000 01111111)
        low_byte = number & 0x007F
        # Shift all value to left, now H bits stay at the final places
        number = number << 1
        print(number)
        # Separate H bits with bitwise AND using bit mask 0x7f00(binary 01111111 00000000)
        high_byte = number & 0x7F00
        print(high_byte)
        print(type(high_byte))
        # Combine low and high bytes together with binary OR
        encode_value = low_byte | high_byte
        print(encode_value)
        print(hex(encode_value))
        # Returning a single 4-character hexadecimal string
        return format(encode_value, 'X')


def decoding():
    start = 0x00
    end = 0x7F
    # Getting hexa decimal strings from user
    high_byte = input("Enter high byte: ")
    print(high_byte)
    print(type(high_byte))
    low_byte = input("Enter Low byte: ")
    # Returns an integer value, which is equivalent of string in the given base.
    hi_byte = int(high_byte, 16)
    print(hi_byte)
    print(type(hi_byte))
    lo_byte = int(low_byte, 16)
    # validating user given input range
    if hi_byte < start or hi_byte > end or lo_byte < start or lo_byte > end:
        print("two bytes should be in the range [0x00..0x7F]")
    else:
        print('good')
        # Shift all value to left 7 bits
        hi_byte = hi_byte << 7
        print(hi_byte)
        print(type(hi_byte))
        # Combine hi and lo bytes together with binary OR
        decode_value = (hi_byte | lo_byte) - 8192
        print(decode_value)
        print(type(decode_value))
        # Returning an integer between [-8192..+8191]
        return decode_value


decode_int = decoding()
encode_string = encoding()
