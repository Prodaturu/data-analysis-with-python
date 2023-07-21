# Tobacco Usage Analysis in India

This project aims to analyze the trend of tobacco usage in different states and union territories of India. The analysis is divided into two main categories: Rural and Urban areas. The data used for this project is stored in a CSV file named 'datafile.csv'.

## Libraries Used

- numpy
- pandas
- matplotlib
- seaborn

## Data Loading and Preprocessing

The data is loaded into a pandas DataFrame from a CSV file. Basic statistics of the data are generated using the `describe()` function. The DataFrame is checked for missing values.

In the dataset, it was found that the 'West Bengal' state was missing an 'Area' value. Upon further inspection, it was found that the entire 'Rural' row was missing for 'West Bengal'. For the purpose of this analysis, 'West Bengal' was dropped from the dataset.

## Analysis

The analysis focuses on the comparison of 'Ever tobacco users (%)' and 'Current tobacco users (%)' in both 'Rural' and 'Urban' areas of each state/UT.

## Visualization

The results of the analysis are visualized using bar plots and scatter plots. The bar plot shows the percentage of 'Ever tobacco users' in each state, divided by area (Rural or Urban). The scatter plots show the relationship between 'Ever tobacco users (%)' and 'Current tobacco users (%)', with one plot showing a linear regression line and the other showing a polynomial regression line.

## How to Run

To run this project, you will need to have Python installed on your machine along with the libraries mentioned above. You can then run the `.ipynb` file using Jupyter Notebook.

## Note

This is a basic analysis and there are many other factors that could be considered. The data used in this project is assumed to be the only data available. In a real-world scenario, missing data would ideally be filled in from a reliable source if available.
