def cleaning_initial_dataframe(df):
    """
    Taking the initial data frame.
    Get rid of column 'resource'.
    If the location is not in the list 'location', get rid of rows.
    Change the Serbian version of the fuel name to English.
    Take rows if year >= 2000
    Get rid of outliers :
        mileage > 500K km,
        100 < price <= 100K euro.

    """
    if 'resource' in df.columns:
        df.drop('resource', axis=1, inplace=True)

    location = ('Danilovgrad', 'Podgorica', 'Bar', 'Herceg Novi', 'Bijelo Polje',
           'Pljevlja', 'Nikšić', 'Berane', 'Cetinje', 'Budva', 'Kotor',
           'Ulcinj', 'Tivat', 'Rožaje', 'Kolašin', 'Andrijevica', 'Mojkovac',
           'Žabljak', 'Plav',
           'Petnjica', 'Šavnik')
    df = df[df.location.isin(location)]

    fuel_dict = {
        'Dizel': 'Diesel',
        'Benzin': 'Gasoline',
        'Hibrid': 'Hybrid',
        'Benzin+Plin': 'Gasoline + Gas',
        'Električno': 'Electric'
    }
    df.fuel = [fuel_dict[f] for f in df.loc[:,'fuel']]

    df = df[df.year > 1999]
    df = df[df.distance <= 500000]
    df = df[df.price <= 100000]
    df = df[df.price > 100]
    df.reset_index(drop=True, inplace=True)

    return df
