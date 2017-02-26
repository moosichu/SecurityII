""" Euclids algorithm """

def gcd(a0, b0):
    """ Greatest common divisor algorithm """
    (a, b) = (a0, b0)
    (aa, ab) = (1, 0)
    (ba, bb) = (0, 1)
    while True:
        q = a // b
        if a == (b * q):
            print("gcd({}, {}) = {} = {} * {} + {} * {}".format(a0, b0, b, a0, ba, b0, bb))
            return b
        (a, b) = (b, a - (b * q))
        (aa, ab, ba, bb) = (ba, bb, aa - (q * ba), ab - (q * bb))

def main():
    """ The main method """
    gcd(2250, 360)
    gcd(733810016255931844845,1187329547587210582322)

if __name__ == "__main__":
    main()
