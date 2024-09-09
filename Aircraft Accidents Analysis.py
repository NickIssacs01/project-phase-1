#!/usr/bin/env python
# coding: utf-8

# ## Aircraft Accidents Analysis

# ## Overview

# This repo helps to explore the relationship between aircraft make and model and the number of fatalities. We'll look at which types of variables to avoid in order to mitigate risks.

# ## Business Problem

# Your company is expanding in to new industries to diversify its portfolio. Specifically, they are interested in purchasing and operating airplanes for commercial and private enterprises, but do not know anything about the potential risks of aircraft. You are charged with determining which aircraft are the lowest risk for the company to start this new business endeavor. You must then translate your findings into actionable insights that the head of the new aviation division can use to help decide which aircraft to purchase.

# ## Data

# The data for this analysis was taken from: https://www.kaggle.com/datasets/khsamaha/aviation-accident-database-synopses?resource=download

# ## Data Description

# #numpy for high level mathematical functions and working with Arrays import numpy as np #pandas data manipulation and analysis for tablular data import pandas as pd #seaborn and matplotlib for data visualization import seaborn as sns import matplotlib.pyplot as plt %matplotlib inline

# ## Visualization

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# ## Conclusion

# The project will consider these three variables in the form of graphs in the decison making of whether it is viable to start purchasing aircrafts. Some of the variables that will influence this decision are:
#     1. Total number of fatalities
#     2. Engine type per fatality
#     3. Aircraft make per fatality
#     4. Number of fatalities through the years

# ## Findings

# From the analysis we get to find out that:
#     1. Reciprocating engine type has the highest number of fatalities of upto 20,000
#     2. It can be observed that the number of injuries decreases as you move to Turbo Fan and Turbo Shaft engines.
#     3. Electric and Geared Turbofan engines show almost no fatal injuries, meaning they are safer in this context.
