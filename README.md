# Fitness Data Analysis and Calories Prediction
## Project Overview

    This project explores a gym workout dataset and builds machine learning models to predict the number of calories burned during exercise.
    The goal is to identify the factors that most strongly affect calorie consumption and compare the performance of different regression models.

## Dataset:
    gym_members_exercise_tracking.csv

## Target Variable:
    Calories_Burned

## Features include:
- Age
- Weight
- Height
- Avg_BPM
- Max_BPM
- Resting_BPM
- Session_Duration
- Workout_Frequency
- Water_Intake
- Experience_Level
- BMI
- Exploratory Data Analysis (EDA)

## The following analyses were performed:
- Dataset inspection with Pandas
- Summary statistics
- Correlation analysis
- Scatter plot visualization

## Key observation:
    Session_Duration has a very strong positive correlation with Calories_Burned.
 
## Machine Learning Models
    
    1. Linear Regression
    Used as the baseline model.
    Steps:
    Train/Test Split
    Model Training
    R² Evaluation
    Mean Absolute Error (MAE)
    
    2. Decision Tree Regressor
    Used to investigate non-linear relationships.
    Observation:
    Very high training score but much lower testing score.
    This indicates:
    Overfitting

    3. Random Forest Regressor
    Used to reduce overfitting found in Decision Trees.
    Observation:
    More stable than a single Decision Tree,
    but did not outperform the final Linear Regression model.

## Feature Engineering

    An interaction feature was created:

    Python
    Duration_Experience =
    Session_Duration * Experience_Level

## Purpose:

    To investigate whether training duration and
    experience level have interaction effects.


## Result:


    Only a small performance improvement was observed.

## Standardization

    All numerical features were standardized using:

    Python
    StandardScaler()

    This allows model coefficients to be compared on the same scale.


## Main findings:

    Session_Duration is the most important predictor of calorie consumption.

    Avg_BPM also contributes significantly to prediction performance.

    Linear Regression achieved the best balance between simplicity and generalization.

    Decision Tree suffered from overfitting.

    Random Forest reduced overfitting but did not surpass Linear Regression.

## Skills Used
- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Data Analysis
- Machine Learning
- Feature Engineering
- Model Evaluation
- What I Learned

## additional remarks:
    all the codes are written in python but some of them are in comment form, you can uncomment them to see the results