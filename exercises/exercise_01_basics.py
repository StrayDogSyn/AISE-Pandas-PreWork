# Exercise 1: Environment Setup and Basic Operations

"""
Pandas Mastery - Exercise 1
Environment Setup and Basic DataFrame Operations

Complete these exercises to verify your setup and practice basic pandas operations.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ===============================================
# PART 1: ENVIRONMENT VERIFICATION
# ===============================================

def test_environment():
    """Test that all required libraries are properly installed"""
    print("🔧 Testing Environment Setup...")
    
    # Test pandas
    print(f"✅ Pandas version: {pd.__version__}")
    
    # Test numpy
    print(f"✅ NumPy version: {np.__version__}")
    
    # Test matplotlib
    import matplotlib
    print(f"✅ Matplotlib version: {matplotlib.__version__}")
    
    # Test seaborn
    try:
        import seaborn as sns
        print(f"✅ Seaborn version: {sns.__version__}")
    except ImportError:
        print("❌ Seaborn not installed")
    
    # Test plotly
    try:
        import plotly
        print(f"✅ Plotly version: {plotly.__version__}")
    except ImportError:
        print("❌ Plotly not installed")
    
    print("\n🎉 Environment test complete!")

# ===============================================
# PART 2: BASIC DATAFRAME OPERATIONS
# ===============================================

def create_sample_data():
    """Create sample data for practice"""
    
    # Your favorite 90s movies dataset
    movies_90s = {
        'title': [
            'The Matrix', 'Titanic', 'Jurassic Park', 'Toy Story',
            'The Lion King', 'Forrest Gump', 'Pulp Fiction', 'The Mask'
        ],
        'year': [1999, 1997, 1993, 1995, 1994, 1994, 1994, 1994],
        'rating': [8.7, 7.8, 8.1, 8.3, 8.5, 8.8, 8.9, 6.9],
        'genre': [
            'Sci-Fi', 'Romance', 'Adventure', 'Animation',
            'Animation', 'Drama', 'Crime', 'Comedy'
        ],
        'box_office_millions': [463.5, 2187.5, 1029.9, 373.6, 968.5, 677.9, 214.2, 351.6]
    }
    
    return pd.DataFrame(movies_90s)

def basic_operations_challenge():
    """Complete basic DataFrame operations"""
    
    print("\n🎬 90s Movie Analysis Challenge")
    print("=" * 40)
    
    # Create the DataFrame
    movies_df = create_sample_data()
    
    # TODO 1: Display basic information about the DataFrame
    print("\n1. DataFrame Info:")
    print(f"Shape: {movies_df.shape}")
    print(f"Columns: {list(movies_df.columns)}")
    print("\nFirst 3 rows:")
    print(movies_df.head(3))
    
    # TODO 2: Find movies with rating > 8.0
    print("\n2. High-rated movies (rating > 8.0):")
    high_rated = movies_df[movies_df['rating'] > 8.0]
    print(high_rated[['title', 'rating']])
    
    # TODO 3: Add a column for late 90s movies (>= 1997)
    movies_df['late_90s'] = movies_df['year'] >= 1997
    print("\n3. Added 'late_90s' column:")
    print(movies_df[['title', 'year', 'late_90s']])
    
    # TODO 4: Calculate average rating by genre
    print("\n4. Average rating by genre:")
    genre_ratings = movies_df.groupby('genre')['rating'].mean().sort_values(ascending=False)
    print(genre_ratings)
    
    # TODO 5: Find the highest grossing movie
    print("\n5. Highest grossing movie:")
    top_grosser = movies_df.loc[movies_df['box_office_millions'].idxmax()]
    print(f"{top_grosser['title']}: ${top_grosser['box_office_millions']:.1f}M")
    
    return movies_df

# ===============================================
# PART 3: DATA CREATION PRACTICE
# ===============================================

def create_student_data():
    """Create a student dataset for practice"""
    
    np.random.seed(42)  # For reproducible results
    n_students = 20
    
    majors = ['Computer Science', 'Mathematics', 'Physics', 'Engineering']
    
    student_data = {
        'student_id': [f"STU{i:03d}" for i in range(1, n_students + 1)],
        'name': [f"Student_{i}" for i in range(1, n_students + 1)],
        'age': np.random.randint(18, 25, n_students),
        'major': np.random.choice(majors, n_students),
        'gpa': np.round(np.random.uniform(2.5, 4.0, n_students), 2),
        'credits_completed': np.random.randint(30, 120, n_students),
        'scholarship': np.random.choice([True, False], n_students, p=[0.3, 0.7])
    }
    
    return pd.DataFrame(student_data)

def student_analysis_challenge():
    """Analyze student data"""
    
    print("\n👩‍🎓 Student Data Analysis Challenge")
    print("=" * 40)
    
    students_df = create_student_data()
    
    # Display the data
    print(f"\nDataset contains {len(students_df)} students")
    print(students_df.head())
    
    # TODO 1: Basic statistics
    print(f"\nAverage GPA: {students_df['gpa'].mean():.2f}")
    print(f"Age range: {students_df['age'].min()} - {students_df['age'].max()}")
    print(f"Scholarship rate: {students_df['scholarship'].mean():.1%}")
    
    # TODO 2: Major distribution
    print("\nMajor distribution:")
    print(students_df['major'].value_counts())
    
    # TODO 3: High achievers with scholarships
    high_achievers_with_scholarship = students_df[
        (students_df['gpa'] >= 3.5) & (students_df['scholarship'] == True)
    ]
    print(f"\nHigh achievers (GPA ≥ 3.5) with scholarships: {len(high_achievers_with_scholarship)}")
    
    # TODO 4: GPA by major
    print("\nAverage GPA by major:")
    gpa_by_major = students_df.groupby('major')['gpa'].mean().sort_values(ascending=False)
    print(gpa_by_major.round(2))
    
    return students_df

# ===============================================
# PART 4: VISUALIZATION PRACTICE
# ===============================================

def create_basic_plots():
    """Create basic plots to test matplotlib integration"""
    
    print("\n📊 Basic Plotting Challenge")
    print("=" * 30)
    
    # Create sample data
    movies_df = create_sample_data()
    
    # Create a simple plot
    plt.figure(figsize=(10, 6))
    
    # Plot 1: Rating distribution
    plt.subplot(2, 2, 1)
    movies_df['rating'].hist(bins=6, edgecolor='black')
    plt.title('Movie Rating Distribution')
    plt.xlabel('Rating')
    plt.ylabel('Count')
    
    # Plot 2: Box office by genre
    plt.subplot(2, 2, 2)
    genre_box_office = movies_df.groupby('genre')['box_office_millions'].sum()
    genre_box_office.plot(kind='bar')
    plt.title('Box Office by Genre')
    plt.xlabel('Genre')
    plt.ylabel('Box Office (Millions)')
    plt.xticks(rotation=45)
    
    # Plot 3: Rating vs Box Office
    plt.subplot(2, 2, 3)
    plt.scatter(movies_df['rating'], movies_df['box_office_millions'])
    plt.title('Rating vs Box Office')
    plt.xlabel('Rating')
    plt.ylabel('Box Office (Millions)')
    
    # Plot 4: Movies by year
    plt.subplot(2, 2, 4)
    movies_df['year'].value_counts().sort_index().plot(kind='line', marker='o')
    plt.title('Movies by Year')
    plt.xlabel('Year')
    plt.ylabel('Count')
    
    plt.tight_layout()
    plt.savefig('exercise_1_plots.png', dpi=150, bbox_inches='tight')
    print("📈 Plots saved as 'exercise_1_plots.png'")
    plt.show()

# ===============================================
# MAIN EXECUTION
# ===============================================

def main():
    """Run all exercises"""
    
    print("🐼 Pandas Mastery - Exercise 1")
    print("=" * 50)
    
    # Part 1: Test environment
    test_environment()
    
    # Part 2: Basic operations
    movies_df = basic_operations_challenge()
    
    # Part 3: Student data analysis
    students_df = student_analysis_challenge()
    
    # Part 4: Basic plotting
    create_basic_plots()
    
    print(f"\n🎉 Exercise 1 Complete!")
    print("🚀 You're ready to move on to more advanced pandas operations!")
    
    return movies_df, students_df

if __name__ == "__main__":
    movies_data, student_data = main()