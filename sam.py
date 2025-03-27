import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # Corrected from 'scabdrn' to 'seaborn'

# Load the data
data = pd.read_csv('5_6271466015318611384.csv')

# Filter for World data only
world_data = data[data['Country Name'] == 'World']

# Filter years from 1980 onwards
world_data = world_data[world_data['Year'] >= 1980]

# Convert GDP values from current US$ to trillions for better readability
world_data['GDP (Trillions)'] = world_data['Value'] / 1e12

# Create the bar chart
plt.figure(figsize=(15, 8))
sns.barplot(x='Year', y='GDP (Trillions)', data=world_data, color='skyblue')

# Customize the plot
plt.title('World GDP Growth (1980-Present)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('GDP (in Trillions US$)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the plot
plt.tight_layout()
plt.show()