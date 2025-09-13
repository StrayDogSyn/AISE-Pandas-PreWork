# Lesson 2: Core Concepts - DataFrames and Series

> If data were a video game, pandas DataFrames would be your main character - versatile, powerful, and capable of incredible feats when you know the right button combinations.

## Learning Objectives

By the end of this lesson, you'll be able to:

- Understand the relationship between DataFrames and Series
- Create DataFrames using multiple methods
- Perform basic DataFrame operations and inspections
- Navigate the DataFrame structure like a pro

## The DataFrame: Your Data's New Best Friend

Think of a DataFrame like a spreadsheet that went to MIT - it's got all the functionality of Excel, but with the power of Python underneath. It's the main character in your data story.

### Creating Your First DataFrame

Like making your character in an RPG, there are several ways to create a DataFrame:

```python
import pandas as pd
import numpy as np

# Method 1: From a dictionary (most common in real projects)
student_data = {
    'name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'age': [23, 24, 22, 25],
    'major': ['CS', 'Math', 'CS', 'Physics'],
    'gpa': [3.8, 3.6, 3.9, 3.7]
}

df = pd.DataFrame(student_data)
print(df)
```

**Output:**
```
      name  age    major  gpa
0    Alice   23       CS  3.8
1      Bob   24     Math  3.6
2  Charlie   22       CS  3.9
3    Diana   25  Physics  3.7
```

```python
# Method 2: From lists of lists
data_matrix = [
    ['Alice', 23, 'CS', 3.8],
    ['Bob', 24, 'Math', 3.6],
    ['Charlie', 22, 'CS', 3.9],
    ['Diana', 25, 'Physics', 3.7]
]

columns = ['name', 'age', 'major', 'gpa']
df = pd.DataFrame(data_matrix, columns=columns)

# Method 3: From NumPy arrays (for numerical data)
np.random.seed(42)  # For reproducible results
numerical_data = np.random.randn(4, 3)  # 4 rows, 3 columns
df_numeric = pd.DataFrame(numerical_data, 
                         columns=['feature1', 'feature2', 'feature3'])

# Method 4: Empty DataFrame (for incremental building)
empty_df = pd.DataFrame(columns=['name', 'age', 'score'])
```

### DataFrame Anatomy: Understanding the Structure

A DataFrame has several key components:

```python
# Basic properties
print(f"Shape: {df.shape}")              # (rows, columns)
print(f"Columns: {df.columns.tolist()}")  # Column names
print(f"Index: {df.index.tolist()}")      # Row labels
print(f"Data types: {df.dtypes}")         # Type of each column
```

**Before vs After: Understanding Data Structure**

```python
# BEFORE (manual inspection - tedious and error-prone)
data = [['Alice', 23], ['Bob', 24]]
print(f"Rows: {len(data)}")
print(f"Columns: {len(data[0]) if data else 0}")
for i, row in enumerate(data):
    print(f"Row {i}: {row}")

# AFTER (pandas magic - comprehensive and instant)
df = pd.DataFrame(data, columns=['name', 'age'])
print(df.info())  # Complete overview in one command
```

## Series: The Building Blocks

A Series is like a single column from a spreadsheet - but with superpowers. Think of it as a smart list that knows about itself.

```python
# Creating a Series - think of it as a smart list
ages = pd.Series([23, 24, 22, 25], name='age')
print(ages)

# With custom index (like giving each value a name tag)
ages_with_names = pd.Series(
    [23, 24, 22, 25], 
    index=['Alice', 'Bob', 'Charlie', 'Diana'],
    name='age'
)
print(ages_with_names)

# Series from DataFrame column
gpa_series = df['gpa']  # This returns a Series
print(type(gpa_series))  # <class 'pandas.core.series.Series'>
```

**Key Insight:** Every DataFrame is essentially a collection of Series. It's like how The Avengers is a collection of individual superheroes - each Series has its own powers, but together they're unstoppable.

## Basic DataFrame Operations

### Information and Inspection

```python
# The essential exploration toolkit
df.head()          # First 5 rows (the movie trailer)
df.tail()          # Last 5 rows (the credits)
df.shape           # Dimensions (rows, columns)
df.info()          # Data types and memory usage (the technical specs)
df.describe()      # Statistical summary (the highlight reel)
df.columns         # Column names (the cast list)
df.dtypes          # Data types for each column
df.nunique()       # Number of unique values per column
```

### Quick Statistics

```python
# Numerical summaries
print(f"Average GPA: {df['gpa'].mean():.2f}")
print(f"Age range: {df['age'].min()} - {df['age'].max()}")
print(f"Most common major: {df['major'].mode()[0]}")

# Count occurrences
major_counts = df['major'].value_counts()
print("Major distribution:")
print(major_counts)
```

## Indexing: Your GPS for Data Navigation

Understanding how to navigate DataFrames is crucial. Think of it like learning the controls for your favorite video game character.

### Row and Column Access

```python
# Single column selection (returns Series)
names = df['name']                    
ages_df = df[['age']]              # Returns DataFrame (note double brackets)

# Multiple column selection
subset = df[['name', 'age', 'gpa']]

# Row selection by position
first_student = df.iloc[0]          # First row by position
first_three = df.iloc[0:3]          # First 3 rows

# Row selection by label (when you have named indices)
df_named = df.set_index('name')
alice_data = df_named.loc['Alice']
```

### Boolean Indexing (The Filtering Magic)

This is where pandas really shines - like having X-ray vision for your data:

