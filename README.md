# Sparse-Matrix-Representations
Various algorithms to represent sparse matrices.

## Distance Histogram Representation
This representation stores the spatial distribution of non-zero elements in a matrix through histograms. It consists of two matrices, with one storing the histograms for the rows of the original matrix, and the other for the columns. The histogram is based on the distance between an element and the principal diagonal of the original matrix. Done deal

This algorithm is adopted from the research paper [Bridging the gap between deep learning and sparse matrix format selection](https://people.engr.ncsu.edu/xshen5/Publications/ppopp18.pdf)