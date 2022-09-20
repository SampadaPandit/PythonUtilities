import pandas as pd
import numpy as np

def analyseDataFile(inputFile):
    readcsv = pd.read_csv(inputFile)
    df = pd.DataFrame(readcsv,index = None)
    numOfCols = len(df.columns)
    print("Number of columns: ",len(df.columns))
    info_df = pd.DataFrame(
        {
            "Column Name":[],
            "Data Type":[],
            "Count of NAN":[],
            "Count of Empty String":[],
            "Count leading/trailing Whitespaces":[]
        }
    )
    count_of_whitespaces = 0
    for x in range(0,numOfCols):        
        if df[df.columns[x]].dtype == 'object':
            count_of_whitespaces = (df[df.columns[x]].str.startswith(" ") | df[df.columns[x]].str.endswith(" ")).sum()
        
        temp_df = pd.DataFrame(
            {
                "Column Name":[df.columns[x]],
                "Data Type":[df[df.columns[x]].dtype],
                "Count of NAN":[df[df.columns[x]].isnull().sum()],
                "Count of Empty String":[df[df.columns[x]].eq('').sum()],   
                "Count of White Spaces":[count_of_whitespaces]
            },
            index=[x+1]
        )
        info_df = pd.concat([info_df,temp_df])
        
    info_df = info_df.astype({"Count of NAN": int, "Count of Empty String": int, "Count of White Spaces": int})    

    print(info_df)