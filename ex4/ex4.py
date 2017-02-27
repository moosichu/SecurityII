""" Exercise 4 """
import hashlib


def genpasswd(password):
    """ Accepts a password and generate new one """
    sha1 = hashlib.sha1(password.encode('utf-8'))
    hashstring = sha1.hexdigest()
    return hashstring[:6]


def findcollision(x0):
    """ Finds two input passwords which give the same output from genpasswd """
    (x1, x2) = (genpasswd(x0), genpasswd(genpasswd(x0)))
    i = 1
    while x1 != x2:
        i = i + 1
        x1 = genpasswd(x1)
        x2 = genpasswd(genpasswd(x2))
    x2 = x1
    x1 = x0
    for j in range(i):
        if genpasswd(x1) == genpasswd(x2):
            print("genpasswd({}) = genpasswd({}) = {}".format(x1, x2, genpasswd(x1)))
            return (x1, x2)
        x1 = genpasswd(x1)
        x2 = genpasswd(x2)
    print("fail")



def main():
    """ The main method """
    passwords = "q1dff2"
    (x1, x2) = findcollision(passwords)

if __name__ == "__main__":
    main()
