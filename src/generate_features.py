import pandas as pd
from sklearn.preprocessing import LabelEncoder

# read dataset file
df = pd.read_csv("../data/Android_Permission.csv", header=0, delimiter=',')

# Drop the columns which have a remarkable number of identic values.
dropper = []
for col in df.columns[10:]:
    if (df[col].value_counts()[0] > 28999 or df[col].value_counts()[0] < 1000):
        dropper.append(col)

df = df.drop(df[dropper], axis = 1)

# Drop Related apps column
df = df.drop(['Related apps'], axis = 1)

# Drop non-existent values
df = df.dropna()

# encoding Category column
le = LabelEncoder()
df['Category'] = le.fit_transform(df['Category'])

# encoding the rest of the text type columns using malign apps patterns
## nombre de majúscules entre les tres columnes
df['App_Upper'] = df['App'].apply(lambda message: sum(1 for c in str(message) if c.isupper()))
df['Pack_Upper'] = df['Package'].apply(lambda message: sum(1 for c in str(message) if c.isupper()))
df['Description_Upper'] = df['Description'].apply(lambda message: sum(1 for c in str(message) if c.isupper()))
## nombre de punts a 'Package'
df['Pack_Periods'] = df['Package'].apply(lambda message: sum(1 for c in str(message) if '.' in c))
## paraules com "free" o "better" en el nom
df['App_Free_Better'] = df['App'].str.contains('free|better').astype(int)
df = df.drop(['App'], axis = 1)
df = df.drop(['Package'], axis = 1)
df = df.drop(['Description'], axis = 1)

