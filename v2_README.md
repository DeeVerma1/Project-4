# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 4: Group Project
---
## Team Members
(alphabetical order)
- Resende, Silvia
- Verma, Deepika
- Wong, Daniel

## Problem Statement

COVID-19 has been with us for 2 years now, with most people fully vaccinated and boosted in most states, while less so in others, theoretically making this less vaccinated segment of the population more vulnerable to infection and hospitalization. While we are not domain experts in epidemiology or public policy, health authorities, aware of their own biases and mindsets, sought a different perspective by tasking us (as data scientists/analysts) with drawing insights from data on covid-19 vaccination, surveillance, and death rates to inform resource allocation decisions, such as:

1. where to distribute covid anti-viral therapeutics
2. where to focus outreach/education campaigns to make people aware of these therapeutics

in efforts to prevent future surges, hospitalizations, and deaths. Through rigorous exploratory data analysis, we sought to determine the extent to which the data shows patterns and correlation between different parameters such as new cases, hospitalization, and vaccination rates. 

This project also aims to use classification models, such as logistic regression, to make some predictions and inferences, as well as a time series model to predict new cases, translating into recommendations for which states might need more anti-viral therapeutics, based on new case numbers and percent of people vaccinated in those states.

## Definition of Success
We define success as identifying states that may need additional resources based on the number of new cases and percentage of people vaccinated, as well as initial times series and classification models that seek to predict the number of new cases and identify the factors most relevant to hospitalizations, which will further inform resource allocation decisions.

## Items in this Repo
1) "code" folder containing:

    - Data Collection
           
        - "01 - Webscraping_Data_Collection.ipynb" (webscraping for COVID surveillance data collection)
    
    - Exploratory Data Analysis jupyter notebooks:

        - "02.1 - EDA_COVID_Cases.ipynb" (examining the covid cases and death dataset)
        - "02.2 - EDA_Vaccination.ipynb" (examining the covid vaccinations dataset)
        - "02.3 - EDA_COVID_Surveillance.ipynb" (examining the covid surveillance dataset)
        - "02.4 - EDA Travel Data.ipynb" (examining the travel data during COVID pandemic)
     

     - Model Tuning jupyter notebook:
     
        - "03.3 - Model-Tuning-Surveillance.ipynb"



2) "Data" folder containing:

    - CSVs of the datasets:
        - United_States_COVID-19_Cases_and_Death_by_State_over_Time.csv
        - covid_vaccination.csv
        - covid_surveillance.csv


3) "Data Dictionaries" folder containing:

    - Text files of data dictionaries (see "Data" section below for data source and description):
        - covid_deaths_data_dict.txt
        - covid_vacc_data_dict.txt
        - covid_surr_data_dict.txt

4) streamlit folder

## The Data 


We used the following COVID-19 datasets from the Centers for Disease Control and Prevention (CDC) website for our analysis:


