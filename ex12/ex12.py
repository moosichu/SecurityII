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



def main():
    """ The main method """
    modexp(123456789, 987654321, pow(2, 80) - 1)
    print("mod 10^8 = {}".format(modexp(7, pow(2, 521) - 1, pow(2, 3217) - 1) % pow(10, 8)))
if __name__ == "__main__":
    main()