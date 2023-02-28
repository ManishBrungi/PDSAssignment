# Importing the necessary libraries
import pandas as pd

# Reading the raw_people_data csv file
raw_people_data = pd.read_csv("D:\\PDS\\raw_people_data.csv")

# Viewing the raw_people_data
print(raw_people_data)
print(raw_people_data.columns)

# Removing the rows where Age is less than 30 using the subset function
clean_people_data = raw_people_data[raw_people_data["Age"] > 30]

# Viewing clean_data
print(clean_people_data)

# Writing clean data into a new csv file and not messing with the original file
clean_people_data.to_csv("D:\\PDS\\clean_people_data.csv", index=False)
