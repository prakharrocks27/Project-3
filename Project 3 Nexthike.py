#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[35]:


df= pd.read_csv('C:\\Users\\Prakhar\\OneDrive\\Desktop\\NextHike\\Project 3\\Housing_data.csv')


# In[36]:


df


# # Exploratory Data Analysis

# # EDA is a phenomenon under data analysis used for gaining a better understanding of data aspects like: 
# 
# 1 Main features of data.
# 
# 2 Variables and relationships that hold between them.
# 
# 3 Identifying which variables are important for our problem.

# # Details of Housing Data(Head, Tail, Shape, Columns & Dimension)

# In[9]:


# Deatils of Housing Data

print('Columns of Housing Data')
print(df.columns)

print('Head of Housing Data')
print(df.head())

print('Tail of Housing Data')
print(df.tail())

print('Shape of Housing Data')
print(df.shape)

print('Dimension of Housing Data')
print(df.ndim)


# # Describe, Correlation and Datatype of Housing Data

# In[15]:


# Describe, Correlation and Datatype of Housing Data

print('\Describe of Housing Data')
print(df.describe())

print('\Correlation of Housing Data')
print(df.corr())

print('\Information of Housing Data')
print(df.info())


# # The Number of Categorical Features in Housing Data

# In[38]:


categorical_cols= df.select_dtypes(include=['category'])


# In[39]:


categorical_cols= df.select_dtypes(exclude=['number','int64','float64'])


# In[40]:


categorical_cols


# In[41]:


numerical_cols = df._get_numeric_data()


# In[42]:


numerical_cols


# In[29]:


len(categorical_cols.columns)


# In[31]:


len(numerical_cols.columns)


# # Univariate Analysis

# In[33]:


# Univariate Analysis
#Univariate analysis is the simplest form of analyzing data.
#“Uni” means “one”, so in other words, data has only one variable.
#It doesn’t deal with causes or relationships and its major purpose is to describe.
#It takes data, summarizes that data, and finds patterns in the data.
#Univariate Analysis can be done either on numerical or categorical features.


# In[38]:


for column in numerical_cols:
    plt.figure(figsize=(10,4))
    sns.boxplot(data= numerical_cols, x=column)
    plt.ylabel('Values', color= 'red')
    plt.title('Box Plot For Numerical Columns')
    plt.show()


# In[39]:


#Analysis
#1. Maximum property Built in year from 1950 to 2000
#2. Remodel Property date was higher from 1965 to 2005
#3. Area used in BsmtUnfSF from 250sqft to 750sqft
#4. Full Bath are maximum used in 1 to 2 bathroom.
#5. In Half Bath, mostly between 1 to 2 bathroom
#6. 2 to 3 Bedroom are mostly used in BedroomAbvGrd
#7. In Total Room Above Grade 5 to 7 bedroom are maximum used
#8. The year guarage was built in 1960 t0 2001
#9. 1 to 2 car maximum used in Garage car
#10. Maximum property was sold in year 2007 till 2009


# # Scatter Plot for 'LotArea' and SalePrice

# In[ ]:





# In[47]:


plt.figure(figsize=(10,2))
sns.scatterplot(x='LotArea',y='SalePrice', data= df, hue='LotShape', style= 'LotShape')
plt.xlabel('LotArea', color= 'red')
plt.ylabel('SalePrice', color= 'red')
plt.title('Scatter Plot for LotArea and SalePrice', color = 'red')
plt.show()


# In[48]:


#Analysis
#1. SalePrice was maximum in Lot Area less than 20000 sqft
#2. Very few SalePrice in lot Area after 50000
#3. LotShape of Reg and IR1 are maximum in SalePrice 


# # Vioilin Plot Month sold and YearSold

# In[12]:


plt.figure(figsize=(10,2))
sns.catplot(data=df, x='MoSold', y="YrSold", Palette= 'virdis',kind="violin", bw_adjust=1.5, cut=4, inner='quartile')
plt.xlabel('Month of Sold', color='green')
plt.ylabel('Year of Sold', color= 'green')
plt.title('Violin Plot')
plt.show()


# In[59]:


