import math

def mash_distance(k,j):
    mash_distance_k = (-1.0/k)*math.log(2.0*j/(1.0+j))
    return mash_distance_k

def mash_containment(k,cde):
    mash_containment_k = cde**(1.0/k)
    return mash_containment_k