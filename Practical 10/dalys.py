import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("C:/Users/Yevette/Desktop/Practical 10")
print(os.getcwd())
print(os.listdir())

dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

print(dalys_data.head(5))
print(dalys_data.info())
print(dalys_data.describe())

first_10_years_dalys = dalys_data.iloc[0:10,2:4]
print("\nFirst 10 rows,Year and DALYs columns: ")
print(first_10_years_dalys)
max_dalys_row = first_10_years_dalys.loc[first_10_years_dalys['DALYs'].idxmax()]

zimbabwe_mask = dalys_data['Entity'] == 'Zimbabwe'
zimbabwe_years = dalys_data.loc[zimbabwe_mask,'Year']
print("\nYears for which DALYS were recorded in Zimbabwe: ")
print(zimbabwe_years.to_list())

recent_data = dalys_data.loc[dalys_data['Year'] == 2019, ['Entity', 'DALYs']]
country_max_dalys = recent_data.loc[recent_data['DALYs'].idxmax()]
country_min_dalys = recent_data.loc[recent_data['DALYs'].idxmin()]
print(f"\nCountry with MAX DALYs in 2019: {country_max_dalys['Entity']} ({country_max_dalys['DALYs']})")
print(f"Country with MIN DALYs in 2019: {country_min_dalys['Entity']} ({country_min_dalys['DALYs']})")
      
# Please answer the question in this comment line：What are the countries with the highest and lowest DALYs in 2019?
# Answer：The highest one is Lesotho，the lowest one is Singapore.
 
country_to_plot = country_max_dalys['Entity']
country_data = dalys_data.loc[dalys_data['Entity'] == country_to_plot]
plt.figure(figsize=(6, 4))
plt.plot(country_data['Year'], country_data['DALYs'], 'b+-')
plt.title(f'DALYs over time in {country_to_plot}')
plt.xlabel('Year')
plt.ylabel('DALYs (rate)')
plt.xticks(country_data['Year'], rotation=90)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(f'dalys_trend_{country_to_plot}.png', dpi=300)
plt.show()

country_to_plot = country_min_dalys['Entity']
country_data = dalys_data.loc[dalys_data['Entity'] == country_to_plot]
plt.figure(figsize=(6, 4))
plt.plot(country_data['Year'], country_data['DALYs'], 'b+-')
plt.title(f'DALYs over time in {country_to_plot}')
plt.xlabel('Year')
plt.ylabel('DALYs (rate)')
plt.xticks(country_data['Year'], rotation=90)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(f'dalys_trend_{country_to_plot}.png', dpi=300)
plt.show()

# Question: What was the distribution of DALYs in all countries in 2019?

plt.figure(figsize=(6, 4))
plt.hist(recent_data['DALYs'], bins=30, edgecolor='black', alpha=0.7)
plt.title('Distribution of DALYs across all countries in 2019')
plt.xlabel('DALYs (rate)')
plt.ylabel('Number of Countries')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('dalys_distribution_2019.png', dpi=300)
plt.show()
print(f"\nDescriptive statistics:")
print(recent_data['DALYs'].describe())

input("\nPress enter to exit.")
