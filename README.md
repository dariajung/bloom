Bloom
============

A simple bloom filter written in Python using the Murmur hash.

###Bloom Filter

-----------------

A bloom filter is a probabalistic data structure that tests for element membership in a set. The element is either *probably in the set*, or is *definitely not in the set*. You can refer to the Wikipedia article [here](http://en.wikipedia.org/wiki/Bloom_filter) and a good tutorial for the basics of bloom filters can be found [here](http://billmill.org/bloomfilter-tutorial/). 

Thanks to [this article](http://ilyasterin.com/blog/2010/02/implementing-bloom-filter-with-a-murmur-hash-function.html) for the single algorithm hashing strategy I use for this project.

###How It Works

-------

####Create an instance of the Bloom class

```
b_f = Bloom(expected-number-of-elements, false-positive, number-of-hashes)

```

Based on the number of expected elements, the false positive rate, and the number of hashes given by the user, the bit array size will be calculated. The bloom filter will attempt to have a false positive rate approximately equal to the given false positive rate.

####Add elements to the bloom filter
```
b_f.add('key')
```

####Query for membership

```
b_f.query('key')
```

This will return one of two possible things:

```
'Key' is possibily in the set and there is a false positive probability of calculated-false-positive-rate
```
or

```
'Key' is definitely not in the set
```

###Short Example
---------

```
b_f = Bloom(100, .1, 5)
b_f.add("Matt")
b_f.add("Daria")

b_f.query("Matt")
b_f.query("KitKat") # KitKat is my cat.
```
returns

```
'Matt' is possibily in the set and there is a false positive probability of 0.100925190275
'KitKat' is definitely not in the set
```

###Notes
    
The probability of a false positive is:
    
```(1 - e^(-kn/m))^k```

* where k is the number of hashing functions
* n is the number of expected elements inserted into the filter
* and m is the number of bits allocated in the bit array

The Bloom class takes as its arguments n, fp (the probability for a false positive), and k. 

It calculates m thusly:

``` m = 1 / (1 - (1 - p ^(1 / k))^(1 / (k * n))) ```

###Todos:
* Test with words.txt, which contains over 200000 words.
* Make the bloom filter serializable. 
