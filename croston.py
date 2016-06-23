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

# create partial calendar
data = pd.DataFrame(resultFromDB, columns=["Date", "Quantity"])
data["Date"] = data["Date"].apply(pd.to_datetime)
data["Quantity"] = data["Quantity"].astype(np.float32)

# create full range calendar
range = pd.date_range(data["Date"].iloc[0], data["Date"].iloc[-1]).tolist()

# add column "Quantity" = 0 to dataframe
demand = pd.DataFrame(range, columns=["Date"])
demand["Quantity"] = np.float32(0.)

# merge data tu db
frame = [data, demand]
demand.combine_first(data)
demand.update(data)

# plot original demand
demand.plot(x="Date", y="Quantity")
plt.ylim(ymin=0)
plt.show()
