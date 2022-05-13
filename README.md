# Should This Loan Be Approved Or Denied: An Exploration Of Risk Classification Using U.S. Small Business Administration Loan Data

>Matt Holsten, Rob Pitkin\
Tufts University, Spring 2022\
CS-135 Machine Learning, Final Project



# Description
The U.S. Small Business Administration ("SBA") has created a large dataset of SBA-guaranteed loans stretching back almost 60 years which documents the information and outcomes of loans. Due to the nature of the SBA and the successes they've helped create, there is an ever-growing desire to have additional risk information for predicting whether or not a borrowing-business will default on their loan. 
\
\
To address this desire, we first employed a _feature analysis_ to discover which aspects of SBA-backed loans contribute most to the risk of defaulting. Then, we confirmed our analysis with two _classification_ methods used to predict the outcomes of loans before they are granted: one linear, _logistic regression model_ and one non-linear, _feed-forward neural network_. Lastly, we created a free, open source [API](https://matthewholsten.pythonanywhere.com/) and [web application](https://matthewholsten.github.io/sba-loan-risk-analysis-webapp/) to deploy our machine learning models. We find that there are 11 significant features which strongly indicate loan risk, with the loan term length having the highest correlation. We also find that both linear and non-linear models produce accuracies around $70\%$ and $80\%$ respectively, thereby demonstrating how our applications can serve as viable tools for SBA Loan Officers, lenders, and small businesses alike.
\
\
A full deep-dive and analysis of our findings can be seen in our formal, NeurIPS-inspired [report](https://github.com/MatthewHolsten/sba-loan-risk-analysis/blob/main/Report%2C%20Should%20This%20Loan%20Be%20Approved%20Or%20Denied%2C%20An%20Exploration%20Of%20Risk%20Classification%20Using%20US%20Small%20Business%20Administration%20Loan%20Data.pdf).

# Work


### 🌐  Web App
> https://matthewholsten.github.io/sba-loan-risk-analysis-webapp/

### 🤖  API
> https://matthewholsten.pythonanywhere.com/

### 📊  Machine Learning Model
> [Python Notebook on Google Colab (.ipynb)](https://colab.research.google.com/drive/1HVOS9IFwqiPWZ4yIHXls7a4HiP-RmNCM?usp=sharing)

### 📑  Report
> [Report, Should This Loan Be Approved Or Denied, An Exploration Of Risk Classification Using US Small Business Administration Loan Data.pdf](https://github.com/MatthewHolsten/sba-loan-risk-analysis/blob/a6212e0732338dc7ec98d1d3f250f6a7ce52fd19/Report,%20Should%20This%20Loan%20Be%20Approved%20Or%20Denied,%20An%20Exploration%20Of%20Risk%20Classification%20Using%20SBA%20Loan%20Data.pdf)

### 🎬  Presentation
> [YouTube Video (~16min)](https://youtu.be/1bDq9xMnCdc)

---
