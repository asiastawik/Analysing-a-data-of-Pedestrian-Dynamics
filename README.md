# Pedestrian Dynamics Analysis

This repository contains an analysis of pedestrian dynamics based on real-world data from experiments conducted in Rennes, France, in 2016. The aim of the project is to study the behavior of pedestrians crossing at different angles and evaluate key metrics such as crossing angles, velocities, and deviations.

## Project Overview

In the experiments, participants were divided into two groups and instructed to cross through each other at various angles (ranging from 0° to 180° in 30° intervals). The data was collected using VICON motion sensing cameras, and the analysis focuses on the following tasks:

### Tasks:
1. **Crossing Angle Calculation:**
   - Compute the actual crossing angles for each experiment by analyzing the trajectories of two groups of participants.
   - Compare the computed angles with the theoretical angles.

2. **Velocity Distribution:**
   - Calculate the velocities of all participants throughout the experiment.
   - Plot normalized velocity distributions for each crossing angle.

3. **Deviation from Expected Path (δ):**
   - Compute the deviation angle, δ, for each participant at each time step, which measures how much they deviate from their expected path.
   - Plot normalized distributions of δ for each crossing angle.

## Data Description

The data includes time-dependent trajectories of participants recorded during the experiments. The key features of the data are:
- **Time Resolution:** The data is recorded at 120 Hz (1 time-step = 1/120 sec).
- **Position Data:** The x and y positions of each participant are provided at each time-step. Odd-numbered columns represent x-positions, and even-numbered columns represent y-positions.

### Example:
- Column 30: x-position of the 15th participant.
- Column 31: y-position of the 15th participant.

## Analysis Outline

1. **Crossing Angle Calculation:**
   - Compute the barycenter (center of mass) of each group’s starting and ending positions.
   - Use these barycenters to define the motion direction of each group.
   - Determine the crossing angle by evaluating the intersection of the motion lines from both groups.

2. **Velocity Calculation:**
   - Estimate the velocities by differentiating the positions with respect to time.
   - Plot normalized velocity distributions for each crossing angle to understand the speed patterns of the pedestrians.

3. **Deviation Calculation (δ):**
   - Calculate δ as the angle between the participant's trajectory and their expected direction.
   - Positive δ represents anti-clockwise deviation, and negative δ represents clockwise deviation.
   - Analyze and plot normalized distributions of δ for each crossing angle to study how deviations are influenced by the crossing angle.

## Visualizations

The repository includes several visualizations to help understand pedestrian behavior under different crossing conditions:
- **Crossing Angle Visualizations** for each trial.
- **Velocity Distribution Plots** for all crossing angles.
- **Deviation Distribution Plots** for each angle showing how participants deviate from their instructed path.

## Conclusion

This project provides insights into the dynamics of pedestrian crowds crossing at various angles. By analyzing trajectories, velocities, and deviations, it helps in understanding the behavior of pedestrians in crowded environments, which can contribute to better crowd management and safety in urban areas.

## Acknowledgments

This analysis is based on data collected by a group of researchers in physics, computer science, and psychology. The data was obtained from a pedestrian dynamics experiment conducted in Rennes, France, in 2016.
