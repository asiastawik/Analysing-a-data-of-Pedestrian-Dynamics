import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Set the directory containing the CSV files
directory = r"C:\Users\asia-\Desktop\BI\Business Intelligence Workplace\Project\csv"

# create the angle_data table with the appropriate column names
angle_data = pd.DataFrame(columns=[0, 30, 60, 90, 120, 150, 180])
#angle_data = pd.DataFrame([['-']*7 for _ in range(20)], columns=['0', '30', '60', '90', '120', '150', '180'])
angle90_list = []
angle0_list = []
angle180_list = []
angle30_list = []
angle60_list = []
angle150_list = []
angle120_list = []

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
                if x_diff < 5000:
                    group1.append(i)
                else:
                    group2.append(i)
            
            print(group1)
            print(group2)
            # Create a new figure for the plot
            fig, ax = plt.subplots()
            
            for i in group1:
                x = df.iloc[:, 1 + 2*i]
                y = df.iloc[:, 1 + 2*i + 1]
                #plt.plot(x, y, color='blue', marker='o')
                plt.scatter(x.iloc[1], y.iloc[1], marker='o', s=10, c='b', linewidths=2)
                plt.scatter(x.iloc[-1], y.iloc[-1], marker='s', s=10, c='b', linewidths=2)
                
            for i in group2:
                x = df.iloc[:, 1 + 2*i]
                y = df.iloc[:, 1 + 2*i + 1]
                #plt.plot(x, y, color='red', marker='x')
                plt.scatter(x.iloc[1], y.iloc[1], marker='o', s=10, c='r', linewidths=2)
                plt.scatter(x.iloc[-1], y.iloc[-1], marker='s', s=10, c='r', linewidths=2)
                
            # Find the barycenters of participants in group 1
            group1_x_cols = [1 + 2*i for i in group1]
            group1_y_cols = [1 + 2*i + 1 for i in group1]
            group1_barycenter_x = df.iloc[:, group1_x_cols].mean(axis=1)
            group1_barycenter_y = df.iloc[:, group1_y_cols].mean(axis=1)
            point1 = (group1_barycenter_x.iloc[1], group1_barycenter_y.iloc[1])
            point2 = (group1_barycenter_x.iloc[-1], group1_barycenter_y.iloc[-1])
            
            ax.scatter(*point1, marker='o', s=100, c='k', linewidths=2)
            ax.scatter(*point2, marker='s', s=100, c='k', linewidths=2)

            #plt.plot(group1_barycenter_x, group1_barycenter_y, color='k', linestyle='--', linewidth=1)
            group1_plot, = plt.plot(group1_barycenter_x, group1_barycenter_y, color='k', linestyle='--', linewidth=1)

            #plt.plot([group1_barycenter_x.iloc[0], group2_barycenter_x.iloc[0]], [group1_barycenter_y.iloc[0], group2_barycenter_y.iloc[0]], color='k', linestyle='--', linewidth=1)

            
            # Find the barycenters of participants in group 2
            group2_x_cols = [1 + 2*i for i in group2]
            group2_y_cols = [1 + 2*i + 1 for i in group2]
            group2_barycenter_x = df.iloc[:, group2_x_cols].mean(axis=1)
            group2_barycenter_y = df.iloc[:, group2_y_cols].mean(axis=1)
            point3 = (group2_barycenter_x.iloc[1], group2_barycenter_y.iloc[1])
            point4 = (group2_barycenter_x.iloc[-1], group2_barycenter_y.iloc[-1])
            
            ax.scatter(*point3, marker='o', s=100, c='g', linewidths=2)
            ax.scatter(*point4, marker='s', s=100, c='g', linewidths=2)
            
            #plt.plot(group2_barycenter_x, group2_barycenter_y, color='k', linestyle='--', linewidth=1)
            group2_plot, = plt.plot(group2_barycenter_x, group2_barycenter_y, color='k', linestyle='--', linewidth=1)
            
            
            # Calculate the observed crossing angle between the two groups
            vec1 = (point2[0]-point1[0], point2[1]-point1[1])
            vec2 = (point4[0]-point3[0], point4[1]-point3[1])
            cos_angle = np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
            crossing_angle_observed = np.arccos(cos_angle) * 180 / np.pi
            angle90_list.append(crossing_angle_observed)
            #print(angle_data)
            
            print(f"Observed crossing angle: {crossing_angle_observed:.2f} degrees")

            
            # Set the title of the plot to the filename
            plt.title(f"Crossing Angle: 90°, Observed: {crossing_angle_observed:.2f}°, Filename: {os.path.basename(filename)}")
            
            plt.xlabel('x [m]')
            plt.ylabel('y [m]')

            # Show the plot
            plt.show()
        
        elif angle == 0:
            # Assign all participants to the same group
            group3 = range(nhel)
            group4 = []
            
            # Create a new figure for the plot
            fig, ax = plt.subplots()
            
            for i in group3:
                x = df.iloc[:, 1 + 2*i]
                y = df.iloc[:, 1 + 2*i + 1]
                #plt.plot(x, y, color='blue', marker='o')
                plt.scatter(x.iloc[1], y.iloc[1], marker='o', s=10, c='b', linewidths=2)
                plt.scatter(x.iloc[-1], y.iloc[-1], marker='s', s=10, c='b', linewidths=2)
                
            # Find the barycenters of participants in group 3
            group3_x_cols = [1 + 2*i for i in group3]
            group3_y_cols = [1 + 2*i + 1 for i in group3]
            group3_barycenter_x = df.iloc[:, group3_x_cols].mean(axis=1)
            group3_barycenter_y = df.iloc[:, group3_y_cols].mean(axis=1)
            point5 = (group3_barycenter_x.iloc[1], group3_barycenter_y.iloc[1])
            point6 = (group3_barycenter_x.iloc[-1], group3_barycenter_y.iloc[-1])
            
            ax.scatter(*point5, marker='o', s=100, c='k', linewidths=2)
            ax.scatter(*point6, marker='s', s=100, c='k', linewidths=2)

            group3_plot, = plt.plot(group3_barycenter_x, group3_barycenter_y, color='k', linestyle='--', linewidth=1)

            # Find the barycenters of participants in group 4
            group4_x_cols = [1 + 2*i for i in group4]
            group4_y_cols = [1 + 2*i + 1 for i in group4]
            group4_barycenter_x = df.iloc[:, group4_x_cols].mean(axis=1)
            group4_barycenter_y = df.iloc[:, group4_y_cols].mean(axis=1)
            point7 = (group4_barycenter_x.iloc[1], group4_barycenter_y.iloc[1])
            point8 = (group4_barycenter_x.iloc[-1], group4_barycenter_y.iloc[-1])
            
            ax.scatter(*point7, marker='o', s=100, c='g', linewidths=2)
            ax.scatter(*point8, marker='s', s=100, c='g', linewidths=2)
        
            group4_plot, = plt.plot(group4_barycenter_x, group4_barycenter_y, color='k', linestyle='--', linewidth=1)
            
            
            # Calculate the observed crossing angle between the two groups
            vec3 = (point6[0]-point5[0], point6[1]-point5[1])
            vec4 = (point8[0]-point7[0], point8[1]-point7[1])
            cos_angle = np.dot(vec3, vec4) / (np.linalg.norm(vec3) * np.linalg.norm(vec4))
            crossing_angle_observed = np.arccos(cos_angle) * 180 / np.pi
            angle0_list.append(crossing_angle_observed)
            
            print(f"Observed crossing angle: {crossing_angle_observed:.2f} degrees")

            # Set the title of the plot to the filename
            plt.title(f"Crossing Angle: 0°, Observed: {crossing_angle_observed:.2f}°, Filename: {os.path.basename(filename)}")
            
            plt.xlabel('x [m]')
            plt.ylabel('y [m]')

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
            
            # Create a new figure for the plot
            fig, ax = plt.subplots()
            
            # Loop over each participant and plot their trajectory
            for i in group5:
                x = df.iloc[:, 1 + 2*i]
                y = df.iloc[:, 1 + 2*i + 1]
                #plt.plot(x, y, color='blue', marker='o')
                plt.scatter(x.iloc[1], y.iloc[1], marker='o', s=10, c='b', linewidths=2)
                plt.scatter(x.iloc[-1], y.iloc[-1], marker='s', s=10, c='b', linewidths=2)
                
            for i in group6:
                x = df.iloc[:, 1 + 2*i]
                y = df.iloc[:, 1 + 2*i + 1]
                #plt.plot(x, y, color='red', marker='x')
                plt.scatter(x.iloc[1], y.iloc[1], marker='o', s=10, c='r', linewidths=2)
                plt.scatter(x.iloc[-1], y.iloc[-1], marker='s', s=10, c='r', linewidths=2)
                
            # Find the barycenters of participants in group 5
            group5_x_cols = [1 + 2*i for i in group5]
            group5_y_cols = [1 + 2*i + 1 for i in group5]
            group5_barycenter_x = df.iloc[:, group5_x_cols].mean(axis=1)
            group5_barycenter_y = df.iloc[:, group5_y_cols].mean(axis=1)
            point9 = (group5_barycenter_x.iloc[1], group5_barycenter_y.iloc[1])
            point10 = (group5_barycenter_x.iloc[-1], group5_barycenter_y.iloc[-1])
            
            ax.scatter(*point9, marker='o', s=100, c='k', linewidths=2)
            ax.scatter(*point10, marker='s', s=100, c='k', linewidths=2)

            group5_plot, = plt.plot(group5_barycenter_x, group5_barycenter_y, color='k', linestyle='--', linewidth=1)

            # Find the barycenters of participants in group 6
            group6_x_cols = [1 + 2*i for i in group6]
            group6_y_cols = [1 + 2*i + 1 for i in group6]
            group6_barycenter_x = df.iloc[:, group6_x_cols].mean(axis=1)
            group6_barycenter_y = df.iloc[:, group6_y_cols].mean(axis=1)
            point11 = (group6_barycenter_x.iloc[1], group6_barycenter_y.iloc[1])
            point12 = (group6_barycenter_x.iloc[-1], group6_barycenter_y.iloc[-1])
            
            ax.scatter(*point11, marker='o', s=100, c='g', linewidths=2)
            ax.scatter(*point12, marker='s', s=100, c='g', linewidths=2)
        
            group6_plot, = plt.plot(group6_barycenter_x, group6_barycenter_y, color='k', linestyle='--', linewidth=1)
            
            
            # Calculate the observed crossing angle between the two groups
            vec5 = (point10[0]-point9[0], point10[1]-point9[1])
            vec6 = (point12[0]-point11[0], point12[1]-point11[1])
            cos_angle = np.dot(vec5, vec6) / (np.linalg.norm(vec5) * np.linalg.norm(vec6))
            crossing_angle_observed = np.arccos(cos_angle) * 180 / np.pi
            angle180_list.append(crossing_angle_observed)
            
            print(f"Observed crossing angle: {crossing_angle_observed:.2f} degrees")

            # Set the title of the plot to the filename
            plt.title(f"Crossing Angle: 180°, Observed: {crossing_angle_observed:.2f}°, Filename: {os.path.basename(filename)}")
            
            plt.xlabel('x [m]')
            plt.ylabel('y [m]')

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
                    
            # Create a new figure for the plot
            fig, ax = plt.subplots()
            
            # Loop over each participant and plot their trajectory
            for i in group7:
                x = df.iloc[:, 1 + 2*i]
                y = df.iloc[:, 1 + 2*i + 1]
                #plt.plot(x, y, color='blue', marker='o')
                plt.scatter(x.iloc[1], y.iloc[1], marker='o', s=10, c='b', linewidths=2)
                plt.scatter(x.iloc[-1], y.iloc[-1], marker='s', s=10, c='b', linewidths=2)
                
            for i in group8:
                x = df.iloc[:, 1 + 2*i]
                y = df.iloc[:, 1 + 2*i + 1]
                #plt.plot(x, y, color='red', marker='x')
                plt.scatter(x.iloc[1], y.iloc[1], marker='o', s=10, c='r', linewidths=2)
                plt.scatter(x.iloc[-1], y.iloc[-1], marker='s', s=10, c='r', linewidths=2)
                
            # Find the barycenters of participants in group 7
            group7_x_cols = [1 + 2*i for i in group7]
            group7_y_cols = [1 + 2*i + 1 for i in group7]
            group7_barycenter_x = df.iloc[:, group7_x_cols].mean(axis=1)
            group7_barycenter_y = df.iloc[:, group7_y_cols].mean(axis=1)
            point13 = (group7_barycenter_x.iloc[1], group7_barycenter_y.iloc[1])
            point14 = (group7_barycenter_x.iloc[-1], group7_barycenter_y.iloc[-1])
            
            ax.scatter(*point13, marker='o', s=100, c='k', linewidths=2)
            ax.scatter(*point14, marker='s', s=100, c='k', linewidths=2)

            group7_plot, = plt.plot(group7_barycenter_x, group7_barycenter_y, color='k', linestyle='--', linewidth=1)

            # Find the barycenters of participants in group 8
            group8_x_cols = [1 + 2*i for i in group8]
            group8_y_cols = [1 + 2*i + 1 for i in group8]
            group8_barycenter_x = df.iloc[:, group8_x_cols].mean(axis=1)
            group8_barycenter_y = df.iloc[:, group8_y_cols].mean(axis=1)
            point15 = (group8_barycenter_x.iloc[1], group8_barycenter_y.iloc[1])
            point16 = (group8_barycenter_x.iloc[-1], group8_barycenter_y.iloc[-1])
            
            ax.scatter(*point15, marker='o', s=100, c='g', linewidths=2)
            ax.scatter(*point16, marker='s', s=100, c='g', linewidths=2)
        
            group8_plot, = plt.plot(group8_barycenter_x, group8_barycenter_y, color='k', linestyle='--', linewidth=1)
            
            
            # Calculate the observed crossing angle between the two groups
            vec7 = (point14[0]-point13[0], point14[1]-point13[1])
            vec8 = (point16[0]-point15[0], point16[1]-point15[1])
            cos_angle = np.dot(vec7, vec8) / (np.linalg.norm(vec7) * np.linalg.norm(vec8))
            crossing_angle_observed = np.arccos(cos_angle) * 180 / np.pi
            angle30_list.append(crossing_angle_observed)
            
            print(f"Observed crossing angle: {crossing_angle_observed:.2f} degrees")

            # Set the title of the plot to the filename
            plt.title(f"Crossing Angle: 30°, Observed: {crossing_angle_observed:.2f}°, Filename: {os.path.basename(filename)}")
            
            plt.xlabel('x [m]')
            plt.ylabel('y [m]')

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
                    
            # Create a new figure for the plot
            fig, ax = plt.subplots()
            
            # Loop over each participant and plot their trajectory
            for i in group9:
                x = df.iloc[:, 1 + 2*i]
                y = df.iloc[:, 1 + 2*i + 1]
                #plt.plot(x, y, color='blue', marker='o')
                plt.scatter(x.iloc[1], y.iloc[1], marker='o', s=10, c='b', linewidths=2)
                plt.scatter(x.iloc[-1], y.iloc[-1], marker='s', s=10, c='b', linewidths=2)
                
            for i in group10:
                x = df.iloc[:, 1 + 2*i]
                y = df.iloc[:, 1 + 2*i + 1]
                #plt.plot(x, y, color='red', marker='x')
                plt.scatter(x.iloc[1], y.iloc[1], marker='o', s=10, c='r', linewidths=2)
                plt.scatter(x.iloc[-1], y.iloc[-1], marker='s', s=10, c='r', linewidths=2)
                
            # Find the barycenters of participants in group 9
            group9_x_cols = [1 + 2*i for i in group9]
            group9_y_cols = [1 + 2*i + 1 for i in group9]
            group9_barycenter_x = df.iloc[:, group9_x_cols].mean(axis=1)
            group9_barycenter_y = df.iloc[:, group9_y_cols].mean(axis=1)
            point17 = (group9_barycenter_x.iloc[1], group9_barycenter_y.iloc[1])
            point18 = (group9_barycenter_x.iloc[-1], group9_barycenter_y.iloc[-1])
            
            ax.scatter(*point17, marker='o', s=100, c='k', linewidths=2)
            ax.scatter(*point18, marker='s', s=100, c='k', linewidths=2)

            group9_plot, = plt.plot(group9_barycenter_x, group9_barycenter_y, color='k', linestyle='--', linewidth=1)

            # Find the barycenters of participants in group 10
            group10_x_cols = [1 + 2*i for i in group10]
            group10_y_cols = [1 + 2*i + 1 for i in group10]
            group10_barycenter_x = df.iloc[:, group10_x_cols].mean(axis=1)
            group10_barycenter_y = df.iloc[:, group10_y_cols].mean(axis=1)
            point19 = (group10_barycenter_x.iloc[1], group10_barycenter_y.iloc[1])
            point20 = (group10_barycenter_x.iloc[-1], group10_barycenter_y.iloc[-1])
            
            ax.scatter(*point19, marker='o', s=100, c='g', linewidths=2)
            ax.scatter(*point20, marker='s', s=100, c='g', linewidths=2)
        
            group10_plot, = plt.plot(group10_barycenter_x, group10_barycenter_y, color='k', linestyle='--', linewidth=1)
            
            
            # Calculate the observed crossing angle between the two groups
            vec9 = (point18[0]-point17[0], point18[1]-point17[1])
            vec10 = (point20[0]-point19[0], point20[1]-point19[1])
            cos_angle = np.dot(vec9, vec10) / (np.linalg.norm(vec9) * np.linalg.norm(vec10))
            crossing_angle_observed = np.arccos(cos_angle) * 180 / np.pi
            angle60_list.append(crossing_angle_observed)
            
            print(f"Observed crossing angle: {crossing_angle_observed:.2f} degrees")

            # Set the title of the plot to the filename
            plt.title(f"Crossing Angle: 60°, Observed: {crossing_angle_observed:.2f}°, Filename: {os.path.basename(filename)}")
            
            plt.xlabel('x [m]')
            plt.ylabel('y [m]')

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
            
            # Create a new figure for the plot
            fig, ax = plt.subplots()
            
            # Loop over each participant and plot their trajectory
            for i in group11:
                x = df.iloc[:, 1 + 2*i]
                y = df.iloc[:, 1 + 2*i + 1]
                #plt.plot(x, y, color='blue', marker='o')
                plt.scatter(x.iloc[1], y.iloc[1], marker='o', s=10, c='b', linewidths=2)
                plt.scatter(x.iloc[-1], y.iloc[-1], marker='s', s=10, c='b', linewidths=2)
                
            for i in group12:
                x = df.iloc[:, 1 + 2*i]
                y = df.iloc[:, 1 + 2*i + 1]
                #plt.plot(x, y, color='red', marker='x')
                plt.scatter(x.iloc[1], y.iloc[1], marker='o', s=10, c='r', linewidths=2)
                plt.scatter(x.iloc[-1], y.iloc[-1], marker='s', s=10, c='r', linewidths=2)
                
            # Find the barycenters of participants in group 11
            group11_x_cols = [1 + 2*i for i in group11]
            group11_y_cols = [1 + 2*i + 1 for i in group11]
            group11_barycenter_x = df.iloc[:, group11_x_cols].mean(axis=1)
            group11_barycenter_y = df.iloc[:, group11_y_cols].mean(axis=1)
            point21 = (group11_barycenter_x.iloc[1], group11_barycenter_y.iloc[1])
            point22 = (group11_barycenter_x.iloc[-1], group11_barycenter_y.iloc[-1])
            
            ax.scatter(*point21, marker='o', s=100, c='k', linewidths=2)
            ax.scatter(*point22, marker='s', s=100, c='k', linewidths=2)

            group11_plot, = plt.plot(group11_barycenter_x, group11_barycenter_y, color='k', linestyle='--', linewidth=1)

            # Find the barycenters of participants in group 12
            group12_x_cols = [1 + 2*i for i in group12]
            group12_y_cols = [1 + 2*i + 1 for i in group12]
            group12_barycenter_x = df.iloc[:, group12_x_cols].mean(axis=1)
            group12_barycenter_y = df.iloc[:, group12_y_cols].mean(axis=1)
            point23 = (group12_barycenter_x.iloc[1], group12_barycenter_y.iloc[1])
            point24 = (group12_barycenter_x.iloc[-1], group12_barycenter_y.iloc[-1])
            
            ax.scatter(*point23, marker='o', s=100, c='g', linewidths=2)
            ax.scatter(*point24, marker='s', s=100, c='g', linewidths=2)
        
            group12_plot, = plt.plot(group12_barycenter_x, group12_barycenter_y, color='k', linestyle='--', linewidth=1)
            
            
            # Calculate the observed crossing angle between the two groups
            vec11 = (point22[0]-point21[0], point22[1]-point21[1])
            vec12 = (point24[0]-point23[0], point24[1]-point23[1])
            cos_angle = np.dot(vec11, vec12) / (np.linalg.norm(vec11) * np.linalg.norm(vec12))
            crossing_angle_observed = np.arccos(cos_angle) * 180 / np.pi
            angle150_list.append(crossing_angle_observed)
            
            print(f"Observed crossing angle: {crossing_angle_observed:.2f} degrees")

            # Set the title of the plot to the filename
            plt.title(f"Crossing Angle: 150°, Observed: {crossing_angle_observed:.2f}°, Filename: {os.path.basename(filename)}")
            
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
            
            # Create a new figure for the plot
            fig, ax = plt.subplots()
            
            # Loop over each participant and plot their trajectory
            for i in group13:
                x = df.iloc[:, 1 + 2*i]
                y = df.iloc[:, 1 + 2*i + 1]
                #plt.plot(x, y, color='blue', marker='o')
                plt.scatter(x.iloc[1], y.iloc[1], marker='o', s=10, c='b', linewidths=2)
                plt.scatter(x.iloc[-1], y.iloc[-1], marker='s', s=10, c='b', linewidths=2)
                
            for i in group14:
                x = df.iloc[:, 1 + 2*i]
                y = df.iloc[:, 1 + 2*i + 1]
                #plt.plot(x, y, color='red', marker='x')
                plt.scatter(x.iloc[1], y.iloc[1], marker='o', s=10, c='r', linewidths=2)
                plt.scatter(x.iloc[-1], y.iloc[-1], marker='s', s=10, c='r', linewidths=2)
                
            # Find the barycenters of participants in group 13
            group13_x_cols = [1 + 2*i for i in group13]
            group13_y_cols = [1 + 2*i + 1 for i in group13]
            group13_barycenter_x = df.iloc[:, group13_x_cols].mean(axis=1)
            group13_barycenter_y = df.iloc[:, group13_y_cols].mean(axis=1)
            point25 = (group13_barycenter_x.iloc[1], group13_barycenter_y.iloc[1])
            point26 = (group13_barycenter_x.iloc[-1], group13_barycenter_y.iloc[-1])
            
            ax.scatter(*point25, marker='o', s=100, c='k', linewidths=2)
            ax.scatter(*point26, marker='s', s=100, c='k', linewidths=2)

            group13_plot, = plt.plot(group13_barycenter_x, group13_barycenter_y, color='k', linestyle='--', linewidth=1)

            # Find the barycenters of participants in group 14
            group14_x_cols = [1 + 2*i for i in group14]
            group14_y_cols = [1 + 2*i + 1 for i in group14]
            group14_barycenter_x = df.iloc[:, group14_x_cols].mean(axis=1)
            group14_barycenter_y = df.iloc[:, group14_y_cols].mean(axis=1)
            point27 = (group14_barycenter_x.iloc[1], group14_barycenter_y.iloc[1])
            point28 = (group14_barycenter_x.iloc[-1], group14_barycenter_y.iloc[-1])
            
            ax.scatter(*point27, marker='o', s=100, c='g', linewidths=2)
            ax.scatter(*point28, marker='s', s=100, c='g', linewidths=2)
        
            group14_plot, = plt.plot(group14_barycenter_x, group14_barycenter_y, color='k', linestyle='--', linewidth=1)
            
            
            # Calculate the observed crossing angle between the two groups
            vec13 = (point26[0]-point25[0], point26[1]-point25[1])
            vec14 = (point28[0]-point27[0], point28[1]-point27[1])
            cos_angle = np.dot(vec13, vec14) / (np.linalg.norm(vec13) * np.linalg.norm(vec14))
            crossing_angle_observed = np.arccos(cos_angle) * 180 / np.pi
            angle120_list.append(crossing_angle_observed)
            
            print(f"Observed crossing angle: {crossing_angle_observed:.2f} degrees")

            # Set the title of the plot to the filename
            plt.title(f"Crossing Angle: 120°, Observed: {crossing_angle_observed:.2f}°, Filename: {os.path.basename(filename)}")
            
            plt.xlabel('x [m]')
            plt.ylabel('y [m]')

            # Show the plot
            plt.show()
            
        else:
            print(f"Angle {angle} is not currently supported.")

# Creating properly shown list
x90 = len(angle90_list)
x0 = len(angle0_list)
for i in range(x90 - x0):
    angle0_list.append('')
angle30_list.append('')
angle60_list.extend([''] * 2)
angle120_list.extend([''] * 2)
angle150_list.extend([''] * 2)
angle180_list.extend([''] * 2)

# Adding lists to angle_data
angle_data[0] = angle0_list
angle_data[30] = angle30_list
angle_data[60] = angle60_list
angle_data[90] = angle90_list
angle_data[120] = angle120_list
angle_data[150] = angle150_list
angle_data[180] = angle180_list

print(angle_data)

# Save the data into Excel file
angle_data.to_excel("angle_data.xlsx")
        
    