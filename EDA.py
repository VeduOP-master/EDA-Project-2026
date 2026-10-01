import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_excel("IPL_matches.xlsx")

# Identify and print ONLY columns that have missing data
missing_data = df.isnull().sum()
print("Columns with missing values:")
print(missing_data[missing_data > 0])

# # Drop 'dl_applied' and 'id' (since ID is just a row number) before running describe
# columns_to_exclude = ['id', 'dl_applied', 'season', 'city', 'date', 'venue', 'team1', 'team2', 'toss_winner', 'toss_decision', 'winner', 'player_of_match']
# print("\nDescriptive Statistics (Numerical):")
# print(df.drop(columns=columns_to_exclude, errors='ignore').describe().round(2))

# 1. True numerical margins (filtering out chasing/defending zeros)
batting_first = df[df['win_by_runs'] > 0]['win_by_runs']
chasing = df[df['win_by_wickets'] > 0]['win_by_wickets']

print("=== NUMERICAL MARGINS (CONDITIONAL) ===")
print("Defending Margins (Win by Runs - 287 matches):")
print(batting_first.describe().round(2))

print("\nChasing Margins (Win by Wickets - 339 matches):")
print(chasing.describe().round(2))

#2. Categorical distributions (percentages and counts)
print("\n=== CATEGORICAL DISTRIBUTIONS ===")
print("Match Results:")
print(df['result'].value_counts())
print("\nToss Decisions (%):")
print((df['toss_decision'].value_counts(normalize=True) * 100).round(1))

print("\nDuckworth-Lewis Adjustments:")
print(df['dl_applied'].value_counts().rename(index={0: 'Normal', 1: 'D/L Applied'}))

# 3. Modal summaries
print("\n=== MODAL VALUES ===")
print(f"Most Frequent Venue: {df['venue'].mode()[0]} ({df['venue'].value_counts().iloc[0]} matches)")
print(f"Most Frequent Winner: {df['winner'].mode()[0]} ({df['winner'].value_counts().iloc[0]} wins)")
print(f"Most Frequent MVP:    {df['player_of_match'].mode()[0]} ({df['player_of_match'].value_counts().iloc[0]} awards)")

# # Generate descriptive statistics for categorical columns (Step 6)
# print("\nCategorical Statistics:")
# print(df.describe(include=['object', 'str']))

# Group by winner to see which team has the most overall victories
# team_wins = df.groupby('winner')['id'].count().sort_values(ascending=False)
# print("Top 10 Teams by Total Wins:")
# print(team_wins.head(10))

# --- STEPS 7 & 11: Univariate Visualization ---
# Plot a count of matches played per season
plt.figure(figsize=(10, 5))
sns.countplot(x='season', data=df, palette='Blues_d', hue='season', legend=False)
plt.title('Number of Matches Played per IPL Season')
plt.xlabel('Season')
plt.ylabel('Number of Matches')
# plt.show() 
 
plt.savefig('matches_per_season.png', bbox_inches='tight')
print("\nVisualization saved as 'matches_per_season.png'")

# --- STEPS 8 & 11: Bivariate Analysis ---
# Create the True/False column first
df['toss_match_winner'] = df['toss_winner'] == df['winner']

# Count the occurrences of True and False
toss_counts = df['toss_match_winner'].value_counts()

plt.figure(figsize=(7, 7))

plt.pie(toss_counts.values, 
        labels=['Toss Winner Won Match', 'Toss Winner Lost Match'], # CORRECT ORDER
        autopct='%1.1f%%', 
        startangle=90, 
        colors=['#66b3ff', '#ff9999'], # Swapped colors to match
        explode=(0.05, 0)) # This slightly separates the slices for a cleaner look

plt.title('Impact of Winning the Toss on Match Result')
plt.savefig('toss_impact_pie.png', bbox_inches='tight')
print("\nToss impact pie chart saved as 'toss_impact_pie.png'")

# Top 10 Players with most 'Player of the Match' awards
plt.figure(figsize=(12, 6))
top_players = df['player_of_match'].value_counts().head(10)
sns.barplot(x=top_players.values, y=top_players.index, palette='magma', hue=top_players.index, legend=False)
plt.title('Top 10 Player of the Match Award Winners')
plt.xlabel('Number of Awards')
plt.ylabel('Player Name')
plt.savefig('top_players.png', bbox_inches='tight')
print("Bivariate visualization saved as 'top_players.png'")

# Top 10 Teams with most wins 
team_wins = df['winner'].value_counts()

plt.figure(figsize=(12, 8))
sns.barplot(x=team_wins.values, y=team_wins.index, palette='viridis', hue=team_wins.index, legend=False)
plt.title('Total IPL Matches Won by Each Team (2008-2017)')
plt.xlabel('Number of Wins')
plt.ylabel('Team Name')
plt.savefig('top_teams_chart.png', bbox_inches='tight')
print("Top teams chart saved as 'top_teams_chart.png'")

# --- STEP 10: Correlation Analysis ---
# Isolate just the numerical columns to calculate correlation
numerical_data = df[['win_by_runs', 'win_by_wickets', 'dl_applied']]
correlation_matrix = numerical_data.corr()

plt.figure(figsize=(7, 5))
# annot=True puts the actual numbers inside the colored squares
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap of Match Margins')
plt.savefig('correlation_heatmap.png', bbox_inches='tight')
print("Correlation heatmap saved as 'correlation_heatmap.png'")