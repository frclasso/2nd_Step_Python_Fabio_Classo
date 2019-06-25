import matplotlib.pyplot as plt

year = [1950, 1970, 1990, 2010]
population = [2.519, 3.962, 5.263, 6.972]




plt.plot(year, population)
plt.scatter(year, population)

plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population Projections')
plt.yticks([0,2,4,6,8,10],
           ['0', '2Bi', '4Bi', '6Bi', '8Bi', '10Bi'])
plt.show()