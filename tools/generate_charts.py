# tools/generate_charts.py
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# === CONFIG (EDIT WITH REAL DATA / OR LOAD FROM file/db) ===
years = [2020, 2021, 2022, 2023, 2024]
projects = [2, 5, 8, 12, 20]
techs = [3, 6, 10, 15, 22]


out_dir = 'assets/charts'
os.makedirs(out_dir, exist_ok=True)


# === DARK THEME SETTINGS ===
plt.style.use('dark_background')
NEON = '#7ef9ff'
ACCENT = '#9b59ff'
FONT = {'family':'sans-serif','size':12}


# Projects line chart
fig, ax = plt.subplots(figsize=(10,3))
ax.plot(years, projects, marker='o', linewidth=3, color=NEON)
ax.fill_between(years, projects, alpha=0.06, color=NEON)
ax.set_title('Projects Completed Over Years', color='white')
ax.set_xlabel('Year', color='white')
ax.set_ylabel('Projects', color='white')
ax.set_xticks(years)
ax.grid(alpha=0.12)
fig.tight_layout()
fig.savefig(os.path.join(out_dir,'projects-growth.png'), dpi=150, facecolor='#041020')
plt.close(fig)


# Technologies bar chart
fig, ax = plt.subplots(figsize=(10,3))
bars = ax.bar(years, techs, color=[NEON]*len(years))
ax.set_title('Technologies Learned Over Years', color='white')
ax.set_xlabel('Year', color='white')
ax.set_ylabel('Technologies Learned', color='white')
ax.set_xticks(years)
ax.grid(axis='y', alpha=0.12)
fig.tight_layout()
fig.savefig(os.path.join(out_dir,'tech-learned.png'), dpi=150, facecolor='#041020')
plt.close(fig)


print('Charts generated ->', out_dir)