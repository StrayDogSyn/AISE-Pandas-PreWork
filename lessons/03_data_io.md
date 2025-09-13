# Lesson 3: Data Loading and I/O Operations

> Reading data files is like opening a present - you never know what you're going to get until you unwrap it. But with pandas, at least you have the right tools to deal with whatever's inside.

## Learning Objectives

By the end of this lesson, you'll be able to:

- Load data from various file formats (CSV, Excel, JSON, databases)
- Handle common data loading challenges (encoding, missing values, formats)
- Save DataFrames in multiple formats
- Optimize data loading for performance and memory

## Reading Data: The Gateway Drug

Data loading is the first step in every data analysis project. Like learning to read before you can write stories, you need to master data input before you can create insights.

### CSV Files: The Universal Language

CSV (Comma-Separated Values) is the lingua franca of data exchange:

```python
import pandas as pd

# Basic CSV reading (the bread and butter)
df = pd.read_csv('data.csv')

# Reading with options (because real data is messy)
df = pd.read_csv(
    'messy_data.csv',
    sep=',',                    # delimiter (could be ';', '|', '\t')
    header=0,                   # which row contains column names
    index_col=0,               # which column to use as index
    na_values=['N/A', 'NULL'], # what to treat as missing values
    encoding='utf-8',          # character encoding
    skiprows=2,                # skip first 2 rows
    nrows=1000                 # only read first 1000 rows
)

# From URL (pandas can read directly from the internet)
url = 'https://raw.githubusercontent.com/user/repo/main/data.csv'
df = pd.read_csv(url)
```

### Excel Files: For When Your Stakeholders Live in Spreadsheets

```python
# Basic Excel reading
df = pd.read_excel('quarterly_report.xlsx')

# Advanced Excel operations
df = pd.read_excel(
    'complex_workbook.xlsx',
    sheet_name='Q4_Data',      # specific sheet
    header=1,                  # header in second row
    index_col='Date',         # use Date column as index
    parse_dates=True,         # automatically parse dates
    na_values=['#N/A', 'NULL']
)

# Read multiple sheets at once
all_sheets = pd.read_excel('workbook.xlsx', sheet_name=None)
q1_data = all_sheets['Q1']
q2_data = all_sheets['Q2']

# Read specific ranges (like Excel formulas)
df = pd.read_excel('data.xlsx', usecols='A:D', nrows=100)
```

### JSON Files: For API Responses and Modern Data

```python
# Simple JSON reading
df = pd.read_json('api_response.json')

# JSON with specific orientation
df = pd.read_json('data.json', orient='records')  # List of dictionaries
df = pd.read_json('data.json', orient='index')    # Dictionary of dictionaries

# From API endpoints
import requests
response = requests.get('https://api.example.com/data')
df = pd.read_json(response.text)
```

### Database Connections: The Enterprise Way

```python
import sqlite3
from sqlalchemy import create_engine

# SQLite (lightweight, file-based)
conn = sqlite3.connect('company_data.db')
df = pd.read_sql('SELECT * FROM customers', conn)
conn.close()

# PostgreSQL/MySQL with SQLAlchemy
engine = create_engine('postgresql://user:password@localhost:5432/database')
df = pd.read_sql('SELECT * FROM sales WHERE date >= %s', engine, 
                 params=['2023-01-01'])

# Read entire table
df = pd.read_sql_table('products', engine)
```

## Writing Data: Saving Your Progress

Like saving your game progress, you need multiple save formats for different purposes:

```python
# Save to CSV (the universal format)
df.to_csv('processed_data.csv', index=False)  # index=False prevents extra index column

# CSV with custom options
df.to_csv(
    'clean_data.csv',
    index=False,
    sep='|',                    # use pipe separator
    encoding='utf-8',
    na_rep='NULL',             # how to represent missing values
    float_format='%.2f'        # format floats to 2 decimal places
)

# Save to Excel with formatting
with pd.ExcelWriter('report.xlsx') as writer:
    df.to_excel(writer, sheet_name='Summary', index=False)
    df.groupby('category').sum().to_excel(writer, sheet_name='Totals')
    
# Multiple sheets with formatting
with pd.ExcelWriter('financial_report.xlsx', engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Raw_Data')
    summary.to_excel(writer, sheet_name='Summary')
    
    # Access workbook to add formatting
    workbook = writer.book
    worksheet = writer.sheets['Summary']
    worksheet.sheet_properties.tabColor = "1072BA"  # Blue tab

# Save to JSON for APIs
df.to_json('data.json', orient='records', indent=2)  # Pretty printed
df.to_json('api_data.json', orient='records', lines=True)  # JSON Lines format
```

## Handling Common Data Loading Challenges

