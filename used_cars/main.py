import pandas as pd
import json

from transform.cleaning_dataframe import cleaning_initial_dataframe
from transform.fit_dataframe_for_charts import form_coordinates
from transform.concatenation import concat_config_and_fits
from transform.vizualization import chart
from transform.charts_config import CHARTS

pd.options.mode.chained_assignment = None
df = pd.read_csv('11_07_23_cars.csv')
df = cleaning_initial_dataframe(df)
fits = form_coordinates(df)
j = json.dumps(CHARTS, indent=4)
js = concat_config_and_fits(j, fits, rewrite=True)
chart(js)

if __name__ == '__main__':
    pass
