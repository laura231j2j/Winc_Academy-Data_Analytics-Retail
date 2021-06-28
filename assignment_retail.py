# -*- coding: utf-8 -*-
"""assignment-retail.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wUROo8bA6l1-R7qowbGAh_PUyN-376dC

<img src="https://static.wincacademy.nl/logos/main-logo.png" height=200px style="height: 200px"/>

# Assignment: Retail

Congratulations! You've reached the final assignment for the course before the bonus modules. Here we'll ask you to work with a dataset from the Dutch *Centraal Bureau voor de Statistiek* (CBS, English: Statistics Netherlands). It contains monthly growth percentages for various branches of the retail sector. You'll be required to answer open questions as well as write code that handles the data and crunches numbers.

*Answer open questions as though you were writing a report. Answers that are too vague, too short or too sloppy will be rejected.*
"""

from google.colab import drive
drive.mount('/content/drive')

"""## 0. Load required modules

First, we need to load some modules that we're going to use. Do that in the next code cell. If you don't know yet which modules you'll use, just read on and come back here to import them later. **Don't forget to run the cell whenever you make an edit!**
"""

import csv
from datetime import datetime as dt
from itertools import combinations
from tabulate import tabulate

"""## 1. Data Preparation
Now we need to load and parse the data. The data should be located in the same folder as this notebook (whether that's on Google Colab or your local machine). Make sure you have working file path from your notebook to the supplied `data.csv` file. Put an `x` in the checkbox below when you're ready.

- [x] *I have a working file path to the `data.csv` file.*

You are now ready to proceed with reading the data into your program.

### 1.1 Read the CSV

The data comes in the form of a `csv`-file. CSV stands for 'comma separated values'. Oddly enough it need not be the case that the values are *really* separated by commas. In this case, the **delimiter** - the character that separates the columns within a datapoint - is *not* a comma. It's up to you to inspect `data.csv` and find out what the delimiter is.

Once you know what the delimiter is, you can use Python's `csv` module to read each of the datapoints to a dictionary. Some tips:

- The module's name is `csv`.
- You can find its documentation [here](https://docs.python.org/3/library/csv.html)
- We suggest you use the `DictReader` class. There's an example on how to use `DictReader` in the linked documentation.
- Instead of printing the rows (like in the example), we suggest you store all the rows as `dict`s in a `list`.

**1. In the code cell below, write code that opens and reads the data. By the end of the cell, you should have a variable `data` that is a list of dictionaries that each contain a datapoint.**
"""

with open('retail-data.csv', newline="") as csvfile:
  reader = csv.DictReader(csvfile, delimiter=';')
  list_retail_data = []
  for row in reader:
    list_retail_data.append(dict(row))
  print(list_retail_data)

"""### 1.2 Parse and clean the data

You now have a list of dictionaries that each contain some data. But what data? Answer the following questions to become familiar with this dataset. It requires you to write and execute Python code (you can add code cells if you wish), and also search the web for terms you're not familiar with.

**2. What are the column names in this dataset, and what do they mean? Be specific.**

- Bedrijfstakken/branches (SBI 2008): This column indicates which industry a company is part of accoring to the 'Standaard Bedrijfsindeling 2008'.
- Perioden: The year and month
- Omzet ongecorrigeerd/Indexcijfers/Waarde (2015=100): The revenue from the turnover in every month from January 2005 till March 2021 compared to revenue of the turnover of 2015. 
- Omzet ongecorrigeerd/Indexcijfers/Volume (2015=100): The volume is the amount of goods and services sold in a given period calculated by dividing the value of sales by the price. This is compared to the volume of 2015.

**3. For each column, list what data type it should have (`str`, `int`, `float` or `datetime.date`).**

- Bedrijfstakken/branches (SBI 2008): 'str'
- Perioden: 'datetime.date'
- Omzet ongecorrigeerd/Indexcijfers/Waarde (2015=100): 'float'
- Omzet ongecorrigeerd/Indexcijfers/Volume (2015=100): 'float'

**4. In the code cell below, write code that changes the column names to something more convenient for writing readable code. Be sure to choose English, correct and meaningful names.**
"""

print(dict.keys(list_retail_data[0]))