### Challenge 1: Character Encoding Issues

```python
# Try different encodings
encodings = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']

for encoding in encodings:
    try:
        df = pd.read_csv('problematic_file.csv', encoding=encoding)
        print(f"Success with encoding: {encoding}")
        break
    except UnicodeDecodeError:
        print(f"Failed with encoding: {encoding}")

# Auto-detect encoding (requires chardet library)
import chardet

with open('mystery_file.csv', 'rb') as f:
    result = chardet.detect(f.read())
    encoding = result['encoding']
    
df = pd.read_csv('mystery_file.csv', encoding=encoding)
```

### Challenge 2: Mixed Data Types in Columns

```python
# Specify data types explicitly
dtype_dict = {
    'customer_id': 'str',      # Keep as string even if numeric
    'amount': 'float64',
    'category': 'category',    # Memory-efficient for repeated values
    'is_active': 'bool'
}

df = pd.read_csv('mixed_data.csv', dtype=dtype_dict)

# Handle mixed types with converters
def clean_currency(value):
    """Convert currency strings to float"""
    if isinstance(value, str):
        return float(value.replace('$', '').replace(',', ''))
    return value

df = pd.read_csv('financial_data.csv', 
                 converters={'amount': clean_currency})
```

### Challenge 3: Date and Time Parsing

```python
# Automatic date parsing
df = pd.read_csv('time_series.csv', parse_dates=['date_column'])

# Custom date parsing
df = pd.read_csv('custom_dates.csv', 
                 parse_dates=['date_col'],
                 date_parser=lambda x: pd.to_datetime(x, format='%d/%m/%Y'))

# Multiple date columns
df = pd.read_csv('events.csv', 
                 parse_dates=[['start_date', 'start_time']])

# Parse dates after loading
df['date_column'] = pd.to_datetime(df['date_column'], format='%Y-%m-%d')
```

## Performance Optimization for Large Files

### Chunking: Eating the Elephant One Bite at a Time

```python
# Read large files in chunks
def process_large_csv(filename, chunk_size=10000):
    """Process large CSV files efficiently"""
    chunk_results = []
    
    for chunk in pd.read_csv(filename, chunksize=chunk_size):
        # Process each chunk
        processed_chunk = chunk[chunk['amount'] > 100]  # Example filtering
        summary = processed_chunk.groupby('category').sum()
        chunk_results.append(summary)
    
    # Combine results
    final_result = pd.concat(chunk_results).groupby(level=0).sum()
    return final_result

# Usage
result = process_large_csv('huge_file.csv', chunk_size=50000)
```

### Memory Optimization

```python
# Optimize data types while reading
df = pd.read_csv('large_file.csv', 
                 dtype={'category': 'category',
                        'small_int': 'int8',
                        'medium_int': 'int16'})

# Read only necessary columns
df = pd.read_csv('wide_file.csv', 
                 usecols=['date', 'amount', 'category'])

# Sample large datasets
df_sample = pd.read_csv('huge_file.csv', 
                        skiprows=lambda i: i > 0 and random.random() > 0.01)
```

## Working with Multiple Files

### Reading Multiple Files of Same Structure

```python
import glob
import os

# Method 1: Using glob
file_pattern = 'data/sales_*.csv'
all_files = glob.glob(file_pattern)

dataframes = []
for file in all_files:
    df = pd.read_csv(file)
    df['source_file'] = os.path.basename(file)  # Track source
    dataframes.append(df)

combined_df = pd.concat(dataframes, ignore_index=True)

# Method 2: List comprehension (more pythonic)
file_list = ['data/jan.csv', 'data/feb.csv', 'data/mar.csv']
quarterly_data = pd.concat([
    pd.read_csv(f).assign(month=os.path.basename(f).split('.')[0])
    for f in file_list
], ignore_index=True)
```

### Reading Directory of Files

```python
def read_directory_csv(directory_path):
    """Read all CSV files in a directory"""
    all_files = glob.glob(os.path.join(directory_path, "*.csv"))
    
    dataframes = []
    for file in all_files:
        try:
            df = pd.read_csv(file)
            df['filename'] = os.path.basename(file)
            df['file_path'] = file
            dataframes.append(df)
        except Exception as e:
            print(f"Error reading {file}: {e}")
    
    if dataframes:
        return pd.concat(dataframes, ignore_index=True)
    else:
        return pd.DataFrame()

# Usage
all_data = read_directory_csv('data/monthly_reports/')
```

## Exercise 3: Data Loading Challenge

### Basic Challenge: File Format Mastery

Create sample data and practice loading/saving in different formats:

