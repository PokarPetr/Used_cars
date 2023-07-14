import numpy as np
import pandas as pd
def form_coordinates(df):
    """
    Form x, y, and y2 coordinates to draw the following charts:
    Distribution cars by fuel(only x and y)
    The top 15 carmakers with average price(all three coordinates),
    The top 15 models with average price(all three coordinates),
    Prices boxplot of the top 15 models(only x and y)
    Distribution cars by year of production with average price(all three coordinates),
    Distribution by location with average price(all three coordinates),
    Distribution car prices by location(only x and y)
    Distribution car by mileage(only x and y)
    """

    fits = {}
    x_fuel = tuple(df.fuel.value_counts(sort=True, normalize=True, ascending=False).keys())
    y_fuel = tuple(df.fuel.value_counts(sort=True, normalize=True, ascending=False).values)
    fits['fuel'] = dict(x=x_fuel, y=y_fuel)
    l_top = ['make', 'model', 'location']
    for name in l_top:
        if name == 'location':
            top = df[name].value_counts(normalize=True)
            x_a = tuple(df.groupby(name, sort=False).price.mean().sort_values(ascending=False).keys())
            y_a = tuple(round(df.groupby(name, sort=False).price.mean().sort_values(ascending=False), 0).values)
            fits['price_by_location'] = dict(x=x_a, y=y_a)
        else:
            top = df[name].value_counts(normalize=True).head(15)
        x = tuple(top.keys())
        temp = df[df[name].isin(x)]

        temp['order'] = [x.index(val) for val in temp[name]]
        temp.sort_values(by=['order'], inplace=True)
        y2 = tuple(round(temp.groupby(name, sort=False).price.mean(), 0).values)
        fits[name] = dict(x=x, y=tuple(top.values), y2=y2)
        if name == 'model':
            y_box = temp.groupby(name, sort=False)
            fits['boxplot'] = dict(x=x, y=temp.to_json())

    l_year = ['all', 'Volkswagen']
    fits['year'] = {}
    for name in l_year:
        if name == 'all':
            temp = df
        else:
            temp = df[df['make'] == name]
        x_year = tuple(temp.groupby('year').price.mean().keys())
        y_year = tuple(temp.sort_values(by=['year']).year.value_counts(sort=False, normalize=True).values)
        y_price_year = tuple(temp.groupby('year').price.mean().values)
        if name == 'all':
            fits['year'] = {'x': x_year, 'y': y_year, 'y2': y_price_year}
        else:
            car_name = ''.join(['year_', name])
            fits[car_name] = {'x': x_year, 'y': y_year, 'y2': y_price_year}

    rang = np.arange(0, 500001, 25000)
    rang = [''.join([str(int(i / 1000)), 'K']) for i in rang]
    rang[0] = '0'
    df['intervals'] = pd.cut(df['distance'], bins=21, precision=0)
    df['left_edge'] = [interval.left for interval in df['intervals']]
    y_mileage = tuple(df.sort_values(by=['left_edge']).left_edge.value_counts(sort=False, normalize=True).values)
    fits['mileage'] = dict(x=tuple(rang), y=y_mileage)

    return fits