print(list_retail_data[0])

# Renaming the columns

for item in list_retail_data:
  item['industry'] = item.pop('Bedrijfstakken/branches (SBI 2008)')
  item['month'] = item.pop('Perioden')
  item['turnover_index_value'] = item.pop('Omzet ongecorrigeerd/Indexcijfers/Waarde (2015=100)')
  item['turnover_index_volume'] = item.pop('Omzet ongecorrigeerd/Indexcijfers/Volume (2015=100)')

# Checking column names

print(list_retail_data)

"""**5. In the code cell below, write code that casts all the data to the right type.**

Tips:
- If you overwite your data, running the casting operation you're about to implement more than once might result in errors. In that case you can opt not to reuse a variable or restart and rerun your notebook for every retry.
- The data is in Dutch. For some columns this does not matter, but for one in particular it makes parsing it a little bit harder. There is a way to handle this in a few lines of code. You'll need Python's `locale` module for this, as well as the special string `'nl_NL.UTF-8'`. If you're not sure how to use this information after searching the web for a while, it's OK to take the long way around and write custom code to handle the Dutch words. *Note: Google Colab does not support the Dutch locale at this time. If you use Google Colab, you unfortunately can't use the `locale` trick and must write extra code yourself to handle the Dutch dates.*
- The parsing script is bound to run into errors. **Do not modify the data file on disk.** Carefully read the error, examine why it works on most values and crashes on some others, and apply a fix in your code! We'll give you some tips:
    - A handful of values in the `Perioden`-column might cause an error due to an unexpected character. You can safely ignore that character.
    - Handle missing numerical values by replacing them with `-1.`. Be sure to maintain the correct datatype for that column!
"""

# Removing * from data

new_data = list_retail_data

for item in new_data:
  no_asterix = item['month'].replace("*", "")
  item['month'] = no_asterix

# no double spaces

for item in new_data:
  no_double_spaces = item['month'].replace("  ", " ")
  item['month'] = no_double_spaces

# Removing leading and trailing whitespaces

for item in new_data:
  no_spaces_ends = item['industry'].strip()
  item['industry'] = no_spaces_ends

for item in new_data:
  no_spaces_ends = item['month'].strip()
  item['month'] = no_spaces_ends

for item in new_data:
  no_spaces_ends = item['turnover_index_value'].strip()
  item['turnover_index_value'] = no_spaces_ends

for item in new_data:
  no_spaces_ends = item['turnover_index_volume'].strip()
  item['turnover_index_volume'] = no_spaces_ends

# Replacing the missing values with -1

for item in new_data:
 if item['turnover_index_value'] == '.':
  item['turnover_index_value'] = -1

for item in new_data:
 if item['turnover_index_volume'] == '.':
  item['turnover_index_volume'] = -1

# translating months

mapping = { 
      "januari": "January",
      "februari": "February",
      "maart": "March",
      "april": "April",
      "mei": "May",
      "juni": "June",
      "juli": "July",
      "augustus": "August",
      "september": "September",
      "oktober": "October",
      "november": "November",
      "december": "December",
    }


def translating_months():
    for item in new_data:
      for key, value in mapping.items():
        english_months = item['month'].replace(key, value)
        item['month'] = english_months


translating_months()

# Checking translation

print(new_data)

# changing the data type

for item in new_data:
  item['month'] = dt.strptime((item['month']), '%Y %B')

for item in new_data:
  item['turnover_index_value'] = float(item['turnover_index_value'])

for item in new_data:
  item['turnover_index_volume'] = float(item['turnover_index_volume'])

# Checking the data types 

print(type(new_data[0]['industry']))
print(type(new_data[0]['month']))
print(type(new_data[0]['turnover_index_value']))
print(type(new_data[0]['turnover_index_volume']))

"""## 2. Data Exploration

You are now ready to explore the data.

**6. In the code cell below, print the following metadata. Format the printed text in a nice and tidy way. Put an `x` in the checkboxes when you've succeeded.**

- [X] **The number of datapoints in the dataset.**
- [X] **The number of unique branches of the retail sector the data covers.**
- [X] **The first month covered by the data.**
- [X] **The last month covered by the data.**
"""