#Analysis
#1. Maximum property sold in year 2007,2008 and 2009.
#2. Maximum propert sold in month are Jan, Feb , Mar & April
#3. less property sold in 2004, 2005, 2010.


# # MultiVariate Analysis

# ### Numeric Vs Numeric

# # LM Plot for GroundLivArea & Saleprice

# In[11]:


plt.figure(figsize=(10,2))
sns.lmplot(data = df, x ='GrLivArea', y ='SalePrice', fit_reg= True, line_kws= {'color': 'deeppink'}, scatter_kws={'color': 'deepskyblue'})
plt.title('GroundLivArea & SalePrice', color= 'red')
plt.show()


# In[62]:


#Analysis
#1.Maximum property SalePrice in GrLivArea between 1000 and 2000sqft
#2.Higher GrLivArea have less Sale


# # LinePlot SalePrice

# In[10]:


plt.figure(figsize=(10,2))
sns.lineplot(df['SalePrice'])
plt.title('House Price')
plt.show()


# In[4]:


#Analysis
#1. Saleprice was constant except in 2 scenario i.e 700 and 1200 where they have crossed more than 7lakh


# # Bubble Plot Overall Quality and SalePrice 

# In[15]:


plt.figure(figsize=(10,2), dpi=150) 
sns.scatterplot(data=df, x='OverallQual', y='SalePrice', hue= 'LotShape', style= 'LotShape') 
plt.xlabel('OverallQual', color= 'blue') 
plt.ylabel('SalePrice', color= 'blue') 
plt.title('Bubble Plpt for Overall Quality & SalePrice', color= 'blue') 
plt.show()


# In[16]:


#Analysis
#1. SalePrice was high when OverAll Quality of house is 10.
#2. Overall Condition of House less then 5, have less saleprice.


# In[6]:


df.head()


# # JointPlot For TotalBsmtSF and SalePrice

# In[19]:


plt.figure(figsize=(10,2), dpi=150) 
sns.jointplot(data=df, x='TotalBsmtSF', y='SalePrice') 
plt.xlabel('TotalBsmtSF', color= 'blue') 
plt.ylabel('SalePrice', color= 'blue') 
plt.title('Joint Plot for TotalBsmtSF & SalePrice', color= 'blue') 
plt.show()


# In[20]:


#Analysis
#1. Total Square Feet of Basement area less than 2000 sqft have higher saleprice.
#2. This indicates that high square feet of basement area have less saleprice or No SalePrice


# In[17]:


df.columns


# # JointPlot For GrLivArea and SalePrice

# In[21]:


plt.figure(figsize=(10,2), dpi=150) 
sns.jointplot(data=df, x='GrLivArea', y='SalePrice', color= 'green') 
plt.xlabel('GrLivArea', color= 'red') 
plt.ylabel('SalePrice', color= 'red') 
plt.title('Joint Plot for GrLivArea & SalePrice', color= 'red') 
plt.show()


# In[22]:


#Analysis
#1. Ground Live aree between 800 to 2000 sqft have maximum sale unit with a price range of 1 lakh to 3 lakh


# # JointPlot For GrLivArea and SalePrice Histogram

# In[24]:


plt.figure(figsize=(10,2), dpi=150) 
sns.jointplot(data=df, x='GrLivArea', y='SalePrice', color= 'purple', kind= 'hist') 
plt.xlabel('GrLivArea', color= 'red') 
plt.ylabel('SalePrice', color= 'red') 
plt.title('Joint Plot for GrLivArea & SalePrice', color= 'red') 
plt.show()


# In[26]:


#Analysis
#1.Ground Live aree between 800 to 2000 sqft have maximum sale unit with a price range of 1 lakh to 3 lakh
#2. Saleprice above 7 lakh and GrLiveArea above 4000 are outliers


# # Histogram Plot for YearBuilt & SalePrice

# In[29]:


plt.figure(figsize=(10,2), dpi=150) 
sns.histplot(data=df, x='YearBuilt', y='SalePrice', color= 'purple') 
plt.xlabel('YearBuilt', color= 'red') 
plt.ylabel('SalePrice', color= 'red') 
plt.title('Histogram Plot for YearBuilt & SalePrice', color= 'red') 
plt.show()


