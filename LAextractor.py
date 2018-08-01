import click


def get_names(shp):
    """Read data file and return a string of valid names

    >>> get_names('ga.shp')
    'Appling Atkins ... White'

    """
    # stub for future use
    return 'A B C'

@click.command()
@click.option('f', '-f', '--filename', type=str, help='Full file path to county shapefile')
@click.option('n', '-n', '--names', type=str, help='Enter list of space separated names')
@click.option('ri', '-ri', '--rasterin', type=str, help='Enter file path of weighted sum landslide raster')
@click.option('ro', '-ro', '--rasterout', type=str, help='Enter file path to your clipped output raster')
def main(f, n, ri, ro):
    import arcpy
    arcpy.CheckOutExtension("Spatial")
    arcpy.MakeFeatureLayer_management(f, "counties_lyr")
    names = ["NAME = '{}'".format(name) for name in n.split()]
    delim = " OR ".join(names)
    arcpy.SelectLayerByAttribute_management("counties_lyr", "NEW_SELECTION", delim)
    # Name:Extract counties.lyr
    # Description: Extract county based data from landslide analysis raster
    outExtractByMask = arcpy.sa.ExtractByMask(ri, "counties_lyr")
    outExtractByMask.save(ro)

if __name__ == '__main__':
    main()
