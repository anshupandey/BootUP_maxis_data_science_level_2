import pandas as pd
import joblib

#load data
df = pd.read_excel(r"input_data.xlsx")

if df.shape[0]<1:
    print("the file is empty, please ensure that there is some data in the file input_data.xlsx")
else:
    df2 = df.copy()

    print("Loaded Data successfully")

    #load model
    model = joblib.load("churn_prediction.pkl")
    preprocessor = joblib.load("preprocessor.pkl")
    print("loaded the models successfully")

    ##########################################################################################################
    # preprocessing on data
    df['vmail_messages'] = pd.cut(df['Number vmail messages'],bins=[0,1,30,200],
                                 labels=['No VM plan','Normal Users','High Frequency users'],
                                 include_lowest=True)

    #Dropping the unwanted column
    df.drop(['Number vmail messages'],axis=1,inplace=True)

    df = df[['International plan', 'vmail_messages', 'Total day minutes',
           'Total eve minutes', 'Total night minutes', 'Total intl minutes',
           'Customer service calls']]
    # preprocessing data for onehotencoding
    df = preprocessor.transform(df)

    print("Done with the preprocessing part")

    ##########################################################################################################
    # getting the predictions
    predictions = model.predict(df)


    df2['predictions'] = predictions
    df2.to_csv("Results.csv")

    print("Exported the results")