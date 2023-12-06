# a.
# Uses ydata-profiling to read the dataset into a DataFrame and writes the
# profiling report to profiling/report.html
# b. See Create a Profiling Report with ydata-profiling for details.

import pandas as pd
from ydata_profiling import ProfileReport
import os

df = pd.read_csv("data/csv/bank-additional/bank-additional-full.csv", delimiter=";")
profile = ProfileReport(df, title="Pandas Profiling Report")

if not os.path.exists("profiling/"):
    os.makedirs("profiling/")

profile.to_file("profiling/report.html")