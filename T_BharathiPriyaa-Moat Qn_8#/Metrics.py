__author__ = 'bharathipriyaa'
import pandas as pd
import math
from pandas import DataFrame


def readFiles():
    return (pd.read_csv("csv/total.csv"), pd.read_csv("csv/coke.csv"), pd.read_csv("csv/pepi.csv"))

def calculate_viewability(total_df, coke_df, pepsi_df):
    # Importing the total impressions database
    total=total_df["Moat Impressions"].sum()
    # Calculating the total Viewability metric
    print "######## Advertising choices in decreasing order of viewability ######"
    total_df["Viewability"]=total_df["Moat Impressions"].divide(total)
    print total_df.sort("Viewability", ascending=False)

    print "######## Calculating the Viewability metric for Coke ######"

    total=coke_df["Moat Impressions"].sum()
    coke_df["Unit/Total"]=coke_df["Moat Impressions"].divide(total)
    for index, row in coke_df.iterrows():
        site_name= row['Site']
        coke_total_effect= row['Unit/Total'] * total_df.loc[total_df['Site'] == site_name]['Viewability']
        coke_total_effect=coke_total_effect[coke_total_effect.index._data[0]]
        coke_df.loc[index,'CokeViewability']=coke_total_effect
    print coke_df
    coke_metric= coke_df['CokeViewability'].sum() *coke_df['Moat Impressions'].sum()
    print "Total coke viewability:{0}".format(coke_metric)
    print "######## Calculating the Viewability metric for Pepsi ######"
    total=pepsi_df["Moat Impressions"].sum()
    pepsi_df["Unit/Total"]=pepsi_df["Moat Impressions"].divide(total)
    for index, row in pepsi_df.iterrows():
        site_name= row['Site']
        pepsi_total_effect= row['Unit/Total'] * total_df.loc[total_df['Site'] == site_name]['Viewability']
        pepsi_total_effect=pepsi_total_effect[pepsi_total_effect.index._data[0]]
        pepsi_df.loc[index,'PepsiViewability']=pepsi_total_effect
    print pepsi_df
    pepsi_metric= pepsi_df['PepsiViewability'].sum() *pepsi_df['Moat Impressions'].sum()
    print "Total Pepsi viewability:{0}".format(pepsi_metric)
    if pepsi_metric>coke_metric:
        print "Pepsi's advertising strategy is more effective than Coke w.r.t Viewability metric"
    else:
        print "Coke's advertising strategy is more effective than Pepsi w.r.t Viewability metric"

def calculateAdStickiness(total_df, coke_df, pepsi_df):

    # Calculating the total Ad stickness metric which is total site visits/total site impressions
    print "######## Calculating the Ad stickness metric ######"
    total_site_visits=total_df["SiteVisits"].sum()

    total_df["Stickiness"]=total_df["Moat Impressions"].divide(total_df["SiteVisits"])
    print "#### in increasing  order of AdEffectiveness(increasiness order of stickiness"
    print total_df.sort('Stickiness')
    #calculate the stickiness for coke

    for index, row in coke_df.iterrows():
        site_name= row['Site']
        coke_stickiness= row['Moat Impressions'] * total_df.loc[total_df['Site'] == site_name]['Stickiness']
        coke_stickiness=coke_stickiness[coke_stickiness.index._data[0]]
        coke_df.loc[index,'coke_stickiness']=coke_stickiness
    total_coke_stickiness=coke_df['coke_stickiness'].sum()
    print coke_df

    print 'Coke Strategy: Total number of actual rendered impressions {0}  '.format(total_coke_stickiness)

     #calculate the stickiness for pepsi

    for index, row in pepsi_df.iterrows():
        site_name= row['Site']
        pepsi_stickiness= row['Moat Impressions'] * total_df.loc[total_df['Site'] == site_name]['Stickiness']
        pepsi_stickiness=pepsi_stickiness[pepsi_stickiness.index._data[0]]
        pepsi_df.loc[index,'pepsi_stickiness']=pepsi_stickiness
    total_pepsi_stickiness=pepsi_df['pepsi_stickiness'].sum()
    print pepsi_df

    print 'Pepsi Strategy: Total number of actual rendered impressions {0} '.format(total_pepsi_stickiness)
    if(total_coke_stickiness>total_pepsi_stickiness):
        print 'Strategy of coke is more effective than Pepsi w.r.t Stickiness metric'
    else:
         print 'Strategy of Pepsi is more effective than Coke w.r.t Stickiness metric'
    print "######## End of Ad stickness metric ######"
    return (total_df, coke_df, pepsi_df)

def calculateCPM(total_df, coke_df, pepsi_df):
    print total_df
    print "######## Calculating the CPM metric for Coke ######"
    for index, row in coke_df.iterrows():
        site_name= row['Site']
        coke_cpm= row['Moat Impressions'] * total_df.loc[total_df['Site'] == site_name]['CPM']
        coke_cpm=coke_cpm[coke_cpm.index._data[0]]
        coke_df.loc[index,'coke_CPM']=coke_cpm
    total_coke_stickiness=coke_df['coke_stickiness'].sum()
    total_cost_coke=coke_df['coke_CPM'].sum()
    total_cost_per_impression_coke=total_cost_coke/total_coke_stickiness

    print coke_df

    print "######## Calculating the CPM metric for Pepsi ######"
    for index, row in pepsi_df.iterrows():
        site_name= row['Site']
        pepsi_cpm= row['Moat Impressions'] * total_df.loc[total_df['Site'] == site_name]['CPM']
        pepsi_cpm=pepsi_cpm[pepsi_cpm.index._data[0]]
        pepsi_df.loc[index,'pepsi_cpm']=pepsi_cpm
    total_pepsi_stickiness=pepsi_df['pepsi_stickiness'].sum()
    total_cost=pepsi_df['pepsi_cpm'].sum()
    total_cost_per_impression_pepsi=total_cost/total_pepsi_stickiness

    print pepsi_df


    print 'Coke Strategy: Total cost spent {0} to  actual rendered impressions {1}  '.format(total_cost_coke,total_coke_stickiness)
    print 'Coke Strategy: Total cost per actual rendered impressions {0}'.format(total_cost_per_impression_coke)

    print 'Pepsi Strategy: Total cost spent {0} to  actual rendered impressions {1}  '.format(total_cost,total_pepsi_stickiness)
    print 'Pepsi Strategy: Total cost per  actual rendered impressions {0}  '.format(total_cost_per_impression_pepsi)
    if(total_cost_per_impression_coke<total_cost_per_impression_pepsi):
        print "Coke spent less than Pepsi per impression"
    else:
        print "Pepsi spent less than Coke per impression"
