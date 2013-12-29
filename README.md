Bloom
============

A simple bloom filter written in Python. 

Uses the Jenkins and Murmur hashes.


###Bloom Filter

A bloom filter is a probabalistic data structure that tests for element membership in a set. The element is either *probably in the set*, or is *definitely not in the set*. You can refer to the Wikipedia article [here](http://en.wikipedia.org/wiki/Bloom_filter) and a good tutorial for the basics of bloom filters can be found [here](http://billmill.org/bloomfilter-tutorial/). 

Thanks to [this article](http://ilyasterin.com/blog/2010/02/implementing-bloom-filter-with-a-murmur-hash-function.html) for the single algorithm hashing strategy I use for this project.

###Notes
    
The probability of a false positive is:
    
```(1 - e^(-kn/m))^k```

* where k is the number of hashing functions
* n is the number of expected elements inserted into the filter
* and m is the number of bits allocated in the bit array

The Bloom class takes as its arguments n and fp (the probability for a false positive). 

It calculates m thusly:

``` m = 1 / (1 - (1 - p ^(1 / k))^(1 / (k * n))) ```

