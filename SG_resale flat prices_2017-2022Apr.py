import pandas as pd
import plotly
import plotly.express as px
import plotly.io as pio

# Dataset taken from https://data.gov.sg/dataset/resale-flat-prices

df = pd.read_csv("resale-flat-prices-based-on-registration-date-from-jan-2017-onwards.csv")
df = df[df['town']=='PASIR RIS']
# Dataframe for average resale_price by flat_type and storey_range 
df_ft_sr = df.groupby(['flat_type','storey_range'],as_index=False)[['resale_price']].mean()
# Dataframe for average resale_price by flat_type and month (historical cost)
# df_m_ft = df[df['flat_type']=='5 ROOM']
df_m_ft = df.groupby(['month','flat_type'],as_index=False)[['resale_price']].mean()

#----------------------------------------------------------------------------------------------
# px.bar method for df_ft_sr (Dataframe with resale price, flat type and storey range) 
bar_chart_ft_sr = px.bar(
    data_frame=df_ft_sr,
    x="flat_type",
    y="resale_price",
    color="storey_range",               # differentiate color of marks
    text="flat_type",
    orientation="v",              # 'v','h': orientation of the marks
    barmode='group',           # 'overlay','group','relative'
    labels={"flat_type":"Unit Type",
    "resale_price":"Resale Price",
    "storey_range":"Storey Range"},           # map the labels of the figure
    title='Average resale prices of flat types and storey range in Pasir Ris from 2017 to April 2022', # figure title
    template='plotly_white',            # 'ggplot2', 'seaborn', 'simple_white', 'plotly',
                                  # 'plotly_white', 'plotly_dark', 'presentation',
                                  # 'xgridoff', 'ygridoff', 'gridon', 'none'
)

#----------------------------------------------------------------------------------------------
# px.bar method for df_m_ft (Dataframe with resale price, month and flat type)
scatter_chart_m_ft = px.scatter(
    data_frame=df_m_ft,
    x="month",
    y="resale_price",
    color="flat_type",               # differentiate color of marks
    # trendline='ewm',
    labels={"month":"Month",
    "resale_price":"Resale Price",
    "flat_type":"Flat Type"},           # map the labels of the figure
    title='Average resale prices of flat types in Pasir Ris from 2017 to April 2022', # figure title
    template='ggplot2',            # 'ggplot2', 'seaborn', 'simple_white', 'plotly',
                                  # 'plotly_white', 'plotly_dark', 'presentation',
                                  # 'xgridoff', 'ygridoff', 'gridon', 'none'
)

# Plotly common renderers - 'browser','firefox','chrome','jupyterlab','png','jpeg','jpg','pdf'
pio.renderers.default="browser"
pio.show(bar_chart_ft_sr)
pio.show(scatter_chart_m_ft)