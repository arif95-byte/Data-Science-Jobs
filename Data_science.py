# %%
import pandas as pd

# Read the CSV file into a pandas DataFrame
data_science = pd.read_csv('jobs_in_data.csv')
data_science.head()

# %%
# explore the data
data_science.info()

# %%
# count the unique value in experience_level column
data_science.experience_level.value_counts()

# %%
# count the unique value in work_setting column
data_science.work_setting.value_counts()

# %%
# count the unique value in company_size column
data_science.company_size.value_counts()

# %%
# count the unique value in employment_type column
data_science.employment_type.value_counts()

# %%
# count the unique value in employee_residence column
data_science.employee_residence.value_counts()

# %%
# convert to excel file to be visualize
data_science.to_excel('data_science_final.xlsx', sheet_name='data_jobs')


