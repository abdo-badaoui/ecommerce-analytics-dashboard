import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load Data
try:
    df = pd.read_csv('data/processed_sales.csv')
except FileNotFoundError:
    print("Error: Please run 'python src/data_pipeline.py' first to generate the dataset.")
    exit()

# Initialize App
app = dash.Dash(__name__)
app.title = "Enterprise Sales Dashboard"

# Create figures with Dark Theme
fig_trend = px.line(df.groupby('Month')['Total_Sales'].sum().reset_index(), 
                    x='Month', y='Total_Sales', 
                    title='Monthly Revenue Trend',
                    template='plotly_dark')
fig_trend.update_traces(line_color='#00ffcc', line_width=3)

fig_cat = px.bar(df.groupby('Category')['Total_Sales'].sum().reset_index(), 
                 x='Category', y='Total_Sales', 
                 title='Revenue by Category',
                 template='plotly_dark', color='Category')

# Layout Configuration
app.layout = html.Div(style={'backgroundColor': '#111111', 'color': '#ffffff', 'padding': '30px', 'fontFamily': 'Arial, sans-serif', 'minHeight': '100vh'}, children=[
    html.H1("E-Commerce Analytics Dashboard", style={'textAlign': 'center', 'marginBottom': '40px', 'letterSpacing': '2px'}),
    
    html.Div([
        html.Div([
            html.H3("Total Revenue", style={'color': '#aaaaaa'}), 
            html.H2(f"${df['Total_Sales'].sum():,.2f}", style={'fontSize': '36px', 'color': '#00ffcc'})
        ], style={'border': '1px solid #333333', 'backgroundColor': '#1a1a1a', 'padding': '20px', 'margin': '10px', 'borderRadius': '10px', 'width': '40%', 'display': 'inline-block', 'textAlign': 'center', 'boxShadow': '0 4px 8px 0 rgba(0,0,0,0.5)'}),
        
        html.Div([
            html.H3("Total Completed Orders", style={'color': '#aaaaaa'}), 
            html.H2(f"{df['OrderID'].nunique():,}", style={'fontSize': '36px', 'color': '#ff00cc'})
        ], style={'border': '1px solid #333333', 'backgroundColor': '#1a1a1a', 'padding': '20px', 'margin': '10px', 'borderRadius': '10px', 'width': '40%', 'display': 'inline-block', 'textAlign': 'center', 'boxShadow': '0 4px 8px 0 rgba(0,0,0,0.5)'})
    ], style={'textAlign': 'center', 'marginBottom': '40px'}),
    
    html.Div([
        dcc.Graph(figure=fig_trend, style={'width': '48%', 'display': 'inline-block', 'verticalAlign': 'top'}),
        dcc.Graph(figure=fig_cat, style={'width': '48%', 'display': 'inline-block', 'verticalAlign': 'top', 'marginLeft': '2%'})
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
