import os
import pandas as pd
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
    
        # Create a new column for the deviations of each pedestrian
        for i in range(nhel):
            df[f"delta_{i}"] = np.nan
        
        # Calculate the velocities of each pedestrian at each time
        for i in range(1, df.shape[0]):
            for j in range(nhel):
                x = df.iloc[i, 1 + 2*j]
                y = df.iloc[i, 1 + 2*j + 1]
                x_prev = df.iloc[i-1, 1 + 2*j]
                y_prev = df.iloc[i-1, 1 + 2*j + 1]
                
                # Calculate the expected direction of motion for the pedestrian
                x_first = df.iloc[0, 1 + 2*j]
                y_first = df.iloc[0, 1 + 2*j + 1]
                x_last = df.iloc[-1, 1 + 2*j]
                y_last = df.iloc[-1, 1 + 2*j + 1]
                expected_direction = np.arctan2(y_last-y_first, x_last-x_first)
                
                # Calculate the angle between the pedestrian's trajectory and the expected direction
                actual_direction = np.arctan2(y-y_prev, x-x_prev)
                delta = actual_direction - expected_direction
                #print(delta)
                
                # Wrap the delta to the range [-pi, pi]
                delta = ((delta + np.pi) % (2*np.pi)) - np.pi
                
                # Set the deviation for the pedestrian at the current time
                df.at[i, f"delta_{j}"] = np.degrees(delta)
        
        df.to_excel(os.path.join(r"C:\Users\asia-\Desktop\BI\Business Intelligence Workplace\Project\deviations", f"{angle}_{filename[:-4]}_with_deviations.xlsx"))

