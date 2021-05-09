
import re
import pandas as pd
from googlesearch import search
import time
import datetime

#input
df = pd.read_csv('keywords.csv')
queries = df["Keyword"].tolist()

#output
finaldf = pd.DataFrame(columns = ['Keyword','Rank','Links'])
row= 0

def get_rank(query):
    try:
        global row
        rank = 1
        print("\n Keyword:",query)
        #Here stop means the rank upto which google will check 
        finaldf.at[row, 'Keyword'] = query
        for i in search(query, tld= "com", num=10, stop= 20, pause= 2, country="India"):
            print ("\n",rank,i)
            if re.search(".*amazon|.*flipkart|.*indiamart|.*snapdeal|.*healthkart|.*pharmeasy|.*1mg", i):
                print("useless")
            else:
                finaldf.at[row, 'Rank'] = rank
                finaldf.at[row, 'Links'] = i
            rank += 1
            row +=1
    
    except:
        pass

for query in queries:
    get_rank(query)
    time.sleep(2)
    x = datetime.datetime.now()
    finaldf.to_csv(str(x.strftime("%A"))+"Output.csv")


