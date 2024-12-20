
import pandas as pd
df = pd.read_csv('dataset_traffic_accident_prediction1.csv')
df

df[df['Weather']=='Clear']

df[df['Weather']!='Clear']

df[df['Weather'].isin(['Rainy','Foggy'])]

df = pd.DataFrame({'Speed_Limit' : df['Speed_Limit']})
df.to_csv('out.csv', index=False)

import numpy as np
age_male = np.random.uniform(low=20, high=30, size=(1,50)).flatten()
age_female = np.random.uniform(low=20, high=30, size=(1,50)).flatten()
df = pd.DataFrame({"age_female": age_female, "age_male": age_male})
df.to_csv('out.csv', index=False)

import plotly.express as px
df = pd.read_csv('dataset_traffic_accident_prediction1.csv')
fig = px.line(df, x="Speed_Limit", y="Driver_Age", color='Driver_Experience')
fig.show()

partial = df[df['Vehicle_Type'].isin(['Car', 'Truck'])]
fig = px.line(partial, x="Driver_Experience", y="Driver_Age", color='Vehicle_Type')
fig.show()

import plotly.express as px
df = pd.read_csv('iris.csv')
df
fig = px.scatter_3d(df, x='Sepal Length (cm)', y= 'Sepal Width (cm)', z = "Petal Width (cm)", color = "Species")
fig.show()

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras import layers, models

df = pd.read_csv('alarms.csv')
fig = px.scatter_3d(df, x= 'sound', y='visibility', z='alarm')
fig.show()

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras import layers, models


df = pd.read_csv('alarms.csv')
fig = px.scatter_3d(df, x= 'sound', y='distance', z='alarm')
fig.show()


X= df[['sound', 'distance', 'visibility']].values
y= df['alarm'].values


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)


model = models.Sequential([
    layers.Dense(1, input_shape = (X_train.shape[1],), activation='sigmoid')
])

model.compile(optimizer = 'adam', loss = 'mean_squared_error', metrics = ['mse'])



model.fit(X_train, y_train, epochs =50, batch_size =32, validation_data=(X_test, y_test))


loss, accuracy = model.evaluate(X_test, y_test)
print("Test Loss:", loss)
print("Test Accuracy:", accuracy)

new_data = np.array([
    [0.7,0.1, 0.7],
    [0.3, 0.7, 0.3],
    [0.4, 0.5, 0.3],
    [0.6, 0.5, 0.7],
    [0.9, 0.1, 0.9],
])

predictions = model.predict(new_data)
print("Predictions:")
print(predictions)

