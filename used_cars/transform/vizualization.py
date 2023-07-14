import matplotlib.pyplot as plt
import pandas as pd
import json

def chart(js):
    plt.style.use('default')
    for _chart in js:
        chart = js.get(_chart)

        fs = chart.get('figsize')
        figsize = fs or (12, 3.75)
        fig, ax = plt.subplots(figsize=figsize)
        tl = chart.get('title')
        if tl:
            title = tl.get('label')
            title_fontsize = tl.get('fontsize') or 22
            ax.set_title(label=title, fontsize=title_fontsize)
        else:
            ax.set_title(label='Distribution', fontsize=22)
        x_label = chart.get('x_label')
        if x_label:
            label = x_label.get('label')
            fontsize = x_label.get('fontsize') or 14
            color = x_label.get('color') or 'black'
            ax.set_xlabel(label, fontsize=fontsize, color=color)
        else:
            ax.set_xlabel('')

        y_label = chart.get('y_label')
        ax.set_ylabel('')
        if y_label:
            label = y_label.get('label') or ''
            fontsize = y_label.get('fontsize') or 14
            color = y_label.get('color') or 'black'
            ax.set_ylabel(label, fontsize=fontsize, color=color)

        x_ticks = chart.get('x_ticks')
        if x_ticks:
            fontsize = x_ticks.get('fontsize') or 14
            ha = x_ticks.get('ha') or 'center'
            rot = x_ticks.get('rot') or 0
            x_ts = x_ticks.get('ticks')
            x_ts_step = x_ticks.get('step')
            for label in ax.get_xticklabels():
                label.set(fontsize=fontsize, ha=ha, rotation=rot)
        else:
            for label in ax.get_xticklabels():
                label.set(fontsize=14, ha='center', rotation=0)

        y_ticks = chart.get('y_ticks')
        y1_ts = None
        if y_ticks:
            y_ticks1 = chart.get('1')
            if y_ticks1:
                fontsize = y_ticks1.get('fontsize') or 14
                va = y_ticks1.get('va') or 'center'
                rot = y_ticks1.get('rot') or 0
                y1_ts = y_ticks1.get('ticks')
                for label in ax.get_yticklabels():
                    label.set(fontsize=fontsize, va=va, rotation=rot)
            else:
                for label in ax.get_yticklabels():
                    label.set(fontsize=14, va='center', rotation=0)
        else:
            for label in ax.get_yticklabels():
                label.set(fontsize=14, va='center', rotation=0)

        if _chart == 'boxplot':
            str_y = chart.get('y')
            cols = chart.get('x')
            if str_y:
                temp = pd.read_json(str_y)
                y_box = temp.groupby('model', sort=False)
                ax = y_box.boxplot(subplots=False, column='price', rot=25, grid=False, color='grey', fontsize=14)
                ax.set_xticklabels(cols)
                # rows = ('-', '0', '10K', '20K', '30K', '40K', '50K', '60K', '70K')
                # ax.set_yticklabels(rows)


        else:
            x = chart.get('x')
            if x_ts:
                xticks = [tick for tick in x if tick % x_ts == 1]
                ax.set_xticks(xticks)
            y = chart.get('y')

            if y1_ts:
                if isinstance(y1_ts, int):
                    yticks = [tick for tick in y if tick % y1_ts == 0]
                    ax.set_yticks(yticks)
                else:
                    initial_ticks = ax.get_yticks()
                    diff = len(initial_ticks) - len(y1_ts)
                    ax.set_yticklabels(y1_ts[:diff])
            bar_color = chart.get('bar_color') or ['white']
            edge_color = chart.get('edge_color')
            lw = chart.get('linewidth') or 2.5
            cont = ax.bar(x, y, color=bar_color[0], edgecolor=edge_color, linewidth=lw)
            if _chart == 'price_by_location':
                coast_color = bar_color[1]
                for lab in ax.get_xticklabels():
                    if lab.get_text() in ('Tivat', 'Kotor', 'Bar', 'Budva', 'Ulcinj', 'Herceg Novi', 'Petrovac'):
                        _x = lab._x
                        cont.patches[_x].set(color=coast_color)

        tw = chart.get('twinx')
        if tw:
            ax2 = ax.twinx()
            y2 = chart.get('y2')
            kind2 = chart.get('kind2') or 'o--'
            lw2 = chart.get('lw2') or 1.05
            ms2 = chart.get('ms2') or 7.5
            color2 = chart.get('line_color') or 'grey'
            grid = chart.get('grid') or False
            legend_label = None
            legend = chart.get('legend')
            if legend:
                legend_label = legend.get('label')
                legend_loc = legend.get('loc') or (0.57, 0.87)
                legend_facecolor = legend.get('facecolor') or 'white'
                legend_edgecolor = legend.get('edgecolor') or 'white'
                legend_figsize = legend.get('figsize') or 14

            ax2.plot(x, y2, kind2, lw=lw2, ms=ms2, color=color2, label=legend_label)
            if legend:
                ax2.legend(loc=legend_loc, facecolor=legend_facecolor, edgecolor=legend_edgecolor, fontsize=legend_figsize)
            ax2.set_ylabel('')
            ax2.grid(grid)
        fn = chart.get('file_name') or '_'
        file_name = ''.join(['charts/', fn])
        plt.savefig(file_name, dpi=200, bbox_inches='tight')
        # plt.show()
        # plt.close()


if __name__ == '__main__':
    pass


