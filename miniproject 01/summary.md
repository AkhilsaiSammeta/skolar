# Data Preprocessing and Feature Engineering Summary

## Data Collection
- Dataset: Titanic dataset from Kaggle
- Features: Mix of numerical (Age, Fare) and categorical (Sex, Embarked) features
- Target Variable: Survived

## Data Inspection
- 891 samples, 11 features
- Missing values in Age, Cabin, and Embarked
- Numerical and categorical features require preprocessing

## Data Preprocessing
### Data Cleaning
- Handled missing values:
  - Filled missing **Age** with median
  - Dropped rows with missing **Embarked**
  - Dropped **Cabin** due to many missing values

### Feature Scaling
- Applied **Min-Max Scaling** to normalize **Age** and **Fare**

### Handling Categorical Data
- Encoded **Sex** with label encoding (male=1, female=0)
- One-Hot Encoded **Embarked** with dummy variables

## Feature Engineering
- Created new feature **FamilySize**: Sum of **SibSp** and **Parch**
- Created **IsAlone**: Binary feature indicating if the passenger was alone

## Imbalanced Data Handling
- No severe imbalance in the **Survived** target variable, so no action taken

## Data Transformation
- Saved the preprocessed dataset to `preprocessed_titanic.csv`

## Analysis
- Visualized **Age** distribution after scaling
- Analyzed the relationship between **FamilySize** and **Survived**
- Summary statistics provided insights into feature scaling and new features

## Conclusion
- Data preprocessing ensured clean, normalized data ready for modeling
- Feature engineering added meaningful features, enhancing the dataset's representation for machine learning tasks
