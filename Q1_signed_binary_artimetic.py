
def to_8bit_binary(num):
    return format(num & 0xFF, '08b')


def signed_value(binary):
    value = int(binary, 2)
    if value >= 128:
        value -= 256
    return value


def add_binary(a, b):
    bin_a = to_8bit_binary(a)
    bin_b = to_8bit_binary(b)

    unsigned_sum = int(bin_a, 2) + int(bin_b, 2)
    result = unsigned_sum & 0xFF
    bin_result = format(result, '08b')

    decimal_result = signed_value(bin_result)

    # Overflow occurs when same-sign operands
    # produce a result with the opposite sign.
    overflow = (
        (a >= 0 and b >= 0 and decimal_result < 0)
        or (a < 0 and b < 0 and decimal_result >= 0)
    )

    print("First operand :", bin_a, "(", a, ")")
    print("Second operand:", bin_b, "(", b, ")")
    print("Binary result :", bin_result)
    print("Decimal result:", decimal_result)
    print("Overflow      :", "Yes" if overflow else "No")
    print()


print("Expression (a): 25 + (+18)")
add_binary(25, 18)

print("Expression (b): (-25) + (-18)")
add_binary(-25, -18)
