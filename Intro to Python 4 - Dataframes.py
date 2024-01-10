# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Dataframes
# The following are software libraries that we will be using to manipulate and analyze tabular data. When importing, you can use the `as` keyword to name a shorthand for accessing the library and it components.

# %%
import pandas as pd 
import numpy as np

# %% [markdown]
# While we'll be learning how to use these libraries as we progress, note that each library has its own resources and documentation that will help you understand how to use it. You can view pandas documentation through `pd?`or [here](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)

# %%
# #pd?

# %% [markdown]
# ### Convert list to dataframe
# You can transfer data from any list into a dataframe. Dataframes also automatically display/assign column and row indices. 

# %%
data = [["Str1", "Str2", "Str3"],["Str4", "Str5", "Str6"],["Str7", "Str8", "Str9"],["Str10", "Str11", "Str12"]]
df = pd.DataFrame(data)
df

# %% [markdown]
# Set column names by specifying arguements for the `columns` parameter. The arguement passed should be a list. Alternatively you can define a dictionary with the following syntax:
#
#     {'Column1 Name': [data1, data2, ...],
#      'Column2 Name': [data1, data2, ...]}

# %%
data = [["Product1","77.2"],["Product2","44.03"],["Product3","97.8"]]
df = pd.DataFrame(data, columns=["Name", "Price"])
df

# alternative
# df = pd.DataFrame({'Name': ["Product1", "Product2", "Product3"],
#                    'Price': ["77.2", "44.03", "97.8"]})

# %% [markdown]
# ### Convert CSV to dataframe
#
# Typically, larger datasets will come in the format of CSV files. We can convert these files into dataframes and have them analyzed within Python. Use the `sample_data.csv` file and convert it into a dataframe. (**Note**: make sure the file is in the same directory/folder as this notebook)

# %%
sample_df = pd.read_csv('input/sample_data.csv')
sample_df

# %% [markdown]
# Our dataset appears to have a built in column for row indexing. This creates redundant data. Similar to how we did **list/string splicing**, we can remove the first column read from the CSV file.

# %%
sample_df = pd.read_csv('input/sample_data.csv').iloc[: , 1:]

# head() displays only the first 5 rows of data
sample_df.head()

# %% [markdown]
# # Data Cleaning
# We'll learn the different functions we can use on dataframes as we do data cleaning. Understand that the justifications behind each data cleaning step will vary depending on both the dataset itself and your intentions for how the dataset will be used moving forward. Knowing how the data was collected helps when deciding an approach for altering the data for cleaning.
#
# Let's get a larger dataset to work on. The [San Francisco Building Permits dataset](https://www.kaggle.com/datasets/aparnashastry/building-permit-applications-data) is a public record of structural permits from Jan 1, 2013-Feb 25th 2018. For simplicity, some of the columns of the dataset have been removed.

# %%
bld_df = pd.read_csv('input/Building_Permits.csv').iloc[:,:-20]
bld_df.head()

# %% [markdown]
# Some rows you may consider non-essential to the analysis and can be removed. You've already seen `iloc` being used to drop columns from the dataset, but if you know the names of the columns you want to remove you can also used `drop()`. Specify the column names in a list and pass them as an arguement for the function's `columns` parameter. 

# %%
bld_df.drop(columns=['Permit Number', 'Block'], inplace=True)
bld_df.head()

# %% [markdown]
# ### Loc and iLoc
#
# These are the primary functions for indexing and selecting items in a Dataframe. They stand for "locate" or "location" and "integer-locate", respectively. `loc` locates items based on labels (column/row names) while `iloc` locates based on the respective integer value (0,1,2,3..). The syntax for both is as follows:
#
#     loc[row_label, column_label]
#     iloc[row_position, column_position]
#
# The inside paramters may each be a list of values, meaning you can specify multiple row/column labels/positions in a single command. The following code demonstrates loc and iloc selection in varying situations. In data cleaning, this can be used to reduce the dataframe to only the necessary rows or columns.

# %%
# #copy of previous dataframe
df = bld_df.head()

# similar to list splicing, ':' selects all rows/columns 

# select columns "Permit Type" and "Permit Type Definition"
df.loc[:,["Permit Type", "Permit Type Definition"]]

