#QUESTION 1
# PLOTTING A LINE GRAPH OF TEMPERATURE READINGS OVER A WEEK: 20,22,19,23,21,24,20
import matplotlib.pyplot as plt
temperatures = [20, 22, 19, 23, 21, 24, 20]
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
plt.plot(days, temperatures, marker='o', linestyle='-', color='blue')
plt.title('Temperature Readings Over a Week')
plt.xlabel('Day')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()

#QUESTION 2
#ARITHMETIC SEQUENCE GENERATOR STARTING AT 5 WITH A COMMON DIFFERENCE OF 3 FOR 8 TERMS

a = 5
d = 3
n = 8
sequence = [a + i*d for i in range(n)]
print("Arithmetic sequence:", sequence)


#QUESTION 3
#CALCULATING VOLUME UNDER SURFACE Z = X**2 + Y**2 OVER THE SQUARE REGION 0<=X, Y<=1

import numpy as np

def z(x, y):
    return x**2 + y**2
a, b = 0, 1
N = 100 
dx = dy = (b - a) / N
x = np.linspace(a, b, N)
y = np.linspace(a, b, N)
X, Y = np.meshgrid(x, y)
Z = z(X, Y)
volume = np.sum(Z) * dx * dy
print("Approximate volume under the surface:", volume)


#QUESTION 4
#Differences between Compiled And Interpreted programming languages. Classify Python in this context

#Compiled Language
#Source code is converted directly into machine code by a compiler before execution
#Generally faster execution as the code is already translated
#Errors are caught during compilation
#Runs faster after compilation.
#Examples are C, C++, Rust

#Interpreted Language
#Source code is executed line by line by an interpreter at runtime
#Generally slower than compiled languages
#Easier to debug and test.
#Examples are Python and  JavaScript.
#Errors are caught during execution

#Python’s Classification
#Python is an interpreted language. However, it uses a hybrid approach
#Python code is first compiled to bytecode
#The bytecode is then interpreted by the Python Virtual Machine (PVM)
#This hybrid approach gives Python some benefits of both compiled and interpreted languages while maintaining its flexibility and ease of use.


