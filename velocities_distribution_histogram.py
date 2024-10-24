import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Set the directory containing the XLSX files with velocities
directory = r"C:\Users\asia-\Desktop\BI\Business Intelligence Workplace\Project\velocities"

# Initialize empty lists for each angle
velocities_0 = []
velocities_30 = []
velocities_60 = []
velocities_90 = []
velocities_120 = []
velocities_150 = []
velocities_180 = []

# Loop over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".xlsx"):
        # Extract the angle from the filename
        angle = int(filename.split("_")[0])
        
        # Load the Excel file into a Pandas DataFrame
        df = pd.read_excel(os.path.join(directory, filename))
        
        # Append the velocities for each angle to the appropriate list
        if angle == 0:
            velocities_0.extend(df.filter(like='v').values.flatten().tolist())
        elif angle == 30:
            velocities_30.extend(df.filter(like='v').values.flatten().tolist())
        elif angle == 60:
            velocities_60.extend(df.filter(like='v').values.flatten().tolist())
        elif angle == 90:
            velocities_90.extend(df.filter(like='v').values.flatten().tolist())
        elif angle == 120:
            velocities_120.extend(df.filter(like='v').values.flatten().tolist())
        elif angle == 150:
            velocities_150.extend(df.filter(like='v').values.flatten().tolist())
        elif angle == 180:
            velocities_180.extend(df.filter(like='v').values.flatten().tolist())
# Create a new figure
fig, ax = plt.subplots()

# Calculate the histogram of velocities_0 with weights
counts, bins, _ = plt.hist(velocities_0, alpha=0.5, bins=40, weights=np.ones_like(velocities_0) / len(velocities_0))
# Normalize the histogram so that the area under the histogram equals 1
normalized_counts = counts / sum(counts)
# Plot the normalized histogram
plt.bar(bins[:-1], normalized_counts, width=(bins[1] - bins[0]), alpha=0.5, label="0")

counts, bins, _ = plt.hist(velocities_30, alpha=0.5, bins=40, weights=np.ones_like(velocities_30) / len(velocities_30))
normalized_counts = counts / sum(counts)
plt.bar(bins[:-1], normalized_counts, width=(bins[1] - bins[0]), alpha=0.5, label="30")

counts, bins, _ = plt.hist(velocities_60, alpha=0.5, bins=40, weights=np.ones_like(velocities_60) / len(velocities_60))
normalized_counts = counts / sum(counts)
plt.bar(bins[:-1], normalized_counts, width=(bins[1] - bins[0]), alpha=0.5, label="60")

counts, bins, _ = plt.hist(velocities_90, alpha=0.5, bins=40, weights=np.ones_like(velocities_90) / len(velocities_90))
normalized_counts = counts / sum(counts)
plt.bar(bins[:-1], normalized_counts, width=(bins[1] - bins[0]), alpha=0.5, label="90")

counts, bins, _ = plt.hist(velocities_120, alpha=0.5, bins=40, weights=np.ones_like(velocities_120) / len(velocities_120))
normalized_counts = counts / sum(counts)
plt.bar(bins[:-1], normalized_counts, width=(bins[1] - bins[0]), alpha=0.5, label="120")

counts, bins, _ = plt.hist(velocities_150, alpha=0.5, bins=40, weights=np.ones_like(velocities_150) / len(velocities_150))
normalized_counts = counts / sum(counts)
plt.bar(bins[:-1], normalized_counts, width=(bins[1] - bins[0]), alpha=0.5, label="150")

counts, bins, _ = plt.hist(velocities_180, alpha=0.5, bins=40, weights=np.ones_like(velocities_180) / len(velocities_180))
normalized_counts = counts / sum(counts)
plt.bar(bins[:-1], normalized_counts, width=(bins[1] - bins[0]), alpha=0.5, label="180")

# Set the plot title and axis labels
plt.title("Normalized Velocity Distribution by Angle")
plt.xlabel("Velocity (m/s)")
plt.ylabel("Normalized frequency")

# Add a legend with the angle labels
plt.legend(title="Angle")

# Show the plot
plt.show()

# Create a new figure
fig, ax = plt.subplots()

# #Plot the histograms for each angle on the same figure
# plt.hist(velocities_0, alpha=0.5, bins=40, label="0")
# #print(np.nansum(velocities_0))
# plt.hist(velocities_30, alpha=0.5, bins=40, label="30")
# plt.hist(velocities_60, alpha=0.5, bins=40, label="60")
# plt.hist(velocities_90, alpha=0.5, bins=40, label="90")
# plt.hist(velocities_120, alpha=0.5, bins=40, label="120")
# plt.hist(velocities_150, alpha=0.5, bins=40, label="150")
# plt.hist(velocities_180, alpha=0.5, bins=40, label="180")

