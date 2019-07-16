

import seaborn as sns
import matplotlib.pyplot as plt

sns.set(color_codes=True)
cd = ['Clinton', 'Trump', 'Sanders', 'Cruz']

ax = sns.barplot(cd, [9, 77, 6, 15])
ax.set(ylabel='count')
plt.show()