import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn import preprocessing, linear_model
import tensorflow as tf
from tensorflow.keras.layers import Input, Dense, Activation,Dropout
from tensorflow.keras.models import Model
import numpy as np
from sklearn.metrics import mean_squared_error
lb = preprocessing.LabelEncoder()
sc = preprocessing.StandardScaler()
model = tf.keras.models.load_model("model.h5")
def train():
    df = pd.read_csv("store.csv", names = ["Name","light_intensity","current_temp","set_temp"])
    print(df.head())
    X = df[["Name","light_intensity","current_temp"]]
    y = df[["set_temp"]]
 
    lb.fit(X['Name'])
    transformed = lb.transform(X['Name'])
    transformed_name = pd.DataFrame(transformed)
    X= pd.concat([transformed_name,X], axis=1).drop(['Name'], axis =1)
    print(X)
    print(X.shape)
    print(y.head())
    
    sc.fit(X)
    X = sc.transform(X)
    

    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size =0.33)
    input_layer = Input(shape=(X.shape[1],))
    layer1 = Dense(100, activation='relu')(input_layer)
    layer2 = Dense(50, activation='relu')(layer1)
    layer3 = Dense(25, activation='relu')(layer2)
    output = Dense(1)(layer3)
    model = Model(inputs=input_layer, outputs=output)
    model.compile(loss="mean_squared_error" , optimizer="adam", metrics=["mean_squared_error"])
    model.fit(X_train, y_train, batch_size=10, epochs=5,validation_split=0.2)
    pred = model.predict(X_test)
    error = np.sqrt(mean_squared_error(y_test,pred))
    print(error)
    
    tf.keras.models.save_model(model,"model.h5",overwrite=True)
def predict_output(x):
    tmp =np.reshape(x[0],(1,-1))
    # print(tmp.shape)
    tmp = lb.transform(tmp)
    # print(tmp)
    x[0] =tmp[0]
    tmp =np.reshape(x,(1,-1))
    tmp = sc.transform(tmp)
    # print(tmp)
    x =tmp
    result = model.predict(x)
    print(result)
    return result[0][0]

if __name__ == '__main__':
    train()
    predict_output(np.array(["None",56,32]))