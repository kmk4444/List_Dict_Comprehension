######################### COMPREHENSION ###############################
# we can write code in a line instead of a few lines by the help of comprehensions.

#### List Comprehension

##################################### TASK 1 #####################################

salaries = [1000, 2000, 3000, 4000, 5000]

# long version
def new_salary(x):
    return x * 20 / 100 + x

null_list = []
for salary in salaries:
    if salary > 3000:
        null_list.append(new_salary(salary))
    else:
        null_list.append(new_salary(new_salary(salary * 2)))

# by doing with list comprehension
# providing that if and else use at the same time, for loop will be the right side.
[new_salary(salary) if salary > 3000 else new_salary(salary * 2) for salary in salaries]


##################################### TASK 2 #####################################

students = ["John", "Mark", "Venessa", "Mariam"]
students_no = ["John", "Venessa"]

# we would like to write students_no upper case, the others are lower case.
[student.lower() if student not in students_no else student.upper() for student in students]

#### Dict Comprehension

dictionary = {"a":1,
              "b":2,
              "c":3,
              "d":4}

dictionary.keys()
dictionary.values()
dictionary.items()

#we want to square each value

{k:v**2 for (k,v) in dictionary.items()}

{k.upper(): v for (k,v) in dictionary.items()}

{k.upper(): v*2 for (k,v) in dictionary.items()}

################### Application - Interview Question #######################

# Goal: The square of even numbers is wanted to be added to a dictionary.

numbers = range(10)
# old way
new_dict = {}
for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2
#comprehension way
{n: n**2 for n in numbers if n % 2 ==0}

################### List & Dictionary Comprehension Application - 1 #######################

# Change variables' name in a dataset (upper case)
import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

# old way
for col in df.columns:
    print(col.upper())

A = []
for col in df.columns:
    A.append(col.upper())

df.columns = A

# comprehension way
df = sns.load_dataset("car_crashes")
df.columns = [col.upper() for col in df.columns]

################### List & Dictionary Comprehension Application - 2 #######################

# if there is "INS" in the name of the variables, we will add "FLAG" to the beginning of the variables;on the contrary, we will add "NO_FLAG".

df.columns = [col.upper() for col in df.columns]

df.columns = ["FLAG " + col if "INS" in col else "NO_FLAG " + col for col in df.columns]

################### List & Dictionary Comprehension Application - 3 #######################

# Target: we would like to create a dictionary like below.
# NOTE: we will analyze this process just numerical variables!

#Output:
# {"total": ["mean", "min", "max", "var"],
#........

#long way
import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

#we find numerical columns.
num_cols = [col for col in df.columns if df[col].dtype != "O"]
soz = {}
agg_list = ["mean", "min", "max", "var"]
for col in num_cols:
    soz[col] = agg_list

# comprehension way
new_dict = {col: agg_list for col in num_cols}

df[num_cols].agg(new_dict)

################################## PYTHON EXERCISES - 1  ##################

# TASK 1: make upper case numeric variables and add "NUM" beginning of the variables.

import seaborn as sns
df =sns.load_dataset("car_crashes")
df.columns

["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]

# TASK 2: make upper case and add "FLAG" to end of the variable if "NO" is not in variables.

import seaborn as sns
df =sns.load_dataset("car_crashes")
df.columns
[col.upper() +"_FLAG" if "no" not in col else col.upper() for col in df.columns]

# TASK 3: Using the List Comprehension structure,
# select the names of the variables that are DIFFERENT from the variable names given below
# and create a new data frame.
import seaborn as sns
df =sns.load_dataset("car_crashes")
df.columns

og_list = ["abbrev", "no_previous"]

new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
new_df.head()