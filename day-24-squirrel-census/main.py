import pandas

PRIMARY_FOUR_COLOR = "Primary Fur Color"
COLUMNS = {
    "": 'Count'
}

squirrel_census_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

squirrel_count_by_color = squirrel_census_data.groupby(PRIMARY_FOUR_COLOR)[PRIMARY_FOUR_COLOR].count()
print(squirrel_count_by_color.rename(COLUMNS))
squirrel_count_by_color.to_csv("squirrel_count_by_color.csv")
