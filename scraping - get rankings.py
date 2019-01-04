#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 28 22:19:11 2017

@author: CPMcIntyre
"""

import requests as re
from bs4 import BeautifulSoup as bs
import pandas as pd
import os
import datetime as dt

date1=dt.date(year=2018, month=11, day=21)
rankinglist = os.listdir('/Users/cpmcintyre/Documents/basketball/data/ranking')
opprankinglist = os.listdir('/Users/cpmcintyre/Documents/basketball/data/rankingopponent')




def getRanking(fmtdt):
    print(fmtdt)
    ht='http://www.basketball-reference.com/friv/standings.fcgi?month='+ str(date1.month) +'&day='+str(date1.day)+'&year='+ str(date1.year) +'&lg_id=NBA'
    print(ht)
    r=re.get(ht)
    k=open('/Users/cpmcintyre/Documents/basketball/dateandrank/'+ fmtdt +'.txt', 'wb')
    k.write(r.content)
    k.close()
    k=open('/Users/cpmcintyre/Documents/basketball/dateandrank/'+ fmtdt +'.txt', 'r')
    msg=''
    for j in k:
        if ('<!--' in j) and ('-->' in j):
            msg=msg+' ' + j
        if '<!--' in j:
                continue
        elif '-->' in j:
                continue
        else:
            msg=msg+' ' + j
    soup=bs(msg,"lxml")            
    tbl=soup.find_all('div', attrs={"id":"all_team", "class":"table_wrapper setup_commented commented"})
    if len(tbl)==0:
        print('out')
    else:
        tb1=tbl[0].find_all('div', attrs={'class':"table_outer_container"})
        tb2=tbl[0].find_all('tbody')
        tb3=tb2[0].find_all('tr')
    
        cols=['Rank',
             'TeamName',
             'GamesPlayed',
             'MinutesPlayed',
             'FieldGoals',
             'FieldGoalAttempts',
             'FieldGoalPercent',
             '3Point',
             '3PointAttempts',
             '3PointPercent',
             '2PFieldGoals',
             '2PFieldGoalAttempts',
             '2PFieldGoalPercent',
             'FreeThrows',
             'FreeThrowAttempts',
             'FreeThrowPercentage',
             'OffensiveRebounds',
             'DefensiveRebounds',
             'TotalRebounds',
             'Assists',
             'Steals',
             'Blocks',
             'Turnovers',
             'PersonalFouls',
             'Points']
    
        data=[]
        for ele in tb3:
            #'Rank',
            rnk=None
            if ele.find('th',attrs={'data-stat':'ranker'}).string !=None:
                rnk=ele.find('th',attrs={'data-stat':'ranker'}).string,
            else:
                rnk=-1,
            dta=[int(rnk[0]),
            #'TeamName',
            ele.find('td',attrs={'data-stat':'team_name'}).string,
            #'GamesPlayed',
            int(ele.find('td',attrs={'data-stat':'g'}).string),
            #'MinutesPlayed',
            int(ele.find('td',attrs={'data-stat':'mp'}).string),
            #'FieldGoals',
            int(ele.find('td',attrs={'data-stat':'fg'}).string),
            #'FieldGoalAttempts',
            int(ele.find('td',attrs={'data-stat':'fga'}).string),
            #'FieldGoalPercent',
            float(ele.find('td',attrs={'data-stat':'fg_pct'}).string),
            #'3Point',
            int(ele.find('td',attrs={'data-stat':'fg3'}).string),
            #'3PointAttempts',
            int(ele.find('td',attrs={'data-stat':'fg3a'}).string),
            #'3PointPercent',
            float(ele.find('td',attrs={'data-stat':'fg3_pct'}).string),
            #'2PFieldGoals',
            int(ele.find('td',attrs={'data-stat':'fg2'}).string),
            #'2PFieldGoalAttempts',
            int(ele.find('td',attrs={'data-stat':'fg2a'}).string),
            #'2PFieldGoalPercent',
            float(ele.find('td',attrs={'data-stat':'fg2_pct'}).string),
            #'FreeThrows',
            int(ele.find('td',attrs={'data-stat':'ft'}).string),
            #'FreeThrowAttempts',
            int(ele.find('td',attrs={'data-stat':'fta'}).string),
            #'FreeThrowPercentage',
            float(ele.find('td',attrs={'data-stat':'ft_pct'}).string),
            #'OffensiveRebounds',
            int(ele.find('td',attrs={'data-stat':'orb'}).string),
            #'DefensiveRebounds',
            int(ele.find('td',attrs={'data-stat':'drb'}).string),
            #'TotalRebounds',
            int(ele.find('td',attrs={'data-stat':'trb'}).string),
            #'Assists',
            int(ele.find('td',attrs={'data-stat':'ast'}).string),
            #'Steals',
            int(ele.find('td',attrs={'data-stat':'stl'}).string),
            #'Blocks',
            int(ele.find('td',attrs={'data-stat':'blk'}).string),
            #'Turnovers',
            int(ele.find('td',attrs={'data-stat':'tov'}).string),
            #'PersonalFouls',
            int(ele.find('td',attrs={'data-stat':'pf'}).string),
            #'Points'
            int(ele.find('td',attrs={'data-stat':'pts'}).string)
        ]
            data.append(dta)
        #print(data)
        rank=pd.DataFrame(data,columns=cols)
        print(rank.shape)
        rank.to_csv('/Users/cpmcintyre/Documents/basketball/Data/Ranking/'+ fmtdt +'.csv')
        k.close()

def oppRanking(fmtdt):
    k=open('/Users/cpmcintyre/Documents/basketball/dateandrank/'+ fmtdt +'.txt', 'r')
    msg=''
    for j in k:
        if ('<!--' in j) and ('-->' in j):
            msg=msg+' ' + j
        if '<!--' in j:
                continue
        elif '-->' in j:
                continue
        else:
            msg=msg+' ' + j
    soup=bs(msg,"lxml")       
    tbl=soup.find_all('div', attrs={"id":"all_opponent", "class":"table_wrapper setup_commented commented"})
    if len(tbl)==0:
        print('opp out')
    else:
        tb1=tbl[0].find_all('div', attrs={'class':"table_outer_container"})
        tb2=tbl[0].find_all('tbody')
        tb3=tb2[0].find_all('tr')
    
        cols=['Rank',
             'TeamName',
             'GamesPlayed',
             'MinutesPlayed',
             'FieldGoals',
             'FieldGoalAttempts',
             'FieldGoalPercent',
             '3Point',
             '3PointAttempts',
             '3PointPercent',
             '2PFieldGoals',
             '2PFieldGoalAttempts',
             '2PFieldGoalPercent',
             'FreeThrows',
             'FreeThrowAttempts',
             'FreeThrowPercentage',
             'OffensiveRebounds',
             'DefensiveRebounds',
             'TotalRebounds',
             'Assists',
             'Steals',
             'Blocks',
             'Turnovers',
             'PersonalFouls',
             'Points']
    
        data1=[]
        for ele in tb3:
            #'Rank',
            rnk=None
            if ele.find('th',attrs={'data-stat':'ranker'}).string !=None:
                rnk=ele.find('th',attrs={'data-stat':'ranker'}).string,
            else:
                rnk=-1,
            dta1=[int(rnk[0]),
            #'TeamName',
            ele.find('td',attrs={'data-stat':'team_name'}).string,
            #'GamesPlayed',
            int(ele.find('td',attrs={'data-stat':'g'}).string),
            #'MinutesPlayed',
            int(ele.find('td',attrs={'data-stat':'mp'}).string),
            #'FieldGoals',
            int(ele.find('td',attrs={'data-stat':'opp_fg'}).string),
            #'FieldGoalAttempts',
            int(ele.find('td',attrs={'data-stat':'opp_fga'}).string),
            #'FieldGoalPercent',
            float(ele.find('td',attrs={'data-stat':'opp_fg_pct'}).string),
            #'3Point',
            int(ele.find('td',attrs={'data-stat':'opp_fg3'}).string),
            #'3PointAttempts',
            int(ele.find('td',attrs={'data-stat':'opp_fg3a'}).string),
            #'3PointPercent',
            float(ele.find('td',attrs={'data-stat':'opp_fg3_pct'}).string),
            #'2PFieldGoals',
            int(ele.find('td',attrs={'data-stat':'opp_fg2'}).string),
            #'2PFieldGoalAttempts',
            int(ele.find('td',attrs={'data-stat':'opp_fg2a'}).string),
            #'2PFieldGoalPercent',
            float(ele.find('td',attrs={'data-stat':'opp_fg2_pct'}).string),
            #'FreeThrows',
            int(ele.find('td',attrs={'data-stat':'opp_ft'}).string),
            #'FreeThrowAttempts',
            int(ele.find('td',attrs={'data-stat':'opp_fta'}).string),
            #'FreeThrowPercentage',
            float(ele.find('td',attrs={'data-stat':'opp_ft_pct'}).string),
            #'OffensiveRebounds',
            int(ele.find('td',attrs={'data-stat':'opp_orb'}).string),
            #'DefensiveRebounds',
            int(ele.find('td',attrs={'data-stat':'opp_drb'}).string),
            #'TotalRebounds',
            int(ele.find('td',attrs={'data-stat':'opp_trb'}).string),
            #'Assists',
            int(ele.find('td',attrs={'data-stat':'opp_ast'}).string),
            #'Steals',
            int(ele.find('td',attrs={'data-stat':'opp_stl'}).string),
            #'Blocks',
            int(ele.find('td',attrs={'data-stat':'opp_blk'}).string),
            #'Turnovers',
            int(ele.find('td',attrs={'data-stat':'opp_tov'}).string),
            #'PersonalFouls',
            int(ele.find('td',attrs={'data-stat':'opp_pf'}).string),
            #'Points'
            int(ele.find('td',attrs={'data-stat':'opp_pts'}).string)
        ]
            data1.append(dta1)
        #print(data)
        rank=pd.DataFrame(data1,columns=cols)
        print(rank.shape)
        rank.to_csv('/Users/cpmcintyre/Documents/basketball/Data/RankingOpponent/'+ fmtdt +'.csv')
        k.close()
   
for i in range(1,10320):
    date1=date1+dt.timedelta(days=1)
    if date1==dt.date.today():
        break
    fmtdate=str(date1.year)+'-'+str(date1.month)+ '-'+ str(date1.day)
    if fmtdate+'.csv' in rankinglist:
        pass
    else:
        getRanking(fmtdate)
        
    if fmtdate+'.csv' in opprankinglist:
        pass
    else:
        oppRanking(fmtdate)