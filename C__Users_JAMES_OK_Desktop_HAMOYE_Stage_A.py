#!/usr/bin/env python
# coding: utf-8

# # LESSON 1
# ## NumPy Array and Vectorization
# 
# NumPy is a library that has ndarray as its basic data structure used to handle arrays and matrices

# In[1]:


# Convention for Importing Numpy 

import numpy as np


# In[4]:


arr = [6, 7, 8, 9]
print(type(arr))


# In[8]:


a = np.array(arr)
print("The value of a is ", a)
print(type(a))
print(a.shape)
print(a.dtype)

# get the dimension of a with ndim
print("The dimension of a is ", a.ndim)


# In[12]:


b = np.array([[1, 2, 3], [4, 5, 6]])
print("The value of b is ", b)
"The dimension of b is ", b.ndim
"The shape of b is ", b.shape


# There are also some inbuilt functions that can be used to initialize numpy which include empty (), zeros (), ones (), full (), random.random()

# In[26]:


# a 2X3 array of ramdom numbers
np.random.random((2,3))


# In[27]:


# a 2X3 array of zeros
np.zeros((2,3))


# In[28]:


# a 2X3 array of ones
np.ones((2,3))


# In[38]:


np.empty((3,3))


# In[154]:


np.eye(3,3)


# In[156]:





# # Intra-operability of arrays and scalars
# 
# Vectorization in numpy arrays allows for faster processing by eliminating for loops when dealing with arrays of equal shape.

# In[40]:


c = np.array([[9.0, 8.0, 7.0], [1.0, 2.0, 3.0]])
d = np.array([[4.0, 5.0, 6.0], [9.0, 8.0, 7.0]])

c + d
c*d
5/c
c**2
c**3


# # Indexing with arrays & using arrays for data processing
# 

# In[46]:


a[0] = 6
a[1] = 10
a[3] = 9
print (a)


# In[44]:


b[0,0] = 1
print(b)


# Elements in arrays can also be retrieved by slicing rows and columns or a combination of indexing and slicing

# In[54]:


e = np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]])
e[:3, :2]


# There are other advanced methods of indexing which are shown below

# In[52]:


# Integer indexing
e[[2, 0, 3, 1], [2, 1, 0, 2]]


# In[59]:


# boolean indexing meeting a specific condition
e[e>15]


# In[60]:


sum(e)


# # LESSON 3
# # Pandas - So much more than a cute animal
# Pandas is a library used for data manipulation and built on Numpy with other ways of indexing other than using integers
# 

# In[66]:


# Convention for importing pandas
import pandas as pd
days = pd.Series(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
print(days)


# In[108]:


# creating series with numpy array

days_list = np.array(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
Pandas_days = pd.Series(days_list)
print(Pandas_days)


# In[119]:


# Using strings as index
days = pd.Series(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'], index = ['a', 'b', 'c', 'd', 'e'])
days


# In[117]:


# Creating series from a dictionary

days1 = pd.Series({'a': 'Monday', 'b': 'Tuesday', 'c': 'Wednesday', 'd': 'Thursday', 'e': 'Friday'})
days1


# Series can be accessed using the specified index as shown below

# In[122]:


days[0]
days[2:]


# A DataFrame can be described as a table (2 dimensions) made up of many series with the same index. It holds data in rows and columns just like a spreadsheet. Series, dictionaries, lists other dataframes and numpy arrays can be used to create new ones. 

# In[128]:


print(pd.DataFrame())


# In[131]:


# Create a dataframe from dictionary
df_dict = {'Country': ['Ghana', 'Kenya', 'Nigeria', 'Togo'], 
           'Capital': ['Acra', 'Nairobi', 'Abuja', 'Lome'], 
           'Population': [10000, 8500, 35000, 12000],
           'Age': [60, 70, 80, 75]
          }
df = pd.DataFrame(df_dict, index = [1, 2, 3, 4])
df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[132]:


import numpy as np
np.random.seed(40)
np.random.random((2,3))


# # LESSON 4
# ## Data Types and Data Wrangling
# The pandas library is vast enough to read data from and save to several file formats such as CSV, JSON, HTML and even databases
# Pandas can connect to databases, get data with queries and save in a dataframe
# 
# 

# In[146]:


url = 'https://raw.githubusercontent.com/WalePhenomenon/climate_change/master/fuel_ferc1.csv'
Fuel_Data = pd.read_csv(url, error_bad_lines = False)
Fuel_Data


# In[147]:


Fuel_Data.describe(include = 'all')


# In[148]:


Fuel_Data.shape


# In[149]:


# Check for missing Data
Fuel_Data.isnull().sum()


# In[150]:


# use groupby to count the sum of each unique value in the fuel Unit column
Fuel_Data.groupby('fuel_unit')['fuel_unit'].count()


# In[151]:


# fill the missing data with mcf which has the highest number of instance
Fuel_Data[['fuel_unit']] = Fuel_Data[['fuel_unit']].fillna(value = 'mcf')


# In[152]:


# Check if the missing Data have being filled
Fuel_Data.isnull().sum()


# In[157]:


Fuel_Data.groupby('report_year')['report_year'].count()


# In[159]:


Fuel_Data.groupby('fuel_type_code_pudl')['fuel_type_code_pudl'].count()


# In[158]:


Fuel_Data.groupby('fuel_type_code_pudl').first()


# In[ ]:




