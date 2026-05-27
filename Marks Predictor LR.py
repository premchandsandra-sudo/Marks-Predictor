import seaborn as sns
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10]
y = [38,45,52,61,67,72,78,85,91,96]

def train():
  n = len(x)
  x_sum = sum(x)
  y_sum = sum(y)

  xy = sum([x[i]*y[i] for i in range(n)])
  square = sum([i*i for i in x])
  slope = (n*xy-sum(x)*sum(y))/(n*square-(sum(x))**2)

  b = (y_sum/n) - slope*(x_sum/n)

  return slope,b

def predict(slope,b,data):
  pred = slope*data+b
  if pred < 0: print(0)
  elif pred > 100: print(100)
  else: print(pred)

slope,b = train()
line = [slope*i + b for i in x]
data = int(input("Enter study hours: "))
predict(slope,b,data)

sns.scatterplot(x=x, y=y, s=100)
sns.lineplot(x=x, y=line)

plt.title("Linear Regression From Scratch")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()