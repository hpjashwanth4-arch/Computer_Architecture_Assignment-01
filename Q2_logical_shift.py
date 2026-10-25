
def logical_left_shift(binary, positions):
    print("Original binary number:", binary)

    result = binary
    for i in range(positions):
        result = result[1:] + '0'
        print("After left shift", i + 1, ":", result)

    print("Final 8-bit result:", result)
    print("Decimal value:", int(result, 2))
    print()


def logical_right_shift(binary, positions):
    print("Original binary number:", binary)

    result = binary
    for i in range(positions):
        result = '0' + result[:-1]
        print("After right shift", i + 1, ":", result)

    print("Final 8-bit result:", result)
    print("Decimal value:", int(result, 2))
    print()


print("Logical Left Shift")
logical_left_shift("10110110", 2)

print("Logical Right Shift")
logical_right_shift("11010100", 2)
