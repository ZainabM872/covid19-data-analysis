# COVID-19 Data Visualization

This repository contains Python scripts for visualizing COVID-19 data using Matplotlib and Pandas. The analysis focuses on confirmed COVID-19 cases globally, with a particular emphasis on Canada.

## Table of Contents

- [Introduction](#introduction)
- [Data Source](#data-source)
- [Installation](#installation)
- [Usage](#usage)
- [Visualizations](#visualizations)

## Introduction
This project aims to analyze and visualize COVID-19 confirmed cases over time. The visualizations aim to provide insights into trends and patterns in the data, helping to understand the impact of the pandemic across different regions. The analysis focuses on the cumulative confirmed cases and daily new cases across different countries.

## Data Source
The COVID-19 data used in this analysis is sourced from the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University. The dataset provides global confirmed COVID-19 cases recorded over time, allowing for in-depth analysis and visualization.
- Data Link: [CSSEGISandData GitHub repository](https://github.com/CSSEGISandData/COVID-19)
- Data Format: The dataset is in CSV format, containing columns for the province/state, country/region, latitude, longitude, and daily confirmed cases for various dates.

## Installation
To run this project, ensure you have Python installed on your system. You will also need to install the following packages:

```bash
pip install pandas matplotlib
```

## Usage
To run the analysis and visualize COVID-19 data, follow these steps:

1. **Clone the repository** to your local machine using the following command:
   ```bash
    git clone https://github.com/ZainabM872/covid19-data-analysis.git
2. **Navigate** to the cloned directory:
    ```bash
    cd covid19-data-analysis
3. **Run the Python script** that contains the data analysis and visualizations. Ensure you have Python installed along with the necessary libraries:
    ```bash
    python covid_analysis.py

## Visualizations
### 1. Distribution of Total Confirmed COVID-19 Cases (Pie Chart)
![piechart](https://github.com/user-attachments/assets/b67c9e43-7bde-48db-a992-044f1a4d8b02)
- This pie chart illustrates the proportion of total confirmed cases among selected countries, providing a clear visual representation of the distribution of cases across different nations.
  
### 2. Cumulative COVID-19 Cases in Selected Countries (Multi-line Plot)
![covid in countries](https://github.com/user-attachments/assets/c09f3cd9-4eb8-4d10-a932-b54365c08ed8)
- This visualization displays the cumulative number of confirmed COVID-19 cases over time for selected countries, allowing users to observe trends and spikes in cases.
  
### 3. Cumulative COVID-19 Cases in Canada (Line Graph)
![Cumulative Covid Cases in Canada](https://github.com/user-attachments/assets/00bf7e15-3093-4ef1-bdd7-9ed8cbfc1c7c)
- This line plot shows the change in the number of cases from January 2020 to May 2023 in Canada. It helps in understanding the daily impact of COVID-19 and identifying peaks in new infections.

### 4. Daily New COVID-19 Cases in Canada (Line Graph)
![Daily New COVID-19 Cases in Canada](https://github.com/user-attachments/assets/11e39dc7-bb47-4d46-a608-153a156cd3e6)

- This line graph shows the daily new confirmed COVID-19 cases in Canada. The x-axis represents the date, and the y-axis displays the number of new cases. This visualization helps identify trends and fluctuations in infection rates over time.
