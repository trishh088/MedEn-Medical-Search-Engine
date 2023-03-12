# Databricks notebook source
# one time execution only
dbutils.fs.mount(
    source="wasbs://meden@meden.blob.core.windows.net",
    mount_point = "/mnt/data",
    extra_configs = {"fs.azure.account.key.meden.blob.core.windows.net":'hfWeCi5qS9bj9s7hU4xwGrWGRl/PjRLxknYZKMgEyU2oLazADEVlC/bQEgkey6oooGyb/3wlvbX2+AStfVw9dA=='})

# COMMAND ----------

import pandas as pd
d = pd.read_csv('/dbfs/mnt/data/data/input/dimensions-covid19-export-2021-09-01-h15-01-02_clinical_trials.csv')

# COMMAND ----------

d.head()
