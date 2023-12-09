# IS477 FA23 Final

## Overview

This repository is an analysis on an University of California Irvine ML dataset called "Bank Marketing." 
The [bank marketing](https://archive.ics.uci.edu/dataset/222/bank+marketing) dataset covers a Portuguese bank and data collected for a direct telephone marketing campaign. Data collected was mostly demographic and financial in nature, and is a mix of quantitative and categorical variables.  

Looking just at marital status and age, we can produce a visualization of the count of respondents per age and compare against how many are married, versus single or divorced. We can see that there is an increasing separation between the number of people married versus not near the middle of the age range, perhaps indicating a generational shift in this sample. 

Our other analysis breaks down jobs by age into a table. This follows a predicable trend where young adults are mostly students. Past the mid-20s the count for blue collar work increases, before other types of work increase. Past 60, the count for retirement starts increasing, while the overall count starts decreasing. 

## Analysis

Using the visual graph titled `output.png` we can compare how many respondents were married versus not married, by age. We can see that there is an increasing separation between the number of people married versus not near the middle of the age range, perhaps indicating a generational shift in this sample. 

## Workflow

![DAG Graph](graph.png)

## Reproducing

1. Clone this repository: https://github.com/HadleyUIUC/is477-fall2023-final-project
2. Pull the docker image: `docker pull uiuchadley/is477-fall2023-final-project:v1`  
3. Run the docker image: `docker run --rm -v ${PWD}:/is477 is477-fall2023-final-project:v1 snakemake --cores 1 prepare`
3. Run the docker image: `docker run --rm -v ${PWD}:/is477 is477-fall2023-final-project:v1 snakemake --cores 1 profile`
3. Run the docker image: `docker run --rm -v ${PWD}:/is477 is477-fall2023-final-project:v1 snakemake --cores 1 analyze`


## License

The UCI Bank Marketing dataset is under a [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/legalcode) license.

UCI Bank Marketing dataset:  
Moro,S., Rita,P., and Cortez,P.. (2012). Bank Marketing. UCI Machine Learning Repository. https://doi.org/10.24432/C5K306.

## References