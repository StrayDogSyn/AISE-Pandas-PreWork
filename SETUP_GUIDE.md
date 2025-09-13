# Environment Setup Guide

This guide will help you set up the Python environment for the AISE Pandas Pre-Work tutorial.

## Quick Setup (Recommended)

The environment has already been set up for you! The virtual environment `pandas-env` contains all required packages.

### Activate the Virtual Environment

```bash
# In the project directory
pandas-env\Scripts\activate
```

### Verify Installation

```bash
python -c "import pandas as pd; print('✅ Pandas:', pd.__version__)"
python -c "import numpy as np; print('✅ NumPy:', np.__version__)"
python -c "import matplotlib; print('✅ Matplotlib:', matplotlib.__version__)"
```

## Package Versions Installed

- pandas: 2.3.2
- numpy: 2.3.3
- matplotlib: 3.10.6
- seaborn: 0.13.2
- plotly: 6.3.0
- scikit-learn: 1.7.2
- jupyter/jupyterlab: 4.4.7
- ipykernel: 6.30.1

## Running the Exercises

1. Open VS Code in this directory
2. Ensure the Python interpreter is set to: `pandas-env\Scripts\python.exe`
3. Run the exercise files directly or open Jupyter notebooks

## Testing Your Setup

Run the first exercise to verify everything works:

```bash
python exercises/exercise_01_basics.py
```

You should see output confirming all packages are working correctly.

## Troubleshooting

If you encounter import errors:

1. Make sure VS Code is using the correct Python interpreter
2. Activate the virtual environment before running commands
3. If issues persist, recreate the environment:
   ```bash
   python -m venv pandas-env-new
   pandas-env-new\Scripts\activate
   pip install -r requirements.txt
   ```

## VS Code Configuration

The Python interpreter should be automatically set to:
`c:\Users\EHunt\Repos\AISE\AISE-Pandas-PreWork\pandas-env\Scripts\python.exe`

If not, use Ctrl+Shift+P → "Python: Select Interpreter" and choose the pandas-env interpreter.