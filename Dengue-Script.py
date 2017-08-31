
# coding: utf-8

# In[ ]:

cd Desktop\Kaggle\dengue_forecast
import pandas as pd
import datetime as dt
import numpy as np

# compostite analysis for sjdata and iquitos

#Directory of C:\Users\mnave\Desktop\Kaggle\dengue_forecast
train = pd.read_csv("dengue_features_train.csv",header=0)
test =pd.read_csv("dengue_features_test.csv",header=0)
total=pd.concat(objs=[train,test])
total.week_start_date=pd.to_datetime(total.week_start_date)

total.drop(labels=['ndvi_ne','ndvi_nw','ndvi_se','ndvi_sw','precipitation_amt_mm','station_avg_temp_c','station_diur_temp_rng_c','station_max_temp_c','station_min_temp_c','station_precip_mm'],axis=1,inplace=True)

# although dew point gives better result than humidty hence didn't drop

total.drop(labels=['reanalysis_precip_amt_kg_per_m2','reanalysis_specific_humidity_g_per_kg'],axis=1,inplace=True)

# All temperature units are left in kelvin scale

total.rename(columns={'reanalysis_air_temp_k':'airt','reanalysis_avg_temp_k':'avgt','reanalysis_dew_point_temp_k':'dewt','reanalysis_max_air_temp_k':'maxt','reanalysis_min_air_temp_k':'mint','reanalysis_relative_humidity_percent':'rhum','reanalysis_sat_precip_amt_mm':'precip','reanalysis_tdtr_k':'diurt'},inplace=True)


total['month']=total['week_start_date'].dt.month

# Now grouping data for imputaion
totalgrp=total.groupby(['year','city','month'],as_index=False)

totalgrp=totalgrp.mean()

# precip hase most nas consolidating it should be enough
totalnull=total[total.precip.isnull() & total.airt.isnull()]

totalgrp.drop(labels=['weekofyear'],axis=1,inplace=True)

total.interpolate(inplace=True)

totalnull=totalnull.iloc[:,[0,1,2,3,-1]]

repl=pd.merge(totalnull,totalgrp,on=['year','city','month'])

# this is important else dual index is created and values are not prooperly replaced

total.reset_index(inplace=True)

# remove excess column in total

total.drop(labels='index',axis=1,inplace=True)

#index of values to be replaced

reindx=list(total[total.week_start_date.isin(list(repl.week_start_date))].index)

total.drop(labels=reindx,inplace=True)

total=pd.concat(objs=[total,repl])
# total.count() reveals all columns hence no null values

# now seperating train and test values with train and test values 
total.reset_index(inplace=True)

trainindex=total[total.week_start_date.isin(list(train.week_start_date))].index


testindex=total[total.week_start_date.isin(list(test.week_start_date))].index

test=total.iloc[testindex,:]

train=total.iloc[trainindex,:]

# Now export train and test for future use 
train =pd.read_csv("train.csv",header=0)
test =pd.read_csv("test.csv",header=0)


train.week_start_date=pd.to_datetime(train.week_start_date)
test.week_start_date=pd.to_datetime(test.week_start_date)

# import train and test


sjtrain=train.loc[train.city=='sj',:]
iqtrain=train.loc[train.city!='sj',:]
iqtest=test.loc[test.city=='iq',:]
sjtest=test.loc[test.city=='sj',:]


#make my data time series index it wid date

dcols=sjtrain.columns
dcols=dcols.drop('week_start_date')
dcols=dcols.drop(labels=['city','year','weekofyear','month'])


sjtrain.index=sjtrain.week_start_date
iqtrain.index=iqtrain.week_start_date
iqtest.index=iqtest.week_start_date
sjtest.index=sjtest.week_start_date

sjtrain.drop(labels=['city','year','weekofyear','month'],axis=1,inplace=True)
iqtrain.drop(labels=['city','year','weekofyear','month'],axis=1,inplace=True)
iqtest.drop(labels=['city','year','weekofyear','month'],axis=1,inplace=True)
sjtest.drop(labels=['city','year','weekofyear','month'],axis=1,inplace=True)




model.from_formula('total_cases ~ airt+avgt+dewt+diurt+maxt+mint+precip+rhum',data=sjtrain2).fit()

endog1=sjtrain['total_cases']
exog1=sjtrain.iloc[:,[1,2,3,4,5,6,7,8]]

