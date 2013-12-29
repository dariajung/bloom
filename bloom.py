
import mmh3
import math
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
        to the filter. Used for number of bits allocated 
        for the bitarray

        fp -- the false positive value the user is willing
        to tolerate.

        k -- the number of desired hash functions

    """

    def __init__(self, n=0, fp=0, k=0):
        try:
            if fp > 0 and fp < 1:
                self.fp = fp
            else:
                raise FPError('False Positive should be given as a decimal value.')
        except FPError as err:
            print "FPError: %s" % err.message
            sys.exit()
        self.k = k
        self.n = n
        self.m = int(math.ceil(1 / (1 - (1 - self.fp ** (1 / float(self.k))) ** (1 / (float(self.k) * float(self.n))))))
        self.eltsAdded = 0
        self.bvector = bitarray(self.m)
        self.bvector.setall(False)

    # Calculates the current false positive probability
    # based on the number of elements added so far
    def get_fp_prob(self):
        return (1 - math.exp(-self.k * self.eltsAdded / self.m))**self.k

    # Calculates k number of hashes using
    # the murmur hash function
    def hash(self, string):
        hash_arr = []
        hash1 = mmh3.hash(string, 0)
        hash2 = mmh3.hash(string, hash1)
        for i in range(self.k):
            hash_arr.append(abs((hash1 + i * hash2) % self.m))

        return hash_arr

    # Adds an element to the bloom filter
    def add(self, string):
        hashes = self.hash(string)
        for elt in hashes:
            self.bvector[elt] = True
        self.eltsAdded += len(hashes)

    # Queries for membership of element in the
    # bloom filter
    def query(self, string):
        hashes = self.hash(string)
        fp = self.get_fp_prob()
        for elt in hashes:
            if self.bvector[elt] != True:
                print "'%s' is definitely not in the set" % string
                return

        print "'%s' is possibily in the set and there is a false positive probability of %s" %(string, fp)

    # Clears the bloom filter and resets all
    # values in the bit vector to 0
    def clear(self):
        self.bvector.setall(False)
        self.eltsAdded = 0

if __name__ == "__main__":
    b_f = Bloom(100, .1, 5)
    b_f.add("Matt")
    b_f.add("Daria")
    b_f.query("Matt")
