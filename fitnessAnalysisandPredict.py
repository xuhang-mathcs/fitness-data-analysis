import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("fitness data.xlsx")

#print(df.head())
# print(df.columns)
# print(df.info())
# print(df.isnull().sum())    
clean_df = df.copy()
# clean_df["body weight"] = clean_df["body weight"].str.replace("kg","").astype(float) 
# clean_df["protein"] = clean_df["protein"].str.replace("g","").astype(float)
# clean_df["sleep hours (night)"] = clean_df["sleep hours (night)"].str.replace("h","").astype(float)
# clean_df["bench press"] = clean_df["bench press"].str.replace("kg","").astype(float)
# print(clean_df["body weight"])
# print(clean_df["body weight"].mean())

def clean_unit(series, unit):
    return (series.astype(str).str.replace(unit,"").astype(float))

clean_df["body weight"] = clean_unit(clean_df["body weight"],"kg")
clean_df["protein"] = clean_unit(clean_df["protein"],"g")
clean_df["sleep hours (night)"] = clean_unit(clean_df["sleep hours (night)"],"h")
clean_df["bench press"] = clean_unit(clean_df["bench press"],"kg")

# print(clean_df["bench press"])

plt.plot(clean_df["bench press"]) 
plt.show()