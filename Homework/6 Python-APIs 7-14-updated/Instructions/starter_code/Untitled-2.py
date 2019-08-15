
#%%
get_ipython().run_line_magic('matplotlib', 'notebook')


#%%
# Import our dependencies
import matplotlib.pyplot as plt
import numpy as np


#%%
# Labels for the sections of our pie chart
labels = ["Humans", "Smurfs", "Hobbits", "Ninjas"]

# The values of each section of the pie chart
sizes = [220, 95, 80, 100]

# The colors of each section of the pie chart
colors = ["red", "orange", "lightcoral", "lightskyblue"]

# Tells matplotlib to seperate the "Python" section from the others
explode = (0.1, 0, 0, 0)


#%%
# Creates the pie chart based upon the values above
# Automatically finds the percentages of each part of the pie chart
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct="%1.1f%%", shadow=True, startangle=140)


#%%
# Tells matplotlib that we want a pie chart with equal axes
plt.axis("equal")


#%%



