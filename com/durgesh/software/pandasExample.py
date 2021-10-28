

import pandas as pd

lst = ["durgesh", "agnihotri"]
lst2 = ["shreya", "agnihotri"]
pandSeries = pd.Series(lst)

print(pandSeries)

csvSeries = pd.read_csv("F:/Github/py-basic-scripting-learning/resources/customer-orders.csv")
cSeries = csvSeries.apply(lambda id1: 1 + id1)
print(csvSeries)
print(cSeries)

st = set(lst)
print(st)

unionColl = st.union(set(lst2))
#st.s
print(unionColl)

lstInt = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: (x % 2 == 0), lstInt))
print("Even numbers from {} are :: {}".format(lstInt, even))

st1 = set(lstInt)
evenSEt = set(filter(lambda x: (x % 2 == 0), st1))
print(evenSEt)
