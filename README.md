# DengAI-Predicting-Disease-Spread
Using environmental data collected by various U.S. Federal Government agencies—from the Centers for Disease Control and Prevention to the National Oceanic and Atmospheric Administration in the U.S. Department of Commerce—I have to predict the number of dengue fever cases reported each week in San Juan, Puerto Rico and Iquitos, Peru. The goal of the competition is to develop a prediction model that would be able to anticipate the cases of dengue in every country depending on a set of climate variables mentioned above.



# Imputing the missing values with mean
Since these are time-series, I saw many NaN values. Since I can't build a model without those values, I'll take a simple approach and just fill those values with the mean value. Initially I thought this is probably a good part of the problem to improve your score by getting smarter. First, I use mean imputation


# Imputing the missing values with ffill()

I'll take a simple approach and just fill those values with the most recent value that I saw up to that point. This is probably a good part of the problem to improve your score by getting smarter.With time series data, using pad/ffill is extremely common so that the “last known value” is available at every time point. First, I use mean imputation, however in case of time series data, a forward The ffill() function imputation might be more appropriate.

The ffill() function is equivalent to fillna(method='ffill') and bfill() is equivalent to fillna(method='bfill')

fillna(method='ffill') replace NaNs by preceding values in pandas DataFrame


# Distribution of labels

Our target variable, total_cases is a non-negative integer, which means we're looking to make some count predictions. Standard regression techniques for this type of prediction include Poisson regression and negative binomial regression. Which technique will perform better depends on many things, but the choice between Poisson regression and negative binomial regression is pretty straightforward. Poisson regression fits according to the assumption that the mean and variance of the population distribution are equal. When they aren't, specifically when the variance is much larger than the mean, the negative binomial approach is better.

# Compute the data correlation matrix

Our next step in this process will be to select a subset of features to include in our regression. Our primary purpose here is to get a better understanding of the problem domain rather than eke out the last possible bit of predictive accuracy. The first thing I will do is to add the total_cases to our data frame, and then look at the correlation of that variable with the climate variables.


Many of the temperature data are strongly correlated, which is expected. But the total_cases variable doesn't have many obvious strong correlations. Interestingly, total_cases seem to only have weak correlations with other variables. Many of the climate variables are much more strongly correlated. Interestingly, the vegetation index also only has weak correlation with other variables. These correlations may give us some hints as to how to improve our model that I'll talk about later in this post. For now, let's take a sorted look at total_cases correlations.

# Many of the temperature data are strongly correlated, which is expected. But the total_cases variable doesn't have many obvious strong correlations


# Dropping least correlated variables from the train data:

After looking into the correlation matrix it’s better to drop the variables which are least correlated with the predicted variable i.e total_cases here in this case for better results. 

# I have drooped the least correlated variables with total_cases and they are to name of few:

	ndvi_se – Pixel southeast of city centroid
	ndvi_sw – Pixel southwest of city centroid
	ndvi_ne – Pixel northeast of city centroid
	station_diur_temp_rng_c – Diurnal temperature range
	reanalysis_tdtr_k – Diurnal temperature range
ndvi_nw – Pixel northwest of city centroid 


# My primary analysis is:
	Because dengue fever is a tropical disease, I would expect it to be more popular in place with high temperature, high precipitation and thus high humidity.
	The disease is transmitted by mosquitoes, whose peak season is summer, so I will expect summer to have more dengue cases than the rest of the year.
	Iquitos is a Peruvian port city  and surrounded by green spaces and water sources, it is an ideal environment for mosquitoes. San juan, in the other hand, is a city on an island (more isolated) and has a much lower population density than Iquitos. All these information’s suggest that I will need 2 separate models, one for each city.
	The correlation strengths differ for each city, but it looks like reanalysis_specific_humidity_g_per_kg and reanalysis_dew_point_temp_k are the most strongly correlated with total_cases. This makes sense: I know mosquitos thrive wet climates, the wetter the better!
	As we all know, "cold and humid" is not a thing. So, it's not surprising that as minimum temperatures, maximum temperatures, and average temperatures rise, the total_cases of dengue fever tend to rise as well.
	Interestingly, the precipitation measurements bear little to no correlation to total_cases, despite strong correlations to the humidity measurements, as evident by the heatmaps above.

# This folder contains 3 scripts of four different Models.
	Model-1 Generalized Linear Models (best accuracy model) score 25.6010
	Model-2 Negative binomial regression Score 25.9976
	Model-3 Neural Networks & Forecasting 26.2933	
  
# Tips 

For better visualization I would recommended python packages like seaborn as sns , matplotlib.pyplot.
In the python the package ‘statsmodels.formula.api’ was very useful to do the statistical modeling in the given data.

