import pandas as pd
import json 
with open("GenreData.json") as Jsondatafile:
    data1 = json.load(Jsondatafile)
    pan = pd.DataFrame(data1)
#Using the pandas to display the items.
for genre in data1["genres"]:
    print(genre["name"])
    print(genre["description"])
#We can also use json module to display the items.
for genre1 in data1["genres"]:
    print(genre1["name"])