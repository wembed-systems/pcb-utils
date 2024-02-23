import pandas as pd
from pandas import DataFrame
from IPython.display import display
import re


# Permanently changes the pandas settings
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

pcb = pd.read_csv('pos.pos', skiprows = 4, delimiter=r"\s+")

pcb.drop(index=pcb.index[-1],axis=0,inplace=True)
#display(pcb.describe())


#display(pcb)

MAX_SIZE = len(pcb.index)


# 0.1 Set the location for the first reference to 0
loc = 0

# 1.0 Navigate through the dataset, select and change the data
while (loc < MAX_SIZE) :
    # 1.1 Select a reference from the dataset
    reference = pcb["Ref"].iloc[loc]

    if(not reference == "REF**") :
        # 1.2 Find the rows which have the reference as a duplicate
        reference_set = pcb[pcb["Ref"].str.match(reference)]

        # 2.1 Process the subset to not contain duplicates
        
        # Skip non-duplicates
        if(len(reference_set.index) > 1) :
            # 2.1.1 Select literal part
            literal = re.match(r"[A-Za-z0-9]+", reference)
            # print(literal)
            # 2.1.2 Add index count part

            for counter in range(len(reference_set.index)) :
                pcb.loc[loc + counter, 'Ref'] = literal.group(0) + "_BOARD_" + str(counter+1)

        # 2.2 Increase the reference count by the amount of 
        # rows found to prepare for the next reference

    loc += len(reference_set.index) 

    
display(pcb)
