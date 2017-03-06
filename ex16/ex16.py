def modexp(g, e, m):
    eb = e
    exponentList = []
    while(eb != 0):
        exponentList.append(eb % 2)
        eb = eb // 2
    exponentList.reverse()
    result = 1
    for miniExp in exponentList:
        if miniExp == 0:
            result = (result * result) % m
        else:
            result = (result * result * g) % m

    print("modexp({}, {}, {}) = {}".format(g, e, m, result))
    return result

def modinv(a0, n0):
    """ Modular inverse algorithm """
    (a, b) = (a0, n0)
    (aa, ba) = (1, 0)
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
                return ba
        (a, b) = (b, a - (b * q))
        (aa, ba) = (ba, aa - (q * ba))

def main():
    """ The main method """
    p = 0x8df2a494492276aa3d25759bb06869cbeac0d83afb8d0cf7cbb8324f0d7882e5d0762fc5b7210eafc2e9adac32ab7aac49693dfbf83724c2ec0736ee31c80291
    q = 0xc773218c737ec8ee993b4f2ded30f48edace915f
    g = 0x626d027839ea0a13413163a55b4cb500299d5522956cefcb3bff10f399ce2c2e71cb9de5fa24babf58e5b79521925c9cc42e9f6f464b088cc572af53e6d78802
    modexp(g, q, p)

    y = 0xeb772a91db3b69af90c5da844d7733f24270bdd11aac373b26f58ff528ef267894b1e746e3f20b8b89ce9e5d641abbff3e3fa7dedd3264b1b313d7cd569656c
    
    m1 = "Monday"
    h_m1 = 0x932eeb1076c85e522f02e15441fa371e3fd000ac
    r1 = 0x8f4378d1b2877d8aa7c0687200640d4bba72f2e5
    s1 = 0x696de4ffb102249aef907f348fb10ca704a4b186

    m2 = "Tuesday"
    h_m2 = 0x42e43b612a5dfae57ddf5929f0fb945ae83cbf61
    r2 = 0x8f4378d1b2877d8aa7c0687200640d4bba72f2e5
    s2 = 0x25f87cbb380eb4d7244963e65b76677bc968297e

    # TODO: verify signatures

if __name__ == "__main__":
    main()