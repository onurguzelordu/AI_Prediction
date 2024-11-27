import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import LabelEncoder


dyolu = 'C:\MS_Model\havadurumu_egit_4.csv'
dyolu1 = 'C:\MS_Model\hava_durumu_test4.csv'

df_train = pd.read_csv(dyolu, encoding='utf-8')
df_test = pd.read_csv(dyolu1, encoding='utf-8')

# One-hot encode Countries (Bu işlemi bir kere yapmak yeterli)

df_train = pd.get_dummies(df_train, columns=['Countries'])
df_test = pd.get_dummies(df_test, columns=['Countries'])


X_train = df_train.drop('Predicted_Tomorrow_T', axis=1)
y_train = df_train['Predicted_Tomorrow_T']

X_test = df_test.drop('Predicted_Tomorrow_T', axis=1)
y_test = df_test['Predicted_Tomorrow_T']

# Eksik değerleri doldurma
imputer = SimpleImputer(strategy='most_frequent')
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


# Tahmin yapma
# y_pred = model.predict(X_test_imputed)

# Sütunun varlığını kontrol ederek yazdırma
# try:
#     print(df_train['Countries'].head())
# except KeyError:
#     print("'Countries' sütunu bulunamadı.")













# # Tahminleri yeni sütuna ata
# df_train['Predicted_Tomorrow_T'] = y_pred

# # Tahminleri bir DataFrame'e dönüştürme
# predictions_df = pd.DataFrame(y_pred, columns=['Predicted_T'])

# # Tahminleri CSV dosyasına yazma
# predictions_df.to_csv('Predicted_Tomorrow_T.csv', index=False)

# print("Tahminler 'Predicted_Tomorrow_T.csv' dosyasına kaydedildi.")

# # Test verileri ve tahminleri birleştirme
# results_df = X_test.copy()
# results_df['Actual_T'] = y_test
# results_df['Predicted_T'] = y_pred

# # Sonuçları CSV dosyasına yazma
# results_df.to_csv('Predicted_Tomorrow_T.csv', index=False)

# print("Tahminler ve test verileri 'Predicted_Tomorrow_T.csv' dosyasına kaydedildi.")













# ---- Tahmin yaptıktan sonra aşağıya inilmeli.------------------------------------

# # Performans metriklerini hesaplama
# mse = mean_squared_error(y_test, y_pred)
# rmse = np.sqrt(mse)
# mae = mean_absolute_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)

# print("MSE:", mse)
# print("RMSE:", rmse)
# print("MAE:", mae)
# print("R-squared:", r2)


# # Gerçek ve tahmin edilen değerleri karşılaştırma grafiği
# plt.figure(figsize=(10, 6))
# plt.scatter(y_test, y_pred)
# plt.xlabel('Gerçek Sıcaklık')
# plt.ylabel('Tahmin Edilen Sıcaklık')
# plt.title('Gerçek vs. Tahmin Edilen Sıcaklık')
# plt.grid(True)
# plt.show()


# # Hata dağılımını inceleme (Residual Plot)
# sns.residplot(x=y_test, y=y_pred, lowess=True)
# plt.xlabel('Gerçek Sıcaklık')
# plt.ylabel('Hatalar')
# plt.title('Residual Plot')
# plt.show()


#  Özellik önemlerini inceleme
# importances = model.feature_importances_
# features = X_train.columns
# indices = np.argsort(importances)

# plt.figure(figsize=(12,8))
# plt.title("Özellik Önemleri")
# plt.barh(range(len(indices)), importances[indices], color='b', align='center')
# plt.yticks(range(len(indices)), [features[i] for i in indices])
# plt.xlabel('Önem')
# plt.ylabel('Özellik')
# plt.show()









