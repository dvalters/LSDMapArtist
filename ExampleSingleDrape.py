#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 11:47:22 2017

An example of using the LSDMapArtist to create drape plots

@author: dav
"""

import lsdmapartist as lsdmap

#Directory = "/mnt/SCRATCH/Dev/LSDMappingTools/test_rasters/peak_flow_rasters/"
Directory = "/run/media/dav/SHETLAND/Analyses/HydrogeomorphPaper/peak_flood_maps/boscastle/peak_flood/"
BackgroundRasterName = "Elevations0.asc"
DrapeRasterName = "WaterDepths2400_GRID_HYDRO.asc"
Colourmap = "Blues"
drape_min_threshold = 0.05
colourbar_label = "Water Depths (m)"

#raster = BaseRaster(RasterName, DataDirectory)
dp = lsdmap.DrapePlot(DrapeRasterName, BackgroundRasterName, Directory,
                      Colourmap, drape_min_threshold=drape_min_threshold)

# Customise the DrapePlot
dp.make_drape_colourbar(cbar_label=colourbar_label)
dp.set_coordinate_labels_axis()

dp.show_plot()