# %%
# select rows index 2-4
df.iloc[[2,3,4],:]

# %% [markdown]
# Items can also be selected by one or more conditions in `loc`.

# %%
# select items with Permit Type 4
df.loc[df["Permit Type"] ==  4]

# %%
# select items with Permit Type 4 AND (&) Street Name Ellis
df.loc[(df["Permit Type"] ==  4) & (df["Street Name"] == "Ellis")]

# %%
# select items with Permit Type 4 OR (|) Permit Type demolitions
df.loc[(df["Permit Type"] ==  4) | (df["Permit Type Definition"] == "demolitions")]

# %% [markdown]
# ## Data Imputation
# One of the first things you'll encounter when analyzing a data set is missing values. Data imputation is done to infer the missing values using the rest of the data. Use `info()` and `isnull()` to get some general information about the dataset, present datatypes and missing values. `Non-Null Count` refers to the number of entries under the column that have a value or not NaN.

# %%
bld_df.info()

# %%
# get the number of missing data points per column

"""
    CODE BREAKDOWN:
    isnull() - outputs True (1) if variable is not NaN, since this is being applied to a df, this outputs a list of lists of boolean values
    sum() - adds all True values per column/list
"""

missing_values_count = bld_df.isnull().sum()

# look at the # of missing points
missing_values_count[:]

# %%
#alternatively, if you just need to know if there are *any* NaN values
"""
    CODE BREAKDOWN:
    isnull() - outputs True (1) if variable is not NaN, since this is being applied to a df, this outputs a list of lists of boolean values
    any() - if at least ONE item in the list is False (i.e if there is at least one NaN), returns True. Otherwise, return False (all items are filled)
"""
bld_df.isnull().any()

# %% [markdown]
# We can see that columns such as `Street Number Suffix` and `Unit Suffix` have a large percentage of missing values. Data imputation has different approaches depending on why the data is missing, if the data needs to be filled and how it will be used. One basic approach is to change NaNs into a default value. Here all NaNs under `Street Number Suffix` are changed to "None".

# %%
# rather than referring to columns by their index, you can also use the column names

"""
    CODE BREAKDOWN:
    
    bld_df["Street Number Suffix"] - column "Street Number Suffix"
    fillna("None", inplace=True) - function that replaces all NaN's with the provided argument "None"
    inplace=True - the function is executed and saved within the dataframe rather than just returning the desired result
                 - alternatively, use default value inplace=False and write as:
                        bld_df["Street Number Suffix"] = bld_df["Street Number Suffix"].fillna("None") 
    
    sample(10, random_state=1) 
                 - samples 10 randomly selected rows from the df
                 - random_state sets a random seed, further calls of sample() using the same random state will result in
                   the same rows being sampled (see next code block)
"""

bld_df["Street Number Suffix"].fillna("None", inplace=True)
bld_df.sample(10, random_state=1)

# %% [markdown]
# If you have NaNs in columns for numerical data, the pandas library automatically ignores NaNs when computing for aggregation functions. The following code gets the average of the `Number of Existing Stories` column an assigns it as the default value to replace the NaNs. 

# %%
# this should show the same number as bld_df.info()
print("Number of Non-NaN: " + str(bld_df["Number of Existing Stories"].count()) + "\n")

avg = bld_df["Number of Existing Stories"].mean()

#round up value
avg = round(avg)
print("Average: " + str(avg))

bld_df["Number of Existing Stories"].fillna(avg, inplace=True)

bld_df.sample(10, random_state=1)

# %% [markdown]
# If you want to drop rows that have NaNs on a specific column, use `dropna`.  

# %%
bld_df = bld_df.dropna(subset = 'Description')

# check for changes in number of missing values in Description column
missing_values_count = bld_df.isnull().sum()
missing_values_count[:]

# %% [markdown]
# ### Convert Dataframe to CSV
# Whatever your resulting dataframe may be, you can convert it back to a CSV file for distribution or processing on other platforms with `to_csv`. Further documentation found [here](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html)

# %%
"""
    'clean.csv' - desired filename (includes extension .csv)
    index - include indices in output file (True) or don't (False)
"""

bld_df.to_csv('clean.csv',  index=False)

df = pd.read_csv('clean.csv')
df.head()

