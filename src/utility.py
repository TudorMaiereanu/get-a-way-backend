from Weights import weights
import pandas as pd
from GoogleAPI import sheet
from skcriteria import Data, MIN, MAX
from skcriteria.madm import closeness, simple

# Set Weigths
# Preference: Activity (0 or 1)
p_act_hike = 0
p_act_surf = 1

# Preference: Feature (0 or 1 or 2)
p_weather = 2
p_corona = 2
p_cost = 0
p_CO2 = 2
p_time = 0

weights = weights(p_weather, p_corona, p_cost, p_CO2, p_time,p_act_hike, p_act_surf).transpose().iloc[0, :].tolist()
# Get Alternative Matrix
SPREADSHEET_ID = '1M-nvjnx8fDUCXRe6nsxV8bmlJgKPer_mVVOpISMCqcE'
RANGE_NAME = 'Alternative Matrix!B2:I6'
alt = sheet(SPREADSHEET_ID, RANGE_NAME)

# Create Optimal Sense
os = [MAX, MIN, MIN, MAX, MAX, MAX, MIN, MIN]

# Combine Alternative Matrix and Optimal Sense
anames = ["Greta", "Scared", "Adrenaline-Outdoor", "Adrenaline-Sport", "Culture"]
RANGE_NAME = 'Alternative Matrix!B1:I1'
cnames = sheet(SPREADSHEET_ID, RANGE_NAME).iloc[0,:].tolist()
data = Data(alt, os, weights=weights, anames=anames, cnames=cnames)

# MCDA method

# TOPSIS
dm = closeness.TOPSIS()
dec = dm.decide(data)
print(data.anames[dec.best_alternative_])