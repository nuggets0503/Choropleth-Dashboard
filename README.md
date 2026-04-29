# 🙍🏻‍♂️📖🙍🏻‍♀️ Global Children Illiteracy Dashboard

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://choropleth-dashboard-jcqbnpf6cvytdvh5gbvuwk.streamlit.app/)

## 📌 Executive Summary
The **Global Children Illiteracy Dashboard** is an interactive web application built with Streamlit and Folium. It provides a geospatial analysis of estimated childhood illiteracy rates (in millions) across the globe. By allowing users to filter data by year, the dashboard highlights critical educational metrics and trends over time, serving as an exploratory tool for understanding global learning deficits.

**Author:** Paolo G. Hilado, MSc.
*Notice: This project is deployed for training and demonstration purposes.*

---

## 🚀 Live Demo
Access the deployed application here: **[Global Children Illiteracy Dashboard](https://choropleth-dashboard-jcqbnpf6cvytdvh5gbvuwk.streamlit.app/)**

---

## ✨ Key Features
* **Dynamic Time Filtering:** An interactive slider allows users to explore illiteracy data across different years.
* **Top-Level KPIs:** Instantly calculates and displays the global Average, Highest, and Lowest estimated millions of illiterate children for the selected year.
* **Interactive Choropleth Map:** Integrates a Folium-based geospatial map with `YlGnBu` color scaling to visually represent illiteracy density by country.
* **Hover Tooltips:** Utilizes GeoJson tooltips so users can hover over specific nations to see exact country names and figures.

---

## 🛠️ Tech Stack
This project relies on the following Python libraries:
* **[Streamlit](https://streamlit.io/):** For the front-end web framework and UI components.
* **[Pandas](https://pandas.pydata.org/):** For data manipulation and metric calculations.
* **[Folium](https://python-visualization.github.io/folium/):** For rendering the interactive Leaflet map.
* **[Streamlit-Folium](https://folium.streamlit.app/):** To bridge the Folium map into the Streamlit UI.
* **[Requests](https://requests.readthedocs.io/):** To fetch the base world-countries GeoJSON data.

---

## 📊 Data Sources
The data utilized in this dashboard is aggregated from several reputable organizations:
* UNESCO Institute for Statistics
* World Bank Learning Poverty Index
* UNICEF MICS Surveys
* Our World in Data
* Pratham ASER Centre & RTI International

**Original Dataset:** [Global Child Illiteracy Dataset (Kaggle)](https://www.kaggle.com/datasets/zkskhurram/global-child-illiteracy-dataset-children-10-yrs)

---

## 💻 Local Installation & Usage

To run this dashboard on your local machine, follow these steps:

**1. Clone the repository**
```bash
git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/yourusername/your-repo-name.git)
cd your-repo-name
