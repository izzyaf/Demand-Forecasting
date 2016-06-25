import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
import preprocessing as pre

matplotlib.style.use("ggplot")

rng = pd.period_range("2014-12", "2017-12", freq="M")
forecastAllItem = pd.DataFrame(index=rng, columns=["Total orders"])
forecastAllItem.update(pre.dfAllItems)
forecastAllItem = pd.ewma(forecastAllItem, span=3)
print(forecastAllItem)

forecastAllItem.plot(ax=pre.dfAllItems.plot())
plt.show()



