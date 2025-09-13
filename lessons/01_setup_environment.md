# Lesson 1: Setup and Environment

> Like building the perfect gaming rig in the 90s, setting up your pandas environment right the first time saves hours of frustration later.

## Learning Objectives

By the end of this lesson, you'll be able to:
- Set up a professional pandas development environment
- Understand the essential libraries for AI data work
- Configure VS Code for optimal pandas development
- Create reproducible environments for collaboration

## The Pandas Ecosystem: Your Data Science Toolbox

Think of pandas as the centerpiece of your data science arsenal - like how Neo needed both martial arts training AND the right crew. Here's your essential toolkit:

### Core Components
- **pandas**: The main attraction - data manipulation superhero
- **NumPy**: The foundation - like the Matrix code underneath everything
- **matplotlib**: Basic plotting - your reliable sidekick
- **seaborn**: Pretty plots - when you need to impress stakeholders

### AI/ML Extensions
- **scikit-learn**: Machine learning made simple
- **plotly**: Interactive visualizations for dashboards
- **ydata-profiling**: Automated data analysis reports

## Installation Methods

### Method 1: Conda (Recommended for Data Science)

```bash
# Create a new environment (like setting up a clean virtual machine)
conda create -n pandas-ai-2026 python=3.11

# Activate your environment (enter the Matrix)
conda activate pandas-ai-2026

# Install the core data science stack
conda install pandas numpy matplotlib seaborn jupyter

# Install additional AI-focused libraries
pip install plotly scikit-learn ydata-profiling
```

**Why conda?** It handles complex dependencies better than pip, especially for data science libraries. It's like having a smart package manager that knows how to avoid version conflicts.

### Method 2: Virtual Environment + pip

```bash
# Create virtual environment
python -m venv pandas-env

# Activate environment
# Windows:
pandas-env\Scripts\activate
# macOS/Linux:
source pandas-env/bin/activate

# Install from requirements file
pip install -r requirements.txt
```

### Method 3: Using the Project Files

```bash
# If you have environment.yml (conda)
conda env create -f environment.yml
conda activate pandas-ai-2026

# If you have requirements.txt (pip)
pip install -r requirements.txt
```

## VS Code Configuration

### Essential Extensions

Install these VS Code extensions for the optimal pandas experience:

1. **Python** (Microsoft) - Core Python support
2. **Jupyter** (Microsoft) - Notebook support in VS Code
3. **GitHub Copilot** - Your AI pair programmer
4. **Data Wrangler** (Microsoft) - Visual data exploration
5. **Python Docstring Generator** - Auto-generate documentation

```bash
# Install extensions via command line
code --install-extension ms-python.python
code --install-extension ms-toolsai.jupyter
code --install-extension github.copilot
code --install-extension ms-toolsai.datawrangler
```

### VS Code Settings for Pandas

Add these to your VS Code settings (Ctrl+Shift+P → "Preferences: Open Settings (JSON)"):

```json
{
    "python.defaultInterpreterPath": "./pandas-env/bin/python",
    "jupyter.askForKernelRestart": false,
    "python.formatting.provider": "black",
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "files.autoSave": "afterDelay",
    "editor.formatOnSave": true,
    "python.terminal.activateEnvironment": true
}
```

## Import Convention: The Universal Law

This is pandas gospel - everyone follows this convention:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# This is like saying "using namespace std" in C++ 
# - everyone does it, don't fight it
```

**Why this matters:** Like how every movie in the 90s had at least one Nokia phone, every pandas tutorial uses `pd` as the alias. It's not just convention - it's muscle memory for millions of developers.

## Verification: Testing Your Setup

Create a test file to verify everything works:

```python
# test_setup.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("🐼 Pandas version:", pd.__version__)
print("🔢 NumPy version:", np.__version__)
print("📊 Matplotlib version:", plt.matplotlib.__version__)
print("🎨 Seaborn version:", sns.__version__)

# Quick functionality test
data = {'Name': ['Alice', 'Bob', 'Charlie'], 
        'Age': [25, 30, 35], 
        'City': ['NYC', 'LA', 'Chicago']}

df = pd.DataFrame(data)
print("\n✅ DataFrame creation test:")
print(df)

# Basic plot test
df['Age'].plot(kind='bar', title='Age Distribution')
plt.savefig('test_plot.png')
print("\n📈 Plot saved as 'test_plot.png'")
print("🎉 Setup successful! You're ready to rock!")
```

Run the test:
```bash
python test_setup.py
```

If you see the output without errors and a plot file is created, you're golden!

## Jupyter Notebook Integration

### Option 1: VS Code Integrated Notebooks
- Create `.ipynb` files directly in VS Code
- Run cells with Shift+Enter
- Seamless debugging and variable inspection

### Option 2: Traditional Jupyter Lab
```bash
# Start Jupyter Lab
jupyter lab

# Or classic notebook
jupyter notebook
```

### Best Practices for Notebook Organization

```python
# Cell 1: Imports and setup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set display options
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)

# Cell 2: Load data
df = pd.read_csv('your_data.csv')

# Cell 3: Initial exploration
df.info()
df.head()

# Continue with analysis...
```

## Common Setup Issues and Solutions

### Issue 1: ImportError for pandas
```
ModuleNotFoundError: No module named 'pandas'
```
**Solution:** Make sure your virtual environment is activated and pandas is installed in that environment.

### Issue 2: Jupyter not finding conda environment
**Solution:** Install ipykernel in your environment:
```bash
conda activate pandas-ai-2026
pip install ipykernel
python -m ipykernel install --user --name pandas-ai-2026
```

### Issue 3: Plots not showing in Jupyter
**Solution:** Add magic command at the start of your notebook:
```python
%matplotlib inline
```

## Performance Configuration

For better performance with large datasets:

```python
# Optimize pandas for performance
import pandas as pd

# Increase display precision
pd.set_option('display.precision', 3)

# Optimize memory usage
pd.set_option('mode.copy_on_write', True)

# For plotting large datasets
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8')  # Better default styling
```

## Exercise 1: Environment Setup Challenge

**Beginner Challenge:** Complete the setup verification
1. Install the pandas environment using your preferred method
2. Run the test script successfully
3. Create a simple notebook with the imports
4. Generate your first plot

**Intermediate Challenge:** Custom configuration
1. Set up VS Code with all recommended extensions
2. Create a custom settings configuration for pandas work
3. Test Jupyter integration with your environment
4. Create a reusable setup script for future projects

**Advanced Challenge:** Team environment
1. Create both conda and pip environment specifications
2. Add development dependencies (testing, formatting)
3. Document the setup process for team members
4. Create a verification script that tests all functionality

## What's Next?

With your environment locked and loaded, you're ready to dive into the actual pandas magic. In the next lesson, we'll explore the fundamental building blocks: DataFrames and Series - the Batman and Robin of data manipulation.

Remember: A properly configured environment is like having the right equipment before climbing Mount Everest. You could probably do it with basic gear, but why make it harder than it needs to be?

---

**Next:** [Lesson 2: Core Concepts - DataFrames and Series](02_core_concepts.md)

**Previous:** [Main README](../README.md)