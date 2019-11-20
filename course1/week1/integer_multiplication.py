

def multiply(left, right):
    """Implementation of Karatsuba integers multiplication algorithm
       Explanation: https://www.youtube.com/watch?v=-dfsxsiGoC8"""
    left_length = len(str(left))
    right_length = len(str(right))

    # perform basic multiplication for single digit numbers
    if left_length == 1 or right_length == 1:
        return left * right

    length = max(left_length, right_length)
    # // - divide by dropping decimal part
    half_length = length // 2

    # ** - raise number to the power
    # split each numbers into halves using divide and remainder operators
    # left = 10^(half_length)*a + b
    a = left // 10 ** half_length
    b = left % 10 ** half_length
    # right = 10^(half_length)*c + d
    c = right // 10 ** half_length
    d = right % 10 ** half_length

    ac = multiply(a, c)
    bd = multiply(b, d)
    ad_plus_bc = multiply(a + b, c + d) - ac - bd

    # (10^length)*ac + (10^(length/2))*(ad + bc) + bd
    # use 2 * half_length takes care of both even and odd numbers
    prod = 10**(2 * half_length) * ac + (ad_plus_bc * 10 ** half_length) + bd

    return prod


def main():
    left = 3141592653589793238462643383279502884197169399375105820974944592
    right = 2718281828459045235360287471352662497757247093699959574966967627
    result = multiply(left, right)
    print(result)


if __name__ == '__main__':
    main()

