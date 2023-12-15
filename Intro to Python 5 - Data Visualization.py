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
# # Data Visualization

# %%
import numpy as np
import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# %% [markdown]
# ## matplotlib 
# matplotlib is one of the more basic data visualization libraries, typically used to generate static, non-interactive visualizations. Given its lightweight qualities and less extensive features compared to more modern visualization libraries, matplotlib is ideally used for simple and quick data visualizations.
#
# The following is a simple plot given list of x and y values.

# %%
#define data
x = [2010,2011,2012,2013,2014,2015,2016,2017]
y = [2.1,2.2,2.5,2.2,2.9,3.2,3.6,3.7]

#plot data
plt.plot(x, y)

#display
plt.show()

# %% [markdown]
# Here we can add another set of y values to compare to the first by using `plot()` again. You can also access the library's methods to customize your graph's appearance.

# %%
#declare new y values
y_2 = [2.3,2.5,2.9,3.0,3.3,3.0,3.7,4.0]

plt.plot(x, y)
plt.plot(x, y_2)

#set labels
plt.ylabel("Population (Millions) ")
plt.xlabel("Year")
plt.title("Population Growth")

plt.grid(True)

#customize lines
lines = plt.plot(x,y,x,y_2)
plt.setp(lines,marker='*')
plt.show()

#display
plt.show()

# %% [markdown]
# Generate multiple plots at once with `subplots`. The figure object `fig` represents the entire image/collection of plots which organizes all them into rows an columns, while `axes` represents each of the plots which can be accessed and edited independent of each other. Each class has its own methods for changing the properties of the plot. You can check the library's [documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html) for an extensive view of each class' attributes and methods.
#
# The following code generates a bar graph and pie graph, represented by `ax1` and `ax2` respectively.

# %%
fig, axes = plt.subplots(1, 2, figsize=(16,8))
fig.suptitle("Sales per Region", fontsize=24)

ax1, ax2 = axes

#declare values
x = ["Asia", "Europe", "NA", "SA", "Oceania", "Africa"]    
y = [409.8, 667.2, 800.33, 340.74, 290.22, 347.9]
y_2 = [774.8, 810.23, 701.99, 380.74, 310.22, 357.0]

#set labels
ax1.set_ylabel("Sales (Millions)", fontsize=12)
ax1.set_xlabel("Region", fontsize=18)
ax2.set_ylabel("Sales (Millions)", fontsize=12)
ax2.set_xlabel("Region", fontsize=18)
fig.tight_layout(pad=2)

ax1.bar(x, y)
ax2.pie(y, labels=x)
plt.show() 
plt.close()

# %% [markdown]
# Here's a customized version of the previous graphs. Each type of visualization has its own required paramaters and customizable attributes so be sure to check the documentation of the respective graphs to get the most out of customizing. Note that Donut Graphs are not built into matplotlib but can be created by changing the `wedgeprops` attribute in `pie()`. 

# %%
#list of named colors found here: https://xkcd.com/color/rgb/
colors = ['saddlebrown', 'wheat', 'crimson', 'lightgrey','lightblue','darkblue']

fig, axes = plt.subplots(1, 2, figsize=(16,8))
fig.suptitle("Sales per Region", fontsize=24)

ax1, ax2 = axes
x = ["Asia", "Europe", "NA", "SA", "Oceania", "Africa"]    
y = [409.8, 667.2, 800.33, 340.74, 290.22, 347.9]
y_2 = [774.8, 810.23, 701.99, 380.74, 250.22, 357.0]


#bar chart labelling
ax1.set_ylabel("Sales (Millions)", fontsize=12)
ax1.set_xlabel("Region", fontsize=18)

#pie chart labelling
ax2.set_ylabel("Sales (Millions)", fontsize=12)
ax2.set_xlabel("Region", fontsize=18)

fig.tight_layout(pad=2)

ax1.barh(x, y, edgecolor='black')
ax2.pie(y, labels=x, colors=colors, wedgeprops={'width': 0.2})

plt.show() 
plt.close()

# %% [markdown]
# Assuming your data is already placed within a dataframe, you can use pandas' sorting functions to arrange the order of how your data is presented.

