#Importing modules
import csv
import csv
import pandas as pd

#Loading and reading CSV
df = pd.read_csv("main.csv")

#Converting columns to lists
df['Radius']=df['Radius'].apply(lambda x: x.replace('$', '').replace(',', '')).astype("float")
radius = df['Radius'].to_list()
mass = df['Mass'].to_list()
gravity =[]

#Calculating gravity
def convert_to_si(radius,mass):
    for i in range(0,len(radius)-1):
        radius[i] = radius[i]*6.957e+8
        mass[i] = mass[i]*1.989e+30
        
convert_to_si(radius,mass)
def gravity_calculation(radius,mass):
    G = 6.674e-11
    for index in range(0,len(mass)):
        g= (mass[index]*G)/((radius[index])**2)
        gravity.append(g)
        
gravity_calculation(radius,mass)

#Making a new CSV
df.to_csv("final.csv")

