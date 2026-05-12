heart_rates = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]
number = len(heart_rates)
mean = sum(heart_rates) / number
print(f"There are {number} patients in the dataset, and the mean heart rate is {mean:.1f} bpm.")

low = [hr for hr in heart_rates if hr<60]
normal = [hr for hr in heart_rates if 60<=hr<=120]
high = [hr for hr in heart_rates if hr>120]
print(f"The number of patients in low categories is {len(low)}, in normal categories is {len(normal)}, in high categories is {len(high)}.")

categories = {'low heart rate':len(low),'normal heart rate':len(normal),'high heart rate':len(high)}
maximum = max(categories,key = categories.get)
print(f"The {maximum} category contains the largest number of patients.")

import matplotlib.pyplot as plt
labels = ['Low heart rate', 'Normal heart rate', 'High heart rate']
sizes = [len(low), len(normal), len(high)]
plt.figure(figsize = (6.4, 4.8))
plt.pie(sizes, radius = 0.5, labels = None, startangle = 90, autopct = lambda pct:f'{pct:.1f}%\n({int(pct * sum(sizes) / 100)} people)', colors = ['lightblue', 'cornflowerblue', 'skyblue'], wedgeprops = {'edgecolor': 'black'})
plt.title('Heart Rates Categories Distribution')
plt.legend(labels, loc ='lower right')
plt.axis('equal')
plt.tight_layout
plt.savefig('heart_rate_analysis.png', dpi = 300, bbox_inches = 'tight')
plt.show()

input("Press enter to exit.")