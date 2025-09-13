# Pandas Mastery Quick Reference Cheat Sheet

## Essential Imports
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

## Data Loading
```python
# CSV files
df = pd.read_csv('file.csv')
df = pd.read_csv('file.csv', sep=';', encoding='utf-8')

# Excel files  
df = pd.read_excel('file.xlsx', sheet_name='Sheet1')

# JSON files
df = pd.read_json('file.json')

# From URL
df = pd.read_csv('https://example.com/data.csv')
```

## Quick Exploration
```python
df.head()                    # First 5 rows
df.tail()                    # Last 5 rows
df.info()                    # Data types and memory usage
df.describe()                # Statistical summary
df.shape                     # (rows, columns)
df.columns                   # Column names
df.dtypes                    # Data types
df.nunique()                 # Unique values per column
df.value_counts()            # Frequency of values
```

## Selection and Filtering
```python
# Single column
df['column']                 # Returns Series
df[['column']]              # Returns DataFrame

# Multiple columns
df[['col1', 'col2']]

# Row selection
df.iloc[0]                   # First row by position
df.iloc[0:5]                 # First 5 rows
df.loc[df['col'] > 5]        # Conditional selection

# Boolean filtering
df[df['column'] > value]                     # Simple condition
df[(df['col1'] > val1) & (df['col2'] == val2)]  # Multiple conditions
df[df['column'].isin(['A', 'B'])]           # Value in list
```

## Data Cleaning
```python
# Missing data
df.isnull().sum()            # Count nulls per column
df.dropna()                  # Drop rows with any NaN
df.fillna(value)             # Fill NaN with value
df.fillna(df.mean())         # Fill with column means

# Data types
df['col'].astype('int')      # Convert data type
pd.to_numeric(df['col'])     # Convert to numeric
pd.to_datetime(df['col'])    # Convert to datetime

# Duplicates
df.drop_duplicates()         # Remove duplicate rows
df.duplicated()              # Boolean mask of duplicates
```

## Creating New Columns
```python
# Simple calculation
df['new_col'] = df['col1'] + df['col2']

# Conditional logic
df['new_col'] = np.where(condition, value_if_true, value_if_false)

# Apply functions
df['new_col'] = df['col'].apply(lambda x: x * 2)
df['new_col'] = df.apply(function, axis=1)  # Apply to rows
```

## Grouping and Aggregation
```python
# Basic grouping
df.groupby('column').mean()               # Average by group
df.groupby('column').sum()                # Sum by group
df.groupby('column').size()               # Count by group
df.groupby('column').agg(['mean', 'std']) # Multiple aggregations

# Multiple columns
df.groupby(['col1', 'col2']).mean()

# Custom aggregation
df.groupby('col').agg({
    'col1': 'mean',
    'col2': ['sum', 'count']
})
```

## Sorting
```python
df.sort_values('column')                  # Sort by column
df.sort_values(['col1', 'col2'])         # Sort by multiple columns
df.sort_values('col', ascending=False)    # Descending order
df.sort_index()                          # Sort by index
```

## String Operations
```python
df['col'].str.upper()                    # Uppercase
df['col'].str.lower()                    # Lowercase
df['col'].str.len()                      # String length
df['col'].str.contains('pattern')        # Contains pattern
df['col'].str.replace('old', 'new')      # Replace text
df['col'].str.split('delimiter')         # Split strings
```

## Date and Time Operations
```python
pd.to_datetime(df['date_col'])           # Convert to datetime
df['date_col'].dt.year                   # Extract year
df['date_col'].dt.month                  # Extract month
df['date_col'].dt.dayofweek              # Day of week (0=Monday)
df.set_index('date_col')                 # Set datetime index
df.resample('M').mean()                  # Resample by month
```

## Combining DataFrames
```python
# Concatenation
pd.concat([df1, df2])                    # Vertical (add rows)
pd.concat([df1, df2], axis=1)            # Horizontal (add columns)

# Merging (like SQL joins)
pd.merge(df1, df2, on='column')          # Inner join
pd.merge(df1, df2, on='column', how='left')   # Left join
pd.merge(df1, df2, on='column', how='outer')  # Outer join
```

## Pivot Tables and Reshaping
```python
# Pivot tables
pd.pivot_table(df, values='value', index='row', columns='col')

# Melt (wide to long)
pd.melt(df, id_vars=['id'], value_vars=['col1', 'col2'])

# Pivot (long to wide)
df.pivot(index='index', columns='column', values='value')
```

## Statistical Operations
```python
df['col'].mean()                         # Average
df['col'].median()                       # Median
df['col'].std()                          # Standard deviation
df['col'].min()                          # Minimum
df['col'].max()                          # Maximum
df['col'].quantile(0.25)                 # 25th percentile
df.corr()                                # Correlation matrix
```

## Saving Data
```python
df.to_csv('output.csv', index=False)     # Save to CSV
df.to_excel('output.xlsx', index=False)  # Save to Excel
df.to_json('output.json')                # Save to JSON
```

## Quick Plotting
```python
df['col'].plot()                         # Line plot
df['col'].hist()                         # Histogram
df.plot.scatter(x='col1', y='col2')      # Scatter plot
df.plot.bar()                            # Bar plot
df.boxplot()                             # Box plot
```

## Performance Tips
```python
# Use vectorized operations instead of loops
df['new_col'] = df['col1'] * df['col2']  # Good
# Not: for i in range(len(df)): ...       # Bad

# Use .loc for selection
df.loc[condition, 'column']              # Good
# Not: df[condition]['column']             # Bad

# Chain operations efficiently
result = (df
    .query("col > 5")
    .groupby('category')
    .mean()
    .sort_values('value'))
```

## Common Patterns
```python
# Find top N values
df.nlargest(10, 'column')

# Find bottom N values  
df.nsmallest(10, 'column')

# Sample data
df.sample(n=100)                         # Random 100 rows
df.sample(frac=0.1)                      # Random 10% of data

# Reset index
df.reset_index(drop=True)                # Reset to default integer index

# Set new index
df.set_index('column')                   # Use column as index
```

## Memory Optimization
```python
# Optimize data types
df['category_col'] = df['category_col'].astype('category')
df['int_col'] = pd.to_numeric(df['int_col'], downcast='integer')

# Check memory usage
df.info(memory_usage='deep')

# Read large files in chunks
for chunk in pd.read_csv('large_file.csv', chunksize=10000):
    # Process chunk
    pass
```

## Debugging Tips
```python
# Display all columns
pd.set_option('display.max_columns', None)

# Display more rows
pd.set_option('display.max_rows', 100)

# Check for issues
df.isnull().sum()                        # Missing values
df.dtypes                                # Data types
df.describe()                            # Statistical overview
df.head()                                # Sample data
```

Remember: When in doubt, check the official pandas documentation at https://pandas.pydata.org/docs/