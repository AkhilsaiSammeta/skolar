
### Step-by-Step Execution :

---

### 1. **Data Loading**:

If you're using a built-in dataset, for example, the **Breast Cancer dataset** from `sklearn.datasets`:

```python
# Import necessary libraries
import pandas as pd
from sklearn.datasets import load_breast_cancer

# Load the dataset
data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

# Inspect the data
print(df.head())
```

---

### 2. **Data Preprocessing**:

Handle missing values, encode categorical features, and scale numerical data.

```python
# Check for missing values
print(df.isnull().sum())  # Assuming no missing values for sklearn dataset

# Feature scaling using StandardScaler
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df.drop(columns=['target'])), columns=data.feature_names)

# Re-add target column to scaled dataframe
df_scaled['target'] = df['target']
```

---

### 3. **Data Splitting**:

Split the dataset into training and testing sets.

```python
from sklearn.model_selection import train_test_split

# Define features (X) and target (y)
X = df_scaled.drop(columns=['target'])
y = df_scaled['target']

# Split data: 80% training, 20% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

---

### 4. **Model Selection**:

Train at least two classification models, such as **Logistic Regression** and **Random Forest**.

```python
# Import models
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

# Train Logistic Regression
log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)

# Train Random Forest
rf = RandomForestClassifier()
rf.fit(X_train, y_train)
```

---

### 5. **Model Evaluation**:

Evaluate the models using accuracy, precision, recall, F1-score, and ROC AUC.

```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Make predictions
log_reg_pred = log_reg.predict(X_test)
rf_pred = rf.predict(X_test)

# Evaluate Logistic Regression
print("Logistic Regression Metrics:")
print("Accuracy:", accuracy_score(y_test, log_reg_pred))
print("Precision:", precision_score(y_test, log_reg_pred))
print("Recall:", recall_score(y_test, log_reg_pred))
print("F1 Score:", f1_score(y_test, log_reg_pred))
print("ROC AUC:", roc_auc_score(y_test, log_reg.predict_proba(X_test)[:, 1]))

# Evaluate Random Forest
print("\nRandom Forest Metrics:")
print("Accuracy:", accuracy_score(y_test, rf_pred))
print("Precision:", precision_score(y_test, rf_pred))
print("Recall:", recall_score(y_test, rf_pred))
print("F1 Score:", f1_score(y_test, rf_pred))
print("ROC AUC:", roc_auc_score(y_test, rf.predict_proba(X_test)[:, 1]))

# Confusion matrix for both models
log_cm = confusion_matrix(y_test, log_reg_pred)
rf_cm = confusion_matrix(y_test, rf_pred)

# Visualize confusion matrix
sns.heatmap(log_cm, annot=True, fmt='d')
plt.title("Logistic Regression Confusion Matrix")
plt.show()

sns.heatmap(rf_cm, annot=True, fmt='d')
plt.title("Random Forest Confusion Matrix")
plt.show()
```

---

### 6. **Cross-Validation (Optional)**:

Use **GridSearchCV** or **RandomizedSearchCV** to tune hyperparameters.

```python
from sklearn.model_selection import GridSearchCV

# Define parameter grid for Random Forest
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20, 30]
}

# GridSearchCV for Random Forest
grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

# Get the best parameters and score
print("Best Parameters:", grid_search.best_params_)
print("Best Cross-Validation Score:", grid_search.best_score_)
```

---

### 7. **Conclusion**:

- Compare the performance of both models based on the metrics.
- Discuss the impact of data preprocessing and scaling.
- Reflect on the improvements seen with hyperparameter tuning.

---

### Optional Visualizations:

**ROC Curve**:

```python
from sklearn.metrics import roc_curve

# ROC curve for Random Forest
rf_probs = rf.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, rf_probs)

plt.plot(fpr, tpr, label='Random Forest')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.show()
```

---

### Key Libraries Used:
1. `pandas` for data handling
2. `scikit-learn` for model training, evaluation, and splitting
3. `matplotlib` and `seaborn` for visualizations

This approach gives a complete workflow to execute a classification model using scikit-learn, including data preprocessing, training, evaluation, and optional tuning.
