import pandas as pd
from pandas import DataFrame
from IPython.display import display

pcb = pd.read_csv('../pnp-centroid-examples/wembed-systems-bms-v2-panelized-top.pos', skiprows = 4, delimiter=r"\s+")

display(pcb.head(2))