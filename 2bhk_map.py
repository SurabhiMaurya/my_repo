# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 23:22:15 2018

@author: surbhi
"""


from gmplot import gmplot

# Place map
gmap = gmplot.GoogleMapPlotter(26.8851417, 75.6504706, 13)
# Scatter points
top_attraction_lats, top_attraction_lons = zip(*[
    
    (26.9079421,75.7980539),#ashok nagar
    (26.9370594,75.8370154),#govind nagar
    (26.8909816,75.7921027),#sahakar marg
    (26.8964479,75.7790567),#hawa sarak
    (26.8965283,75.7771607),#22-godwon
    (26.9061473,75.8183943),#adarsh nagar
    (26.8890491,75.8040896),#bapu nagar
    (26.9079128,75.7939934),#C scheme
    (26.9006459,75.7318068),#chitrakoot scheme
    (26.8728892,75.7750922),#gopalpura by pass
    (27.0075699,75.7588038),#hamada
    (26.9061148,75.7669022),#jamuna nagar
    (26.8558533,75.7817864),#mahaveer nagar
    (26.8830687,75.7984976),#main tonk road
    (26.8963598,75.7778129),#nandpuri hawa sadak
    (26.8205306,75.8087861),#prabhu dayal marg
    (26.8945295,75.8263396),#rajapark
    (26.8804115,75.7758558),#tonk phatak
    
     ])
gmap.scatter(top_attraction_lats, top_attraction_lons, '#110011', size=100, marker=False)

# Draw
gmap.draw("2bhk_map.html")