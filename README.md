# android_Validation
## v.1.007
# File Description
## Data_1005.py
- Data download protocol settings code
## Processing_Main_1005.py
- Data download program
- You can change the list of [Ae_Name] and [term_day] and [Start_Month] inside to set the items and duration to download
## sumCSV.py
- It is a code that merges the tar or zip file provided directly from the Android executor and the file downloaded from the Mobius server
- File structure must be set like file structure description file as [structure.txt]
## csv_to_df_val_1005.ipynb
- Data verification and collection rate output program
# Program execution steps
1. Download data from user
2. Read [structure.txt] file and set folder path
3. Processing_Main_1005.py
4. mergeCSV.py
4. csv_to_df_val_1005.ipynb
