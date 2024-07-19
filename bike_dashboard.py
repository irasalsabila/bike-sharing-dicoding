# ===============================================================
#           CREATE DASHBOARD BIKE SHARING USING STREAMLIT       =
#           ---------------------------------------------       =
# Nama          : Salsabila Zahirah / Ira Salsabila             =
# Email         : irasalsabila@gmail.com                        =
# Id Dicoding   : dicoding.com/users/irasalsabila/              =
# ===============================================================

# Import Library
import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import calendar

import warnings

# ==============================
# LOAD DATA
# ==============================


@st.cache_data
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Dropdown to select the dataset
selected_dataset = st.selectbox("Select Dataset", ["Daily", "Hourly"])

if selected_dataset == "Daily":
    file_path = "dataset/day.csv"
elif selected_dataset == "Hourly":
    file_path = "dataset/hour.csv"

data = load_data(file_path)



# ==============================
# TITLE DASHBOARD
# ==============================
# Set page title
st.title("Bike Sharing Dashboard")

# ==============================
# SIDEBAR
# ==============================
st.sidebar.title("Information:")
st.sidebar.markdown("**• Nama: Ira Salsabila**")
st.sidebar.markdown(
    "**• Email: [irasalsabila@gmail.com](irasalsabila@gmail.com)**")
st.sidebar.markdown(
    "**• Dicoding: [irasalsabila](https://www.dicoding.com/users/irasalsabila/)**")
st.sidebar.markdown(
    "**• LinkedIn: [Salsabila Zahirah](https://www.linkedin.com/in/irasalsabila/)**")


st.sidebar.title("Dataset Bike Share")
# Show the dataset
if st.sidebar.checkbox("Show Dataset"):
    st.subheader("Raw Data")
    st.write(data)

# Display summary statistics
if st.sidebar.checkbox("Show Summary Statistics"):
    st.subheader("Summary Statistics")
    st.write(data.describe())

# ==============================
# VISUALIZATION
# ==============================

# Custom function to assign colors
def get_color(val, max_val, min_val, color_scale):
    # Normalize the value
    norm_val = (val - min_val) / (max_val - min_val)
    # Calculate the index in the color scale
    color_idx = int(norm_val * (len(color_scale) - 1))
    return color_scale[color_idx]

# Define a blue color scale in hex
blue_color_scale = [
    "#EFF3FF",  # lightest blue
    "#C6DBEF",
    "#9ECAE1",
    "#6BAED6",
    "#4292C6",
    "#2171B5",
    "#08519C"   # darkest blue
]

# create a layout with two columns
col1, col2 = st.columns(2)

with col1:
    # Season-wise bike share count

    season_mapping = {1: "spring", 2: "summer", 3: "fall", 4: "winter"}
    data["season_label"] = data["season"].map(season_mapping)

    season_count = data.groupby("season_label")["cnt"].sum().reset_index()
    max_cnt = season_count["cnt"].max()
    min_cnt = season_count["cnt"].min()

    season_count["color"] = season_count["cnt"].apply(get_color, 
                                                      args=(max_cnt, min_cnt, blue_color_scale))


    fig_season_count = px.bar(season_count, x="season_label",
                              y="cnt", title="Season-wise Bike Share Count")
    
    fig_season_count.update_traces(marker_color=season_count["color"])

    fig_season_count.update_xaxes(title="Season")
    fig_season_count.update_yaxes(title="Rental bikes")
    st.plotly_chart(fig_season_count, use_container_width=True,
                    height=400, width=600)

