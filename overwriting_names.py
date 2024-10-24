import os

angle_0_files = ['CF106', 'CF105', 'CF104', 'CF103', 'CF102', 'CF101', 'CF1004', 'CF1003', 'CF1002', 'CF1001']
angle_30_files = ['CF227', 'CF226', 'CF225', 'CF224', 'CF109', 'CF108', 'CF107', 'CF2024', 'CF2023', 'CF2022', 'CF2021', 'CF112', 'CF111', 'CF110', 'CF1008', 'CF1007', 'CF1006', 'CF1005']
angle_60_files = ['CF223', 'CF222', 'CF221', 'CF220', 'CF2020', 'CF2019', 'CF2018', 'CF2017', 'CF118', 'CF117', 'CF116', 'CF115', 'CF114', 'CF113', 'CF1012', 'CF1011', 'CF1010']
angle_90_files = ['CF218', 'CF217', 'CF216', 'CF203', 'CF202', 'CF2016', 'CF2015', 'CF2014', 'CF2013', 'CF201', 'CF124', 'CF122', 'CF121', 'CF120', 'CF119', 'CF1016', 'CF1015', 'CF1014', 'CF1013']
angle_150_files = ['CF214', 'CF213', 'CF212', 'CF2008', 'CF2007', 'CF2006', 'CF2005', 'CF136', 'CF135', 'CF134', 'CF133', 'CF132', 'CF131', 'CF1024', 'CF1023', 'CF1022', 'CF1021']
angle_120_files = ['CF211', 'CF210', 'CF209', 'CF208', 'CF2011', 'CF2010', 'CF2009', 'CF130', 'CF129', 'CF128', 'CF127', 'CF126', 'CF125', 'CF1020', 'CF1019', 'CF1018', 'CF1017']
angle_180_files = ['CF207', 'CF206', 'CF205', 'CF204', 'CF2004', 'CF2003', 'CF2002', 'CF2001', 'CF142', 'CF141', 'CF140', 'CF139', 'CF138', 'CF137', 'CF1028', 'CF1026', 'CF1025']

directory = r"C:\Users\asia-\Desktop\BI\Business Intelligence Workplace\Project\csv"
modified_directory = r"C:\Users\asia-\Desktop\BI\Business Intelligence Workplace\Project\modified_csv"

# List of tuples containing the angle and corresponding list of files
angle_to_files = {
    0: angle_0_files,
    30: angle_30_files,
    60: angle_60_files,
    90: angle_90_files,
    150: angle_150_files,
    120: angle_120_files,
    180: angle_180_files
}

# Iterate through each angle and its list of filenames, and rename the files
for angle, filenames in angle_to_files.items():
    for filename in filenames:
        old_filepath = os.path.join(directory, f"{filename}.csv")
        new_filename = f"{angle}_{filename}"
        new_filepath = os.path.join(directory, f"{new_filename}.csv")
        os.rename(old_filepath, new_filepath)
        
# Deleting CF1009 file, because it has angle = 45.
file_to_delete = "CF1009.csv"
file_path = os.path.join(directory, file_to_delete)

os.remove(file_path)
