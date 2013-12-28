# euler's number = math.exp(1)

import mmh3
import math
from jenkins import hashlittle
from bitarray import bitarray
import sys

class Error(Exception):
    """Base class for exceptions."""
    pass

class FPError(Error):
    """Exception raised for error in inputting the false positive.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message

class Bloom:
    """ A simple implementation of a bloom filter. 

    Attributes:
        n -- the expected number of elements to be added
        to the filter. The value for n will be used for m,
        the number of bits allocated for the bitarray

        fp -- the false positive value the user is willing
        to tolerate.

    """

    def __init__(self, n=0, fp=0):
        try:
            if fp > 0 and fp < 1:
                self.fp = fp
            else:
                raise FPError('False Positive tolerance should be given as a decimal value.')
        except FPError as err:
            print "FPError: %s" % err.message
            sys.exit()
        self.n = n
        self.bvector = bitarray(n)
        self.bvector.setall(False)

    def add(self, string):
        jenkins = abs(hashlittle(string) % self.n)
        murmur = abs(mmh3.hash(string) % self.n)
        self.bvector[jenkins] = True
        self.bvector[murmur] = True

    def query(self, string):
        jenkins = abs(hashlittle(string) % self.n)
        murmur = abs(mmh3.hash(string) % self.n)
        if self.bvector[jenkins] == True and self.bvector[murmur] == True:
            print "'%s' is possibily in the set" % string
        else:
            print "'%s' is definitely not in the set" % string

if __name__ == "__main__":
    b_f = Bloom(1000, .1)

