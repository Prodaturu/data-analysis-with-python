import pandas as pd
import numpy as np
import plotly.express as px
# import plotly.graph_objects as go

#. Importing dataset into file
sharedData = pd.read_csv("project1/apple_products.csv")

#. Cleaning data
missing_data = sharedData.isnull().sum() #, check missing data
if missing_data.any():
    print("Warning: There is missing data in the following columns:")
    print(missing_data[missing_data > 0])
    print("Missing data can lead to inaccurate results. Consider cleaning the data before proceeding with the analysis.")
else:
    print("No missing data found, The data should be clean.") 

#. Sorting Data
#: Saving 10 most rated products  in a variable
most_rated = sharedData.sort_values(by = ["Number Of Ratings"], ascending= False).head(10)

#: Saving 10 highest rated products in a variable
highest_rated = sharedData.sort_values(by = ["Star Rating"], ascending = False).head(10)

#: The names of the top 10 rated products can be printed using the commented line below
# print(highest_rated["Product Name"])

#: Counting the number of times each product appears in the top rated list
unique_highest_rated = highest_rated['Product Name'].value_counts()

#: The product names will be used as the x-axis labels in the graph
x_label = unique_highest_rated.index

#: The number of Ratings will be used as the y-axis of graph-1.
highest_rated_ratings_count = highest_rated["Number Of Ratings"]

#: The number of Reviews will be used as the y-axis of graph-2.
highest_rated_reviews_count = highest_rated["Number Of Reviews"]

#* Bar Graph of "Name of Products" vs "Number of Ratings" for highest rated iphone's.
fig1 = px.bar(highest_rated, x = x_label, y=  highest_rated_ratings_count, title = "Ratings count for top 10 best rated iphone's")
fig1.show()

#* Bar Graph of "Name of Products" vs "Number of Reviews" for highest rated iphone's.
fig2 = px.bar(highest_rated, x = x_label, y= highest_rated_reviews_count, title = "Reviews count for top 10 best rated iphone's ")
fig2.show()

#* Scatter Plot of for "Number Of Ratings" vs "Sale price".
fig3 = px.scatter(data_frame=sharedData, x ="Number Of Ratings", y = "Sale Price", size = "Discount Percentage", trendline = "ols", title = "Sale price vs Num of Ratings")
fig3.show()

#* Scatter Plot of "Number of Ratings" vs "Discount Percentage"
fig4 = px.scatter(data_frame= sharedData, x = "Number of Ratings", y = "Discount Percentage", size = "Sale Price", trendline = "ols", title = "Discounts vs Num of Ratings")
fig4.show()
