# PPHA 30535
# Spring 2022
# Homework 6

# Joshua Charles

# Joshua Charles
# JoshuaCPython

# Due date: Sunday May 15th before midnight
# Write your answers in the space between the questions, and commit/push only
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put
# thought into your work.

##################

#NOTE: All of the plots the questions ask for should be saved and committed to
# your repo under the name "q1_plot.png", "q2_plot.png", etc. If a question calls
# for more than one plot, name them "q1a_plot", "q1b_plot", etc.

#NOTE: If no specific library is called for by the question, then you may freely
# use Matplotlib, Pandas, Seaborn, or a combination to answer the question.

# Question 1: With the x and y values below, create a plot using only Matplotlib.
# You should plot y1 as a scatter plot and y2 as a line, using different colors
# and a legend.  You can name the data simply "y1" and "y2".  Make sure the
# axis labels are legible.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x = pd.date_range(start='1990/1/1', end='1991/12/1', freq='MS')
y1 = np.random.normal(10, 2, len(x))
y2 = [np.sin(v)+10 for v in range(len(x))]

# Plotting all three plots in a single plot

plt.plot(x, x, color = 'r', label  = 'x', linestyle = '-')
plt.plot(len(x), y1, color = 'g', label = 'Scatter Plot', linestyle = '-.')
plt.plot(range(len(x)), y2, color = 'b', label = 'Line', linestyle = '--')

plt.legend()

plt.show()

# Question 2: Using only Matplotlib, reproduce the figure in this repo named
# question_2_figure.png.

import matplotlib.pyplot as plt

#create data

x = [0,2,4,6,8,10]
y = [0,2,4,6,8,10]

# plot lines

plt.plot(x, y, label = 'Blue')
plt.plot(y, x, label = 'Red')

plt.legend()

plt.show()

# Question 3: Load the mpg.csv file that is in this repo, and create a
# plot that tests the following hypothesis: a car with an engine that has
# a higher displacement (i.e. is bigger) will get worse gas mileage than
# one that has a smaller displacement.  Test the same hypothesis for mpg
# against horsepower and weight.

firstpath = r'C:\Users\joshu\Downloads\homework-4-and-5-JoshuaCPython-main.zip\homework-4-and-5-JoshuaCPython-main\mpg.csv'

path = os.path.join(firstpath,'mpg.csv')  

normplot(mpg)

sample_means =mean(mpg)

[h, pvalue,ci] = ztest(mpg/)

# Question 4: Continuing from question 3, create a scatter plot with mpg
# on the y-axis and cylinders on the x-axis.  Explain what is wrong with this
# plot with a one-line comment.  Now create a box plot using Seaborn
# that uses cylinders as the groupings on the x-axis, and mpg as the values
# up the y-axis.

# Question 5: Continuing from question 3, create a two-by-two grid of
# subplots, where each one has mpg on the y-axis and one of displacement,
# horsepower, weight, and acceleration on the x-axis.  To clean up this 
# plot, remove the y-axis labels on the right two plots - the scale will 
# already be aligned because the mpg values are the same.

# Question 6: Are cars from the USA, Japan, or Europe the least fuel
# efficient, on average?  Answer this with a plot.

# Question 7: Using Seaborn, create a scatter plot of mpg versus displacement,
# while showing dots as different colors depending on the country of origin.

import seaborn as sns
df = sns.load_dataset('iris')

fig, ax = plt.subplots()
ax = sns.scatterplot(x='sepal_length', y='petal_length',
                data=df, hue='species', ax=ax)
fig.savefig('myplot.png')
