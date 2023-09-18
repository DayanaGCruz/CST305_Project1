# Dayana Gonzalez Cruz 
# CST-305 Principles of Modeling
# WF1100A Citro
# Project 1
# The objective of this program is solve and model Amdahl's Law by defining it as a recursive function in python. 

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import scipy

# Define Amdahl's Law where:
# f is portion of instructions/system that is parallelizable 
# n is the number of processors

def amdahls(f, n):
	if(n == 800):	
		speedup.append(1/((1-f)+f/n))
		return
	speedup.append(1/((1-f)+f/n))
	n += 1
	amdahls(f, n)
	
# Initial Values
# Suggested: 1
f = float(input("Please enter initial value (double) for parallelization factor, f (e.g. 0.95): "))
# Suggested: 0.95
n0 = int(input("Please enter initial value (integer) for number of processors, n (e.g. 1): "))
speedup = []

amdahls(f, n0)

# Plot solutions 
plt.plot(speedup)
plt.title('Amdahls Law')
plt.xlabel('Number of Processors')
plt.ylabel('Speedup')
plt.show()

