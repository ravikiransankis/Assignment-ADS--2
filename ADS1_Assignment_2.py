#!/usr/bin/env python
# coding: utf-8

# In[294]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as se


# In[295]:


def dataset_1(df):
    '''
    Takes in a dataset in a df, then skipping the four rows of the beginning rows of datset
    Dropping the Unnamed columns of the dataset then copying the dataset into data_1 variable
    Them dropping the unwanted columns from the dataset and making the index with the Country Name data
    Then with the transposing of the dataset the Country Name data indexes are turned to columns and return of the dataframe.
    '''
    df_1=pd.read_csv(df,skiprows=4)# reading the dataset after skipping four rows at the beginning of the dataset.
    df_1= df_1.drop(["Unnamed: 66"], axis = 1)# dropping of the Unnamed columns from the dataset
    data_1= df_1.copy()# copying of the dataset into data_1 variable
    df_2 = data_1.drop(columns =["Country Code","Indicator Name","Indicator Code"],axis =1)# dropping the columns from the dataset
    df_2=df_2.set_index("Country Name")# Making the Country Name in the dataset
    df_2=df_2.transpose()# Transposing of the data for chaning the index of Country Name to Columns
    return df_1, df_2


# In[296]:


# Getting the dataset as the argumenet
df_year,df_country = dataset_1("API_19_DS2_en_csv_v2_4902199.csv")


# In[297]:


# calling the first dataframe where Country Name are columns
df_country


# In[298]:


# Calling the second created dataframe where Years data are columned.
df_year


# In[334]:


# Describing the statistical methods values of the related data in the dataframe of df_country where country name are columned. 
df_country.describe()


# In[300]:


# Describing the statistical method analysis using the describe function for the dataframe of df_year
df_year.describe()


# In[301]:


# Filling the missing values or NaN values with 0 in the dataframe of df_year.
df_year.fillna(0)


# In[302]:


# Creating new dataframe where there is group by with "Agricultural land (% of land area of data)" of df_year dataframe which is indicator name. 
gk = df_year.groupby("Indicator Name")
gk_1=gk.get_group("Agricultural land (% of land area)")#getting group by
gk_1# calling the grouped by dataframe


# In[303]:


# Creating new dataframe where there is group by with "United Kingdom" of df_year dataframe which is country name. 
grp = df_year.groupby("Country Name")
grp_1=grp.get_group("United Kingdom")# Grouping of the country
grp_1=grp_1.drop(["Country Code","Indicator Code","Country Name"], axis=1)# Dropping of the unwanted columns
grp_1=grp_1.set_index("Indicator Name") # INdexing the Indicator name in the dataset
grp_1 # Calling the created dataframe of grouped by country name


# In[304]:


# Getting the columns of the dataframe of grp_1 which is grouped by country name of United Kingdom
grp_1.columns


# In[305]:


# Implementing the wanted data columns of years in the grp_1 dataframe.
grp_1=grp_1[['2000', '2001', '2002', '2003', '2004',
       '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013',
       '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']]
grp_1 # Calling of the grp_1 dataframe


# In[306]:


# Getting info about the data type and counts related to the columns of the grp_1 dataframe
grp_1.info()


# In[311]:


# Transposing the grp_1 dataframe for making the indicator name data to columns in the dataframe
grp_1=grp_1.transpose()
grp_1 # Calling of the grp_1 dataframe


# In[312]:


# Getting info about the columns of the grp_1 dataframe
grp_1.columns


# In[335]:


# Implementing of the proposed indicator names for calcultaing the correlation between them and making new dataframe of grp_2.
grp_2=grp_1[["Forest area (% of land area)",
"Arable land (% of land area)",
"Urban population growth (annual %)",
"Population growth (annual %)",
"Agricultural land (% of land area)"]]
grp_2 # Calling of the grp_2 dataframe


# In[353]:


