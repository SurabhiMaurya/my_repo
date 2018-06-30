# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 14:19:19 2018

@author: surbhi
"""

from gmplot import gmplot

# Place map
gmap = gmplot.GoogleMapPlotter(26.8851417, 75.6504706, 10)
# Scatter points
top_attraction_lats, top_attraction_lons = zip(*[
    (26.9198857,75.8194477),#chaura rasta rd
    (26.9200347,75.8249383),#johri bazar
    (26.8504847,75.8001958),#malviya nagar
    (26.9079421,75.7980539),#ashok nagar
    (26.8466574,75.8073311),#girdhar marg
    (26.9370594,75.8370154),#govind nagar
    (26.8916497,75.7907282),#lalkothi
    (26.9241727,75.7926167),#sindhi camp
    (26.783114,75.8222804),#sitapura
    (26.9167676,75.8109164),#MI road
    (26.8997037,75.8005478),#rambagh
    (26.9555944,75.7685048),#vidyadhar nagar
    ])
gmap.scatter(top_attraction_lats, top_attraction_lons, '#f21804', size=100, marker=False)


# Draw and save file as top10
gmap.draw("top10_hot_ar.html")