import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

matplotlib.style.use("ggplot")

# ----------------------------------

# input retail.xlsx
retail = pd.ExcelFile(io="data/retail.xlsx")

# create a list of all dataframe
dfList = []

# 1. all_items
dfAllItems = retail.parse(sheetname="all_items", parse_cols=[1, 2], header=None, names=["Bucket", "Total orders"])
dfAllItems["Bucket"] = pd.to_datetime(dfAllItems["Bucket"], format="%b %y")
dfAllItems["Bucket"] = dfAllItems["Bucket"].dt.to_period("M")
dfAllItems.set_index("Bucket", drop=True, inplace=True)
dfList.append(dfAllItems)

# 2. umpire_chair
dfUmpireChair = retail.parse(sheetname="umpire_chair", parse_cols=[1, 2], header=None, names=["Bucket", "Total orders"])
dfUmpireChair["Bucket"] = pd.to_datetime(dfUmpireChair["Bucket"], format="%b %y")
dfUmpireChair["Bucket"] = dfUmpireChair["Bucket"].dt.to_period("M")
dfUmpireChair.set_index("Bucket", drop=True, inplace=True)
dfList.append(dfUmpireChair)

# 3. tennis_tshirt_long_sleeves
dfTennisTshirtLongSleeves = retail.parse(sheetname="tennis_tshirt_long_sleeves", parse_cols=[1, 2], header=None,
                                         names=["Bucket", "Total orders"])
dfTennisTshirtLongSleeves["Bucket"] = pd.to_datetime(dfTennisTshirtLongSleeves["Bucket"], format="%b %y")
dfTennisTshirtLongSleeves["Bucket"] = dfTennisTshirtLongSleeves["Bucket"].dt.to_period("M")
dfTennisTshirtLongSleeves.set_index("Bucket", drop=True, inplace=True)
dfList.append(dfTennisTshirtLongSleeves)

# 4. tennis_short
dfTennisShort = retail.parse(sheetname="tennis_short", parse_cols=[1, 2], header=None,
                             names=["Bucket", "Total orders"])
dfTennisShort["Bucket"] = pd.to_datetime(dfTennisShort["Bucket"], format="%b %y")
dfTennisShort["Bucket"] = dfTennisShort["Bucket"].dt.to_period("M")
dfTennisShort.set_index("Bucket", drop=True, inplace=True)
dfList.append(dfTennisShort)

# 5. tennis_racket
dfTennisRacket = retail.parse(sheetname="tennis_racket", parse_cols=[1, 2], header=None,
                              names=["Bucket", "Total orders"])
dfTennisRacket["Bucket"] = pd.to_datetime(dfTennisRacket["Bucket"], format="%b %y")
dfTennisRacket["Bucket"] = dfTennisRacket["Bucket"].dt.to_period("M")
dfTennisRacket.set_index("Bucket", drop=True, inplace=True)
dfList.append(dfTennisRacket)

# 6. socks
dfSocks = retail.parse(sheetname="socks", parse_cols=[1, 2], header=None,
                       names=["Bucket", "Total orders"])
dfSocks["Bucket"] = pd.to_datetime(dfSocks["Bucket"], format="%b %y")
dfSocks["Bucket"] = dfSocks["Bucket"].dt.to_period("M")
dfSocks.set_index("Bucket", drop=True, inplace=True)
dfList.append(dfSocks)

# 7. hard_tennis_ball_pack
dfHardTennisBallPack = retail.parse(sheetname="hard_tennis_ball_pack", parse_cols=[1, 2], header=None,
                                    names=["Bucket", "Total orders"])
dfHardTennisBallPack["Bucket"] = pd.to_datetime(dfHardTennisBallPack["Bucket"], format="%b %y")
dfHardTennisBallPack["Bucket"] = dfHardTennisBallPack["Bucket"].dt.to_period("M")
dfHardTennisBallPack.set_index("Bucket", drop=True, inplace=True)
dfList.append(dfHardTennisBallPack)

