import pandas as pd
import json 
with open("GenreData.json") as Jsondatafile:
    data1 = json.load(Jsondatafile)
    pan = pd.DataFrame(data1)
print(pan)