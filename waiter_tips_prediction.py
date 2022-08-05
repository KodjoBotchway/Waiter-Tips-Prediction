# import necessary packages and modules
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import sweetviz as sv
import seaborn as sns

# read in dataset
data = pd.read_csv("data/tips.csv")
data.describe()
sv.analyze(data).show_html('data.html')
#profile = ProfileReport(data)
#profile.to_file('Output.html')

# showing the spread of bills to the tips wrt the day
figure = px.scatter(data_frame = data,x = "total_bill",
                   y = "tip",color ="day",
                    size="size",trendline="ols")
figure.show()

# showing the distribution tips wrt the sex, the day and the time
figure = px.pie(data,values= "tip",names='day',hole=0.5)
figure.show()

figure = px.pie(data,values="tip",names ='sex' ,hole=0.5)
figure.show()

figure = px.pie(data, 
             values='tip', 
             names='time',hole = 0.5)
figure.show()

# converting the categorical to numeric
from sklearn import preprocessing
le = preprocessing.LabelEncoder()
# use "list(le.classes_)" after encoding to get the mappings starting from 0
data["sex"] = le.fit_transform(data['sex'])
data["smoker"] = le.fit_transform(data['smoker'])
data["day"] = le.fit_transform(data['day'])
data["time"] = le.fit_transform(data['time'])
data.head()

x = np.array(data[["total_bill", "sex", "smoker", "day", 
                   "time", "size"]])
y = np.array(data["tip"])

# splitting the data into testing and training data
from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(x, y, 
                                                test_size=0.3, 
                                                random_state=1)

# model building
# using linear regression
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(xtrain, ytrain)
# random forest
from sklearn.ensemble import RandomForestRegressor
model2 = RandomForestRegressor()
model2.fit(xtrain, ytrain)

# testing against the testing data
ypred = model.predict(xtest)
ypred2 = model2.predict(xtest)

# testing accuracy
from sklearn.metrics import r2_score
print("Linear")
#print("Mean absolute error: %.2f" % np.mean(np.absolute(ypred - ytest)))
#print("Residual sum of squares (MSE): %.2f" % np.mean((ypred - ytest) ** 2))
print("R2-score: %.2f" % r2_score(ytest , ypred))

print("Random Forest")
print("R2-score: %.2f" % r2_score(ytest , ypred2))

#### features = [[total_bill, "sex", "smoker", "day", "time", "size"]]
features = np.array([[24.50, 1, 0, 0, 1, 4]])
model2.predict(features)