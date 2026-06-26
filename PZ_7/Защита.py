def cubedigits(n):
    result = ""
    sign = "-" if n < 0 else ""

    n = abs(n)

    if n == 0:
        return 0
    cube = 1
    for digit in str(n):
        cube *= 3
        result += str(cube)

    return int(sign + result)

print(cubedigits(123))
print(cubedigits(23))
print(cubedigits(12))