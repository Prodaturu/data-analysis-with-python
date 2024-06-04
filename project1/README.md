# Project Description

## Overview
This project analyses a dataset of Apple products using Python and various libraries such as Pandas, NumPy, and Plotly. The dataset contains information about Apple products including their names, ratings, reviews, sale prices, discount percentages, and other attributes.

## Steps
1. **Importing Data**: The dataset (`apple_products.csv`) is imported into a Pandas DataFrame named `sharedData`.

2. **Data Cleaning**: Missing data is checked using `isnull()` function, and if any missing data is found, a warning message is printed. Otherwise, a message indicating clean data is printed.

3. **Sorting Data**:
   - The top 10 most rated and top 10 highest rated products are extracted and stored in variables `most_rated` and `highest_rated` respectively.
   - Number of times each product appears in the highest rated list is counted and stored in `unique_highest_rated`.

4. **Visualization**:
   - Two bar graphs are created using Plotly Express (`px`) library to visualize:
     - Number of ratings for the top 10 best-rated iPhones (`fig1`).
     - Number of reviews for the top 10 best-rated iPhones (`fig2`).
   - Two scatter plots are created to visualize:
     - The relationship between the number of ratings and the sale price (`fig3`).
     - The relationship between the number of ratings and the discount percentage (`fig4`).
   
5. **Displaying Graphs**: Each graph is displayed using the `show()` method.

## Files
- `apple_products.csv`: Dataset containing information about Apple products.
- `analysis.py`: Python script containing the analysis code.
- `README.md`: Documentation providing an overview of the project, steps involved, and file descriptions.

## How to Use
1. Ensure Python and required libraries are pre-installed.
2. Place the dataset file (`apple_products.csv`) in the same directory as `analysis.py`.
3. Run the `analysis.py` script.
4. View the generated graphs to analyze the data visually.
