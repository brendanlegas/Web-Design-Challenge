import pandas as pd 
from IPython.display import HTML

cities = pd.read_csv("cities.csv")
print(cities.head())

data = cities.to_html(classes='table table-striped table-hover')

text_file = open("table.html", "w")
text_file.write(data)
text_file.close()


