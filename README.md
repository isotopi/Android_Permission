# Pràctica Kaggle APC UAB 2021-22
### Name: Iker Soto Picon
### NIU: 1565939
### DATASET: Android Permission Dataset
### URL: [kaggle](https://www.kaggle.com/saurabhshahane/android-permission-dataset)

## Summary
This dataset named Android Permission Dataset contains information about some android apps with their permissions and it classifies those apps into benign(0) or malware(1).
It is composed of 29999 samples with 184 attributes. About 33.3% (10000) of the samples are benign apps. There are some text type samples which only one of them ('Category') is a categorical attribute. 

## Dataset objectives
The main objective is to classify apps into benign(0) or malware(1). Different experiments have been used to try to predict in which class pertains a given app.

## Experiments
In this project, 14 different models have been tested and ranked depending on its accuracy metric. The same experiment has been done with and without normalized data. With those results the top three models have been further studied and tuned as to search for optimum hyperparameters. While all of these have been done using pycaret library, these three same models have been tested using sklearn library as well. 

## Preprocessing
The following processing of the data was applied in this project:
 
 - As mentioned above, normalization of the data has been applied, however there was no significant difference on the results. 
 
 - For the text type columns, 'Category' attribute was encoded using Label Encoder, 'Related apps' was removed, and the rest of them were converted into numerical searching for common patterns which malware apps share. 
 
 - A large number of columns were eliminated as well due to the majority of identical values in the column. 
 
 - All non-existent values were dropped because there were only a few of them.
 
## Model
The best three models after tuning for the hyperparameter search are shown in the table below:

| |**Model** | **Hiperparametres** | **Accuracy** | **Temps** |
| -- | -- | -- | :--: | :--: |
| **lightgbm** | Light Gradient Boosting Machine | learning_rate=0.1 | 82% | 0.13s |
| **gbc** | Gradient Boosting Classifier | learning_rate=0.15, max_depth=7 | 81% | 0.96s |
| **rf** | Random Forest Classifier | max_depth=5, bootstrap=False | 80% | 0.70s |

## Demo
Demo contains an explanation on how to execute the respective files to clean and transform the data or train the model.

## Conclusions
After all the analysis and the results obtained, the following conclusions can be exposed:

 - There is no notable relation between attributes and the target 'Class'.
 - There is a higher number of malware apps than benign ones.
 - It has been possible to make different classification models for the dataset.
 - The worst models have been the Quadratic Discriminant Analysis and the SVM - Linear Kernel.
 - The best models have been the ones that impelements the gradient descens classification method.
 - Pycaret has produced better results than sklearn.
 - The best model has an accuracy of an 82%, which is rather acceptable.
 
## Ideas for the future
During the course of the project I have found how amusing it is to study something I use daily, android apps in this case. I look forward to explore resembling projects, for example one about Windows applications or something not so similar such as data about the actual people who downloaded malware apps and got their smartphone infected. I think this last one would be a very interesting topic to research.

## License
This project has been developed under the license [Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

