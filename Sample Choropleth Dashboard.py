import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import st_folium
from folium.features import GeoJsonTooltip
import requests

st.set_page_config(layout="wide")


# Load REAL dataset
df = pd.read_csv("child_illiteracy_by_country.csv")


# Title
st.markdown(
    f"<p style='font-size:65px; color:#FCC761; font-weight:bold;'>"
    f"Global Children Illiteracy Dashboard 🙍🏻‍♂️📖🙍🏻‍♀️"
    f"</p>",
    unsafe_allow_html=True
    )

st.markdown(
    f"<p style='font-size:26px; color:##EDE5E1'>"
    f"Paolo G. Hilado MSc. | Notice: This is only for Training Purposes."
    f"</p>",
    unsafe_allow_html=True
    )

year = st.slider("Select Year", int(df.year.min()), int(df.year.max()), 2010)
filtered_df = df[df["year"] == year]


# KPIs
avg = filtered_df["est_illiterate_children_millions"].mean()
hi = filtered_df["est_illiterate_children_millions"].max()
lo = filtered_df["est_illiterate_children_millions"].min()

col1, col2, col3 = st.columns(3)

col1.markdown("##### Avg Children illiteracy (in millions)")
col1.markdown(
f"<p style='font-size:55px; color:#E8F1F6; font-weight:bold;'>"
f"{avg:.4f}"
f"</p>",
unsafe_allow_html=True
)

col2.markdown("##### Highest Children illiteracy (in millions)")
col2.markdown(
f"<p style='font-size:55px; color:#0C60B7; font-weight:bold;'>"
f"{hi:.4f}"
f"</p>",
unsafe_allow_html=True
)

col3.markdown("##### Lowest Children illiteracy (in millions)")
col3.markdown(
f"<p style='font-size:55px; color:#FEECC0; font-weight:bold;'>"
f"{lo:.4f}"
f"</p>",
unsafe_allow_html=True
)

# Choropleth Map (Folium)
st.markdown(
    f"<p style='font-size:25px; color:#FCC761; font-weight:bold;'>"
    f"Children Illiteracy at a Glance 👀"
    f"</p>",
    unsafe_allow_html=True
    )

geo_url = "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/world-countries.json"
geo_data = requests.get(geo_url).json()

# create lookup dictionary
value_dict = dict(zip(
    filtered_df["iso3_code"],
    filtered_df["est_illiterate_children_millions"]
))

# inject into geojson
for feature in geo_data["features"]:
    country_id = feature["id"]
    feature["properties"]["est_illiterate_children_millions"] = value_dict.get(country_id, None)

# map setup
m = folium.Map(
    location=[20, 0],
    zoom_start=2.5,
    tiles="cartodb positron",
    max_bounds=True,
    no_wrap=True
)

# choropleth layer
folium.Choropleth(
    geo_data=geo_data,
    data=filtered_df,
    columns=["iso3_code", "est_illiterate_children_millions"],
    key_on="feature.id",
    fill_color="YlGnBu",
    fill_opacity=0.5,
    line_opacity=0.3,
    nan_fill_color="#C9BEB1",
    legend_name="Children Illiteracy (Millions)",
).add_to(m)

# hover tooltip layer
folium.GeoJson(
    geo_data,
    style_function=lambda x: {
        "fillColor": "transparent",
        "color": "transparent",
        "weight": 0,
    },
    tooltip=folium.features.GeoJsonTooltip(
        fields=["name", "est_illiterate_children_millions"],
        aliases=["Country:", "Children Illiteracy (Millions):"],
        localize=True,
        sticky=True
    )
).add_to(m)

st_folium(m, height=500, use_container_width=True)

st.markdown("""
    <div style="font-size:15px; color:#EDE5E1;">
    <b>Sources: UNESCO Institute for Statistics, World Bank Learning Poverty Index, UNICEF MICS Surveys, Our World in Data, Pratham ASER Centre, and RTI International | Data retrieved from: </b>
    <a href="https://www.kaggle.com/datasets/zkskhurram/global-child-illiteracy-dataset-children-10-yrs" target="_blank"> Click Here for Link </a>
    </div>
    """, unsafe_allow_html=True)
