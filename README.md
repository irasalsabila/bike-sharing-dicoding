# Bike Sharing Dashboard

[Bike Sharing Dashboard Streamlit App](https://bike-sharing-irasalsabila.streamlit.app/)

## Table of Contents
- [Bike Sharing Dashboard](#bike-sharing-dashboard)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Project Structure](#project-structure)
  - [Installation](#installation)
  - [Usage](#usage)

## Overview
This project is a data analysis and visualization project focused on bike sharing public data. It includes code for data wrangling, exploratory data analysis (EDA), and a Streamlit dashboard for interactive data exploration. This project aims to analyze data on the Bike Sharing Public Dataset.

## Project Structure
- `dataset/`: Directory containing the raw CSV data files.
- `notebook.ipynb`: This file is used to perform data analysis.
- `README.md`: This documentation file.
- `requirements.txt`: This is the requirements library to install file.
- `bike_dashboard.py`: This is the dashboard file.

## Installation
1. Clone this repository to your local machine:
```
git clone https://github.com/irasalsabila/bike-sharing-dicoding
```
2. Go to the project directory
```
cd bike-sharing-dicoding
```
3. Install the required Python packages by running:
```
pip install -r requirements.txt
```

## Usage
1. **Data Wrangling**: Data wrangling scripts are available in the `notebook.ipynb` file to prepare and clean the data.

2. **Exploratory Data Analysis (EDA)**: Explore and analyze the data using the provided Python scripts. EDA insights can guide your understanding of e-commerce public data patterns.

3. **Visualization**: Run the Streamlit dashboard for interactive data exploration:

```
streamlit run bike_dashboard.py
```
Access the dashboard in your web browser at `http://localhost:8501`.