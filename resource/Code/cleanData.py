import pandas as pd
import numpy as np

def searchLinkRecord(df):

    df["processID"]=""
    idGenerator = 0
    
    def searchParent(childrenRow,idGenerator):
        ifFound=False
        for row in df.itertuples():
            print(row)
            if row.Index != childrenRow.Index and  str(childrenRow._13).split("#")[1].strip()==str(row._9).strip():
                df.at[row.Index,"processID"]= idGenerator
                df.at[childrenRow.Index,"processID"]= idGenerator
                ifFound = True
        if ifFound:
            idGenerator=idGenerator+1
        return idGenerator
    
    for row in df.itertuples():
        if pd.notnull(row._13):
            if pd.isnull(df.loc[row.Index,"processID"]):
                pass
            else:
                idGenerator=searchParent(row,idGenerator)
    return df

def cleanNull(df):
    max= pd.to_numeric(df["processID"]).max()
    for row in df.itertuples():
        print(df.at[row.Index,"processID"])
        if not isinstance(df.loc[row.Index,"processID"],int):
            max=max+1
            df.at[row.Index,"processID"]= max
    return df

def main():
    df = pd.read_excel("data/testFinalData.xlsx")
    kang = searchLinkRecord(df)
    kang = cleanNull(kang)
    kang.to_csv("outtest.csv", index=False)

if __name__ == "__main__":
    main()