# In[28]:


#Analysis
#1. Property built in 2010 have high saleprice


# # Histogram Plot for SalePrice

# In[33]:


plt.figure(figsize=(10,2), dpi=150) 
sns.histplot(data=df, x='SalePrice', color= 'purple', kde= True) 
plt.xlabel('SalePrice', color= 'blue') 
plt.ylabel('Count', color= 'blue') 
plt.title('Histogram Plot for SalePrice', color= 'blue') 
plt.show()


# In[32]:


#Analysis
#1.Sale Price between 1.3 lakh to 1.4 lakh have maximum count 


# # PairPlot for columns

# In[36]:


plt.figure(figsize=(10,2), dpi=150) 
sns.pairplot(df[['SalePrice','OverallCond','ExterQual','GrLivArea','GarageArea']]) 
plt.title('PairPlot for Different Columns', color= 'blue') 
plt.show()


# In[37]:


#Analysis
#1. we have considered columns for PairPlot are SalePrice','OverallCond','ExterQual','GrLivArea','GarageArea'


# # HeatMap Using Correlation of Data

# In[54]:


df.corr(numeric_only= True)


# In[56]:


plt.figure(figsize=(12,10))
sns.heatmap(df.corr(numeric_only= True)[['OverallQual', 'OverallCond','LotFrontage','LotArea', 'SalePrice']],annot= True, cmap= 'crest',linewidth = .5)
plt.show()


# In[57]:


#Analysis
#1.OverallQuality & GrlivArea are highly correlataed
#2.TotalbsmtSf,GarageyeBuilt, Garagecar are less correlated


# In[34]:


df.columns


# # Numerical Vs Categorical

# In[58]:


categorical_cols


# # Boxplot of Lot Shape & SalePrice

# In[63]:


plt.figure(figsize=(10,2), dpi=150) 
sns.boxplot(data=df, x='LotShape', y= 'SalePrice', color= 'purple', hue= 'LotConfig') 
plt.xlabel('LotShape', color= 'darkgreen') 
plt.ylabel('SalePrice', color= 'darkgreen') 
plt.title('Box Plot of LotShape &SalePrice', color= 'blue') 
plt.show()


# In[65]:


#Analysis
#1. In LotShape , IR2, Floor 3 have SalePrice in range of 2 to 4 lakh


# # Violin plot for Sale condition and SalePrice

# In[71]:


plt.figure(figsize=(10,2))
sns.catplot(data=df, x='SaleCondition', y='SalePrice', Palette= 'virdis',hue='ExterQual' ,kind="violin", bw_adjust=1.5, cut=4, inner='quartile')
plt.xlabel('SaleCondition', color='green')
plt.ylabel('SalePrice', color= 'green')
plt.title('Violin Plot')
plt.show()


# In[72]:


#Analysis
#1. Partial saleconditin have saleprice of 2 lakh to 4 lakh
#2. Excellent Exterior Quality lying partial sale condition have saleprice of 2 to 5 lakh


# # BAR Plot for HouseStyle and SalePrice

# In[79]:


plt.figure(figsize=(10,2))
sns.barplot(data=df, x='HouseStyle', y='SalePrice', estimator='count', errorbar=None)
plt.xlabel('HouseStyle', color='green')
plt.ylabel('SalePrice', color= 'green')
plt.title('Bar Plot with HouseStyle and Saleprice')
plt.show()


# In[80]:


#Analysiss
#1.1Story have maximum Saleprice of 600 count
#2. 1.5unf,SFoyer, Slvl, 2.5Unf & 2.5 fin have less sale count


# # Swam Plot for Salecondition and Sale price

# In[82]:


plt.figure(figsize=(12,5), dpi= 250)
sns.swarmplot(data=df, x='SaleCondition', y='SalePrice', palette="deep")
plt.xlabel('SaleCondition', color='green')
plt.ylabel('SalePrice', color= 'green')
plt.title('Swarm Plot with Salecondition and Saleprice')
plt.show()


# In[83]:


#Analysis
#1. Normal sale condition have saleprice between 1 to 3 lakh.
#2 Adjland sale condition have less unit sold


