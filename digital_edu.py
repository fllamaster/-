#создай здесь свой индивидуальный проект!
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
df = pd.read_csv('train.csv')

df.drop(['id','bdate', 'has_photo', 'has_mobile', 'followers_count', 'graduation', 'last_seen','career_start', 'career_end', 'life_main', 'city', 'people_main', 'occupation_name'], axis = 1, inplace = True)

def edu_status_apply(edu_status):
    if edu_status == 'Undegraduate applicant':
        return 0
    if edu_status == 'Student (Specialist)' or edu_status == 'Student (Bachelor`s)' or edu_status == 'Student (Master`s)':
        return 1
    if edu_status == 'Alums (Master`s)' or edu_status == 'Alumnus (Specialist)' or edu_status == 'Alumnus (Bachelor`s)':
        return 2
    if edu_status == 'PhD' or edu_status == 'Candidate of Sciences':
        return 3

def edu_form_apply(edu_form):
    if edu_form == 'Full-time':
        return 0
    if edu_form == 'Distance Learning':
        return 1
    if edu_form == 'Part-time':
        return 2

def occupation_type_apply(occupation_type):
    if occupation_type == 'university':
        return 0
    if occupation_type == 'work':
        return 1

def split_langs(langs):
    return langs.split(';')
df['langs'] = df['langs'].apply(split_langs)
df['langs'] = df['langs'].apply(len)

df['edu_status'] = df['edu_status'].apply(edu_status_apply)
df['edu_form'] = df['edu_form'].apply(edu_form_apply)
df['occupation_type'] = df['occupation_type'].apply(occupation_type_apply)
df.info()

X = df.drop('result', axis = 1) 
y = df['result'] 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25) 

sc = StandardScaler() 
X_train = sc.fit_transform(X_train) 
X_test = sc.transform(X_test) 
  
classifier = KNeighborsClassifier(n_neighbors = 5) 
classifier.fit(X_train, y_train) 
  
y_pred = classifier.predict(X_test)
print('Процент правильно предсказанных исходов:', round(accuracy_score(y_test, y_pred) * 100, 2))

#print(df['occupation_type'].value_counts())
