import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.preprocessing   import LabelEncoder, OneHotEncoder

# Veri yükleme
dyolu = 'C:\MS_Model\havadurumu_egit_4.csv'
dyolu1 = 'C:\MS_Model\hava_durumu_test4.csv'

df_train = pd.read_csv(dyolu, encoding='utf-8')
df_test = pd.read_csv(dyolu1, encoding='utf-8')

# Kategorik verileri one-hot encoding ile dönüştürme
categorical_cols = ['Countries']  # Dönüştürülecek sütunları buraya ekleyin
encoder = OneHotEncoder()
encoded_features = encoder.fit_transform(df_train[categorical_cols])
encoded_features = encoded_features.toarray()

# One-hot encoded verileri orijinal veri çerçevesine ekleme
df_train = pd.concat([df_train.drop(categorical_cols, axis=1), pd.DataFrame(encoded_features)], axis=1)
df_test = pd.concat([df_test.drop(categorical_cols, axis=1), pd.DataFrame(encoder.transform(df_test[categorical_cols]))], axis=1)

# Eksik değerleri doldurma (sayısal sütunlar için)
numerical_cols = ['']  # Sayısal sütunların isimlerini buraya ekleyin
imputer = SimpleImputer(strategy='median')
df_train[numerical_cols] = imputer.fit_transform(df_train[numerical_cols])
df_test[numerical_cols] = imputer.transform(df_test[numerical_cols])

# Özellik ve hedef değişkenlerin belirlenmesi
X_train = df_train.drop('Predicted_Tomorrow_T', axis=1)
y_train = df_train['Predicted_Tomorrow_T']
X_test = df_test.drop('Predicted_Tomorrow_T', axis=1)
y_test = df_test['Predicted_Tomorrow_T']

# Özellik ve hedef değişkenlerin belirlenmesi
X_train = df_train.drop('Predicted_Tomorrow_T', axis=1)
y_train = df_train['Predicted_Tomorrow_T']

X_test = df_test.drop('Predicted_Tomorrow_T', axis=1)
y_test = df_test['Predicted_Tomorrow_T']

# Eksik değerleri doldurma
imputer = SimpleImputer(strategy='median')
X_train_imputed = imputer.fit_transform(X_train)
X_test_imputed = imputer.transform(X_test)

# Model eğitimi (hata kontrolü)
try:
    model = RandomForestRegressor()
    model.fit(X_train_imputed, y_train)
except Exception as e:
    print(f"Model eğitimi sırasında hata oluştu: {e}")
else:
    print("Model başarıyla eğitildi!")
