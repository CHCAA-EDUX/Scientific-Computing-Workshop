
# Pandas and Matplotlib

## Pandas
Pandas is a library for data analysis. It is built on top of NumPy and provides an easy-to-use data structure called a DataFrame. DataFrames allow you to store and manipulate tabular data in rows of observations and columns of variables. We will come back to looking more at NumPy later.

This section will guide you through the basics of Pandas. However it is a very large library and we will only be able to cover the basics. If you want to learn more about Pandas you can check out the [Pandas documentation](https://pandas.pydata.org/docs/).

### Installing external libraries

To install external libraries we use the `pip` command. To install pandas we use the following command:
```bash
pip install pandas
```

### Importing Pandas
To import pandas we use the following command:
```python
import pandas as pd
```

### Creating a DataFrame
To create a DataFrame we can use a dictionary. The keys of the dictionary will be the column names and the values will be the values in the columns. We can then pass this dictionary to the `pd.DataFrame` function.

```python
import pandas as pd

data = {
    "name": ["kenneth", "anders", "scott"],
    "age": [28, 32, 5]
}

df = pd.DataFrame(data)
```

## Accessing data in a DataFrame

### Accessing a column
To access a column we can use the following syntax:
```python
df["name"]
```

### Accessing a row
To access a row we can use the following syntax:
```python
df.iloc[0] # get the first row
```

### Accessing a cell
To access a cell we can use the following syntax:
```python
df["name"].iloc[-1] # get the last name
df.iloc[1]["age"] # get the second age
```

## Operations on a DataFrame

### Adding a column
To add a column we can use the following syntax:
```python
df["height"] = [180, 190, 110]
```

### Adding a row
To add a row we can use the following syntax:
```python
df.loc[3] = ["jacob", 2, 100]
```

### Removing a column
To remove a column we can use the following syntax:
```python
df.drop("height", axis=1)
```

### Changing a value or a column
To change a value we can use the following syntax:
```python
df["age"].iloc[0] = 29
```
Or change a column:
```python
df["age"] = df["age"] + 1
```

### Filtering a DataFrame
To filter a DataFrame we can use the following syntax:
```python
new_df = df[df["age"] > 10] # get all rows where age is greater than 10
```

### Computing statistics
To compute statistics we can use the following syntax:
```python
df["age"].mean() # get the mean age
df["age"].max() # get the maximum age
df["age"].min() # get the minimum age
```

### Slicing the dataframe
You can select specific columns using:
```python
df2 = df[["height", "age"]]
df2
```

### Grouping data
To group data we can use the following syntax:
```python
df2.groupby("age").mean() # group by age and get the mean of each group
```

In our case that is a bit boring, but if we had a column with a lot of different values it would be more interesting.

### Exercise 1: Grouping data
Add a column called `is_american` to the DataFrame. Then group by `is_american` and get the mean age of each group. You decide what the values in the `is_american` column should be.

### Reading a CSV file
To read a CSV file we can use the following syntax:
```python
df = pd.read_csv("data.csv")
```

### Exercise 2: Reading in data
- Read in the file `height-weight.csv` and print the mean height and weight.
You can find the file in the following path:

```
modules/05_pandas_and_matplotlib/data/height-weight.csv
```

- After you have read in the file calculate the mean height and weight according to `lives_in_city`
- Add the column `bmi` to the DataFrame. The BMI is calculated as:

$$
BMI = \frac{weight}{height^2}
$$

Where height is in meters and weight is in kilograms. Then calculate the mean BMI according to `lives_in_city`.

## Plotting with Matplotlib

Matplotlib is a plotting library for Python. It is very powerful and can be used to create a wide variety of plots. We will only be looking at the basics here. If you want to learn more about Matplotlib you can check out the [Matplotlib documentation](https://matplotlib.org/stable/contents.html).

We will start of by installing Matplotlib:
```bash
pip install matplotlib
```

### Creating a simple plot
To create a simple plot we can use the following syntax:
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]

plt.plot(x, y)
plt.show()
```

### Adding labels
To add labels we can use the following syntax:
```python
plt.xlabel("x")
plt.ylabel("y")
```

### Adding a title
To add a title we can use the following syntax:
```python
plt.title("My plot")
```

### Adding a group/legend
It is possible to add multiple groups to the same plot. To do this we can use the following syntax:

```python
score_a = [1, 2, 3, 4, 5]
score_b = [5, 4, 3, 2, 2]
x = [1, 2, 3, 4, 5]

plt.plot(x, score_a, label="Score A")
plt.plot(x, score_b, label="Score B")
plt.legend()
plt.show()

```

### Plotting a scatter plot
Matplotlib has a variety of different plot types. One of them is a scatter plot. To plot a scatter plot we can use the following syntax:
```python
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 3, 2]

plt.scatter(x, y)
plt.show()
```


### Exercise 3: Plotting
- Read in the file `height-weight.csv` and plot the height and weight of each person.  
- Add labels and a title to the plot.
- Add a legend to the plot according to `lives_in_city`.
- Save the plot as a png file. You will have to search how to do this.


# Exercise 4: Importing functions:
Now our script is starting to get a bit large. Let is clean it up a bit.

- Create a file called `utils.py` in the folder you are working in
- Create a function called `read_data` that takes a filename as input and returns a DataFrame
- Create a function called `plot_data` that takes a DataFrame as input, plots the data and saves it as a png file
- Import the functions into your script and use them. You can do this using:

```python
from utils import read_data, plot_data

df = read_data("data.csv")
plot_data(df)
```

# Exercise 5: Creating a script
Now we have created a lot of code, but I would like to save this code for 
my next project. The utils file is a good start, but I would like to be able to run the script from the command line.

```
python create_plot --input_file data.csv --output_file plot.png --title "My plot" --x_label "x" --y_label "y"
```

