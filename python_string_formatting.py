# https://www.hackerrank.com/challenges/python-string-formatting/problem
def print_formatted(number):
    number_bin = bin(number)
    width = len(number_bin) - 2

    for x in range(1, number+1):  
        x_oct = oct(x)[2:]
        x_hex = hex(x)[2:].upper()
        x_bin = bin(x)[2:]
        x_pad = '{:>{}}'.format(x, width)
        x_oct_pad = '{:>{}}'.format(x_oct, width)
        x_hex_pad = '{:>{}}'.format(x_hex, width)
        x_bin_pad = '{:>{}}'.format(x_bin, width)

        print(x_pad, x_oct_pad, x_hex_pad, x_bin_pad)

n = int(input())
print_formatted(n)