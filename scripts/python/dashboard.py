from dash import Dash, dcc, html
import pandas as pd
import plotly.express as px

# load the enhanced dataset

file_path = "C:/data/feature_enhanced_energy_dataset.csv"
data = pd.read_csv(file_path)

# initialize the dash app

app = Dash(__name__)

# create plots for the dashboard

# line chart: CO2 emissions over the years

line_chart = px.line(
    data.groupby('Year')['CO2_Emissions'].mean().reset_index(),
    x='Year', y='CO2_Emissions',
    title="Average CO2 Emissions Over the Years",
    labels={"CO2_Emissions": "Average CO2 Emissions", "Year": "Year"}
)

# bar chart: average renewable percentage by region

region_cols = [col for col in data.columns if col.startswith('Region_')]
data['Region'] = data[region_cols].idxmax(axis=1).str.replace('Region_', '')
bar_chart = px.bar(
    data.groupby('Region')['Renewable_Percentage'].mean().reset_index(),
    x='Region', y='Renewable_Percentage',
    title="Average Renewable Percentage by Region",
    labels={"Renewable_Percentage": "Average Renewable Percentage", "Region": "Region"}
)

# scatter plot: renewable vs fossil fuel percentage

scatter_plot = px.scatter(
    data,
    x='Renewable_Percentage', y='Fossil_Percentage',
    color='High_Renewable_Adoption',
    title="Renewable vs Fossil Fuel Percentage",
    labels={"Renewable_Percentage": "Renewable Percentage", "Fossil_Percentage": "Fossil Percentage"},
    color_continuous_scale="Viridis"
)

# layout for the dashboard

app.layout = html.Div([
    html.H1("Global Energy Trends Dashboard", style={'text-align': 'center'}),
    dcc.Graph(figure=line_chart),
    dcc.Graph(figure=bar_chart),
    dcc.Graph(figure=scatter_plot)
])

# run the app

if __name__ == '__main__':
    app.run_server(debug=True)
