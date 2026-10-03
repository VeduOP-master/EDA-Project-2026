# IPL Matches Exploratory Data Analysis (EDA)

An exploratory data analysis of Indian Premier League (IPL) matches. This project explores match trends, team and player performances, victory margins, and the strategic impact of toss decisions using Python, Pandas, Matplotlib, and Seaborn.

---

## Features & Analyses Performed

* **Missing Value Diagnostics:** Identifies columns with missing values across the dataset.
* **Victory Margin Distribution:** Evaluates conditional summary statistics for defending margins (`win_by_runs`) and chasing margins (`win_by_wickets`).
* **Categorical Summaries:** Calculates distribution metrics for toss decisions, Duckworth-Lewis (`dl_applied`) match adjustments, match results, most frequent venues, and MVPs.
* **Matches per Season:** Visualizes the distribution of total matches hosted across seasons.
* **Toss Impact Analysis:** Evaluates whether winning the toss translates into match victories.
* **Player of the Match Leaders:** Ranks and plots the top 10 players by MVP awards won.
* **All-Time Team Wins:** Visualizes total match wins achieved by each IPL franchise.
* **Margin Correlation Heatmap:** Analyzes numerical relationships across win margins and D/L interruptions.

---

## Repository Structure

```text
├── EDA.py               # Main data analysis and visualization script
├── IPL_matches.xlsx     # IPL dataset (Excel format)
├── requirements.txt     # Python library dependencies
└── README.md            # Project documentation
