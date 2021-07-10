import numpy as np
from fractions import Fraction


def rowReductionInverse(m):

    mSize = len(m)                                                      # Get size of matrix
    I = np.array([ [Fraction(0,1)] * mSize for i in range(mSize)])      # Create identity matrix, I, with the size of the mSize
    for i in range(mSize):
        I[i][i] = Fraction(1,1)
        
    for col in range(mSize):                                            # Going through column by column

        if m[col][col] == 0:                                            # If the diagonal value is 0. Find a row (within the column) with value and turn it to 1
            rowWithValue = None
            for irow in range(mSize):
                if m[irow][col] != 0:
                    rowWithValue = irow
                    break
            
            var = m[rowWithValue][col]
            m[col] = m[col] + (m[rowWithValue] / var)
            I[col] = I[col] + (I[rowWithValue] / var)
        
        else:                                                           # Else divide the row by itself to get 1 for the diagonal cell 
            var = m[col][col]
            m[col] = m[col] / var
            I[col] = I[col] / var
        
        for row in range(mSize):                                        # Go through the rest of the rows and zero them
            
            if row == col:                                              # Ignore diagonals since its already processed
                continue
                
            if m[row][col] == 0:
                continue

            var = m[row][col]
            m[row] = m[row] - (m[col] * var)
            I[row] = I[row] - (I[col] * var)

    return I