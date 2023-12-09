# a. Computes summary statistics for one or more fields/variables
# b. Performs a simple analytical or classification task
# c. Creates a simple visualization

import pandas as pd
import os
import matplotlib.pyplot as plt

df = pd.read_csv("data/csv/bank-additional/bank-additional-full.csv", delimiter=";")



if not os.path.exists("results/"):
    os.makedirs("results/")

with open("results/summary.txt", "w") as f:
    f.write(str(df.describe()))

df_group = df[["age", "job", "marital"]].groupby(by=['age', 'job']).count()
df_group.rename(columns={'marital': 'count'}, inplace=True)
with open("results/age_job.txt", "w") as f:
    f.write(str(df_group.to_string()))

df['count'] = 1
df['married'] = 0
df.loc[df['marital'] == 'married', 'married'] = 1
df_group_age = df[["age", "married", "count"]].groupby(by=['age'], group_keys=['married']).sum()

ax = df_group_age.plot.bar(rot=0, figsize=(20,10))

fig = ax.get_figure()
fig.savefig("results/output.png")