import joblib
import pandas as pd
import sys

model = joblib.load("model.pkl")
pipeline = joblib.load("pipeline.pkl")

filename = sys.argv[1]

df = pd.read_excel(filename)
print("#*****************# loaded file successfully")

df['vmail_messages'] = pd.cut(df['Number vmail messages'],bins=[0,1,30,200],
                             labels=['No VM plan','Normal Users','High Frequency users'],
                             include_lowest=True)
df2 = df[['International plan','vmail_messages','Total day minutes','Total eve minutes',
     'Total night minutes','Total intl minutes','Customer service calls']]
df2 = pipeline.transform(df2)


df['Predictions'] = model.predict(df2)
print("#*****************# Done with predictions")


df.to_excel("output_file.xlsx")
print("#*****************# Exported output file at current location as output_file.xlsx")

