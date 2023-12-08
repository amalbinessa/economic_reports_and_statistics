
import pandas as pd
# 
# # import pandas_profiling
import streamlit as st
# # from pydantic_settings import BaseSettings # NEW
# # from streamlit_pandas_profiling import st_profile_report

df = pd.read_excel("Data/SAMA_StatisticalReport_2023_clean.xlsx")
print(df)
df.replace('-', 0, inplace=True)

# # pr = df.profile_report()

# # st_profile_report(pr)

columns_list = df.columns.to_list()[1:]
print(columns_list)
print(type(columns_list))
df.reset_index()
Exports = df.loc[2,:].values.flatten().tolist()[1:]
Imports = df.loc[3,:].values.flatten().tolist()[1:]

df_flatten_Agriculture_Forestry_and_Fishing  = df.loc[5,:].values.flatten().tolist()[1:]

df_flatten_Mining_and_Quarrying = df.loc[6,:].values.flatten().tolist()[1:]

df_flatten_Gross_Domestic_Product = df.loc[7,:].values.flatten().tolist()[1:]


print(df_flatten_Gross_Domestic_Product)
columns=['البند','year','صادرات السلع و الخدمات','واردات السلع و الخدمات','الزراعة و الغابات و الاسماك','التعدين و التحجير','الناتج المحلي الاجمالي']

df_flatten = pd.DataFrame({columns[1]:columns_list,
                           columns[2]:Exports,
                           columns[3]:Imports,
                           columns[4]:df_flatten_Agriculture_Forestry_and_Fishing,
                           columns[5]:df_flatten_Mining_and_Quarrying,
                           columns[6]:df_flatten_Gross_Domestic_Product
                           })
print(df_flatten)

import pandas as pd
import plotly.express as px
import streamlit as st

# Assuming you have a DataFrame named 'df_flatten' as described
numeric_columns = [columns[2], columns[3], columns[4], columns[5], columns[6]]
df_flatten[numeric_columns] = df_flatten[numeric_columns].astype(float)

# Create the bubble chart using Plotly Express
fig = px.scatter(df_flatten, x=columns[2], y=columns[3], size=columns[6],
                 hover_data=[columns[4], columns[5]], animation_frame=columns[1],
                 range_x=[df_flatten[columns[2]].min(), df_flatten[columns[2]].max()],
                 range_y=[df_flatten[columns[3]].min(), df_flatten[columns[3]].max()],
                 labels={columns[2]: 'Exports', columns[3]: 'Imports', columns[6]: 'GDP'},
                 title='Bubble Chart with Timeline')

# Display the bubble chart in Streamlit
st.plotly_chart(fig)



# import streamlit as st
# import plotly.graph_objects as go


# # Sample data for the bubble chart
# data = [
#     {'x': 'Category A', 'y': '2022-01-01', 'value': 10, 'text': 'Data point 1'},
#     {'x': 'Category B', 'y': '2022-03-01', 'value': 15, 'text': 'Data point 2'},
#     {'x': 'Category C', 'y': '2022-05-01', 'value': 20, 'text': 'Data point 3'},
#     {'x': 'Category D', 'y': '2022-07-01', 'value': 25, 'text': 'Data point 4'},
#     {'x': 'Category E', 'y': '2022-09-01', 'value': 30, 'text': 'Data point 5'}
# ]

# # Convert the dates to datetime objects
# for d in data:
#     d['y'] = pd.to_datetime(d['y'])

# # Create the bubble chart
# fig = go.Figure(data=go.Scatter(
#     x=[d['x'] for d in data],
#     y=[d['y'] for d in data],
#     mode='markers',
#     marker=dict(
#         size=[d['value'] for d in data],
#         sizemode='diameter',
#         sizeref=0.1,
#         color=[d['value'] for d in data],
#         colorscale='Viridis',
#         showscale=True,
#         colorbar=dict(title='Value')
#     ),
#     text=[d['text'] for d in data]
# ))

# # Set the layout
# fig.update_layout(
#     title='Bubble Chart with Timeline',
#     xaxis=dict(title='Categories'),
#     yaxis=dict(title='Timeline'),
#     hovermode='closest'
# )

# # Render the bubble chart in Streamlit
# st.plotly_chart(fig)



