#!/usr/bin/env python
# coding: utf-8

# In[4]:


from __future__ import print_function
import numpy as np


# In[2]:


import numpy as np
def determinant():
    while True:
        try:
            rows = int(input("Enter the number of rows: "))
            cols = int(input("Enter the number of columns: "))
            if rows != cols:
                print("Opps your rows is not the same as the columns")
                continue
        except:
            print("Check your input and try again")
            continue
        break
    while True:
        try:
            arr = []
            arr = input("Enter the values of matrix %s x %s: "%(rows,cols))
            arr = np.array(arr)
            if len(arr) != int(rows):
                print("The row of the matrix is not %s"%(rows))
                continue
            else:
                for row in arr:
                    if len(row) != int(rows):
                        print("The column %s of the matrix is not %s"%(row,cols))
                        continue
        except:
            print("The array is not valid, try again")
            continue
        break
    return "The determinant of the matrix equals %f"%np.linalg.det(arr)


# In[3]:


determinant()


# In[ ]:




