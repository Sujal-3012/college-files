#you need a csv file for execution which is uploaded
import pandas as pd 
import matplotlib.pyplot as plt 

pdata = pd.read_csv('marks.csv')
print(pdata)

plt.plot(pdata['Range'] , pdata['CSE1'] , label = "CSE1")
plt.plot(pdata['Range'] , pdata['CSE2'] , label = "CSE1")
plt.legend()
plt.title("CSE marks distribution")
plt.xlabel("Marks cored by students")
plt.ylabel("Range of marks")
plt.show()
