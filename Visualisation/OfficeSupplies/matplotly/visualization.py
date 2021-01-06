# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from mylib import autolabel_bar,axe_set_size

of = pd.read_csv("P12-OfficeSupplies.csv")
of["Sales Price"] = of["Units"] * of["Unit Price"]
sales_by_rep_region = of.groupby(["Rep","Region"])["Sales Price"].sum().reset_index().sort_values(by=['Sales Price','Region','Rep'])
regions = sales_by_rep_region.groupby(["Region"])["Region"].count()
regions.head(40)


# %%
width = 0.15  # the width of the bars
fig = plt.figure()
gs = fig.add_gridspec(ncols=regions.size, wspace=0, width_ratios=regions.values)

axes = gs.subplots(sharey=True)

fig.set_figwidth(10)
fig.set_figheight(7)
fig.tight_layout()

axes[0].set_ylabel('Sales')
i = 0
for region in regions:
    ax = axes[i]
    data = sales_by_rep_region[sales_by_rep_region.Region == region]

    x = np.arange(data.Rep.size)
    bars = ax.bar(x,data["Sales Price"].values, width,color ='C9')
    autolabel_bar(bars,ax)
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_title(region)
    ax.set_xticks(x)
    ax.set_xticklabels(data.Rep.values)
    i+=1



plt.show()


# %%



