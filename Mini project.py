#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas as pd
import plotly.express as px

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("PS_20174392719_1491204439457_log.csv")


# In[29]:


#Visualizing data 
fig= px.pie(df, names='type', color_discrete_sequence=px.colors.sequential.RdBu)

fig.show()


# In[30]:


#Spliting data and training the model

X = df.drop(['isFraud', 'isFlaggedFraud', 'nameOrig', 'nameDest'], axis=1)

X = pd.get_dummies(X, columns=['type'], drop_first=True)

y = df['isFraud']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)


# In[31]:


#Testing 

# step, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest, type_CASH_OUT, type_DEBIT, type_PAYMENT,  type_TRANSFER
example = [[ 4,   13707.11, 13707.11, 0, 0, 0, 0, 0, 0, 1]] 
predicted_fraud = model.predict(example)
accuracy = model.score(X_test, y_test)

fraud_status = "Fraud" if predicted_fraud[0] == 1 else "Not Fraud"
print("Predicted Transaction Status:", fraud_status)
print("Accuracy:", accuracy)


# In[ ]:




