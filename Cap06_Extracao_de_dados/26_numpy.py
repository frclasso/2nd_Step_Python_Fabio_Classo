import numpy as np

positions = ['GK', 'M', 'A', 'D']
heights = [191, 184, 185, 180]


np_positions = np.array(positions)
np_heights = np.array(heights)

# Alturas  dos GK (Goal Keepers)
gk_heigths = np_heights[np_positions == 'GK']

print(gk_heigths)

others_heights = np_heights[np_positions != 'GK']
print(others_heights)

print('Media as alturas  dos GoalKeepers: '+str(np.mean(others_heights)))