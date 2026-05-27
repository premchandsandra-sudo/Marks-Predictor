import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

x = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
y = [[38],[45],[52],[61],[67],[72],[78],[85],[91],[96]]

xtrain, xtest, ytrain, ytest = train_test_split(
    x, y, test_size=0.2, random_state=0
)

model = LinearRegression()
model.fit(xtrain, ytrain)
ypred = model.predict(xtest)
line = model.predict(x)

x_values = [i[0] for i in x]
y_values = [i[0] for i in y]
line_values = [i[0] for i in line]

custom_input = int(input("Enter study hours: "))
prediction = model.predict([[custom_input]])
print("Predicted Score:", prediction[0])

sns.scatterplot(x=x_values, y=y_values, s=100)
sns.lineplot(x=x_values, y=line_values)

plt.title("Linear Regression with Scikit-Learn")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()