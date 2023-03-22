"""
This script filters and rank the esummary data based on the presence of some assembly parameters,
 i.e assembly accession id, assembly gi and completeness.
 Its prints the rank greater than zero for score, assemblygi, organism and updatedate columns
"""

import pandas as pd
from pathlib import Path

# place the path to your base directory
base_dir = Path(r"\path\to\base\directory")
data_dir = base_dir / "data"

df = pd.read_csv(data_dir / 'esummary.csv')

# Create score column
df['score'] = 0

# filtering and ranking based on presence of assembly accession no., gene id and completeness
# if the row have the required variable, the score column would increment accordingly
df.loc[df['assemblyacc'].notnull(), 'score'] += 3
df.loc[df['assemblygi'].notnull(), 'score'] += 2
df.loc[df['completeness'].notnull(), 'score'] += 1

# Sort by score
df = df.sort_values(by='score', ascending=False)

# Filter rows with score > 0
filtered_df = df[(df['score'] >= 0)]
print(filtered_df[['score', 'assemblygi', 'organism', 'updatedate']])