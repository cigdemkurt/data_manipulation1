import pandas as pd
road_file= 'SuperMarketAnalysis.csv'

my_data=pd.read_csv(road_file)

#the_best_rating= my_data.loc[my_data['Rating'].idxmax()]

#print(f'the branch that has the highest rating: {the_best_rating['Branch']}- Rating: {the_best_rating['Rating']}')

# the branch that has the highest rating: Giza- Rating: 10.0

#print(f'the product line that has the most rating: {the_best_rating['Product line']}- Rating: {the_best_rating['Rating']}')

#the product line that has the most rating: Sports and travel- Rating: 10.0

rating_counts= my_data.groupby(['Product line', 'Gender']).size().unstack(fill_value=0)

most_voted_product_line = rating_counts.sum(axis=1).idxmax()
most_voted_gender = rating_counts.loc[most_voted_product_line].idxmax()


print(f"The most voted product line: {most_voted_product_line}")
print(f"The gender that gives these votes: {most_voted_gender}")

#The most voted product line: Fashion accessories
#The gender that gives these votes: Female

