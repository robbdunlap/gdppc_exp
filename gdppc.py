import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px

gdp_df = pd.read_csv("data/gdppc_data.csv")

countries = gdp_df.country.unique()

st.title("Comparison of Countries' GDPs per capita")
st.markdown('___')
st.header('')

st.header('Select a date range of interest')
st.sidebar.title('Choose 3 Countries to Compare')
country_1_selected = st.sidebar.selectbox('Select country of interest #1', countries, index=(29))
country_2_selected = st.sidebar.selectbox('Select state of interest #2', countries, index=(70))
country_3_selected = st.sidebar.selectbox('Select state of interest #3', countries, index=(160))

countries_for_comparison = []
countries_for_comparison.append(country_1_selected)
countries_for_comparison.append(country_2_selected)
countries_for_comparison.append(country_3_selected)

subselect_of_gdp = gdp_df[gdp_df['country'].isin(countries_for_comparison)]
countries_for_plotting = subselect_of_gdp.pivot(index='year',columns='country',values='gdppc')
countries_for_plotting = countries_for_plotting.reset_index()


value = st.slider('test', min_value=1000, max_value=2018, value=(1900, 2018), step=100)
for_plotting = countries_for_plotting[(countries_for_plotting['year'] >= value[0]) & (countries_for_plotting['year'] <= value[1])]


# Chart title and legends
x_axis_title =  'Date'
y_axis_title =  'GDP per capita'

# State 1 Chart
fig1 = px.line(for_plotting, 
             x="year", 
             y=[country_1_selected, country_2_selected, country_3_selected], 
             labels={"variable":"Countries"},
             title = f"<b>GDP per capita for {country_1_selected}, {country_2_selected}, and {country_3_selected}</b>")
fig1.update_yaxes(title_text=y_axis_title)
fig1.update_xaxes(showgrid=True, title_text=x_axis_title)
#fig1.update_traces(hovertemplate=None, hoverinfo='skip')

st.plotly_chart(fig1, use_container_width=True)

st.header('Tabular version of the above data')
st.markdown('Sort the data by clicking on colunn headers')
st.dataframe(for_plotting)