# %% [markdown]
# ### Inconsistent Data Entry
# This case typically applies to text and/or categorical data. There will be entries that represent the same thing but are written differently in the data (e.g. misspellings). This may cause issues later in the data analysis process. Consider this dataframe of continents.

# %%
np.random.seed(0)
words = ["Asia", "asia", "Europe", "Euroe", "N.America", "North America", "NA", "SA", "South America", "Oceania", "Africa", "Africaa"]
continents = []
i = 0

while i < 100:
    continents.append(np.random.choice(words))
    i += 1

con_df = pd.DataFrame(continents, columns=["continent"])    
con_df.head()

# %% [markdown]
# You can check for each unique value in a column with `unique()` to check for inconsistencies. Once you've identified which entries correspond to which category, you can reassign their values using a dictionary and `replace()`.

# %%
con_df["continent"].unique()

# %%
con_df["continent"].replace(
    {"asia": "Asia", 
     "NA": "North America", 
     "Euroe": "Europe",
     "SA": "South America",
     "N.America": "North America",
     "Africaa": "Africa"}, inplace=True)

con_df["continent"].unique()

# %% [markdown]
# ## merge()
#     merge(left, right, ...)
#
# Often databases will have information that refers to one item separated into multiple tables. To ease processing of the data, you may need to merge the tables into one. The pandas library provides the `merge()` function for connecting tables regardless of relationship (one-to-one, one-to-many, many-to-many). `merge()` takes at least 2 arguements, `left` and `right` are the dataframes to be combined. The order of the dataframes will be relevant if you intend on doing inner/outer joins. Further documentation [here](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html)
#
# Consider the following database schema where `prod_id` is the primary key representing one product:
#
# ![db_schema.png](attachment:e9e740e4-b2d6-446b-9be2-ac85990d311f.png)

# %%
#generate sample data
names_df = pd.DataFrame({'prod_id': [34, 35, 36, 37, 38],
                         'name': ['Product 1', 'Product 2', 'Product 3', 'Product 4', 'Product 5']})

prices_df = pd.DataFrame({'prod_id': [35, 36, 34, 37, 38],
                          'price': [194.2, 2088, 612.05, 430, 72.4]})

manu_df = pd.DataFrame({'product_id': [36, 34, 37, 35, 38],
                        'manufacturer': ['Manufacturer A', 'Manufacturer B', 'Manufacturer C', 'Manufacturer A', 'Manufacturer C']})

sales_df = pd.DataFrame({'prod_id': [35, 34, 36, 37, 35, 34, 35, 12],
                         'customer_id': [73, 74, 73, 75, 72, 70, 75, 100]})

display('names_df', names_df, 
        'prices_df', prices_df, 
        'manu_df', manu_df, 
        'sales_df', sales_df)

# %%
# one-to-one merging
df = pd.merge(names_df, prices_df, on='prod_id')
df

# %% [markdown]
# `on` - merge key, this arguement specifies which column will be used as the basis of merging. The column must also be present on both tables
#
# By default, on will look for a matching pair of column names and use that column as the basis of merging. Omitting `on` in our example will not cause any changes. <br>
# In the case of multiple identical columns, specifying `on` may be necessary.
#
# Next, lets merge with `manu_df`

# %%
# one-to-many merging
df = pd.merge(df, manu_df, left_on='prod_id', right_on = 'product_id')
df

# %% [markdown]
# Notice how product ID is labeled differently in `manu_df`
# If you want to merge on columns that don't have identical labels we instead have to use `left_on` and `right_on`.
# These represent the column names of the 1st and 2nd dataframes passed, respectively. This does, however, create an excess/redundant column, which we can remove.

# %%
df.drop('product_id', axis=1, inplace=True)
df

# %%
# many-to-many merging
pd.merge(df, sales_df)

# %% [markdown]
# The resulting table is a record of individual sales of products. Notice how 2 products are missing from the final table. <br>
# __prod_id 12__ does not have a corresponding ID in the other tables besides `sales_df`, while __prod_id 38__ has no entry in `sales_df` despite being present in other tables. If we want to merge into a table that includes these entries we'll have to make use of joins. Let's return to a previous version of our relevant tables.

