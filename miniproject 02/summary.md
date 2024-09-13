# Building a Classification Model with Scikit-learn

## Objective:
Build a binary classification model using scikit-learn, perform data preprocessing, train multiple models, and evaluate their performance.

---

## Tasks:

### 1. **Data Loading**:
- Choose a dataset from sklearn's built-in datasets (or any reliable external source).
- Load the dataset into a pandas DataFrame.
- Display the first few rows for inspection.

### 2. **Data Preprocessing**:
- Handle missing values (if any).
- Encode categorical variables.
- Scale/normalize numerical features for consistency.

### 3. **Data Splitting**:
- Split the data into training (70-80%) and testing (20-30%) sets.
- Use `train_test_split` from sklearn for this task.

### 4. **Model Selection**:
- Train at least two classification models from scikit-learn:
  - Example models: **Logistic Regression**, **Decision Tree**, **Random Forest**, **SVM**.
- Train each model using the training set.

### 5. **Model Evaluation**:
- Evaluate models using key metrics:
  - Accuracy
  - Precision
  - Recall
  - F1-score
  - ROC AUC
- Compare the models' performance on the test set.
- Use visualizations such as a **confusion matrix** and **ROC curve**.

### 6. **Cross-Validation** (Optional):
- Use **cross-validation** techniques like `GridSearchCV` or `RandomizedSearchCV` for hyperparameter tuning (optional).

### 7. **Conclusion**:
- Summarize findings from model performance comparisons.
- Discuss strengths and weaknesses of the models tested.
- Reflect on the impact of data preprocessing and model evaluation metrics.

---

## Submission Guidelines:
- Submit a well-documented Jupyter Notebook or Python script.
- Include code for:
  - Data loading, preprocessing, splitting.
  - Model training and evaluation.
  - Hyperparameter tuning (optional).
- Include visualizations like confusion matrix and ROC curve.
