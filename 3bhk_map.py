# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 00:00:21 2018

@author: surbhi
"""


from gmplot import gmplot

# Place map
gmap = gmplot.GoogleMapPlotter(26.8851417, 75.6504706, 10)
# Scatter points
top_attraction_lats, top_attraction_lons = zip(*[
  
    (26.8909816,75.7921027),#sahakar marg
    (26.9061473,75.8183943),#adarsh nagar
    (26.8890491,75.8040896),#bapu nagar
    (26.9079128,75.7939934),#C scheme
    (26.8963598,75.7778129),#nandpuri hawa sadak
    (26.8945295,75.8263396),#rajapark
    (26.9079421,75.7980539),#ashok nagar
    (26.8665057,75.7940857),#bajaj nagar
    (26.9433195,75.8084808),#brahmpuri
    (26.8889089,75.7380051),#brijlapura
    (26.9625993,75.7718827),#cental spine
    (26.9073357,75.7734218),#civil lines
    (26.9009732,75.7684349),#elevatd ajmer road
    (26.8541403,75.8577789),#ghati karolan
    (26.8538759,75.7954121),#jai jawan colony
    (26.9200347,75.8249383),#johri bazar
    (26.8916497,75.7907282),#lalkothi
    (26.8504847,75.8001958),#malviya nagar
    (26.8317063,75.759542),#takht-e-shahi rd
    
     ])
gmap.scatter(top_attraction_lats, top_attraction_lons, '#110011', size=100, marker=False)

# Draw
gmap.draw("3bhk_map.html")
