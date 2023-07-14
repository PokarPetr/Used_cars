CHARTS = {
    'fuel': {
        'title': {'label': 'Distribution of the number of cars by type of fuel', 'fontsize': 22}
        , 'twinx': False
        , 'figsize': (12, 3.75)
        , 'bar_color': ['white']
        , 'edge_color': 'grey'
        , 'line_color': 'grey'
        , 'x_label': ''
        , 'y_label': {'label': 'Share of all cars', 'fontsize': 15, 'color': 'black'}
        , 'x_ticks': {'rot': 0, 'fontsize': 15, 'ha': 'center', 'ticks': None}
        , 'y_ticks': {'1': {'rot': 0, 'fontsize': 15, 'va': 'center', 'ticks': None}
            , '2': {'rot': 0, 'fontsize': 15, 'va': 'center'}}
        , 'legend': None
        , 'file_name': 'Distribution_by_fuel.png'
    }
    , 'make': {
        'title': {'label': 'Distribution of the top 15 car manufacturers with average price of cars', 'fontsize': 22}
        , 'twinx': True
        , 'bar_color': ['#EDA461']
        , 'edge_color': '#EDA461'
        , 'line_color': 'grey'
        , 'x_label': ''
        , 'y_label': {'label': 'Share of all cars', 'fontsize': 14, 'color': 'black'}
        , 'x_ticks': {'rot': 22, 'fontsize': 14, 'ha': 'right', 'ticks': None}
        , 'y_ticks': {'1': {'rot': 0, 'fontsize': 14, 'va': 'center', 'ticks': None}
            , '2': {'rot': 0, 'fontsize': 15, 'va': 'center', 'ticks': None}}
        ,
        'legend': {'label': 'Average car price [Euro]', 'loc': (0.57, 0.87), 'facecolor': 'white', 'edgecolor': 'white',
                   'figsize': 14}
        , 'file_name': 'The_top_15_carmakers_distribution.png'
    }
    , 'model': {
        'title': {'label': 'Distribution of the top 15 car models', 'fontsize': 22}
        , 'twinx': True
        , 'bar_color': ['#EDA461']
        , 'edge_color': '#EDA461'
        , 'line_color': 'grey'
        , 'x_label': ''
        , 'y_label': {'label': 'Share of all cars', 'fontsize': 14, 'color': 'black'}
        , 'x_ticks': {'rot': 22, 'fontsize': 14, 'ha': 'right', 'ticks': None}
        , 'y_ticks': {'1': {'rot': 0, 'fontsize': 14, 'va': 'center', 'ticks': None}
            , '2': {'rot': 0, 'fontsize': 14, 'va': 'center', 'ticks': None}}
        ,
        'legend': {'label': 'Average car price [Euro]', 'loc': (0.57, 0.87), 'facecolor': 'white', 'edgecolor': 'white',
                   'figsize': 14}
        , 'file_name': 'The_top_15_models_distribution.png'
    }
    , 'year': {
        'title': {'label': 'Distribution of all cars by the year of manufacture', 'fontsize': 22}
        , 'twinx': True
        , 'bar_color': ['white']
        , 'edge_color': 'grey'
        , 'line_color': '#EDA461'
        , 'x_label': ''
        , 'y_label': {'label': 'Share of all cars', 'fontsize': 14, 'color': 'black'}
        , 'x_ticks': {'rot': 0, 'fontsize': 14, 'ha': 'center', 'ticks': 2}
        , 'y_ticks': {'1': {'rot': 0, 'fontsize': 14, 'va': 'center', 'ticks': None}
            , '2': {'rot': 0, 'fontsize': 15, 'va': 'center', 'ticks': None}}
        ,
        'legend': {'label': 'Average car price [Euro]', 'loc': (0.50, 0.87), 'facecolor': 'white', 'edgecolor': 'white',
                   'figsize': 14}
        , 'file_name': 'Distribution_all_cars_by_year.png'
    }
    , 'year_Volkswagen': {
        'title': {'label': 'Distribution of the Volkswagen by the year of manufacture', 'fontsize': 22}
        , 'twinx': True
        , 'bar_color': ['white']
        , 'edge_color': 'grey'
        , 'line_color': '#EDA461'
        , 'x_label': ''
        , 'y_label': {'label': 'Share of all cars', 'fontsize': 14, 'color': 'black'}
        , 'x_ticks': {'rot': 0, 'fontsize': 14, 'ha': 'center', 'ticks': 2}
        , 'y_ticks': {'1': {'rot': 0, 'fontsize': 14, 'va': 'center', 'ticks': None}
            , '2': {'rot': 0, 'fontsize': 14, 'va': 'center', 'ticks': None}}
        ,
        'legend': {'label': 'Average car price [Euro]', 'loc': (0.50, 0.87), 'facecolor': 'white', 'edgecolor': 'white',
                   'figsize': 14}
        , 'file_name': 'Distribution_Volkswagen_by_year.png'
    }
    , 'location': {
        'title': {'label': 'Distribution of all cars by location', 'fontsize': 22}
        , 'twinx': True
        , 'bar_color': ['#EDA461']
        , 'edge_color': '#EDA461'
        , 'line_color': 'grey'
        , 'x_label': ''
        , 'y_label': {'label': 'Share of all cars', 'fontsize': 14, 'color': 'black'}
        , 'x_ticks': {'rot': 30, 'fontsize': 14, 'ha': 'right', 'ticks': None}
        , 'y_ticks': {'1': {'rot': 0, 'fontsize': 14, 'va': 'center', 'ticks': None}
            , '2': {'rot': 0, 'fontsize': 14, 'va': 'center', 'ticks': None}}
        ,
        'legend': {'label': 'Average car price [Euro]', 'loc': (0.62, 0.87), 'facecolor': 'white', 'edgecolor': 'white',
                   'figsize': 14}
        , 'file_name': 'Distribution_by_location.png'
    }
    , 'price_by_location': {
        'title': {'label': 'The average prices distribution by location [Euro]', 'fontsize': 22}
        , 'twinx': False
        , 'bar_color': ['#EDA461', 'grey']
        , 'edge_color': None
        , 'line_color': '#EDA461'
        , 'x_label': ''
        , 'y_label': {'label': '', 'fontsize': 15, 'color': 'black'}
        , 'x_ticks': {'rot': 30, 'fontsize': 15, 'ha': 'right', 'ticks': None}
        , 'y_ticks': {'1': {'rot': 0, 'fontsize': 15, 'va': 'center', 'ticks': 2}
            , '2': {'rot': 0, 'fontsize': 15, 'va': 'center'}}
        , 'legend': None
        , 'file_name': 'The_average_prices_distribution_by_location.png'
    }
    , 'mileage': {
        'title': {'label': 'Car distribution by mileage', 'fontsize': 22}
        , 'twinx': False
        , 'bar_color': ['white']
        , 'edge_color': 'grey'
        , 'line_color': '#EDA461'
        , 'x_label': {'label': 'Mileage [km]', 'fontsize': 14, 'color': 'black'}
        , 'y_label': {'label': 'Share of all cars', 'fontsize': 14, 'color': 'black'}
        , 'x_ticks': {'rot': 0, 'fontsize': 14, 'ha': 'center', 'ticks': None, 'step': None}
        , 'y_ticks': {'1': {'rot': 0, 'fontsize': 14, 'va': 'center', 'ticks': None}
            , '2': {'rot': 0, 'fontsize': 14, 'va': 'center', 'ticks': None}}
        , 'legend': None
        , 'file_name': 'Distribution_by_mileage.png'
    }
    , 'boxplot': {
        'title': {'label': 'The price boxplots of the 15 most common models', 'fontsize': 22}
        , 'twinx': False
        , 'bar_color': ['grey']
        , 'edge_color': 'grey'
        , 'line_color': '#EDA461'
        , 'x_label': ''
        , 'y_label': {'label': 'Euro', 'fontsize': 15, 'color': 'black'}
        , 'x_ticks': {'rot': 0, 'fontsize': 15, 'ha': 'center', 'ticks': None}
        , 'y_ticks': {
            '1': {'ticks': ('-', '0', '10K', '20K', '30K', '40K', '50K', '60K', '70K'), 'rot': 0, 'fontsize': 15,
                  'va': 'center'}
            , '2': {'rot': 0, 'fontsize': 15, 'va': 'center', 'ticks': None}}
        , 'legend': None
        , 'file_name': 'Boxplot.png'
    }
}

if __name__ == '__main__':
    pass
