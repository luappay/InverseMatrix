# Inversing Matrix

### Motivation

I recently did a coding challenge that needed me to implement a matrix inversion function. I knew how to inverse matrices on paper, but to actually code it out is another thing. 

### **The Issue**

Tried to search for solutions online but almost all the advices were to use the numpy's native matrix inverse method numpy.linalg.inv() which did not help since I wanted to use the Fractions library for the values in the matrix. As such, I have to implement my own solution.

### **Row Reduction**

The solution I implemented takes advantage of a method I found called **Row Reduction**. 

In essence, these are the steps for any invertible matrix m;

- Create an Identity Matrix, I, of the same size
- Perform row-wise operations using the rows of the matrix m such that m becomes an Identity Matrix of itself
- Perform the same operation on Identity Matrix I
- The resulting Matrix I will be the inverse of m

For people who are more visual, I referenced this [video](https://www.youtube.com/watch?v=7g9yZCR-5Jc&ab_channel=MathswithJay) a lot.

Below is the implementation;

```python
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
```