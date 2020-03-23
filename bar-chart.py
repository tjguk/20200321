#import os
import matplotlib
matplotlib.use('TkAgg')

#
# Show the same summary on a horizontal bar chart
#
import matplotlib.pyplot as plt

ages = {
    "Alice" : 20,
    "Bob" : 15,
    "Charlie" : 25,
    "Denise" : 12,
    "Eddie" : 30
}

labels = list(ages.keys())
values = list(ages.values())
bar_chart = plt.barh(labels, values)
plt.ylabel("Names")
plt.xlabel("Ages")
plt.show()