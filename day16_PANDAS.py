# # ==============================================
# # ================= PANDAS =====================
# # ==============================================

# # ---- What is Pandas -----
# # Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.
# # https://pandas.pydata.org/about/index.html

# # ==> Pandas Series
# # A Pandas Series is like a column in a table. It is a 1-D array holding data of any type.
# # Means: Every column in a table is a pandas series. It can hold any data type and the array is 1D.
# # Series will have 2 things - Index and its value
# #   eg. 0   India
# #       1   USA
# #       2   NEpal
# # Index is alotted to values by pandas 

# # ===> Importing pandas
import numpy as np
import pandas as pd

# # Series from Python Lists

# # string
# country = ['India', 'USA', 'Nepal', 'SriLanka', "France"]
# res = pd.Series(country)
# print(res)

# # integers
runs = [13,65,7,65,3,54,99,4,3,44,56,0,67]
# res = pd.Series(runs)
# print(res)

# # custom index -- by user
# marks = [67,88,32,66]
# subjects = ['maths', 'science', 'sst', 'english']
# res = pd.Series(marks, index=subjects, name='Ashirwad ke marks')
# print(res)

# # series from dictionary
# marks = {
#     'maths': 67,
#     'english': 77,
#     'science': 33,
#     'hindi': 72
# }
# marks_series = pd.Series(marks, name="Ashirwad ke marks")
# print(marks_series)

# # ===> Series Attributes
# # 1. size
# print("size: ",marks_series.size)

# # 2. is_unique
# print("Is there unique in series: ", marks_series.is_unique)

# # 3. index
# print("Index of marks_series: ", marks_series.index)

# # 4. values
# print("Values of marks_series: ", marks_series.values)

# # 5. name
# print("Series ka naam hai: ", marks_series.name)

# # 6. dtype
# print("series ka datatype hai: ", marks_series.dtype)


# # ===================================================
# # =============== Series using read_csv =============
# # ===================================================

# # csv files --- csv files are like excell sheets, csv stands for coma separated values

# # ------------ with one col ------------------- 
# # this is not a series till now, to make it a series --> have to add a parameter called "squeeze=true"
subs = pd.read_csv('Contents/subs.csv').squeeze('columns')
# print(subs)


# # ---------------- with 2 columns --------------------
kohli_runs = pd.read_csv('Contents/kohli_ipl.csv', index_col='match_no').squeeze('columns')
# print(kohli_runs)

movie_leads = pd.read_csv('Contents/bollywood.csv', index_col='movie').squeeze('columns')
# print(movie_leads)

# ===================================================
# =================== Series Methods ================
# ===================================================

# # head and tail 

# # head() ---> by default will show you 5 top data
# # to get 5 +- data just pass that value like head(10)
# print(subs.head())
# print(subs.head(10))

# # tail() --> bu default will show last 5 data
# # to get 5 +- data just pass that value like tail(10)
# print(subs.tail())
# print(subs.tail(10))

# # sample() ---> randomly show 1 row from the data
# print(movie_leads.sample())
# print(movie_leads.sample(5))

# # value_counts() ---> It returns the frequency of data in decreasing order
# print(movie_leads.value_counts()) # no. of movies done by each actor

# # sort_values() -----> by default sort the values in ascending order
# print(kohli_runs.sort_values())
# print(kohli_runs.sort_values(ascending=False)) # sorting in descending order

# # sort_index ---> y default sort the indexes in ascending order
# print(movie_leads.sort_index())
# print(movie_leads.sort_index(ascending=False)) # sorting in descending order


# # ===================================================
# # =============== Maths Series Methods ==============
# # ===================================================

# # count ---> it doesnt count missing values
# print("VK matches played: ", kohli_runs.count())

# # sum and product
# print("Total subscribers in 1 year: ", subs.sum())

# # mean/median/mode/std/var
# print("mean of subscribers: ", subs.mean())
# print("median of vk runs: ", kohli_runs.mean())
# print('maximim no of movies by an actor: ', movie_leads.mode())

# # min/max
# print("maximum subscribers in a day: ", subs.max())
# print("minimum subscribers in a day: ", subs.min())

# # describe  --> it will show the overall mathematical stats
# print("vk runs stats: \n",kohli_runs.describe())


# # ===================================================
# # =============== Series Indexing ===================
# # ===================================================

# x = pd.Series([12,13,14,15,7,567,5,4,6,8,44,65,90])

# # positive indexing
# print(x[0])

# # negative indexing ---> not works in pandas

# # movies
# print(movie_leads['Uri: The Surgical Strike'])
# print(movie_leads.iloc[1]) # if index is string in file --> use iloc to use number as index to fetch data

# # slicing
# print(kohli_runs[5:15])

# # -ve slicing --> will work same as python
# print(kohli_runs[-5:])
# print(movie_leads[-12:])
# print(movie_leads[::5])

# # fancy indexing
# print(kohli_runs[[1,5,6,22,55]])



# # ===================================================
# # ================ Editing Series ===================
# # ===================================================

# # using indexing
# runs[1] = 100
# print(runs)

# # what if an index does not exist --> will through error
# runs[13] = 200
# print(runs)

# # using slicing
# runs[2:5] = [300,300,300]
# print(runs)
