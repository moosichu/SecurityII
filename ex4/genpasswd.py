""" Exercise 4 """
import hashlib


def genpasswd(password):
    """ Accepts a password and generate new one """

    sha1 = hashlib.sha1(password.encode('utf-8'))
    hashstring = sha1.hexdigest()
    return hashstring[:6]


def findcollision():
    """ Finds two input passwords which give the same output from genpasswd """
    pass


def main():
    """ The main method """
    passwords = "q1dff2"
    hash_val = genpasswd(passwords)
    print(hash_val)

if __name__ == "__main__":
    main()
