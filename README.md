# LandslideAnalysis
Hello,

This is a commandline environment utilizing arcpy commands to work with specific landslide analysis data based on the selected county names.

To work with the data, the folder "Directory" has been included.

Contiguous Command (Place the commands on one line separated by spaces):

Extractor.py
-f "<Insert filename directory path to georgia counties shapefile>"
-n <"Insert SPACE delimited county NAMES to extract from the counties shapefile">
-ri <"Insert filename directory path to landslide analysis, weighted sum">
-ro <"Insert filename directory path for the raster output (.tif)">

Example:
LAExtractor.py
-f "C:\Users\rkband8493\Desktop\LandslideAnalysis/Directory/Counties/Counties.shp"
-n "Hall Fulton Forsyth"
-ri "C:\Users\rkband8493\Desktop\LandslideAnalysis\Directory\WeightWeight.tif"
-ro "C:\Users\rkband8493\Desktop\LandslideAnalysis\Directory\Clipped Output/Hall Fulton Forsyth.tif"