# The number of datapoint in the dataset

print(f'This dataset contains {len(new_data)} datapoints.')

# The number of unique branches of the retail sector the data covers.

list_branches = []
for item in new_data:
  list_branches.append(item['industry'])
  set_branches = set(list_branches)
  len(set_branches)

print(f'There are {len(set_branches)} unique branches in the dataset.')

# The first and last month covered by the data.

all_months = []
for item in new_data:
  all_months.append(item['month'])

first_month = min(all_months).strftime('%B %Y')
last_month = max(all_months).strftime('%B %Y')

print(f'The first month covered by the data is {first_month}.')
print(f'The last month covered by the data is {last_month}.')

"""**7. In the code cell below, extract the revenue numbers for the following two sectors and put them in a list named exactly as indicated. Also create a list that contains all the months in ascending order. Run the cell after it to see a plot of the numbers if you did it correctly.**

- [X] Months in ascending order $\Longrightarrow$ `months`
- [X] Clothing stores $\Longrightarrow$  `clothing_stores_revenue`
    - Tip: the Dutch word for *'clothing'* is *'kleding'*
- [X] Mail order companies and web shops $\Longrightarrow$ `mail_order_revenue`
    - Tip: the Dutch term for *'mail order companies'* is *'postorderbedrijven'*
"""

# Months in ascending order

set_months = set(all_months)
months = sorted(set_months)
print(months)

# Revenue clothing stores
clothing_stores_revenue = []
for item in new_data:
  if 'kleding' in item['industry']:
    clothing_stores_revenue.append(item['turnover_index_value'])

print(clothing_stores_revenue)

# Mail order companies and web shops
mail_order_revenue = []
for item in new_data:
  if 'Postorderbedrijven' in item['industry']:
    mail_order_revenue.append(item['turnover_index_value'])

print(mail_order_revenue)

# Commented out IPython magic to ensure Python compatibility.
# Do not modify the code in this cell.
import matplotlib.pyplot as plt
# %matplotlib inline

try:
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.plot(months, clothing_stores_revenue, label="Clothing stores' revenue")
    ax.plot(months, mail_order_revenue, label="Mail order companies' revenue")
    ax.set_xlabel('Date')
    ax.set_ylabel('Percent, 2015=100')
    ax.legend()
    plt.show()
except Exception as e:
    print('There was an error creating the plot.\n'
          'Check if your lists are correctly named and assembled.\n'
          "Here's your error, for your debugging pleasure.")
    raise e

"""**8. How do the two branches compare? Discuss any yearly cycles you observe, as well as long-term developments. Also explain why you think these patterns are there. Pretend you are writing this to your supervisor or a client who asked you to analyze this dataset.**

- In the revenue of clothing stores a clear yearly cycle is visible. The revenue is low in January, and a smaller dip can be seen in the summer. The low revenue of Januray could be caused by the fact that people spended a lot of money with the holidays in december and/or have decided to buy less clothes due to new year resolutions. The small dip in summer could be caused by the summer holidays, in which people might tend to buy less clothes.
- In the revenue of mail order companies is growing (exponentially). This can be due to the fact that more and more people order items online. The past years there is a spike in November. This could be due to the Black Friday Sales and people that order gifts for the holidays. 
- During the Covid-19 pandemic the revenue of clothing stores decreased, probably because there were less social gatherings, and therefore less need for new clothes. The revenue of mail order companies increased during the pandemic, this is at least partially caused by the closing of regular stores and fear to go outside.

## 3. Computing With Data

### 3.1 Year Over Year Change

Let's take a closer look at these two branches of retail: clothing stores and mail order companies. A commonly used metric in business is the year-over-year revenue change. It is computed like so:

$$\text{YoY}_\text{month} = \frac{\text{Revenue}_\text{month}}{\text{Revenue}_\text{same month last year}} \times 100$$

Search the web for a longer explanation of this term if you'd like one.

**9. Why should we compare revenue for a particular month to the revenue of that same month, one year ago?**

*It is clear that yearly cycles have a lot of influence on the revenue of a company. When there is for example one month in which the revenue is always high, it makes no sense to compare it to the previous month or the month after. You can, however, compare it to the year before, and see whether the revenue has increased or decreased. *

**10. In the code cell below, compute the year-over-year revenue change for every month, for both branches of the retail sector, each in their own new list. Skip the first year (why?). Put an `x` in the checkboxes when you're ready. Run the next cell to see a new plot for your data.**

- [X] Clothing stores $\Longrightarrow$ `clothing_stores_yoy`
- [X] Mail order companies $\Longrightarrow$ `mail_order_yoy`
"""

