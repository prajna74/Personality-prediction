# Personality-prediction
Big Five Personality of set of individuals is predicted by asking 25 questions to the user.

## Approach

Five characteristics of different individuals commonly known as big five characteristics namely, openness, neuroticism, conscientiousness, agreeableness and extraversion are stored in a dataset and used for training. Based on this training, the personality of individuals are predicted using data mining concepts. Before testing the dataset, it is pre-processed using different data mining concepts like handling missing values, data discretization, normalisation etc.This pre-processed data can then be used to classify/predict user personality based on past classifications. The system analyses user characteristics and behaviors. System then predicts new user personality based on personality data stored by classification of previous user data.
Model used to predict test dataset is “Multi class Logistic Regression” because Multi class  Logistic regression is an effective model to predict output class labels for dependent categorical data.

## Dataset Description

Attribute Description: No. of attributes are 7 as listed below.

1	Gender	            
2	Age	                
3	Openness	       
4	Neuroticism	       
5	Conscientiousness	
6	Agreeableness	    
7	Extraversion	  
 

## Class label description:

No. of class labels: 5 </br>
Type: Nominal </br>
Values: ● Extraverted ● Serious ● Responsible ● Lively ● dependable </br>
