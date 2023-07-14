import pandas as pd
import json

from transform.cleaning_dataframe import cleaning_initial_dataframe
from transform.fit_dataframe_for_charts import form_coordinates
from transform.concatenation import concat_config_and_fits
from transform.vizualization import chart
from transform.charts_config import CHARTS


if __name__ == '__main__':
    pd.options.mode.chained_assignment = None
    df = pd.read_csv('11_07_23_cars.csv')
    df = cleaning_initial_dataframe(df)
    fits = form_coordinates(df)
    j = json.dumps(CHARTS, indent=4)
    js = concat_config_and_fits(j, fits, rewrite=True)
    chart(js)
    # print(fits.keys())
    # full_charts = CHARTS
    # for chart in ('fuel', 'make', 'model', 'boxplot', 'price_by_location', 'location', 'year', 'mileage'):
    #     # full_charts[chart]['x'] = fits[chart]['x']
    #     if chart == 'year':
    #         for opt in ('all', 'Volkswagen'):
    #             print(fits[chart][opt]['y'])
    #     else:
    #         print(fits[chart]['y'])
    # fuel_chart(df)
    # top_makers_chart(df)
    # print(df.location.unique())
    # print(os.path.abspath(__file__))
    # l = ['fuel', 'make', 'model', 'price_by_location', 'location', 'year', 'mileage']