# %%
# use lists of column values to create a dataframe
df = pd.DataFrame(list(zip(x, y)), columns = ['Region', 'y'])
df

# %%
"""
    sort_values() arranges the order according to the column name specified in 'by'
    ascending = False arranges in descending order, omit this or set to True for ascending order
"""
df.sort_values(by=['y'], ascending=False, inplace=True)
df

# %%
#list of named colors found here: https://xkcd.com/color/rgb/
colors = ['saddlebrown', 'wheat', 'crimson', 'lightgrey','lightblue','darkblue']

fig, axes = plt.subplots(1, 2, figsize=(16,8))
fig.suptitle("Sales per Region", fontsize=24)

ax1, ax2 = axes

#bar chart labelling
ax1.set_ylabel("Sales (Millions)", fontsize=12)
ax1.set_xlabel("Region", fontsize=18)

#pie chart labelling
ax2.set_ylabel("Sales (Millions)", fontsize=12)
ax2.set_xlabel("Region", fontsize=18)

fig.tight_layout(pad=2)

ax1.barh(df['Region'], df['y'], edgecolor='black')
ax2.pie(df['y'], labels=df['Region'], colors=colors, wedgeprops={'width': 0.2}, startangle=90)

plt.show() 
plt.close()

# %%
# grouped bar chart

# %% [markdown]
# > **_NOTE:_** It is a good practice to close the figure windows when we don't need them it keeps the code clean and saves a lot of memory. Use the `plt.close(fig)` command. Use the `plt.close()` command to close all open figure windows.
#
# The following are a scatter plot and correlation heatmap using attributes of the [Iris dataset](https://www.kaggle.com/datasets/uciml/iris). Showing any potential relationships in the physical traits of the Iris species. 

# %%
iris_df = pd.read_csv('Iris.csv')
iris_df.info()

x = iris_df["SepalLengthCm"]
y = iris_df["SepalWidthCm"]

plt.scatter(x,y)
plt.close()

# %%
corr_matrix = iris_df.drop(columns=["Id","Species"]).corr()

plt.figure(figsize=(4, 3))
plt.imshow(corr_matrix)

# %%
np.random.seed(2)

#generate random data
data_1 = np.random.normal(50, 40, 200)
data_2 = np.random.normal(60, 30, 200)
data_3 = np.random.normal(100, 70, 200)
data_4 = np.random.normal(80, 10, 200)

data = [data_1, data_2, data_3, data_4]
plt.figure(figsize=(4, 5))
plt.boxplot(data)

plt.show()
plt.close()

# %%
data = np.random.normal(100, 100, 500)

plt.figure(figsize=(4, 3))
plt.hist(data, bins=20, color='#43a193')

plt.show()
plt.close()

# %% [markdown]
# ## plotly
# plotly is a more advanced data visualization library capable of generating interactive visuals. Compared to matplotlib, plotly is generally heavier and uses more resources. You'll notice the following plots take a bit longer for the code to generate. While the libraries are used to accomplish similar tasks, consider the following factors when deciding which is most fit for your task: customizability, acceptable input data formats, convenience, code readability and cross-compatibility.
#
# The following series of code demonstrates similar visualizations to what we've already done in matplotlib. Data used is taken from varying columns from the [World University Rankings Dataset](https://www.kaggle.com/datasets/mylesoneill/world-university-rankings). Hover your cursor over the datapoints to see more information about them. [Figure Documentation](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#id0)

# %%
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

# %%
times_df = pd.read_csv("univ_ranks/timesData.csv")
times_df.info()

# %%
df = times_df.iloc[:100,:]

"""
    different graph types are accessed through plotly's graph_objects (abbreviated as 'go')
    instances of this are referred to as a trace
"""
data = go.Scatter(
                x = df.world_rank,
                y = df.citations,
                mode = "lines+markers",
                name = "citations",
                marker = dict(color = '#a6200c'),
                line = dict(color = 'green'),
                text= df.university_name
                )

"""
    When customizing colors, they can be referred to by name (see list at https://xkcd.com/color/rgb/)
    or through HEX or RGB. Regardless of format, they should be expressed as a string
"""

#create Figure instance
fig = go.Figure(data)