```python
# Simple filtering
high_performers = df[df['gpa'] > 3.7]
cs_majors = df[df['major'] == 'CS']

# Multiple conditions (use & for AND, | for OR)
young_high_performers = df[(df['age'] < 24) & (df['gpa'] > 3.7)]
cs_or_math = df[df['major'].isin(['CS', 'Math'])]

# Complex filtering with query (more readable)
complex_filter = df.query("age >= 23 and gpa > 3.6 and major in ['CS', 'Math']")
```

**Before vs After: Data Filtering**

```python
# BEFORE (manual iteration - slow and verbose)
high_gpa_students = []
for index, row in df.iterrows():
    if row['gpa'] > 3.7:
        high_gpa_students.append(row)
result_df = pd.DataFrame(high_gpa_students)

# AFTER (pandas magic - one line, vectorized, fast)
high_gpa_students = df[df['gpa'] > 3.7]
```

Why this is better: The pandas way is not only shorter but also much faster. It's like upgrading from dial-up to broadband.

## Working with Data Types

Understanding and managing data types is crucial for effective pandas usage:

```python
# Check current data types
print(df.dtypes)

# Convert data types
df['age'] = df['age'].astype('int32')        # Optimize integer storage
df['major'] = df['major'].astype('category') # Memory-efficient for repeated strings

# Handle mixed types in object columns
mixed_series = pd.Series(['1', '2', 'three', '4'])
numeric_series = pd.to_numeric(mixed_series, errors='coerce')  # NaN for non-numeric
print(numeric_series)
```

## Adding and Modifying Data

DataFrames are mutable - you can modify them after creation:

```python
# Add new columns
df['graduation_year'] = 2024
df['age_at_graduation'] = df['graduation_year'] - (2024 - df['age'])

# Conditional column creation
df['honor_roll'] = df['gpa'] >= 3.5
df['academic_level'] = df['gpa'].apply(
    lambda x: 'Excellent' if x >= 3.8 
    else 'Good' if x >= 3.5 
    else 'Satisfactory'
)

# Modify existing data
df.loc[df['major'] == 'CS', 'major'] = 'Computer Science'
```

## Exercise 2: DataFrame Fundamentals

### Basic Challenge
Create a DataFrame representing your favorite movies from the 90s:

```python
# Your mission: Create this DataFrame
movie_data = {
    'title': ['The Matrix', 'Titanic', 'Jurassic Park', 'Toy Story'],
    'year': [1999, 1997, 1993, 1995],
    'rating': [8.7, 7.8, 8.1, 8.3],
    'genre': ['Sci-Fi', 'Romance', 'Adventure', 'Animation']
}

movies_df = pd.DataFrame(movie_data)

# Tasks:
# 1. Display basic information about the DataFrame
# 2. Find all movies with rating > 8.0
# 3. Add a column indicating if the movie is from the late 90s (>=1997)
# 4. Calculate the average rating by genre
```

### Intermediate Challenge

```python
# Create a larger student dataset
np.random.seed(42)
n_students = 50

large_student_data = {
    'student_id': range(1, n_students + 1),
    'name': [f'Student_{i}' for i in range(1, n_students + 1)],
    'age': np.random.randint(18, 26, n_students),
    'major': np.random.choice(['CS', 'Math', 'Physics', 'Engineering'], n_students),
    'gpa': np.round(np.random.uniform(2.5, 4.0, n_students), 2),
    'credits': np.random.randint(60, 150, n_students),
    'scholarship': np.random.choice([True, False], n_students, p=[0.3, 0.7])
}

students_df = pd.DataFrame(large_student_data)

# Advanced tasks:
# 1. Find the top 10% of students by GPA
# 2. Calculate scholarship rate by major
# 3. Create age groups (18-20, 21-23, 24-26) and analyze GPA by group
# 4. Identify students who are both high achievers (GPA > 3.5) and have scholarships
```

### Advanced Challenge

```python
# Data quality challenge - work with messy data
messy_data = {
    'name': ['Alice Johnson', 'bob smith', 'CHARLIE BROWN', None, 'diana PRINCE'],
    'age': ['23', '24.0', 'twenty-five', '22', '26'],
    'gpa': [3.8, '3.6', 'unknown', 3.9, '3.7'],
    'major': ['CS', 'cs', 'Computer Science', 'CS', 'mathematics']
}

messy_df = pd.DataFrame(messy_data)

# Cleaning tasks:
# 1. Standardize the name format (Title Case)
# 2. Convert age to numeric (handle the text entry)
# 3. Clean and convert GPA to numeric
# 4. Standardize major names
# 5. Handle missing values appropriately
```

## Key Takeaways

1. **DataFrames are collections of Series** - understand this relationship
2. **Boolean indexing is your superpower** - master filtering techniques
3. **Data types matter** - optimize for memory and performance
4. **Inspection is essential** - always understand your data structure
5. **Pandas beats loops** - embrace vectorized operations

## Common Beginner Pitfalls

1. **Forgetting double brackets**: `df['col']` returns Series, `df[['col']]` returns DataFrame
2. **Chaining operations unsafely**: Use `.copy()` when needed
3. **Ignoring data types**: Check and convert types appropriately
4. **Not using boolean indexing**: Don't iterate when you can filter
5. **Modifying while iterating**: Use vectorized operations instead

## What's Next?

Now that you understand the fundamental building blocks, we'll explore how to get data into and out of your DataFrames. Because even the best video game character is useless without knowing how to load your save file!

---

**Next:** [Lesson 3: Data Loading and I/O Operations](03_data_io.md)

**Previous:** [Lesson 1: Setup and Environment](01_setup_environment.md)