""" Euclids algorithm """

def modinv(a0, n0):
    """ Moduluar inverse algorithm """
    (a, b) = (a0, n0)
    (aa, ab) = (1, 0)
    (ba, bb) = (0, 1)
    while True:
        q = a // b
        if a == (b * q):
            if b != 1:
                print("modinv({}, {}) = fail".format(a0, n0))
                return -1
            else:
                if(ba < 0):
                    ba += n0
                print("modinv({}, {}) = {}".format(a0, n0, ba))

                return bb
        (a, b) = (b, a - (b * q))
        (aa, ab, ba, bb) = (ba, bb, aa - (q * ba), ab - (q * bb))

def main():
    """ The main method """
    modinv(806515533049393, 1304969544928657)
    modinv(4505490,7290036)

if __name__ == "__main__":
    main()
