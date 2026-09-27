import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import StandardScaler
df = pd.read_csv("gym_members_exercise_tracking.csv")

# print(df.columns)
# print(df.info())

# print(df.describe())

# plt.scatter(df["Calories_Burned"],df["Session_Duration (hours)"])
# plt.xlabel("Calories Burned")
# plt.ylabel("Session Duration (hours)")
# plt.show()




# print(df[["Session_Duration (hours)","Calories_Burned"]].corr())
# relation
# print(df.corr(numeric_only=True)["Calories_Burned"])

# df["Calories_Burned_perhour"] = df["Calories_Burned"] / df["Session_Duration (hours)"]
# print(df.groupby("Workout_Type")["Calories_Burned_perhour"].mean())
  
model = LinearRegression()
# model = DecisionTreeRegressor()
# model = RandomForestRegressor()

# find the interconnection between the variables
df["Duration_Experience"] = df["Session_Duration (hours)"] * df["Experience_Level"]



# X = df[["Duration_Experience","Session_Duration (hours)","Experience_Level","Workout_Frequency (days/week)","Water_Intake (liters)"]]
# X = df[["Session_Duration (hours)"]]
# standardscaler
X = df.select_dtypes(include = "number").drop(columns = ["Calories_Burned"])            
scaler = StandardScaler()                                                                                  
X_scaled = scaler.fit_transform(X)

y = df["Calories_Burned"]
# model.fit(X,y)
# print(model.coef_)
# print(model.intercept_)

X_train,X_test,y_train,y_test = train_test_split(X_scaled,y,test_size = 0.2,random_state = 19)
model.fit(X_train,y_train)

# analyse the difference under linear regression
# y_pred = model.predict(X_test)
# plt.scatter(y_test,y_pred)
# plt.plot([y_test.min(),y_test.max()],[y_test.min(),y_test.max()],color = "red")
# plt.xlabel("Actual")
# plt.ylabel("Predicted")
# plt.show()

# print(mean_absolute_error(y_test,y_pred))


print("train",model.score(X_train,y_train))
print("test",model.score(X_test,y_test))

for name, coef in zip(X.columns, model.coef_):
    print(name, coef)

print(df[["Session_Duration (hours)","Avg_BPM","Calories_Burned"]].corr())


