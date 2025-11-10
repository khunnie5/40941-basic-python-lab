from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns  # ถ้าไม่มี ให้ !pip install seaborn (สำหรับ Colab)
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

digits = datasets.load_digits()
X = digits.data      # ข้อมูลภาพ (n_samples, 64)
y = digits.target    # ป้ายกำกับ (0-9)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.1, random_state=42
)

print(X_train.shape)
print(X_test.shape)


model = LogisticRegression(max_iter=1500, solver='liblinear', multi_class='auto')
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"Accuracy = {acc:.4f}")
print(classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6,5))
sns.heatmap(cm, annot=True, fmt='d')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("True")
plt.show()