# Year-over-year revenue change for every month in mail order branche

mail_order_yoy = []
a = 12
b = 0
for item in mail_order_revenue[12:]:
  this_year_revenue = mail_order_revenue[a]
  last_year_revenue = mail_order_revenue[b]
  yoy = this_year_revenue/last_year_revenue*100
  mail_order_yoy.append(yoy)
  a = a + 1
  b = b + 1

print(mail_order_yoy)

# Year-over-year revenue change for every month in clothing stores branche

clothing_stores_yoy = []
a = 12
b = 0
for item in clothing_stores_revenue[12:]:
  this_year_revenue = clothing_stores_revenue[a]
  last_year_revenue = clothing_stores_revenue[b]
  yoy = this_year_revenue/last_year_revenue*100
  clothing_stores_yoy.append(yoy)
  a = a + 1
  b = b + 1

print(clothing_stores_yoy)

try:
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.plot(months[12:], clothing_stores_yoy, label="Clothing stores' YoY")
    ax.plot(months[12:], mail_order_yoy, label="Mail order companies' YoY")
    ax.set_xlabel('Date')
    ax.set_ylabel('YoY change, 2015=100')
    ax.legend()
    plt.show()
except Exception as e:
    print('There was an error creating the plot.\n'
          'Check if your lists are correctly named and assembled.\n'
          "Here's your error, for your debugging pleasure.")
    raise e

"""**11. In the code cell below, find the best and worst months for both branches of the retail sector in terms of year-over-year revenue change. Print the branch, month and YoY in a nice and tidy way.**"""

# Best and worst month for clothing stores.

index_minimum_clothing = clothing_stores_yoy.index(min(clothing_stores_yoy))
min_month_clothing = months[(index_minimum_clothing+12)].strftime('%B %Y')
print(f'{min_month_clothing} was the worst month for the clothing stores with a year-over-year revenue change of {min(clothing_stores_yoy)}.')

index_maximum_clothing = clothing_stores_yoy.index(max(clothing_stores_yoy))
max_month_clothing = months[(index_maximum_clothing+12)].strftime('%B %Y')
print(f'{max_month_clothing} was the best month for the clothing stores with a year-over-year revenue change of {max(clothing_stores_yoy)}.')

# Best and worst month for mail order companies.

index_minimum_mail = mail_order_yoy.index(min(mail_order_yoy))
min_month_mail = months[(index_minimum_mail+12)].strftime('%B %Y')
print(f'{min_month_mail} was the worst month for the mail order companies with a year-over-year revenue change of {min(mail_order_yoy)}.')

index_maximum_mail = mail_order_yoy.index(max(mail_order_yoy))
max_month_mail = months[(index_maximum_mail+12)].strftime('%B %Y')
print(f'{max_month_mail} was the best month for the mail order companies with a year-over-year revenue change of {max(mail_order_yoy)}.')

