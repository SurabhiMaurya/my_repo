# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 22:49:51 2018

@author: surbhi
"""


from gmplot import gmplot

# Place map
gmap = gmplot.GoogleMapPlotter(26.8851417, 75.6504706, 10)
# Scatter points
top_attraction_lats, top_attraction_lons = zip(*[
    (26.9198857,75.8194477),#chaura rasta 
    (26.9079421,75.7980539),#ashok nagar
    (26.8466574,75.8073311),#girdhar marg
    (26.9370594,75.8370154),#govind nagar
    (26.8916497,75.7907282),#lalkothi
    (26.9241727,75.7926167),#sindhi camp
    (26.783114,75.8222804),#sitapura
    (26.9167676,75.8109164),#MI road
    (26.8997037,75.8005478),#rambagh
    (26.9555944,75.7685048),#vidyadhar nagar
    (26.9233844,75.8375756),#laxmi narayan puri
    (26.8909816,75.7921027),#sahakar marg
    (26.8317063,75.759542),#takht-e-shahi road
    (26.9015115,75.7608306),#sodala
    (26.8747939,75.7658824),#gopalpura
    (26.8964479,75.7790567),#hawa sarak
    ])
gmap.scatter(top_attraction_lats, top_attraction_lons, '#110011', size=100, marker=False)


# Draw
gmap.draw("1bhk_map.html")