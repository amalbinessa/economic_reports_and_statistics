# -*- coding: utf-8 -*-
import pandas as pd

# # import pandas_profiling
import streamlit as st
# # from pydantic_settings import BaseSettings # NEW
# # from streamlit_pandas_profiling import st_profile_report
file_path =  'Data/import_export_2_version.xlsx'
with open(file_path, 'r', encoding='UTF-8') as f:
        data = pd.read_excel(f)
# data = pd.read_excel(file_path, encoding='UTF-8')
data.replace('-', 0, inplace=True)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# Translate the column names from Arabic to English
column_translations = {
    'العام': 'Year',
    'صادرات السلع غير النفطية': 'Non-Oil Exports',
    'واردات السلع': 'Imports of Goods',
    'الميزان التجاري': 'Trade Balance',
    'الميزان التجاري باللوغاريتم': 'Trade Balance (Logarithmic)',
    'صادرات االخدمات': 'Service Exports',
    'واردات الخدمات': 'Service Imports',
    'الزراعة ـ الغابات ـ والاسماك': 'Agriculture, Forestry, and Fisheries',
    'التعدين والتحجير': 'Mining and Quarrying',
    'مجموع الموارد الطبيعية': 'Total Natural Resources',
    'الناتج المحلي الإجمالي': 'Gross Domestic Product (GDP)',
    'النمو الاقتصادي': 'Economic Growth'
}


# Renaming the columns
data.rename(columns=column_translations, inplace=True)
data['Economic Growth percentage'] = data['Economic Growth']*100
st.write(data)

# Streamlit page configuration
st.title('Economic Dashboard')
st.subheader('Comparison between Average Trade Balance Change and Economic Growth Rate')

# Creating the line chart
fig, ax = plt.subplots()
ax.plot(data['Year'], data['Trade Balance'], label='Trade Balance')
ax.plot(data['Year'], data['Economic Growth percentage'], label='Economic Growth Rate')
ax.set_xlabel('Year')
ax.set_ylabel('Values')
ax.legend()
ax.grid(True)

# Display the chart in Streamlit
st.pyplot(fig)

# Streamlit page setup
st.title('Economic Insights Dashboard')

# Interactive elements for user input, like sliders or dropdowns, can be added here

# Trade Balance Trend
st.subheader('Trade Balance Trend')
fig, ax = plt.subplots()
ax.plot(data['Year'], data['Trade Balance'])
ax.set_xlabel('Year')
ax.set_ylabel('Trade Balance')
st.pyplot(fig)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to load data

# Streamlit page setup
st.title('Economic Insights Dashboard')

# Trade Balance Trend Analysis
st.subheader('Trade Balance Trend')
fig, ax = plt.subplots()
ax.plot(data['Year'], data['Trade Balance'], color='blue', marker='o')
ax.set_xlabel('Year')
ax.set_ylabel('Trade Balance')
st.pyplot(fig)

# Economic Growth vs Trade Balance
st.subheader('Economic Growth vs Trade Balance')
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(data['Year'], data['Economic Growth'], color='green', marker='o')
ax2.plot(data['Year'], data['Trade Balance'], color='red', marker='o')
ax1.set_xlabel('Year')
ax1.set_ylabel('Economic Growth', color='green')
ax2.set_ylabel('Trade Balance', color='red')
st.pyplot(fig)

# Non-Oil Exports and Service Exports Analysis
st.subheader('Non-Oil Exports and Service Exports')
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
ax1.plot(data['Year'], data['Non-Oil Exports'], color='purple', marker='o')
ax1.set_title('Non-Oil Exports')
ax2.plot(data['Year'], data['Service Exports'], color='orange', marker='o')
ax2.set_title('Service Exports')
for ax in (ax1, ax2):
    ax.set_xlabel('Year')
    ax.set_ylabel('Value')
st.pyplot(fig)

# Import Patterns and Economic Health
st.subheader('Import Patterns')
fig, ax = plt.subplots()
ax.plot(data['Year'], data['Imports of Goods'], color='brown', marker='o')
ax.set_xlabel('Year')
ax.set_ylabel('Imports of Goods')
st.pyplot(fig)

# Sector Analysis
# Placeholder for sector analysis plots
st.subheader('Sector Analysis')
st.write("Placeholder for sector analysis plots")

# Natural Resources Utilization
st.subheader('Natural Resources Utilization')
# Placeholder for natural resources utilization plot
st.write("Placeholder for natural resources utilization plot")

# Additional analyses can be added here

# Run this script using 'streamlit run your_script.py'
