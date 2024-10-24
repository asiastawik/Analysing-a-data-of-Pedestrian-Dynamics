import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Set the directory containing the CSV files
directory = r"C:\Users\asia-\Desktop\BI\Business Intelligence Workplace\Project\csv"

# Loop over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        # Extract the angle from the filename
        angle = int(filename.split("_")[0])

        # Load the CSV file into a Pandas DataFrame
        df = pd.read_csv(os.path.join(directory, filename))

        # Get the number of participants
        nhel = (df.shape[1] - 1) // 2

        # Group participants based on angle-specific conditions
        if angle == 90:
            # Initialize empty lists for group assignments
            group1, group2 = [], []
            for i in range(nhel):
                x_diff = abs(df.iloc[1, 1 + 2*i] - df.iloc[-1, 1 + 2*i])
                #y_diff = abs(df.iloc[1, 2*i + 2] - df.iloc[0, 2*i + 1])
                if x_diff < 5000:
                    group1.append(i)
                else:
                    group2.append(i)
                    
            # Create a new figure for the plot
            plt.figure()
            #print(group1)

            # Loop over each participant and plot their trajectory
            for i in group1:
                x = df.iloc[:, 1 + 2*i]
                y = df.iloc[:, 1 + 2*i + 1]
                #plt.plot(x, y, color='blue', marker='o')
                plt.scatter(x.iloc[1], y.iloc[1], marker='o', s=100, c='b', linewidths=2)
                plt.scatter(x.iloc[-1], y.iloc[-1], marker='s', s=100, c='b', linewidths=2)
                
            for i in group2:
                x = df.iloc[:, 1 + 2*i]
                y = df.iloc[:, 1 + 2*i + 1]
                #plt.plot(x, y, color='red', marker='x')
                plt.scatter(x.iloc[1], y.iloc[1], marker='o', s=100, c='r', linewidths=2)
                plt.scatter(x.iloc[-1], y.iloc[-1], marker='s', s=100, c='r', linewidths=2)
                
            # Set the title of the plot to the filename
            plt.title(filename)

            # Show the plot
            plt.show()

        elif angle == 0:
            # Assign all participants to the same group
            group3 = range(nhel)
            group4 = []
            
            for i in group3:
                x = df.iloc[:, 1 + 2*i]
                y = df.iloc[:, 1 + 2*i + 1]
                #plt.plot(x, y, color='blue', marker='o')
                plt.scatter(x.iloc[1], y.iloc[1], marker='o', s=100, c='b', linewidths=2)
                plt.scatter(x.iloc[-1], y.iloc[-1], marker='s', s=100, c='b', linewidths=2)
                
            # Set the title of the plot to the filename
            plt.title(filename)

            # Show the plot
            plt.show()

        elif angle == 180:
            # Initialize empty lists for group assignments
            group5, group6 = [], []
            for i in range(nhel):
                y_diff = df.iloc[-1, 2*i + 2] - df.iloc[1, 2*i + 1]
                if y_diff > 0:
                    group5.append(i)
                else:
                    group6.append(i)
            
            # Loop over each participant and plot their trajectory
            for i in group5:
                x = df.iloc[:, 1 + 2*i]
                y = df.iloc[:, 1 + 2*i + 1]
                #plt.plot(x, y, color='blue', marker='o')
                plt.scatter(x.iloc[1], y.iloc[1], marker='o', s=100, c='b', linewidths=2)
                plt.scatter(x.iloc[-1], y.iloc[-1], marker='s', s=100, c='b', linewidths=2)
                
            for i in group6:
                x = df.iloc[:, 1 + 2*i]
                y = df.iloc[:, 1 + 2*i + 1]
                #plt.plot(x, y, color='red', marker='x')
                plt.scatter(x.iloc[1], y.iloc[1], marker='o', s=100, c='r', linewidths=2)
                plt.scatter(x.iloc[-1], y.iloc[-1], marker='s', s=100, c='r', linewidths=2)
                
            # Set the title of the plot to the filename
            plt.title(filename)

            # Show the plot
            plt.show()

        elif angle == 30:
            # Initialize empty lists for group assignments
            group7, group8 = [], []
            for i in range(nhel):
                x_diff = abs(df.iloc[1, 1 + 2*i] - df.iloc[-1, 1 + 2*i])
                y_diff = abs(df.iloc[1, 2*i + 2] - df.iloc[-1, 2*i + 1])
                if x_diff < 5000:
                    group7.append(i)
                else:
                    group8.append(i)
            
            # Loop over each participant and plot their trajectory
            for i in group7:
                x = df.iloc[:, 1 + 2*i]
                y = df.iloc[:, 1 + 2*i + 1]
                #plt.plot(x, y, color='blue', marker='o')
                plt.scatter(x.iloc[1], y.iloc[1], marker='o', s=100, c='b', linewidths=2)
                plt.scatter(x.iloc[-1], y.iloc[-1], marker='s', s=100, c='b', linewidths=2)
                
            for i in group8:
                x = df.iloc[:, 1 + 2*i]
                y = df.iloc[:, 1 + 2*i + 1]
                #plt.plot(x, y, color='red', marker='x')
                plt.scatter(x.iloc[1], y.iloc[1], marker='o', s=100, c='r', linewidths=2)
                plt.scatter(x.iloc[-1], y.iloc[-1], marker='s', s=100, c='r', linewidths=2)
                
            # Set the title of the plot to the filename
            plt.title(filename)

            # Show the plot
            plt.show()
        
        elif angle == 60:
            # Initialize empty lists for group assignments
            group9, group10 = [], []
            for i in range(nhel):
                x_diff = abs(df.iloc[1, 1 + 2*i] - df.iloc[-1, 1 + 2*i])
                y_diff = abs(df.iloc[1, 2*i + 2] - df.iloc[-1, 2*i + 1])
                if x_diff < 12800:
                    group9.append(i)
                else:
                    group10.append(i)
            
            # Loop over each participant and plot their trajectory
            for i in group9:
                x = df.iloc[:, 1 + 2*i]
                y = df.iloc[:, 1 + 2*i + 1]
                #plt.plot(x, y, color='blue', marker='o')
                plt.scatter(x.iloc[1], y.iloc[1], marker='o', s=100, c='b', linewidths=2)
                plt.scatter(x.iloc[-1], y.iloc[-1], marker='s', s=100, c='b', linewidths=2)
                
            for i in group10:
                x = df.iloc[:, 1 + 2*i]
                y = df.iloc[:, 1 + 2*i + 1]
                #plt.plot(x, y, color='red', marker='x')
                plt.scatter(x.iloc[1], y.iloc[1], marker='o', s=100, c='r', linewidths=2)
                plt.scatter(x.iloc[-1], y.iloc[-1], marker='s', s=100, c='r', linewidths=2)
                
            # Set the title of the plot to the filename
            plt.title(filename)

            # Show the plot
            plt.show()

        elif angle == 150:
            # Initialize empty lists for group assignments
            group11, group12 = [], []
            for i in range(nhel):
                x_diff = abs(df.iloc[1, 1 + 2*i] - df.iloc[-1, 1 + 2*i])
                y_diff = abs(df.iloc[1, 2*i + 2] - df.iloc[-1, 2*i + 1])
                if x_diff > 2500:
                    if y_diff > 2500:
                        group11.append(i)
                    else:
                        group12.append(i)
                else:
                    group12.append(i)
                    
            # Loop over each participant and plot their trajectory
            for i in group11:
                x = df.iloc[:, 1 + 2*i]
                y = df.iloc[:, 1 + 2*i + 1]
                #plt.plot(x, y, color='blue', marker='o')
                plt.scatter(x.iloc[1], y.iloc[1], marker='o', s=100, c='b', linewidths=2)
                plt.scatter(x.iloc[-1], y.iloc[-1], marker='s', s=100, c='b', linewidths=2)
                
            for i in group12:
                x = df.iloc[:, 1 + 2*i]
                y = df.iloc[:, 1 + 2*i + 1]
                #plt.plot(x, y, color='red', marker='x')
                plt.scatter(x.iloc[1], y.iloc[1], marker='o', s=100, c='r', linewidths=2)
                plt.scatter(x.iloc[-1], y.iloc[-1], marker='s', s=100, c='r', linewidths=2)
                
            # Set the title of the plot to the filename
            plt.title(filename)
            plt.xlabel('x [m]')
            plt.ylabel('y [m]')
            # Show the plot
            plt.show()
        
        elif angle == 120:
            # Initialize empty lists for group assignments
            group13, group14 = [], []
            for i in range(nhel):
                x_diff = abs(df.iloc[1, 1 + 2*i] - df.iloc[-1, 1 + 2*i])
                y_diff = abs(df.iloc[1, 2*i + 2] - df.iloc[-1, 2*i + 1])
                if x_diff < 14000:
                    group13.append(i)
                else:
                    group14.append(i)
            
            # Loop over each participant and plot their trajectory
            for i in group13:
                x = df.iloc[:, 1 + 2*i]
                y = df.iloc[:, 1 + 2*i + 1]
                #plt.plot(x, y, color='blue', marker='o')
                plt.scatter(x.iloc[1], y.iloc[1], marker='o', s=100, c='b', linewidths=2)
                plt.scatter(x.iloc[-1], y.iloc[-1], marker='s', s=100, c='b', linewidths=2)
                
            for i in group14:
                x = df.iloc[:, 1 + 2*i]
                y = df.iloc[:, 1 + 2*i + 1]
                #plt.plot(x, y, color='red', marker='x')
                plt.scatter(x.iloc[1], y.iloc[1], marker='o', s=100, c='r', linewidths=2)
                plt.scatter(x.iloc[-1], y.iloc[-1], marker='s', s=100, c='r', linewidths=2)
                
            # Set the title of the plot to the filename
            plt.title(filename)
            
            # Show the plot
            plt.show()