with col2:
    # Weather situation-wise bike share count

    weather_mapping = {1: "Cloudy", 2: "Foggy", 3: "Snowy", 4: "Rainy"}
    data['weather_description'] = data['weathersit'].map(weather_mapping)

    weather_count = data.groupby("weather_description")["cnt"].sum().reset_index()
    max_cnt = weather_count["cnt"].max()
    min_cnt = weather_count["cnt"].min()

    weather_count["color"] = weather_count["cnt"].apply(get_color, 
                                                        args=(max_cnt, min_cnt, blue_color_scale))

    fig_weather_count = px.bar(weather_count, x="weather_description",
                            y="cnt", title="Weather Situation-wise Bike Share Count")
    
    fig_weather_count.update_traces(marker_color=weather_count["color"])

    fig_weather_count.update_xaxes(title="Weather Situation")
    fig_weather_count.update_yaxes(title="Rental bikes")
    st.plotly_chart(fig_weather_count, use_container_width=True, height=400, width=800)


# Define colors for each season
season_colors = {
    "spring": "#636EFA",
    "summer": "#EF553B",
    "fall": "#00CC96",
    "winter": "#AB63FA",
}

# Streamlit app
# st.title("User Data by Season")
# User selection for type of users
user_types = ["casual", "registered"]
selected_users = st.multiselect("Select user types to display", user_types, default=user_types)

# User selection for season
seasons = list(season_mapping.values())
selected_season = st.selectbox("Select season", seasons)

# Filter data based on selected user types
filtered_data = data[['season_label', 'casual', 'registered']]
filtered_data = filtered_data.melt(id_vars='season_label', value_vars=selected_users, var_name='user_type', value_name='count')

# Filter data based on selected season
selected_data = filtered_data[filtered_data['season_label'] == selected_season]

# Create scatter plot using Plotly Express
fig = px.scatter(
    selected_data,
    x='user_type',
    y='count',
    color='user_type',
    title=f"Number of Users in {selected_season.capitalize()}",
    color_discrete_map={user_types[0]: '#636EFA', user_types[1]: '#EF553B'}
)

# Show plot in Streamlit
# Update the legend labels to show weekday names instead of RGB codes
for i, day_name in enumerate(selected_season):
    fig.data[i].name = day_name

st.plotly_chart(fig, use_container_width=True)

humidity_vs_cnt = data.groupby(["weekday", "hum", "temp", "windspeed"])["cnt"].sum().reset_index()

humidity_vs_cnt["weekday"] = humidity_vs_cnt["weekday"].apply(lambda x: calendar.day_name[x])

# Allow selection of multiple weekdays
selected_weekdays = st.multiselect("Select weekdays", list(calendar.day_name))

selected_data = humidity_vs_cnt[humidity_vs_cnt["weekday"].isin(selected_weekdays)]

selected_variable = st.selectbox("Select a variable for X-axis", ["Humidity", "Temperature", "Wind Speed"])

if selected_variable == "Humidity":
    x_data = "hum"
    x_title = "Humidity"
elif selected_variable == "Temperature":
    x_data = "temp"
    x_title = "Temperature"
elif selected_variable == "Wind Speed":
    x_data = "windspeed"
    x_title = "Wind Speed"

weekday_colors = {
    "Monday": "#636EFA",
    "Tuesday": "#EF553B",
    "Wednesday": "#00CC96",
    "Thursday": "#AB63FA",
    "Friday": "#FFA15A",
    "Saturday": "#FF6692",
    "Sunday": "#B6E880"
}

# Map weekday names to colors
selected_data['color'] = selected_data['weekday'].map(weekday_colors)

fig = px.scatter(selected_data, x=x_data, y="cnt", color='color',
                 title=f"Bike Share Count vs. {x_title} for {', '.join(selected_weekdays)}",
                 color_discrete_map={color_code: day_name for color_code, day_name in weekday_colors.items()})

# Update the legend title and axis titles
fig.update_traces(showlegend=True)
fig.update_layout(legend_title='Weekday')
fig.update_xaxes(title=x_title)
fig.update_yaxes(title="Bike Share Count")

# Update the legend labels to show weekday names instead of RGB codes
for i, day_name in enumerate(selected_weekdays):
    fig.data[i].name = day_name

st.plotly_chart(fig, use_container_width=True)
