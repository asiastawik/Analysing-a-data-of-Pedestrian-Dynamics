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
    
        # Create a new column for the velocities of each pedestrian
        for i in range(nhel):
            df[f"v_{i}"] = np.nan
        
        # Calculate the velocities of each pedestrian at each time
        for i in range(1, df.shape[0]):
            for j in range(nhel):
                x = df.iloc[i, 1 + 2*j]
                y = df.iloc[i, 1 + 2*j + 1]
                x_prev = df.iloc[i-1, 1 + 2*j]
                y_prev = df.iloc[i-1, 1 + 2*j + 1]
                velocity = ((x - x_prev)**2 + (y - y_prev)**2)**0.5 / 1000 * 120
                df.at[i, f"v_{j}"] = velocity
        
        df.to_excel(os.path.join(r"C:\Users\asia-\Desktop\BI\Business Intelligence Workplace\Project\velocities", f"{angle}_{filename[:-4]}_with_velocities.xlsx"))