# # Categorical Vs Categorical

# In[96]:


plt.figure(figsize=(12,5), dpi= 250)
sns.countplot(data=df, x='Neighborhood', hue= 'LotConfig')
plt.xlabel('Neighborhood', color='green')
plt.ylabel('Count', color= 'green')
plt.title('CountPlot for Neighborhood and LotConfig')
plt.show()


# In[ ]:


#Analysis
#1.


# # Dist Plot Saleprice

# In[93]:


plt.figure(figsize=(12,5), dpi= 250)
sns.distplot(x= df['SalePrice'],color= 'blue', hist= True)
plt.xlabel('SalePrice', color='green')
plt.ylabel('Volume', color= 'green')
plt.title('Distplot for SalePrice')
plt.show()


# In[97]:


#analysis
#1. Volume is high when the sale price is 1.7 lakh to 1.8 lakh


# # Bar Chart for Overall

# In[15]:


plt.figure(figsize=(12,5), dpi= 250)
df['OverallQual'].value_counts().plot.bar(color= 'blue')
plt.xlabel('OverallQual', color='green')
plt.ylabel('Value Counts', color= 'green')
plt.title('Bar Plot for OverallQual')
plt.show()


# In[16]:


#Analysis

#1. Overall Qualitty of 5 & 6 are the highest , whem the OverAll Quality was 10, it was below averge


# 
# # Bubble Plot for LotShape & LotConfig with hue as HouseStyle

# In[16]:


plt.figure(figsize=(8,4), dpi= 100)
sns.scatterplot(data=df, x='LotShape', y= 'LotConfig', hue= 'HouseStyle', color= 'red')
plt.xticks(rotation = 90)
plt.xlabel('LotShape', color='green')
plt.ylabel('LotConfig', color= 'green')
plt.title('Bubble Plot for LotShape & LotConfig with hue as HouseStyle')
plt.show()


# In[17]:


#Analysis
#1.this indicates that 1 story - Housestyle is using maximum in Lotshape


# In[18]:


import plotly.express as px


# # Radar Chart Using HouseStyle,RoofStyle,ExterQual,SaleType & SaleCondition

# In[20]:


df = pd.DataFrame(dict(
    r=[1, 5, 2, 2, 3],
    theta=['HouseStyle','RoofStyle','ExterQual',
           'SaleType', 'SaleCondition']))
fig = px.line_polar(df, r='r', theta='theta', line_close=True)
fig.update_traces(fill='toself')
fig.show()


# In[ ]:


#Analysis
#1


# # Feature VS Feature

# # KDE PLOt YearBuilt, YrSold hue is SaleCondition

# In[44]:


plt.figure(figsize=(8,4), dpi= 200)
sns.kdeplot(x ='YearBuilt', y= 'YrSold',data=df,  hue= 'SaleCondition', level= 5,fill= True)
plt.xlabel('YearBuilt', color='green')
plt.ylabel('YrSold', color= 'green')
plt.title('KDE for YearBuilt & YrSold with hue as SaleCondition', color= 'green')
plt.show()


# In[46]:


#Analysis
#1. The property built in 2000 and onwards , sold within 4-5 year.
#2. There are property which built before 1900 sold in 2006
#3. the property which are Partial in salecondition also sold maximum in year 2005 onwards


# In[ ]:





# In[ ]:


# Feature Vs Target


# In[ ]:


label


# In[49]:


plt.figure(figsize=(10,5), dpi= 200)
sns.stripplot(x='YrSold', y='SalePrice', data=df, jitter=True, hue='RoofStyle', palette='deep', dodge=True)
sns.pointplot(x='YrSold', y='SalePrice', data=df, hue='RoofStyle', palette='deep', dodge=True, linestyles='', errorbar=None)
plt.xlabel('Year Property Sold')
plt.ylabel('SalePrice')
plt.title('Sale price of the Property Year Sold')
plt.show()


# In[50]:


# Analysis
#1.The property which sold in 2007 has sold at a higher price more than 7 lakh.
#2. the Property having a Roof style is Gable, sold at very minimum price less than 50000( from 2006 t0 2010 year property sold)
 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




