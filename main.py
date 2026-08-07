#import datetime
# import pandas as pd
# import numpy as np
# print(pd.__version__)
# print(np.__version__)
# #list
# #series1 = pd.Series((1, 2, 3, 4, 5))  #pandas  series
# series1 = pd.Series([1, 2, 3, 4, 5], index=['A','B','C','D','E']) # pandas series
# print(type(series1)) #check the data type of series
# #series1[0] = 100 #mutate/change values of numpy series
# print(series1.loc['B':'E'])# STRING
# #print(series1['A'])
# print(series1.index)
# #Numpy array
# #arr = np.arange(10, 20)
# #series2 = pd.Series(arr)

# #print(series2)
# #print(series2[5:])
# def say(message, times = 1):

#     print(message * times, end='  ')

# say("Hello")

# say("World", 5)
# #What will be the output of the following code?
# x = (1, 2, 3)

# y = x

# y += (4, 5)

 

# print(x)

# print(y)
# print(type(10))


# d1 = datetime.date(2024,1,2)
# d2 = datetime.date(2024,1,12)
# print(d2-d1)

def sum(*args):

        '''Function returns the sum of all values'''

        r = 0

        for i in args:

            r += i

        return r

print(sum(1, 2, 3), end='  ')

print(sum(1, 2, 3, 4, 5))

a =  [1, 2, 3, 4, 5]

print(a[3:0:-1])