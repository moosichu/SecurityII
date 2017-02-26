""" Euclids algorithm """

def gcd(a0, b0):
    """ Greatest common divisor algorithm """
    a = a0
    b = b0
    while True:
        q = a // b
        if a == (b * q):
            print("gcd({}, {}) = {}".format(a0, b0, b))
            return b
        (a, b) = (b, a - (b * q))


def main():
    """ The main method """
    gcd(2250, 360)

if __name__ == "__main__":
    main()
