from matplotlib import cm
import numpy as np

def colorgen(cmap_name, UNIQ_COLORS=8):
    cmap = cm.get_cmap(cmap_name)

    gen = np.linspace(0.0, 1.0, UNIQ_COLORS)
    count = 0
    while True:
        color = cmap(gen[count])
        count += 1
        count %= UNIQ_COLORS
        yield color