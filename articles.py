import plotly.figure_factory as ff 
import statistics 
import random
import csv
import pandas as pd
df=pd.read_csv("medium_data.csv")
article = df['claps'].to_list()
articlemean = statistics.mean(article)
standarddeviation = statistics.stdev(article)
print(standarddeviation)
print(articlemean)
def randomsetofmean (counter):
    dataset = []
    for i in range(0,counter):
        randomindex  = random.randint (0,len(article)-1)
        value  = article[randomindex]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return(mean)     
def showfig(meanlist):
    df = meanlist
    mean = statistics.mean(df)
    fig = ff.create_distplot([df],["article"],show_hist = False)
    fig.show()
def setup():
    meanlist = []
    for i in range(0,1000):
        setofmeans = randomsetofmean(100)
        meanlist.append(setofmeans)
    showfig(meanlist)
    mean = statistics.mean(meanlist)
    sd=statistics.stdev(meanlist)
    print(mean,sd)
setup()        
