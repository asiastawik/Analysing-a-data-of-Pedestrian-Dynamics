import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Set the directory containing the XLSX files with deviations
directory = r"C:\Users\asia-\Desktop\BI\Business Intelligence Workplace\Project\deviations"

# Initialize empty lists for each angle
deviations_0 = []
deviations_30 = []
deviations_60 = []
deviations_90 = []
deviations_120 = []
deviations_150 = []
deviations_180 = []

# Loop over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".xlsx"):
        # Extract the angle from the filename
        angle = int(filename.split("_")[0])
        
        # Load the Excel file into a Pandas DataFrame
        df = pd.read_excel(os.path.join(directory, filename))
        
        # Append the deviations for each angle to the appropriate list
        if angle == 0:
            deviations_0.extend(df.filter(like='delta').values.flatten().tolist())
        elif angle == 30:
            deviations_30.extend(df.filter(like='delta').values.flatten().tolist())
        elif angle == 60:
            deviations_60.extend(df.filter(like='delta').values.flatten().tolist())
        elif angle == 90:
            deviations_90.extend(df.filter(like='delta').values.flatten().tolist())
        elif angle == 120:
            deviations_120.extend(df.filter(like='delta').values.flatten().tolist())
        elif angle == 150:
            deviations_150.extend(df.filter(like='delta').values.flatten().tolist())
        elif angle == 180:
            deviations_180.extend(df.filter(like='delta').values.flatten().tolist())

# Create a new figure
fig, ax = plt.subplots()

counts, bins, _ = plt.hist(deviations_0, alpha=0.5, bins=40, weights=np.ones_like(deviations_0) / len(deviations_0))
normalized_counts = counts / sum(counts)
ax.plot(bins[:-1], normalized_counts, label="0")

counts, bins, _ = plt.hist(deviations_30, alpha=0.5, bins=40, weights=np.ones_like(deviations_30) / len(deviations_30))
normalized_counts = counts / sum(counts)
ax.plot(bins[:-1], normalized_counts, label="30")

counts, bins, _ = plt.hist(deviations_60, alpha=0.5, bins=40, weights=np.ones_like(deviations_60) / len(deviations_60))
normalized_counts = counts / sum(counts)
ax.plot(bins[:-1], normalized_counts, label="60")

counts, bins, _ = plt.hist(deviations_90, alpha=0.5, bins=40, weights=np.ones_like(deviations_90) / len(deviations_90))
normalized_counts = counts / sum(counts)
ax.plot(bins[:-1], normalized_counts, label="90")

counts, bins, _ = plt.hist(deviations_120, alpha=0.5, bins=40, weights=np.ones_like(deviations_120) / len(deviations_120))
normalized_counts = counts / sum(counts)
ax.plot(bins[:-1], normalized_counts, label="120")

counts, bins, _ = plt.hist(deviations_150, alpha=0.5, bins=40, weights=np.ones_like(deviations_150) / len(deviations_150))
normalized_counts = counts / sum(counts)
ax.plot(bins[:-1], normalized_counts, label="150")

counts, bins, _ = plt.hist(deviations_180, alpha=0.5, bins=40, weights=np.ones_like(deviations_180) / len(deviations_180))
normalized_counts = counts / sum(counts)
ax.plot(bins[:-1], normalized_counts, label="180")

# Set the plot title and axis labels
plt.title("Deviation Distribution by Angle")
plt.xlabel("Deviation - delta [degrees]")
plt.ylabel("Frequency")

# Add a legend with the angle labels
plt.legend(title="Angle")

# Show the plot
plt.show()

# Create a new figure
fig, ax = plt.subplots()

# Calculate the histogram of deviations_0 with weights
counts, bins, _ = plt.hist(deviations_0, alpha=0.5, bins=40, weights=np.ones_like(deviations_0) / len(deviations_0))
# Normalize the histogram so that the area under the histogram equals 1
normalized_counts = counts / sum(counts)
# Plot the normalized histogram
plt.bar(bins[:-1], normalized_counts, width=(bins[1] - bins[0]), alpha=0.3, label="0")
ax.plot(bins[:-1], normalized_counts, label="0")

# Set the plot title and axis labels
plt.title("Deviation Distribution by Angle")
plt.xlabel("Deviation - delta [degrees]")
plt.ylabel("Frequency")

# Add a legend with the angle labels
plt.legend(title="Angle")

# Show the plot
plt.show()

fig, ax = plt.subplots()
counts, bins, _ = plt.hist(deviations_30, alpha=0.5, bins=40, weights=np.ones_like(deviations_30) / len(deviations_30))
normalized_counts = counts / sum(counts)
plt.bar(bins[:-1], normalized_counts, width=(bins[1] - bins[0]), alpha=0.3, label="30")
ax.plot(bins[:-1], normalized_counts, label="30")
plt.title("Deviation Distribution by Angle")
plt.xlabel("Deviation - delta [degrees]")
plt.ylabel("Frequency")
plt.legend(title="Angle")
plt.show()

fig, ax = plt.subplots()
counts, bins, _ = plt.hist(deviations_60, alpha=0.5, bins=40, weights=np.ones_like(deviations_60) / len(deviations_60))
normalized_counts = counts / sum(counts)
plt.bar(bins[:-1], normalized_counts, width=(bins[1] - bins[0]), alpha=0.3, label="60")
ax.plot(bins[:-1], normalized_counts, label="60")
plt.title("Deviation Distribution by Angle")
plt.xlabel("Deviation - delta [degrees]")
plt.ylabel("Frequency")
plt.legend(title="Angle")
plt.show()

