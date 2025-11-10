#testing #2
# โหลดข้อมูล & แสดงภาพเดี่ยว
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt

digits = datasets.load_digits()
X = digits.data
y = digits.target
# plt.imshow(np.reshape(X[1], (8, 8)), cmap='gray')
# plt.title(f"label = {y[1]}")
# plt.axis('off'); plt.show()

# แบ่งข้อมูล & ฝึกโมเดล
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
print("Accuracy:", accuracy_score(y_test, model.predict(X_test)))

y_pred = model.predict(X_test)

print(classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6,5))
sns.heatmap(cm, annot=True, fmt='d')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("True")
plt.show()