# Databricks notebook source
#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np


# In[ ]:


def read_data():
    df = pd.read_csv('/dbfs/mnt/data/data/input/dimensions-covid19-export-2021-09-01-h15-01-02_clinical_trials.csv')
#     df=pd.read_csv('https://meden.blob.core.windows.net/meden/data/input/dimensions-covid19-export-2021-09-01-h15-01-02_datasets.csv?sp=r&st=2022-12-02T19:47:13Z&se=2022-12-03T03:47:13Z&spr=https&sv=2021-06-08&sr=b&sig=9CtObvEpkiDtpKXvFuBza4hJ4%2F2DmsRBnZ%2BRqAZ3sL0%3D')   #for preprocessing
    df1=pd.read_csv('/dbfs/mnt/data/data/input/dimensions-covid19-export-2021-09-01-h15-01-02_clinical_trials.csv')
#     df1=pd.read_csv('https://meden.blob.core.windows.net/meden/data/input/dimensions-covid19-export-2021-09-01-h15-01-02_datasets.csv?sp=r&st=2022-12-02T19:47:13Z&se=2022-12-03T03:47:13Z&spr=https&sv=2021-06-08&sr=b&sig=9CtObvEpkiDtpKXvFuBza4hJ4%2F2DmsRBnZ%2BRqAZ3sL0%3D')  #for returning results
    return df.iloc[:100,:]

