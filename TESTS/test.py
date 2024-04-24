from matplotlib import *
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure(layout="constrained", figsize=(8, 4))
axs = fig.subplots(1, 2)
for i, ax in enumerate(axs):
    im = ax.imshow(np.arange(9).reshape((3, 3)), aspect="auto")
    fig.colorbar(im, pad=0, ticks=[])
axs[0].set(xlim=(-.5, 2.5), xticks=[0, 1, 2], yticks=[])
axs[1].set(xlim=(0, 3), xticks=[0, 1, 2, 3], yticks=[])

# Try to fix padding

#axs[1].xaxis.set_in_layout(False)
#bbox = axs[1].get_tightbbox()
#axs[1].set(clip_box=bbox)

#axs[1].get_figure()
#axs[1].figure.set_layout_engine('tight')

#cb = axs[1].images[-1].colorbar
#cb.update_normal(cb.mappable)

plt.show()