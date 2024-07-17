
# Assignment 2: Scikit-Learn and Data Visualization

## Scikit-Learn

### Summary of Scikit-Learn Tutorial for Beginners

**Scikit-Learn** is a powerful and user-friendly library for machine learning in Python. It provides a wide range of tools for building and evaluating models with ease.

### Basic Concepts and Functionalities

1. **Installation**:
   - Install Scikit-Learn using pip:

     ```bash
     pip install scikit-learn
     ```

2. **Core Components**:
   - **Estimators**: Scikit-Learn’s primary components include estimators, which are objects that implement methods such as `fit()`, `predict()`, and `score()`. These include classifiers, regressors, and clustering algorithms.
   - **Transformers**: These are used for preprocessing data. They implement methods like `fit()`, `transform()`, and `fit_transform()`, such as scaling and encoding features.

3. **Model Building**:
   - **Classification**: Implements various classification algorithms, including Logistic Regression, Support Vector Machines (SVM), and k-Nearest Neighbors (k-NN).

     ```python
     from sklearn.datasets import load_iris
     from sklearn.model_selection import train_test_split
     from sklearn.linear_model import LogisticRegression

     # Load dataset
     iris = load_iris()
     X = iris.data
     y = iris.target

     # Split dataset
     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

     # Train model
     model = LogisticRegression()
     model.fit(X_train, y_train)

     # Predict
     predictions = model.predict(X_test)
     ```

   - **Regression**: Supports algorithms like Linear Regression and Polynomial Regression for predicting continuous values.

     ```python
     from sklearn.linear_model import LinearRegression

     # Train model
     model = LinearRegression()
     model.fit(X_train, y_train)

     # Predict
     predictions = model.predict(X_test)
     ```

   - **Clustering**: Provides clustering algorithms such as k-Means and DBSCAN for grouping similar data points.

     ```python
     from sklearn.cluster import KMeans

     # Train model
     model = KMeans(n_clusters=3)
     model.fit(X)

     # Predict cluster labels
     labels = model.predict(X)
     ```

4. **Model Evaluation**:
   - **Metrics**: Evaluate models using metrics like accuracy, precision, recall, and F1-score for classification. For regression, use metrics like mean squared error (MSE) and R-squared.

     ```python
     from sklearn.metrics import classification_report

     # Evaluate model
     report = classification_report(y_test, predictions)
     ```

   - **Cross-Validation**: Use `cross_val_score` to assess model performance and avoid overfitting.

     ```python
     from sklearn.model_selection import cross_val_score

     # Cross-validation
     scores = cross_val_score(model, X, y, cv=5)
     ```

5. **Pipeline and Grid Search**:
   - **Pipeline**: Combine preprocessing steps and model training into a single workflow using `Pipeline`.

     ```python
     from sklearn.pipeline import Pipeline
     from sklearn.preprocessing import StandardScaler

     # Define pipeline
     pipeline = Pipeline([
         ('scaler', StandardScaler()),
         ('classifier', LogisticRegression())
     ])

     # Train model
     pipeline.fit(X_train, y_train)
     ```

   - **Grid Search**: Use `GridSearchCV` to find the best hyperparameters for your model.

     ```python
     from sklearn.model_selection import GridSearchCV

     # Define parameter grid
     param_grid = {'classifier__C': [0.1, 1, 10]}

     # Grid search
     grid_search = GridSearchCV(pipeline, param_grid)
     grid_search.fit(X_train, y_train)
     ```

## Matplotlib vs. Seaborn

### Matplotlib

**Matplotlib** is a comprehensive library for creating static, animated, and interactive visualizations in Python.

#### Strengths:
- **Flexibility**: Provides extensive customization options for plots, including colors, styles, and annotations. Ideal for detailed and varied plotting needs.
- **Wide Adoption**: Established library with extensive documentation and support.

#### Weaknesses:
- **Complexity**: Can be verbose and requires more code to create complex plots.
- **Default Aesthetics**: Basic plots may look less polished compared to other libraries without additional styling.

#### When to Use:
- When you need precise control over plot details and customization.
- For creating a wide variety of plots, including complex figures with multiple axes.

### Seaborn

**Seaborn** is a high-level interface built on top of Matplotlib, designed to simplify the creation of attractive and informative statistical graphics.

#### Strengths:
- **Ease of Use**: Simplifies complex visualizations with concise code and built-in themes.
- **Statistical Plots**: Provides advanced plots such as pair plots, violin plots, and heatmaps that are useful for statistical analysis.
- **Aesthetic Styles**: Comes with default themes and color palettes that enhance the visual appeal of plots.

#### Weaknesses:
- **Less Control**: Offers less fine-grained control over plot customization compared to Matplotlib.
- **Limited Scope**: Primarily focused on statistical graphics, which may not cover all visualization needs.

#### When to Use:
- When you want to quickly create visually appealing statistical plots with minimal code.
- For exploratory data analysis and visualizing relationships between variables.

### Comparison Summary

- **Matplotlib**: Best suited for users needing detailed control and customization of their visualizations. Ideal for creating complex plots and multiple-axis figures.
- **Seaborn**: Ideal for users who need to create attractive statistical plots quickly and with minimal code. Provides easy-to-use features for statistical analysis and visualization.
