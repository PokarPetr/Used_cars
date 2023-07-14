import json


def concat_config_and_fits(charts, fits, rewrite=False):
    charts = json.loads(charts)

    FULL_CHART_DATA = charts.copy()
    for chart in charts:
        if charts.get(chart).get('twinx'):
            FULL_CHART_DATA[chart]['x'] = fits[chart].get('x')
            FULL_CHART_DATA[chart]['y'] = fits[chart].get('y')
            FULL_CHART_DATA[chart]['y2'] = fits[chart].get('y2')
        else:
            FULL_CHART_DATA[chart]['x'] = fits[chart].get('x')
            FULL_CHART_DATA[chart]['y'] = fits[chart].get('y')
    if rewrite:
        with open('full_charts_data.json', 'w') as f:
            json.dump(FULL_CHART_DATA, f, indent=4)

    return FULL_CHART_DATA







if __name__ == "__main__":
    concat_config_and_fits(5)