"""### 3.2 Similarity Between Branches

We've seen that the pattern for revenue is quite different for clothing stores and mail order companies. In other words: their revenues don't move up or down together. A way to make this observation more specific is to compute the **correlation coefficient**. It is a number between $-1$ and $1$ that describes the relation between two *random variables*. Here is how it works applied to our revenue numbers:

- If the correlation coefficient for the revenue of two branches of the retail sector is $1$, their revenue is *positively correlated*. This means that when the revenue of branch A goes up, the revenue of branch B also goes up. In other words: the revenues for both branches go up together.
- If the correlation coefficient is $-1$, the revenues of the two branches are *negatively correlated*. This means that if A's revenue goes up, B's revenue goes down. Similarly, if B's revenue goes up, A's revenue goes down. They move in the exact opposite direction.
- If the correlation coefficient is $0$, there is no clear pattern between the revenues of both branches.

Here's a table that summarizes this information:

| Correlation coefficient | Meaning                              |
|-------------------------|--------------------------------------|
| $1$                     | Revenues go up together              |
| $0$                     | No pattern                           |
| $-1$                    | Revenues move in opposite directions |

Note that there is a continuous scale between $-1$ and $1$! A correlation coefficient of $0.3$ indicates a somewhat positively correlated relationship.

And here's an image that visualizes the correlation coefficient.

<img src="https://upload.wikimedia.org/wikipedia/commons/d/d4/Correlation_examples2.svg"/>

We've provided a function `corrcoef` that computes the correlation coefficient for two lists.

**11. In the code cell below, use the function `corrcoef` to compute the correlation coefficient for each pair of branches in our dataset. Then print a sorted table that shows each unique pair and their correlation coefficients. Sort by the correlation coefficient, in descending order. You can take inspiration from this table (but it doesn't have to look exactly like it):**

```
Coeff   Branch A                                          Branch B                                          
===========================================================================================================
0.98    4711, 472 Winkels in voedingsmiddelen             4711 Supermarkten                                 
0.91    475 Winkels in overige huishoudwaren              4752 Winkels in doe-het-zelfartikelen             
0.91    47528 Bouwmarkten                                 4752 Winkels in doe-het-zelfartikelen               
```
"""

import numpy as np


# Provided function. Use this to obtain the correlation coefficient for two lists.
def corrcoef(branch_a, branch_b):
    return np.corrcoef(branch_a, branch_b)[0, 1]


# Creating a list with all possible branch combinations

list_of_branches = list(set(list_branches))
combinations_two_branches = list(combinations(list_of_branches, 2))
list_of_list_branches = []
for item in combinations_two_branches:
  list_of_list_branches.append(list(item))

print(list_of_list_branches)

# Calculating the correlation coefficient of each pair of branches and creating a new list of lists containing: branch a, branch b, correlation coefficient.

list_table = []
for pair in list_of_list_branches:
  branch_a = pair[0]
  branch_b = pair[1]
  revenue_branch_a = []
  revenue_branch_b = []
  for item in new_data:
    if branch_a == item['industry']:
      revenue_branch_a.append(item['turnover_index_value'])
    if branch_b == item['industry']:
      revenue_branch_b.append(item['turnover_index_value'])
  list_table.append([branch_a, branch_b, corrcoef(revenue_branch_a, revenue_branch_b)])

print(list_table)

# Printing the table.

print(tabulate(list_table, headers=['Branch A', 'Branch B', 'Coeff']))

"""**12. Pick two correlation coefficients from the table you created and explain why you think these values are the way that they are. Be sure to pick two coefficients that are not close to each other.**

There is quite a high correlation between the '4759 Winkels overige huishoudartikelen' and 'Winkels in meubels, woninginrichting alg' (with a correlation coefficient of 0.840273). This could be caused by the fact that both branches sell similiar items for your home. If money is thight this is a branch that will have less revenue, as most items sold are non-essential. Therefore, the trends of both branches will be similar. 

There is no clear correlation between '476 Winkels in recreatieartikelen' and '47741 Drogisterijen' (correlation coefficient = 0.00958343). Whereas you can buy a lot of essential items in drugstores ('drogisterijen'), this is not the case for recreational shops ('winkels in recreatieartikelen'). The sale of recreational items will probably be high during holidays, whereas items of drugstores will be more stable during the year. Therefore, there is no clear correlation between those two branches. 

**13. Imagine you are a very risk-averse investor shaping your portfolio of investments in the retail sector. How would you use the information in the table you created to minimize your investment risk? Which two branches of the retail sector would you invest in if you had to pick two? Use the correlation coefficient in your answer.**

I would pick '4791 Postorderbedrijven, webwinkels' and '4765 Speelgoedwinkels' as this pair has the most negative correlation coefficient: -0.560225. This would mean that when the revenue of the first branch goes down, the revenue of the second branch is more likely to go up. And vice versa. The chance of them both going down is limited.

## 4. Conclusion

You made it! This was the Retail assignment. Before you hand it in: restart the kernel and run all the cells. Then save it to GitHub and share the link with us in the usual way.
"""