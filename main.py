import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')
study_time_min = data['StudyTime'].min()
study_time_max = data['StudyTime'].max()

print("Study Time Range:", study_time_min, "to", study_time_max)

# print(data)

# plt.scatter(data.StudyTime, data.Marks) # plotting where x is the study time and y is the marks
# plt.show() # seeing the scatter plot 

def loss_function(m,b,points):
    total_error = 0
    for i in range(len(points)):
        x = points.iloc[i].StudyTime
        y = points.iloc[i].Marks
        total_error += ((m*x + b) - y)**2
    plt.plot(x,total_error / float(2*len(points)))
    plt.show()
    return total_error / float(2*len(points))

def gradient_descent(m_now, b_now, points, learning_rate):
    m_gradient = 0
    b_gradient = 0

    n = len(points)

    for i in range(n):
        x = points.iloc[i].StudyTime
        y = points.iloc[i].Marks

        m_gradient += (1/n*((m_now*x + b_now) - y)) * x
        b_gradient += (1/n*((m_now*x + b_now) - y))

    m = m_now - learning_rate*m_gradient
    b = b_now - learning_rate*b_gradient

    return m,b
    
m = 0
b = 0
learning_rate = 0.0001
iterations = 1000

error = loss_function(m,b,data)

for i in range(iterations):
    if i % 50 == 0:
        print (f"iteration : {i}")

    m,b = gradient_descent(m, b, data, learning_rate)

print(f"y = {m}x + {b}")

plt.scatter(data.StudyTime, data.Marks, color = "black")
plt.plot(list(range(0, 10)),[m * x + b for x in range(0, 10)], color = "red")
plt.xlabel("Study Time")
plt.ylabel("Marks")
plt.title("Scatter Plot with Linear Regression Line")
plt.show()

    








