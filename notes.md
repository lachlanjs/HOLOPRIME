# plan

Create a modular application using HoloViz which incorporates a user-driven feedback loop.

- Based on exploring the [prime number dataset](https://johnhw.github.io/umap_primes/index.md.html)

Integers can be converted to vectors in a variety of ways. Could have a 1 in the respective column when that factor is present - as in the original. Could also increase the factor when it is repeated.

Different distance metrics are possible (cosine chief among them, but what about manhattan?). Could directly provide the integers to the distance function, then it works out the prime factors between them? Could use Dask and partition the pairwise comparisions into blocks, generating a big distance matrix, and use that. Heaps of options to explore

Different rendering options also possible. Definite case for datashader too. Definite case for a minimap. Definite case for float panels for clustering or for alternative colouring schemes.

Choosing a large enough $N$ means that the compute job is going to be significant - so can explore parallelism.

# data structures

- Use sparse binary dask array for the factorizations data. Chunk with whole rows.

- Use sympy's factorization function

- Have a mapping from primes to their index (generate primes using sympy)

- 

# application:

## activities

- PrimeParametersActivity

- EmbeddingViewerActivity

  - EmbeddingClusterViewer

- RawViewerActivity

## parameters

- PrimeParameters

- UMAPParameters

- PrimeData

  - Embedding

  - Raw Vectors

  - Length

  - Clusters (PrimeClusters)

- 

## computation
