Bloom
============

A simple bloom filter written in Python. 

Uses the Jenkins and Murmur hashes.


#####Couple things of note:

A good tutorial for the basics of bloom filters can be found [here](http://billmill.org/bloomfilter-tutorial/).
    
The probability of a false positive is:
    
```(1 - e^(kn/m))^k```

* where k is the number of hashing functions
* n is the number of expected elements inserted into the filter
* and m is the number of bits allocated in the bit array

Or more simply:

Take the number of 1s in the bit array, divide by the total number of bits in the array, and take that to the power of k, the number of hash functions.