```python
# Create sample data
sample_data = {
    'product': ['Widget A', 'Widget B', 'Gadget X', 'Gadget Y'],
    'sales': [1000, 1500, 800, 1200],
    'profit_margin': [0.3, 0.25, 0.4, 0.35],
    'region': ['North', 'South', 'East', 'West'],
    'launch_date': ['2023-01-15', '2023-02-20', '2023-03-10', '2023-04-05']
}

df = pd.DataFrame(sample_data)

# Tasks:
# 1. Save in CSV, JSON, and Excel formats
# 2. Reload each format and verify data integrity
# 3. Save Excel with multiple sheets
# 4. Export summary statistics to separate files
```

### Intermediate Challenge: Real-World Data Issues

```python
# Create intentionally messy data
messy_sales_data = """date,product,amount,region,notes
2023-01-15,"Widget A","$1,500",North,Good sales
2023-01-16,"Widget B",NULL,South,"Promotion ended"
2023/01/17,Gadget X,800.50,East,
invalid_date,"Widget A","2,000",West,Back to school season
2023-01-19,"Gadget Y",1200.75,North,"Best seller"
"""

# Save to file and practice loading
with open('messy_sales.csv', 'w') as f:
    f.write(messy_sales_data)

# Challenge tasks:
# 1. Load the data handling various date formats
# 2. Clean the currency column to numeric
# 3. Handle NULL values appropriately
# 4. Deal with the invalid date row
# 5. Create a clean version for analysis
```

### Advanced Challenge: Performance Optimization

```python
# Create a large dataset for performance testing
import numpy as np

large_data = {
    'transaction_id': range(1, 100001),
    'customer_id': np.random.randint(1, 10000, 100000),
    'amount': np.random.lognormal(3, 1, 100000),
    'category': np.random.choice(['A', 'B', 'C', 'D'], 100000),
    'date': pd.date_range('2023-01-01', periods=100000, freq='1H')
}

large_df = pd.DataFrame(large_data)
large_df.to_csv('large_dataset.csv', index=False)

# Performance challenges:
# 1. Load only the first 1000 rows efficiently
# 2. Load only specific columns
# 3. Process the file in chunks of 10,000 rows
# 4. Optimize data types to reduce memory usage
# 5. Create a sampling strategy for quick analysis
```

## Pro Tips for Data Loading

### 1. Always Inspect First

```python
# Quick peek at file structure
with open('unknown_file.csv', 'r') as f:
    print(f.readline())  # First line
    print(f.readline())  # Second line

# Load just a few rows first
sample = pd.read_csv('large_file.csv', nrows=5)
print(sample.info())
```

### 2. Create Loading Functions

```python
def smart_csv_loader(filename, **kwargs):
    """Intelligent CSV loader with error handling"""
    try:
        # Try UTF-8 first
        df = pd.read_csv(filename, encoding='utf-8', **kwargs)
    except UnicodeDecodeError:
        try:
            # Fall back to latin-1
            df = pd.read_csv(filename, encoding='latin-1', **kwargs)
        except Exception as e:
            print(f"Failed to load {filename}: {e}")
            return None
    
    print(f"Loaded {len(df)} rows from {filename}")
    return df
```

### 3. Document Your Data Sources

```python
# Create metadata for your datasets
data_catalog = {
    'sales_2023.csv': {
        'description': 'Monthly sales data for 2023',
        'source': 'Sales team export',
        'last_updated': '2023-12-01',
        'columns': ['date', 'product', 'amount', 'region'],
        'encoding': 'utf-8'
    }
}

def load_with_metadata(filename):
    """Load data with associated metadata"""
    if filename in data_catalog:
        metadata = data_catalog[filename]
        print(f"Loading: {metadata['description']}")
        df = pd.read_csv(filename, encoding=metadata['encoding'])
        df.attrs['metadata'] = metadata  # Store metadata with DataFrame
        return df
    else:
        print(f"No metadata found for {filename}")
        return pd.read_csv(filename)
```

## Common Pitfalls and Solutions

1. **Mixed delimiters**: Use `sep=None` to auto-detect
2. **Extra whitespace**: Use `skipinitialspace=True`
3. **Multiple header rows**: Use `header=[0,1]` for MultiIndex columns
4. **Inconsistent missing values**: Provide comprehensive `na_values` list
5. **Large files crashing**: Always use chunking for files > 1GB

## What's Next?

Now that you can get data in and out of pandas like a pro, it's time to explore what's actually inside that data. In the next lesson, we'll become data detectives, learning to explore and select exactly what we need from our datasets.

Remember: Loading data is like unpacking after a move - you need to know what you have before you can organize it effectively!

---

**Next:** [Lesson 4: Data Exploration and Selection](04_exploration_selection.md)

**Previous:** [Lesson 2: Core Concepts](02_core_concepts.md)