import matplotlib.pyplot as plt


def fuel_chart(df, figsize=(12, 3.75), style='default'):
    plt.style.use(style)
    plt.figure(figsize=figsize)
    df.fuel.value_counts(sort=True, normalize=True, ascending=False).plot(kind='bar', color='white', edgecolor='grey', lw=3.2);
    plt.title('Distribution of the number of cars by type of fuel', fontsize=22)
    plt.ylabel('Share of all cars', fontsize=15, color='black')
    plt.yticks(fontsize=15)
    plt.xticks(fontsize=15, rotation=0, horizontalalignment='center')
    plt.grid(False)
    plt.savefig('charts/Distribution_by_fuel.png', dpi=200, bbox_inches='tight')
    plt.show()

def top_makers_chart(df, figsize=(12, 3.75), style='default'):
    plt.style.use(style)
    fig, ax = plt.subplots(figsize=figsize)
    fs = 14
    top_makers = tuple(dict(df.make.value_counts().head(15)).keys())
    df_top = df[df.make.isin(top_makers)].reset_index()
    make = list(df_top.make.value_counts(normalize=True).keys())
    df_top['order'] = [make.index(x) for x in df_top.make]
    df_top.sort_values(by=['order'], inplace=True)

    ax = df_top.make.value_counts(normalize=True).plot(kind='bar', color='#EDA461', label='Carmakers')

    ax.set_title('chart/Distribution of the top 15 car manufacturers with average price of cars', fontsize=20)
    ax.set_ylabel('Share of all cars', fontsize=fs)
    plt.xticks(fontsize=fs, rotation=20, horizontalalignment='right')
    for label in ax.get_yticklabels():
        label.set(rotation=0, fontsize=fs)

    ax2 = ax.twinx()
    x = list(round(df_top.groupby('make', sort=False).price.mean(), 0).keys())
    y = round(df_top.groupby('make', sort=False).price.mean(), 0).values
    ax2.plot(x, y, 'o--', lw=1.05, ms=7.5, color='grey', label='Average car price [Euro]')

    ax2.set_ylabel('')
    for label in ax2.get_yticklabels():
        label.set(rotation=0, fontsize=fs)
    ax2.legend(loc=(0.57, 0.87), facecolor='white', edgecolor='white', fontsize=fs)

    plt.savefig('charts/Distribution_the_top_makers.png', dpi=200, bbox_inches='tight')
    plt.show()