fig, ax = plt.subplots()
counts, bins, _ = plt.hist(deviations_90, alpha=0.5, bins=40, weights=np.ones_like(deviations_90) / len(deviations_90))
normalized_counts = counts / sum(counts)
plt.bar(bins[:-1], normalized_counts, width=(bins[1] - bins[0]), alpha=0.3, label="90")
ax.plot(bins[:-1], normalized_counts, label="90")
plt.title("Deviation Distribution by Angle")
plt.xlabel("Deviation - delta [degrees]")
plt.ylabel("Frequency")
plt.legend(title="Angle")
plt.show()

fig, ax = plt.subplots()
counts, bins, _ = plt.hist(deviations_120, alpha=0.5, bins=40, weights=np.ones_like(deviations_120) / len(deviations_120))
normalized_counts = counts / sum(counts)
plt.bar(bins[:-1], normalized_counts, width=(bins[1] - bins[0]), alpha=0.3, label="120")
ax.plot(bins[:-1], normalized_counts, label="120")
plt.title("Deviation Distribution by Angle")
plt.xlabel("Deviation - delta [degrees]")
plt.ylabel("Frequency")
plt.legend(title="Angle")
plt.show()

fig, ax = plt.subplots()
counts, bins, _ = plt.hist(deviations_150, alpha=0.5, bins=40, weights=np.ones_like(deviations_150) / len(deviations_150))
normalized_counts = counts / sum(counts)
plt.bar(bins[:-1], normalized_counts, width=(bins[1] - bins[0]), alpha=0.3, label="150")
ax.plot(bins[:-1], normalized_counts, label="150")
plt.title("Deviation Distribution by Angle")
plt.xlabel("Deviation - delta [degrees]")
plt.ylabel("Frequency")
plt.legend(title="Angle")
plt.show()

fig, ax = plt.subplots()
counts, bins, _ = plt.hist(deviations_180, alpha=0.5, bins=40, weights=np.ones_like(deviations_180) / len(deviations_180))
normalized_counts = counts / sum(counts)
plt.bar(bins[:-1], normalized_counts, width=(bins[1] - bins[0]), alpha=0.3, label="180")
ax.plot(bins[:-1], normalized_counts, label="180")
plt.title("Deviation Distribution by Angle")
plt.xlabel("Deviation - delta [degrees]")
plt.ylabel("Frequency")
plt.legend(title="Angle")
plt.show()

# # Plot the histograms for each angle on the same figure
# plt.hist(deviations_0, alpha=0.5, bins=40, label="0")
# #print(np.nansum(deviations_0))
# plt.hist(deviations_30, alpha=0.5, bins=40, label="30")
# plt.hist(deviations_60, alpha=0.5, bins=40, label="60")
# plt.hist(deviations_90, alpha=0.5, bins=40, label="90")
# plt.hist(deviations_120, alpha=0.5, bins=40, label="120")
# plt.hist(deviations_150, alpha=0.5, bins=40, label="150")
# plt.hist(deviations_180, alpha=0.5, bins=40, label="180")

# # Set the plot title and axis labels
# plt.title("Deviation Distribution by Angle")
# plt.xlabel("Deviation - delta [degrees]")
# plt.ylabel("Frequency")

# # Add a legend with the angle labels
# plt.legend(title="Angle")

# # Show the plot
# plt.show()

# fig, ax = plt.subplots()
# plt.hist(deviations_0, alpha=0.5, bins=40, label="0")
# plt.title("Deviation Distribution by Angle")
# plt.xlabel("Deviation - delta [degrees]")
# plt.ylabel("Frequency")
# plt.legend(title="Angle")
# plt.show()

# fig, ax = plt.subplots()
# plt.hist(deviations_30, alpha=0.5, bins=40, label="30")
# plt.title("Deviation Distribution by Angle")
# plt.xlabel("Deviation - delta [degrees]")
# plt.ylabel("Frequency")
# plt.legend(title="Angle")
# plt.show()

# fig, ax = plt.subplots()
# plt.hist(deviations_60, alpha=0.5, bins=40, label="60")
# plt.title("Deviation Distribution by Angle")
# plt.xlabel("Deviation - delta [degrees]")
# plt.ylabel("Frequency")
# plt.legend(title="Angle")
# plt.show()

# fig, ax = plt.subplots()
# plt.hist(deviations_90, alpha=0.5, bins=40, label="90")
# plt.title("Deviation Distribution by Angle")
# plt.xlabel("Deviation - delta [degrees]")
# plt.ylabel("Frequency")
# plt.legend(title="Angle")
# plt.show()

# fig, ax = plt.subplots()
# plt.hist(deviations_120, alpha=0.5, bins=40, label="120")
# plt.title("Deviation Distribution by Angle")
# plt.xlabel("Deviation - delta [degrees]")
# plt.ylabel("Frequency")
# plt.legend(title="Angle")
# plt.show()

# fig, ax = plt.subplots()
# plt.hist(deviations_150, alpha=0.5, bins=40, label="150")
# plt.title("Deviation Distribution by Angle")
# plt.xlabel("Deviation - delta [degrees]")
# plt.ylabel("Frequency")
# plt.legend(title="Angle")
# plt.show()

# fig, ax = plt.subplots()
# plt.title("Deviation Distribution by Angle")
# plt.xlabel("Deviation - delta [degrees]")
# plt.ylabel("Frequency")
# plt.legend(title="Angle")
# plt.show()

# fig, ax = plt.subplots()
# plt.hist(deviations_180, alpha=0.5, bins=40, label="180")
# plt.title("Deviation Distribution by Angle")
# plt.xlabel("Deviation - delta [degrees]")
# plt.ylabel("Frequency")
# plt.legend(title="Angle")
# plt.show()