#display figure
pio.show(fig)


# %% [markdown]
# You can include multiple traces into one figure to plot more than one set of data on the same graph. Note that setting parameters/customization is done separately per trace.

# %%
# prepare data frame
df = times_df.iloc[:100,:]

# Creating trace1
trace1 = go.Scatter(
                    x = df.world_rank,
                    y = df.citations,
                    mode = "lines",
                    name = "citations",
                    marker = dict(color = 'green'),
                    text= df.university_name)

# Creating trace2
trace2 = go.Scatter(
                    x = df.world_rank,
                    y = df.teaching,
                    mode = "lines+markers",
                    name = "teaching",
                    marker = dict(color = 'black'),
                    text= df.university_name)

data = [trace1, trace2]
layout = dict(title = 'Citation and Teaching vs World Rank of Top 100 Universities',
              xaxis= dict(title= 'World Rank',ticklen= 5,zeroline= False))

fig = dict(data = data, layout = layout)
pio.show(fig)

# %%
# prepare data frames
df2014 = times_df[times_df.year == 2014].iloc[:3,:]

# create trace1 
trace1 = go.Bar(
                x = df2014.university_name,
                y = df2014.citations,
                name = "citations",
                marker = dict(color = 'rgba(255, 174, 255, 0.5)',
                line = dict(color='rgb(0,0,0)',width=1.5)),
                text = df2014.country)
# create trace2 
trace2 = go.Bar(
                x = df2014.university_name,
                y = df2014.teaching,
                name = "teaching",
                marker = dict(color = 'rgba(255, 255, 128, 0.5)',
                line = dict(color='rgb(0,0,0)',width=1.5)),
                text = df2014.country)

#group traces
data = [trace1, trace2]

layout = go.Layout(barmode = "group")
fig = go.Figure(data = data, layout = layout)
pio.show(fig)

# %% [markdown]
# Traces do not have to be of the same type for the figure to function but this may lead to incompatible or messy visualizations.

# %%
# trace3 is a Scatter trace taken from the previous block of code
# mixes bar traces and scatter traces
data = [trace1, trace2, trace3]

layout = go.Layout(barmode = "group")
fig = go.Figure(data = data, layout = layout)
pio.show(fig)

# %%
# prepare data
x2011 = times_df.student_staff_ratio[times_df.year == 2011]
x2012 = times_df.student_staff_ratio[times_df.year == 2012]

# creating trace 1
trace1 = go.Histogram(
    x=x2011,
    opacity=0.75,
    name = "2011",
    marker=dict(color='rgba(171, 50, 96, 0.6)'))

# creating trace 2
trace2 = go.Histogram(
    x=x2012,
    opacity=0.75,
    name = "2012",
    marker=dict(color='rgba(12, 50, 196, 0.6)'))

#group data
data = [trace1, trace2]

#configure layout
layout = go.Layout(barmode='overlay',
                   title=' students-staff ratio in 2011 and 2012',
                   xaxis=dict(title='students-staff ratio'),
                   yaxis=dict( title='Count'),
                  )

#instantiate Figure object
fig = go.Figure(data=data, layout=layout)

#display
pio.show(fig)

# %% [markdown]
# ## General Rules of Data Visualization
#
# 1. Selecting the appropriate chart type
#     - Every chart type is suited for different situations and different types of data
#     - Showcasing **trends** or time series data is ideally done through a Line charts
#     - **Comparisons** between categories an assessing the proportion of data relative to other data points is best represented through bar or pie charts
#     - Scatter plots can be used to find **relationships** between two variables
#     - The **distribution** within a dataset can be visualized through histograms. <br><br>
#     
# 2. Avoid misleading visualizations
#     - The scale of your axes may understate or overexaggerate the implications of the data
#     - Data labels can misrepresent or display biased interpretation. <br><br>
#
# 3. Avoid clutter and highlight key data points
#     - Consider the message or idea your visualization should be conveying, unecessary elements that don't contribute to this should be removed to avoid muddying the data.
#     - Use color to differentiate and highlight data points. Use it to convey additional information that enables viewers to digest the visualization at a glance. 
#     - Structure the data to tell a clear narrative. 

# %%

# %%
