# LandslideAnalysis
Hello,

This is a commandline environment utilizing arcpy commands to work with specific landslide analysis data based on the selected county names.

To work with the data, the folder "Directory" has been included.

Contiguous Command (Place the commands on one line separated by spaces):

myclip.py
-f "<Insert filename directory path to georgia counties shapefile>"
-n <"Insert SPACE delimited county NAMES to extract from the counties shapefile">
-ri <"Insert filename directory path to landslide analysis, weighted sum">
-ro <"Insert filename directory path for the raster output (.tif)">

Example:

-f "D:/School/9-Summer 2018/Application Development/Landslide Analysis/Directory/Counties/Counties.shp"
-n "Hall Fulton Forsyth"
-ri "D:/School/9-Summer 2018/Application Development/Landslide Analysis/Directory/Weight/Weight.tif"
-ro "D:/School/9-Summer 2018/Application Development/Landslide Analysis/Directory/Clipped Output/Hall Fulton Forsyth.tif"