# 8. clay_tennis_shoes
dfClayTennisShoes = retail.parse(sheetname="clay_tennis_shoes", parse_cols=[1, 2], header=None,
                                 names=["Bucket", "Total orders"])
dfClayTennisShoes["Bucket"] = pd.to_datetime(dfClayTennisShoes["Bucket"], format="%b %y")
dfClayTennisShoes["Bucket"] = dfClayTennisShoes["Bucket"].dt.to_period("M")
dfClayTennisShoes.set_index("Bucket", drop=True, inplace=True)
dfList.append(dfClayTennisShoes)

# 9. clay_tennis_ball_pack
dfClayTennisBallPack = retail.parse(sheetname="clay_tennis_ball_pack", parse_cols=[1, 2], header=None,
                                    names=["Bucket", "Total orders"])
dfClayTennisBallPack["Bucket"] = pd.to_datetime(dfClayTennisBallPack["Bucket"], format="%b %y")
dfClayTennisBallPack["Bucket"] = dfClayTennisBallPack["Bucket"].dt.to_period("M")
dfClayTennisBallPack.set_index("Bucket", drop=True, inplace=True)
dfList.append(dfClayTennisBallPack)

# 10. all_surface_tennis_shoes
dfAllSurfaceTennisShoes = retail.parse(sheetname="all_surface_tennis_shoes", parse_cols=[1, 2], header=None,
                                       names=["Bucket", "Total orders"])
dfAllSurfaceTennisShoes["Bucket"] = pd.to_datetime(dfAllSurfaceTennisShoes["Bucket"], format="%b %y")
dfAllSurfaceTennisShoes["Bucket"] = dfAllSurfaceTennisShoes["Bucket"].dt.to_period("M")
dfAllSurfaceTennisShoes.set_index("Bucket", drop=True, inplace=True)
dfList.append(dfAllSurfaceTennisShoes)

# 11. all_sports_gear
dfAllSportsGear = retail.parse(sheetname="all_sports_gear", parse_cols=[1, 2], header=None,
                               names=["Bucket", "Total orders"])
dfAllSportsGear["Bucket"] = pd.to_datetime(dfAllSportsGear["Bucket"], format="%b %y")
dfAllSportsGear["Bucket"] = dfAllSportsGear["Bucket"].dt.to_period("M")
dfAllSportsGear.set_index("Bucket", drop=True, inplace=True)
dfList.append(dfAllSportsGear)

# 12. all_surface_tennis_ball_pack
dfAllSurfaceTennisBallPack = retail.parse(sheetname="all_surface_tennis_ball_pack", parse_cols=[1, 2], header=None,
                                          names=["Bucket", "Total orders"])
dfAllSurfaceTennisBallPack["Bucket"] = pd.to_datetime(dfAllSurfaceTennisBallPack["Bucket"], format="%b %y")
dfAllSurfaceTennisBallPack["Bucket"] = dfAllSurfaceTennisBallPack["Bucket"].dt.to_period("M")
dfAllSurfaceTennisBallPack.set_index("Bucket", drop=True, inplace=True)
dfList.append(dfAllSurfaceTennisBallPack)

# 13. novak_racket
dfNovakRacket = retail.parse(sheetname="novak_racket", parse_cols=[1, 2], header=None,
                             names=["Bucket", "Total orders"])
dfNovakRacket["Bucket"] = pd.to_datetime(dfNovakRacket["Bucket"], format="%b %y")
dfNovakRacket["Bucket"] = dfNovakRacket["Bucket"].dt.to_period("M")
dfNovakRacket.set_index("Bucket", drop=True, inplace=True)
dfList.append(dfNovakRacket)

# 13. all_material
dfAllMaterial = retail.parse(sheetname="all_material", parse_cols=[1, 2], header=None,
                             names=["Bucket", "Total orders"])
dfAllMaterial["Bucket"] = pd.to_datetime(dfAllMaterial["Bucket"], format="%b %y")
dfAllMaterial["Bucket"] = dfAllMaterial["Bucket"].dt.to_period("M")
dfAllMaterial.set_index("Bucket", drop=True, inplace=True)
dfList.append(dfAllMaterial)
