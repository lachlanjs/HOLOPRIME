"""
This file contains functions to generate a dask array of prime factorizations
"""

import numpy as np
# import sparse
import scipy as scp
import scipy.sparse as sparse

import dask.array as da
import sympy

def prime_count_ub(N: int):
    """ Provides an upper bound to the number of primes up to N
        Source: https://en.wikipedia.org/wiki/Prime-counting_function#Inequalities

    Args:
        N (int): the number that we want to know how many primes are beneath. 
        i.e. there are 8 primes beneath 20, so 8 < prime_count_ub(20)
    """

    N = float(N)

    return int(np.ceil((N / np.log(N)) * (1 + (1 / np.log(N))) + (2 / np.pow(np.log(N), 2)) + (7.59 / np.pow(np.log(N), 3))))

def generate_prime_factorizations(
    N: int
):
    
    # create big sparse array
    cols = prime_count_ub(N)

    
    
    # pf_arr = sparse.COO(np.array([]), np.array([], dtype=np.bool), shape=(N, cols))
    # pf_arr = da.from_array(pf_arr, chunks=(128, cols)).map_blocks(sparse.COO)
    pf_arr = sparse.csr_array((N, cols), dtype=np.bool)
    pf_arr = da.from_array(pf_arr, chunks=(128, cols)).map_blocks(sparse.csr_array)

    # get primes
    primes_N = list(sympy.primerange(N))
    prime_to_idx = dict(zip(primes_N, range(len(primes_N))))

    for n in range(N):

        # get the prime factors of n
        pf_n = sympy.primefactors(n)

        for factor in pf_n:
            pf_arr[n, prime_to_idx[factor]] = True # or 1?

    return pf_arr