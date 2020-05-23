import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import load_boston
boston=load_boston()
print(bos.DESCR)

#access data attributes
dataset=boston.data
for name, index in enumerate(boston.feature_names):
    print(index,name)
    
#reshaping data
data=dataset[:,12].reshape(-1,1)

#shape of data
np.shape(dataset)

#target values
target=boston.target.reshape(-1,1)
np.shape(target)

#ensuring matplotlib is working inside the notebook
%matplotlib inline
plt.scatter(data, target, color='c')
plt.xlabel('Lower income population')
plt.ylabel('Cost of House')
plt.show()

#regression
from sklearn.linear_model import LinearRegression

#creating a regression model
reg=LinearRegression()

#fitting the model
reg.fit(data,target)

#prediction
pred=reg.predict(data)

#ensuring matplotlib is working inside the notebook
%matplotlib inline
plt.scatter(data, target, color='c')
plt.xlabel('Lower income population')
plt.ylabel('Cost of House')
plt.plot(data,pred,color='r')
plt.show()

#circumventing curve issue using polynomial model
from sklearn.preprocessing import PolynomialFeatures

#to allow merging of models
from sklearn.pipeline import make_pipeline
model=make_pipeline(PolynomialFeatures(3),reg)
model.fit(data,target)

pred=model.predict(data)
#ensuring matplotlib is working inside the notebook
%matplotlib inline
plt.scatter(data, target, color='c')
plt.xlabel('Lower income population')
plt.ylabel('Cost of House')
plt.plot(data,pred,color='r')
plt.show()

#r_2 metric
from sklearn.metrics import r2_score

#predict
r2_score(pred,target)

output= 0.4798911810275662
