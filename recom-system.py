# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 20:04:18 2020

@author: Shiva
"""


import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_job_from_index(Index):
	return df[df.Index == Index]["Company_Name"].values[0],df[df.Index == Index]["Job_Title"].values[0],df[df.Index == Index]["Location"].values[0],df[df.Index == Index]["Job_Salary"].values[0]
def get_index_from_job(Job_Title,Location,Job_Salary):
	return df[df.Job_Title == Job_Title]["Index"].values[0]

#Read csv file
df = pd.read_csv('My_data - Sheet1.csv')

#Select features
features = ['Job_Title','Location','Job_Salary']


#Create a column in DF which combines all selected features
def combine_features(row):
    return row['Job_Title']+""+row['Location']+""+row['Job_Salary']
df["combined_features"] = df.apply(combine_features,axis=1)


#Create count matrix from this new combined column
cv = CountVectorizer()
count_matrix = cv.fit_transform(df["combined_features"])

#Compute the Cosine Similarity based on the count_matrix
cosine_sim = cosine_similarity(count_matrix)

#Features requested by the user
User_job='Data Analyst'
User_loc='Bangalore'
User_sal='Rs 500000'

#Get index of this job from its choice
User_choice= get_index_from_job(User_job,User_loc,User_sal)
jobs_available = list(enumerate(cosine_sim[User_choice]))

#Get a list of similar jobs in descending order of similarity score
sorted_jobs_available= sorted(jobs_available,key=lambda x:x[1],reverse=True)

#Print the details of first 5 jobs
i=0
for job in sorted_jobs_available:
    print( get_job_from_index(job[0]))
    i=i+1
    if i>5:
        break