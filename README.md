# How did the COVID-19 Pandemic Effect Crime in Chicago?

## Table of contents
*  Current state notes
*  Overview
*  Requirements
*  Repository structure
*  Sources

# Running the project
> python main.py
* Run from the directory main is in.
* Additional options are available for arrest analysis by modifying main.py

# Overview
1. An analysis of crime records from Chicago in the years 2019, 2020, and 2021 (up to Nov. 14).

2. An analysis of Chicago districts with crime statistics: dates, arrests, type.

3. proposal.pdf contains more information on motivation and research questions.

# Requirements
1. Git-lfs to access data.

2. Python 3 & packages: Pandas, Numpy, Matplotlib, tqdm, scipy

# Repository structure
1. *data* subdirectory contains raw data.

2. *scripts* subdirectory contains common-use scripts and notebooks for tasks like preprocessing.

3. Research questions each have their own subdirectory (*arrests*, *districts*, *domestic*) with a module that can be called by main, as well as any supplementary files that module needs to run.

# Sources

1. [https://www.kaggle.com/chicago/chicago-crime]
2. [https://data.cityofchicago.org/]
