import pandas as pd 
json = pd.read_json("Intermediate/my_file.json")
print(json)
print(json.loc[0])
print(json["languages"])
dicJSON = json.to_dict()
print(dicJSON)