# Calculating the correlation value between indicators names with the use of heatmaop function of Seaborn module where the annotation  is true and color of the correlation is determined.
se.heatmap(grp_2.corr(),annot=True,cmap="twilight_shifted")
plt.title("United Kingdom Inidicators correlation")


# In[341]:


def bieplot(P):
    '''
    Making the function of bieplot for the plotting of the data in the form of bar chart
    droppping of the unused column from the dataset
    Determining the value of bar as per the Indicator name which is Urban Poulation
    Then the country name are grouped by where top 15 countries are headed for the data visualization of them
    plotting of the four data from the year of 1961, 1981, 2001 and 2021
    And proper plottation function is created
    '''
    P = P.drop(["Country Code","Indicator Code"],axis =1) #drop the unused column from the dataset
    P.set_index("Indicator Name",inplace = True) # setting up the index for the "Indicator Name"
    P = P.loc["Urban population"]
    P = P.reset_index(level = "Indicator Name")
    P.groupby(["Country Name"]).sum() #group the data on the base of country Name
    # taking the head 15 simple data of country
    P = P.head(15)
    # ploting the data in bar plot
    P.plot(x= "Country Name",y = ['1961','1981', '2001', "2021"],figsize = (15,5), kind="bar")
    plt.title("Urban population")
    plt.ylabel("Frequency")
    plt.show()


# In[342]:


# Calling the bar chart plottation adn implementing in the data of df_year dataframe
data_1=df_year
bieplot(data_1) # Calling the bieplot function


# In[347]:


def plotter(P,ind,pt,x,y):
    '''
    Definning the function name of plotter where dataframe is taken by P, Plot title is taken by ind, and the width and height of the plot is taken by x and y respectively
    Indexing of the Indicator name and grouping of the country name for the proper plot of the data as per the country name
    Plotting of the 12 countries in the plot as per the argument type of plot
    then proper plot function of plotter is created for better plotting of the data from the dataframe
    '''
    P = P.drop(["Country Code","Indicator Code"],axis =1) #drop the un-used column form the dataset
    P.set_index("Indicator Name",inplace = True) # set-up the index for the "Indicator Name"
    P = P.loc[ind]
    P = P.reset_index(level = "Indicator Name")
    P.groupby(["Country Name"]).sum() #group the data on the base of country Name
    # taking the head 12 simple data
    P = P.head(12)
    # ploting the data in the line plot
    P.plot(x= "Country Name",y = ["2021","2020"], kind=pt,stacked=False,figsize=(x,y))
    plt.title(ind)
    plt.ylabel("Frequency")
    plt.show()


# In[348]:


# Calling of the plotter function for plottig the data in df_year dataframe with the title and data related to "Population growth (annual %)" and plot type of barh where the plot size is demonstrated. 
plotter(df_year,"Population growth (annual %)","barh",8,6)


# In[355]:


# Calling of the plotter function for plottig the data in df_year dataframe with the title and data related "Agriculture, forestry, and fishing, value added (% of GDP)" and plot type of area where the plot size is demonstrated. 
plotter(df_year,"Agriculture, forestry, and fishing, value added (% of GDP)","area",15,6)


# In[350]:


# Calling of the plotter function for plottig the data in df_year dataframe with the title and data related to "Mortality rate, under-5 (per 1,000 live births)" and plot type of box where the plot size is demonstrated. 
plotter(df_year,"Mortality rate, under-5 (per 1,000 live births)","box",8,6)


# In[351]:


# Calling of the plotter function for plottig the data in df_year dataframe with the title and data related to "Population growth (annual %)" and plot type of line where the plot size is demonstrated. 
plotter(df_year,"Population growth (annual %)","line",10,8)


# In[358]:


# Calling of the plotter function for plottig the data in df_year dataframe with the title and data related to "Arable land (% of land area)" and plot type of line where the plot size is demonstrated. 
plotter(df_year,"Arable land (% of land area)","line",10,8)