# %%
display('df', df, 
        'sales_df', sales_df)

# %% [markdown]
# By changing the function's `how` paramter, we can select what type of join to use when merging tables. Left and right tables are decided depending which is passed as the first and second tables respectively. For now, we'll refer to our current `df` as left and `sales_df` as right.
#
# A __left join__ merges while keeping all records from the left table, entries without a corresponding key/ID on the right table will have their columns filled out with NaN.

# %%
df_left, df_right = df, sales_df
pd.merge(df_left, df_right, on='prod_id', how='left')

# %% [markdown]
# A __right join__ merges while keeping all records from the right table, entries without a corresponding key/ID on the left table will have their columns filled out with NaN.

# %%
pd.merge(df_left, df_right, on='prod_id', how='right')

# %% [markdown]
# An __outer join__ does both, keeping all records from all columns.

# %%
pd.merge(df_left, df_right, on='prod_id', how='outer')

# %% [markdown]
# An __inner join__ keeps the intersection of both tables (i.e. only rows with matching keys on both tables). This is the default behavior of `merge`. 

# %%
df = pd.merge(df_left, df_right, on='prod_id', how='inner')
df

# %% [markdown]
# ## Data Aggregation
# The numpy library provides an array of aggregation and statistical analysis functions for processing columns on your dataset. We can use this to gain some insight on `price` column of the previous table.

# %%
import numpy as np

data = df['price']
data

sum = np.sum(data)
print("sum :",sum)

mean = np.mean(data)
print("mean :",mean)

median = np.median(data)
print("median :",median)

standard_deviation = np.std(data)
print("standard_deviation :",standard_deviation)

variance = np.var(data)
print("variance :",variance)

# returns lowest value in a given list
minimum = np.min(data)
print("minimum value :",minimum)

# returns highest value in a given list
maximum = np.max(data)
print("maximum value :",maximum)

# %% [markdown]
# ### groupby()
#     DataFrame.groupby(column_name)
#     
# The `groupby` function allows us to split the data into categories and apply the previous aggregations to those groups individually. 

# %%
# number of sales per manufacturer
df.groupby('manufacturer').count()['name']

# %%
# sum of sales per manufacturer
df.groupby('manufacturer').sum()['price']

# %% [markdown]
# > __NOTE__: a column is specified at the end to reduce the output to just the relevant column for aggregation. If a column is not specified, the function will be applied to all possible columns

# %%
df.groupby('manufacturer').sum()

# %% [markdown]
# You can also group by multiple columns. (passed as a list)

# %%
# sum of sales per product per manufacturer
df.groupby(['manufacturer', 'name']).sum()['price']

# %%
df.groupby(['manufacturer', 'name']).mean()['price']

# %% [markdown]
# Note that the `groupby()` function returns its own groupby object, which contains the information of each group. Groups may be accessed individually should they require separate processing.

# %%
groups = df.groupby('manufacturer')

# 'name` and 'grp' here refer to the group name an the actual dataframe of each group, respectively. 
for name, grp in groups:
    print(name)
    print(grp)
    print()

# %% [markdown]
# # Assignment
# Using `sample_data.csv` from earlier, do the following:
# 1. Convert into a dataframe
# 2. remove the first column
# 3. merge with `names_df`
# 4. drop all rows without a Township or Product Type
# 5. export the resulting dataframe into a csv file, this will be used it Module 5
# 5. Per township, get the number of properties per product type
# 6. Per township, get the mean PPSQM per product type

# %%
buyer_names = list(map(lambda n:"Buyer " + str(n), np.arange(25)))
names_df = pd.DataFrame({'Buyer ID': np.arange(25),
                         'Buyer Name': buyer_names})

sample_df = pd.read_csv('input/sample_data.csv')

# %%
df2 = sample_df.iloc[:, 1:]
df2.head()

# %%
df2 = pd.merge(df2, names_df)
df2.head()

# %%
df2 = df2.dropna(subset = ['Township','Product Type'])
df2.head()

# %%
df2.to_csv('new.csv',  index=False)

# %%
df2.groupby(['Township', 'Product Type']).count()['Property']

# %%
df2.groupby(['Township', 'Product Type']).mean(numeric_only=True)['PPSQM']

# %%
