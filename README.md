# End-to-End Loan-prediction Model with deployment on heroku
The loan prediction model actually predicts whether a loan will be approved or not on the applicant's profile/info

## Model preprocessing
In this Model, i have applied the preprocessing techniques as follows:
1. Hypothesis generation before model builting: It come from the domian knowledge..I actually chosen some key points that we face while applying for any loan in Bank
2. Uni and Bivariate Analysis: By visualising insights and trends of the features with target help us in future while feature selection and outlier treatment.
3. Data Cleaning: Missing value Treatment by mode or median and Outlier Removal by percentile or boxplot method.
4. Feature Engineering: Add/removal of features by visualising correlation using heatmap or pairplot and also multicollinarity can be checked that would bias our model and confuse gradient descent also.
5. Standardisation: It actually makes our population/data into standard normal(Gaussian) distribution..instead our data if right skewed using log transformation we can convert it into normal distribution...standardisation means mean=0 & standard deviation=1
6. Principle components analysis: Best method for model selection before going to any ML algorithm.
7. Model Building: By chosing different ML algo's and checking the training and validation accuracy we can best select the model.
8. Imbalance Dataset handling: If our dataset is imbalance then it would bias towards some data may lead to incorrect result..it can effectively handled using smote as oversampling technique and Ensemble with undersampling.
9. Model performace: If our model has high bias and very low Variance >6%...model is overfitting and is both bias and variance are low then underfitting
10. Validation Technique: To deal with overfitting and imbalance dataset **bold**StratifiedKFold  is efficient.
11. Feature engineering: It's better to add any features for improving model performance on them..addition of new features based on hypothesis generated before..
12. Model Selection: I have applied LogisticRegression , DecisionTreeClassifier , RandomForestClassifier, SVC, Naive bayes,  XGBoost, KNN, 
13. Performance improvement by using hyper-parameter optimisation..and Select the Model..I have chosen Logistic Regression coz, it's giving better accuracy.

## Tools Used-
1. Python - 3.9.
2. Google Colab - for analysis.
3. Pycharm - for streamlit webapp builting.
4. Heroku - for deployment.

 ## Dataset- 
 From Kaggle i got the dataset

 ## Libraries Used -
 1. Pandas -   1.2.4
 2. Numpy -    1.20.4
 3. Matplotlib- 3.3.4
 4. Seaborn    - 0.11.0
 5. Scikit-learn- 0.24.1
 6. Streamlit-    0.88.0 
 
 ## Classifiers Used: 
 1. Logistic Regression      --> 
 2. Polynomial Regression    -->
 3. Decision Tree classifier -->
 4. Random Forest classifier -->
 5. Support vector classifier-->
 6. KNN                      -->
 7. Naive Bayes              -->

# Deployment -
Heroku Deployment through GitHub : <font color='Purple'> "Below is the loan-prediction-webapp Link"
	