* [`covid_cases_deaths_by_state_over_time.csv`](./data/United_States_COVID-19_Cases_and_Deaths_by_State_over_Time.csv) | [data dictionary](https://github.com/DeeVerma1/Project-4/blob/main/Data%20Dictionaries/covid_deaths_data_dict.txt)
    - Description: This dataset contains archived aggregate daily counts of COVID-19 cases and deaths by state. The data covers the period from January 2020 to October 2022. Source: https://data.cdc.gov/Case-Surveillance/United-States-COVID-19-Cases-and-Deaths-by-State-o/9mfq-cb36


* [`covid_vaccination_trends.csv`](./data/covid_vaccination_trends.csv) | [data dictionary](https://github.com/DeeVerma1/Project-4/blob/main/Data%20Dictionaries/covid_vacc_data_dict.txt)
    - Description: Overall Trends in Number of COVID-19 Vaccinations in the US at national and jurisdictional levels. Data represents all vaccine partners including jurisdictional partner clinics, retail pharmacies, long-term care facilities, dialysis centers, Federal Emergency Management Agency and Health Resources and Services Administration partner sites, and federal entity facilities. The data covers the period from December 2020 to June 2022. Source: https://data.cdc.gov/Vaccinations/COVID-19-Vaccination-Trends-in-the-United-States-N/rh2h-3yt2


* [`covid_surveillance.csv`](./data/covid_surveillance.csv) | [data dictionary](https://github.com/DeeVerma1/Project-4/blob/main/Data%20Dictionaries/covid_surr_data_dict.txt) 
    - Description: This case surveillance public use dataset has 19 elements for all COVID-19 cases shared with CDC and includes demographics, geography (county and state of residence), any exposure history, disease severity indicators and outcomes, and presence of any underlying medical conditions and risk behaviors. The data covers the period from March 2020 to September 2022. Source: https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data-with-Ge/n8mc-b4w4

* [`covid_travel.csv`] too big to include on github | [data dictionary](https://github.com/DeeVerma1/Project-4/blob/main/Data%20Dictionaries/covid_travel_data_dict.txt) 
    - Description: This dataset includes entries for travel information during Covid time. The travel statistics are produced from an anonymized national panel of mobile device data from multiple sources. All data sources used in the creation of the metrics contain no personal information. Data analysis is conducted at the aggregate national, state, and county levels. A weighting procedure expands the sample of millions of mobile devices, so the results are representative of the entire population in a nation, state, or county. Source: https://data.bts.gov/Research-and-Statistics/Trips-by-Distance/w96p-f2qv


## Approach
We used the following criteria to identify states that might need additional resources:

- The percentage of people in a state with both a primary series and booster
- Monthly new cases in each state

We posit that states with a recent uptick in new cases and a relatively low percentage of people with both a primary series and a booster makes the population more susceptible to illness and may require additional anti-viral therapeutics to deal with a potential increase in hospitalizations. We chose to look at the percentage of people with both a primary series and a booster versus just a primary series because we assess it provides a clearer picture of the population's current immunization as the effectiveness from just a primary series may have waned over time.

## Modeling/Prediction

To further aid resource allocation efforts, we also created models to predict the number of new covid cases and identify factors most relevant to hospitalizations in the US in the short-term, which we can later fine-tune to apply to the state-wide level, particularly to those states assessed to need additional resources based on the criteria outlined above.

- A time series model to predict new covid cases

- Binary classification models to identify the extent to which factors, such as age, sex, race, and location (state), contribute to a person being hospitalized versus not hospitalized. We will try different classification techniques and look at the balanced accuracy and recall as our evaluation metrics with target >0.65 for each, especially recall because we'd rather err on the side of caution and hospitalize someone who we later find out to not have covid (false positive), rather than not hospitalize a person who we later find out to have covid.

## Findings/Recommendations

- North Carolina experienced an uptick in new covid cases over the past months (471) and have the lowest percentage of people with both a primary series and booster among all states, 28% suggesting we should allocate additional anti-viral therapeutics to this state, at least in the near-term, to prepare for any upticks in demand.

The choropleth plot below show colormap of number of cases in the states for Sept-2022.
 ![This is an image](./images/word_count_distn.png)
 
The choropleth plot below show color map of percent of population with completed primary series and a booster as of June 2022.
 ![This is an image](./images/word_count_distn.png)
 
 From the plots above, North Carolina is one of the states with highest no. of cases and lowest percentage of vaccinated population.


- As is usually the case with time series predictions, accurately predicting new covid cases proved difficult, but was made moreso by our lack of additional features such as exongenous variables that could have improved accuracy. There are most likely hundreds of factors that contribute to new covid cases, and since we lack the domain knowledge and resources to create a truly comprehensive time series model, the model we did create will serve as the foundation for further exploration and refinement.

- Heavily imbalanced classes affected the performance of our logistic regression model to classify hospitalized versus not hospitalized even after applying undersampling techniques. Our baseline accuracy was 96% for the target variable. Our production model (Logistic Regression with Undersampling)  has a **Balanced Accuracy of 0.75** and **Recall of 0.75.**
  
The table below shows top 10 significant factors in determining hospitalization of a patient.
![This is an image](./images/word_count_distn.png)

It shows that the age groups 65+ year and 50-64 year and some of the locations like NJ and KS are among the five most significant factors that affect the hospitalization. This gives an insight on possible guiding factors in helping prepare for upcoming surges. For example, if someone is in age group 65+, they are 27 times (looking at the exp_coefficient) as likely to be hospitalized when compared to someone in 1-17 years age group. This suggests that the states/counties that have higher population in these age groups might need more resource allocations, support and preparations to prevent hospitalizations. The table also lists some of the states like New Jersey and Kensas indicating that there might be location specific factors, like population density, population's inclination towards getting vaccinated etc. that can be further analyzed to help guide the proper resource allocations. 

## Streamlit App
-A Streamlit app was create for visualization and exploration of the findings of this project.

## Potential Areas for Model Improvement
- Classification model: add data to balance out the imbalanced classes, and other factors beyond age, race, sex, and location that might factor into a person's chances of being hospitalzed.

- Time series model: add features to Vector Autoregression and/or ARIMA exogenous models, such as number of people traveling (by air, car) over the same time period to see how it might affect accuracy of predicting new cases. 



---

