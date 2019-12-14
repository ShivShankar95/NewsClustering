import pandas as pd
from HealthNewsClustering import NewsClusters,preprocess 
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
headers = ['tweetId', 'dateTime', 'tweet']
dataframe = pd.read_csv(dir_path + '/Health-Tweets/bbchealth.txt', sep='|', header=None, names=headers)
preprocess(dataframe)

K = [5,7,9,11,13]

for i in K:
 newsClusters = NewsClusters(dataframe, i)
 newsClusters.fit()
 newsClusters.report()
