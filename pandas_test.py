# To install dependencies into the same directory as this file...
# Run these from command prompt in this directory
# 
# py -m pip install pandas -t .
# py -m pip install matplotlib -t .
#
# Examples from: http://pandas.pydata.org/pandas-docs/stable/pandas.pdf
#

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series([1,3,5,np.nan,6,8])
print("==================")
print("        Series")
print("==================")
print(s)

dates = pd.date_range('20130101', periods=6)
print("==================")
print("        date_range")
print("==================")
print(dates)

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print("==================")
print("   DataFrame (df)")
print("==================")
print(df)

df2 = pd.DataFrame({ "A": 1.,
                     "B": pd.Timestamp("20130302"),
                     "C": pd.Series(1, index=list(range(4)), dtype="float32"),
                     "D": np.array([3] * 4, dtype="int32"),
                     "E": pd.Categorical(["test", "train", "test", "train"]),
                     "F": "foo"})

print("==================")
print("  DataFrame (df2)")
print("==================")
print(df2)

print("==================")
print("  df2.dtypes")
print("==================")
print(df2.dtypes)

print("==================")
print("  df2.head")
print("==================")
print(df2.head)

print("==================")
print("  df2.tail(2)")
print("==================")
print(df2.tail(2))

print("==================")
print("  df2.index")
print("==================")
print(df2.index)

print("==================")
print("  df2.columns")
print("==================")
print(df2.columns)

print("==================")
print("  df2.values")
print("==================")
print(df2.values)

print("==================")
print("  df2.describe")
print("==================")
print(df2.describe())

print("==================")
print("  df2.T (transposing)")
print("==================")
print(df2.T)

print("==================")
print("  df2.sort_index(axis=1, ascending=False)")
print("==================")
print(df2.sort_index(axis=1, ascending=False))

print("==================")
print("  df2.sort_index(axis=1, ascending=True)")
print("==================")
print(df2.sort_index(axis=1, ascending=True))

print("==================")
print("  df2.sort_values(by=\"E\"")
print("==================")
print(df2.sort_values(by="E"))



