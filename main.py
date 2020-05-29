import numpy as np
from dist_hist import row_histogram, column_histogram

def main():
    #Distance histogram representation
    sparse = np.array([[45,0,0,0,0,0,0,0],[0,-25,0,0,0,0,0,0],[0,0,89,37,0,0,0,0],[0,0,43,94,0,0,0,0],[77,0,0,0,0,15,0,0],[0,0,0,0,36,78,0,0],[0,0,0,0,0,0,0,23],[0,0,0,17,0,0,11,0]])
    # sparse matrix example
    R = row_histogram(sparse,4,4)
    ans_row = np.array([[2,0,0,0],[4,0,0,0],[3,0,1,0],[2,0,1,0]])
    b_row = (R == ans_row)
    assert b_row.all(),"Not correct row histogram" 
    # check row histogram
    C = column_histogram(sparse,4,4)
    ans_col = np.array([[2,0,1,0],[4,0,1,0],[3,0,0,0],[2,0,0,0]])
    b_col = (C == ans_col)
    assert b_col.all(),"Not correct column histogram"

    print("row_histogram = \n",R)
    print("column_histogram = \n ", C)

if __name__ == "__main__":
    main()