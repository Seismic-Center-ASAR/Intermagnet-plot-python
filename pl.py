import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# Make a request to the website page
url = 'https://imag-data.bgs.ac.uk/GIN_V1/GINServices?Request=GetData&format=HTML&testObsys=0&observatoryIagaCode=SUA&samplesPerDay=minute&publicationState=Best%20available&dataStartDate=2023-05-01&dataDuration=1'
response = requests.get(url)

# Parse the HTML source code using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table element based on the class attribute
table = soup.find('table')

# Extract the table data and convert it to a pandas DataFrame
df = pd.read_html(str(table))[0]

# Rename the columns to match the data
df.columns = ['Time', 'X', 'Y', 'Z', 'F']

# Convert the 'Time' column to a dateTime object
df['Time'] = pd.to_datetime(df['Time'], format='%Y-%m-%dT%H:%M:%SZ')

# Set the 'Time' column as the index
df.set_index('Time', inplace=True)

# Select only the 'X' column
x_df = df['X']

# Plot the X component data
x_df.plot(figsize=(12, 6))

# Set the plot title and axis labels
plt.title('SUA Magnetic Field X Component')
plt.xlabel('Time (UTC)')
plt.ylabel('Magnetic Field (nT)')

# Display the plot
plt.show()

#--------Y------
x_df = df['Y']

# Plot the X component data
x_df.plot(figsize=(12, 6))

# Set the plot title and axis labels
plt.title('SUA Magnetic Field Y Component')
plt.xlabel('Time (UTC)')
plt.ylabel('Magnetic Field (nT)')

# Display the plot
plt.show()

#---------Z---
x_df = df['Z']

# Plot the X component data
x_df.plot(figsize=(12, 6))

# Set the plot title and axis labels
plt.title('SUA Magnetic Field Z Component')
plt.xlabel('Time (UTC)')
plt.ylabel('Magnetic Field (nT)')

# Display the plot
plt.show()

#------All axis combined--
df.plot(y=['X', 'Y', 'Z'], figsize=(12, 6))

# Set the plot title and axis labels
plt.title('SUA Magnetic Field Components')
plt.xlabel('Time (UTC)')
plt.ylabel('Magnetic Field (nT)')

# Display the plot
plt.show()

#----subplots all 3---
fig, axs = plt.subplots(3, 1, figsize=(12, 8), sharex=True)

# Plot X on the first subplot
axs[0].plot(df.index, df['X'], color='r')
axs[0].set_title('X Component')

# Plot Y on the second subplot
axs[1].plot(df.index, df['Y'], color='g')
axs[1].set_title('Y Component')

# Plot Z on the third subplot
axs[2].plot(df.index, df['Z'], color='b')
axs[2].set_title('Z Component')

# Set the y-axis labels for all subplots
for ax in axs:
    ax.set_ylabel('Magnetic Field (nT)')

# Add a common x-axis label for all subplots
fig.text(0.5, 0.05, 'Time (UTC)', ha='center', va='center')

# Set the plot title
fig.suptitle('SUA Magnetic Field Components')

# Display the plot
plt.show()