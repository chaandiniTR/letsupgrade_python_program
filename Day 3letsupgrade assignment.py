#!/usr/bin/env python
# coding: utf-8

# # Day 3 Assignment 

# # IF ELSE and ELIF to write a program for Report Cards.

# In[1]:


marks = 80
if marks >=90:
    print("A")
elif marks >=80:
    print("B")
elif marks >=70:
    print("C")
elif marks >=60:
    print("D")
else:
    print("Failed")


# # For Loop to Print Prime Numbers in between 1 to 1000

# In[2]:


for i in range(1,100):
  if i>1:
    for j in range(2,i):
        if(i % j==0):
            break
    else:
        print(i)


# # program for printing the tables from 1,10 using Nested For Loop

# In[3]:


num = 1
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)


# # program to Print X Prime Numbers using While Loop starting from 0,

# In[ ]:


while i in range(1,100):
  if i>1:
    for j in range(2,i):
        if(i % j==0):
            break
    else:
        print(i)


# In[ ]:




