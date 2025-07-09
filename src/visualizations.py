import pandas as pd
import matplotlib.pyplot as plt

def plot_team_summary(df, team):
    m = df[(df.home_team == team) | (df.away_team == team)]
    wins = ((m.home_team == team) & (m.home_score > m.away_score)) | \
           ((m.away_team == team) & (m.away_score > m.home_score))
    draws = m.home_score == m.away_score
    losses = (~wins) & (~draws)
    
    counts = [wins.sum(), draws.sum(), losses.sum()]
    plt.figure(figsize=(6,4))
    plt.bar(['Wins','Draws','Losses'], counts)
    plt.title(f'{team}: World Cup outcomes (1930–2022)')
    plt.show()

