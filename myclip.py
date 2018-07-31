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
def main(f, n):
    pass


if __name__ == '__main__':
    main()