counts, bins = np.histogram(velocities_0, bins=40, range=(0, 5))
normalizedcounts = counts / counts.sum()
ax.plot(bins[:-1], normalizedcounts, label="0")

counts, bins = np.histogram(velocities_30, bins=40, range=(0, 5))
normalizedcounts = counts / counts.sum()
ax.plot(bins[:-1], normalizedcounts, label="30")

counts, bins = np.histogram(velocities_60, bins=40, range=(0, 5))
normalizedcounts = counts / counts.sum()
ax.plot(bins[:-1], normalizedcounts, label="60")

counts, bins = np.histogram(velocities_90, bins=40, range=(0, 5))
normalizedcounts = counts / counts.sum()
ax.plot(bins[:-1], normalizedcounts, label="90")

counts, bins = np.histogram(velocities_120, bins=40, range=(0, 5))
normalizedcounts = counts / counts.sum()
ax.plot(bins[:-1], normalizedcounts, label="120")

counts, bins = np.histogram(velocities_150, bins=40, range=(0, 5))
normalizedcounts = counts / counts.sum()
ax.plot(bins[:-1], normalizedcounts, label="150")

counts, bins = np.histogram(velocities_180, bins=40, range=(0, 5))
normalizedcounts = counts / counts.sum()
ax.plot(bins[:-1], normalizedcounts, label="180")

# Set the plot title and axis labels
plt.title("Normalized Velocity Distribution by Angle")
plt.xlabel("Velocity (m/s)")
plt.ylabel("Normalized frequency")

# Add a legend with the angle labels
plt.legend(title="Angle")

# Show the plot
plt.show()

# fig, ax = plt.subplots()
# plt.hist(velocities_0, alpha=0.5, bins=40)
# counts, bins = np.histogram(velocities_0, bins=40, range=(0, 5))
# ax.plot(bins[:-1], counts, label="0")
# plt.title("Velocity Distribution by Angle")
# plt.xlabel("Velocity (m/s)")
# plt.ylabel("Frequency")
# plt.legend(title="Angle")
# plt.show()

# fig, ax = plt.subplots()
# plt.hist(velocities_30, alpha=0.5, bins=40)
# counts, bins = np.histogram(velocities_30, bins=40, range=(0, 5))
# ax.plot(bins[:-1], counts, label="30")
# plt.title("Velocity Distribution by Angle")
# plt.xlabel("Velocity (m/s)")
# plt.ylabel("Frequency")
# plt.legend(title="Angle")
# plt.show()

# fig, ax = plt.subplots()
# plt.hist(velocities_60, alpha=0.5, bins=40)
# counts, bins = np.histogram(velocities_60, bins=40, range=(0, 5))
# ax.plot(bins[:-1], counts, label="60")
# plt.title("Velocity Distribution by Angle")
# plt.xlabel("Velocity (m/s)")
# plt.ylabel("Frequency")
# plt.legend(title="Angle")
# plt.show()

# fig, ax = plt.subplots()
# plt.hist(velocities_90, alpha=0.5, bins=40)
# counts, bins = np.histogram(velocities_90, bins=40, range=(0, 5))
# ax.plot(bins[:-1], counts, label="90")
# plt.title("Velocity Distribution by Angle")
# plt.xlabel("Velocity (m/s)")
# plt.ylabel("Frequency")
# plt.legend(title="Angle")
# plt.show()

# fig, ax = plt.subplots()
# plt.hist(velocities_120, alpha=0.5, bins=40)
# counts, bins = np.histogram(velocities_120, bins=40, range=(0, 5))
# ax.plot(bins[:-1], counts, label="120")
# plt.title("Velocity Distribution by Angle")
# plt.xlabel("Velocity (m/s)")
# plt.ylabel("Frequency")
# plt.legend(title="Angle")
# plt.show()

# fig, ax = plt.subplots()
# plt.hist(velocities_150, alpha=0.5, bins=40)
# counts, bins = np.histogram(velocities_150, bins=40, range=(0, 5))
# ax.plot(bins[:-1], counts, label="150")
# plt.title("Velocity Distribution by Angle")
# plt.xlabel("Velocity (m/s)")
# plt.ylabel("Frequency")
# plt.legend(title="Angle")
# plt.show()

# fig, ax = plt.subplots()
# plt.hist(velocities_180, alpha=0.5, bins=40)
# counts, bins = np.histogram(velocities_180, bins=40, range=(0, 5))
# ax.plot(bins[:-1], counts, label="180")
# plt.title("Velocity Distribution by Angle")
# plt.xlabel("Velocity (m/s)")
# plt.ylabel("Frequency")
# plt.legend(title="Angle")
# plt.show()