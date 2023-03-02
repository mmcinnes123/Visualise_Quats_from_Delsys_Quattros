# This script reads and plots quaternions from a raw Delsys Quattro IMU file

import matplotlib.pyplot as plt
import pandas as pd
import math

### SETTINGS
name = "MovA"
how_many_sensors = 4
plot_sen1 = True
plot_sen2 = True
plot_sen3 = True
plot_sen4 = True
save_fig = True


# Define some names
input_file = name + ".csv"
figname1 = name + "_Sen1" + ".png"
figname2 = name + "_Sen2" + ".png"
figname3 = name + "_Sen3" + ".png"
figname4 = name + "_Sen4" + ".png"


### IMPORT AND PREPARE THE DATA

# Time
with open(input_file, 'r') as file:
    time_column = [8]
    Time = pd.read_csv(file, header=35, usecols=time_column)

# Define which columns to use based on how many sensors
columns = ["Quattro sensor 1: ORIENT.W 1", "Quattro sensor 1: ORIENT.X 1", "Quattro sensor 1: ORIENT.Y 1", "Quattro sensor 1: ORIENT.Z 1"]
if how_many_sensors >= 2:
    columns.extend(["Quattro sensor 2: ORIENT.W 2", "Quattro sensor 2: ORIENT.X 2", "Quattro sensor 2: ORIENT.Y 2", "Quattro sensor 2: ORIENT.Z 2"])
if how_many_sensors >= 3:
    columns.extend(["Quattro sensor 3: ORIENT.W 3", "Quattro sensor 3: ORIENT.X 3", "Quattro sensor 3: ORIENT.Y 3", "Quattro sensor 3: ORIENT.Z 3"])
if how_many_sensors >= 4:
    columns.extend(["Quattro sensor 4: ORIENT.W 4", "Quattro sensor 4: ORIENT.X 4", "Quattro sensor 4: ORIENT.Y 4", "Quattro sensor 4: ORIENT.Z 4"])

# Open the file and create a data frame
with open(input_file, 'r') as file:
    df = pd.read_csv(file, header=35, usecols=columns)

# Add time column in
combo = [Time, df]
df = pd.concat(combo, axis=1)

# Get rid of rows with zeros (before data has started streaming)
for row in df.index:
    if df["Quattro sensor 1: ORIENT.W 1"][row] == 0:
        df.drop(row, axis=0, inplace=True)



### PLOT EACH SENSOR IN SAME FIGURE (QUATS)

figure, axis = plt.subplots(4, 1)
plt.subplots_adjust(hspace=0.9)

# Plot quaternions of sensor 1
if plot_sen1 == True:
    df.plot(x="X[s].4", y=["Quattro sensor 1: ORIENT.W 1", "Quattro sensor 1: ORIENT.X 1",
                                "Quattro sensor 1: ORIENT.Y 1", "Quattro sensor 1: ORIENT.Z 1"], figsize=(10,8), ax=axis[0], grid=True)
    axis[0].set_title("Sensor 1 Quaternions")
    axis[0].set_xlabel("Time [s]")
    axis[0].legend(["W1", "X1", "Y1", "Z1"])
    axis[0].grid(visible=True, which="both")
    axis[0].set_yticks([-1, -0.5, 0, 0.5, 1])
# Plot quaternions of sensor 2
if plot_sen2 == True:
    df.plot(x="X[s].4", y=["Quattro sensor 2: ORIENT.W 2", "Quattro sensor 2: ORIENT.X 2",
                                "Quattro sensor 2: ORIENT.Y 2", "Quattro sensor 2: ORIENT.Z 2"], figsize=(10,8), ax=axis[1])
    axis[1].set_title("Sensor 2 Quaternions")
    axis[1].set_xlabel("Time [s]")
    axis[1].legend(["W1", "X1", "Y1", "Z1"])
    axis[1].grid(visible=True, which="both")
    axis[1].set_yticks([-1, -0.5, 0, 0.5, 1])
# Plot quaternions of sensor 3
if plot_sen3 == True:
    df.plot(x="X[s].4", y=["Quattro sensor 3: ORIENT.W 3", "Quattro sensor 3: ORIENT.X 3",
                                "Quattro sensor 3: ORIENT.Y 3", "Quattro sensor 3: ORIENT.Z 3"], figsize=(10,8), ax=axis[2])
    axis[2].set_title("Sensor 3 Quaternions")
    axis[2].set_xlabel("Time [s]")
    axis[2].legend(["W1", "X1", "Y1", "Z1"])
    axis[2].grid(visible=True, which="both")
    axis[2].set_yticks([-1, -0.5, 0, 0.5, 1])
# Plot quaternions of sensor 4
if plot_sen4 == True:
    df.plot(x="X[s].4", y=["Quattro sensor 4: ORIENT.W 4", "Quattro sensor 4: ORIENT.X 4",
                                "Quattro sensor 4: ORIENT.Y 4", "Quattro sensor 4: ORIENT.Z 4"], figsize=(10,8), ax=axis[3])
    axis[3].set_title("Sensor 4 Quaternions")
    axis[3].set_xlabel("Time [s]")
    axis[3].legend(["W1", "X1", "Y1", "Z1"])
    axis[3].grid(visible=True, which="both")
    axis[3].set_yticks([-1, -0.5, 0, 0.5, 1])

if save_fig == True:
    plt.savefig(figname1)
# plt.show()
plt.clf()
