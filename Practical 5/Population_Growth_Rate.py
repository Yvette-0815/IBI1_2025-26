countries = ['UK', 'China', 'Italy', 'Brazil', 'USA']
n2020 = [66.7, 1426, 59.4, 208.6, 331.6]
n2024 = [69.2, 1410, 58.9, 212, 340.1]
intergration=[]
for i in range(len(countries)):
    percent_change = ((n2024[i]-n2020[i]) / n2020[i]) * 100
    intergration.append((countries[i], percent_change))
print(intergration)

sort = sorted(intergration, key = lambda x:x[1], reverse = True)
print(f"Sort in descending order: {sort}")
print(f"The country with the largest increase is {sort[0][0]}, the country with the largest decrease is {sort[-1][0]}.")

import matplotlib.pyplot as plt
ind = list(range(len(countries)))
change = [item[1]for item in intergration]
pl = plt.bar(ind, change, width = 0.35, edgecolor = 'black')
plt.bar_label(pl, fmt = '%.1f%%', padding = 3)
plt.title('Population Changes by Country (2020-2024)')
plt.xlabel("Coutries")
plt.ylabel("Changes(%)")
plt.xticks(ind, countries)
plt.yticks(range(-2, 6, 1))
plt.axhline(y = 0, color = 'gray', linestyle = '--', linewidth = 1)
plt.savefig('population_growth.png', dpi = 300, bbox_inches = 'tight')
plt.show()

input("Press enter to exit.")