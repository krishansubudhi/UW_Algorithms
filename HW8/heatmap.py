import matplotlib.pyplot as plt
import warnings
import numpy as np

def makeHeatMap(data, names, color, outputFileName):
    #to catch "falling back to Agg" warning
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        #code source: http://stackoverflow.com/questions/14391959/heatmap-in-matplotlib-with-pcolor
        fig, ax = plt.subplots()
        #create the map w/ color bar legend
        heatmap = ax.pcolor(data, cmap=color)
        cbar = plt.colorbar(heatmap)

        # put the major ticks at the middle of each cell
        ax.set_xticks(np.arange(data.shape[0])+0.5, minor=False)
        ax.set_yticks(np.arange(data.shape[1])+0.5, minor=False)

        # want a more natural, table-like display
        ax.invert_yaxis()
        ax.xaxis.tick_top()

        label_count = len(names)
        ax.set_xticklabels(range(1, label_count+1))
        ax.set_yticklabels(names)

        plt.tight_layout()

        plt.savefig(outputFileName, format = 'png')
        plt.close()

if __name__ == "__main__":
    import numpy as np
    data = np.array(
        [
            [0,1]*10
        ]*20
    )
    names = range(1,21)
    color = 'viridis'
    outputFileName = 'heatmap.png'
    makeHeatMap(data, names, color, outputFileName)