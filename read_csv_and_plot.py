import os
import pandas as pd
import matplotlib.pyplot as plt

# Set the directory containing the CSV files
directory = r"C:\Users\asia-\Desktop\BI\Business Intelligence Workplace\Project\csv"

# Loop over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        # Load the CSV file into a Pandas DataFrame
        df = pd.read_csv(os.path.join(directory, filename))

        # Get the number of participants
        nhel = (df.shape[1] - 1) // 2

        # Create a new figure for the plot
        plt.figure()

        # Loop over each participant and plot their trajectory
        for i in range(nhel):
            x = df.iloc[:, 1 + 2*i]
            y = df.iloc[:, 1 + 2*i + 1]
            plt.plot(x, y)
            plt.scatter(x.iloc[1], y.iloc[1], marker='o', s=100, facecolors='none', edgecolors='k', linewidths=2)
            plt.scatter(x.iloc[-1], y.iloc[-1], marker='o', s=100, facecolors='none', edgecolors='r', linewidths=2)
            
            
            # Plotting only initial and final positions
            #x = df.iloc[[0, -1], 1 + 2*i]
            #y = df.iloc[[0, -1], 1 + 2*i + 1]
            #plt.scatter(x, y)

        # Set the title of the plot to the filename
        plt.title(filename)
        plt.xlabel('x [m]')
        plt.ylabel('y [m]')
        
        # Show the plot
        plt.show()
