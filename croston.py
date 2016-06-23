import numpy as np
import pandas as pd
import psycopg2
import matplotlib
from matplotlib import pyplot as plt

matplotlib.style.use('ggplot')

# connect to postgresql
connection = psycopg2.connect(database="frepple", user="minhphl", password="qweasd")

# open a cursor to perform db operations
cursor = connection.cursor()

# query: get all demand by date
query = "SELECT DATE(DUE), SUM(QUANTITY) FROM DEMAND GROUP BY DUE ORDER BY DUE ASC"
cursor.execute(query)
resultFromDB = cursor.fetchall()

# close connection
cursor.close()
connection.close()

# passing data to pandas' data structure

data = pd.DataFrame(resultFromDB, columns=["Date", "Quantity"])
data["Date"] = data["Date"].apply(pd.to_datetime)
data["Quantity"] = data["Quantity"].astype(np.int32)

print (data)
print (data.dtypes)

# plot original demand
data.plot(x="Date", y="Quantity")
plt.ylim(ymin=0)
plt.show()




