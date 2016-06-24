import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

matplotlib.style.use("ggplot")

# retail.xlsx
dfAllItems = pd.read_excel(io="data/retail.xlsx", sheetname="all_items", parse_cols=[1, 2], header=None,
                           names=["Bucket", "Total orders"])
print(dfAllItems)
dfAllItems["Bucket"] = pd.to_datetime(dfAllItems["Bucket"], format="%b %y")
dfAllItems["Bucket"] = dfAllItems["Bucket"].dt.to_period("M")
dfAllItems.plot(x="Bucket", y="Total orders")
plt.ylim(ymin=0)
plt.show()
