import pandas as pd

# Read the input file and filter records for 10/08/2016
df = pd.read_csv('input_file.tsv', delimiter='\t')
df['PLAY_TS'] = pd.to_datetime(df['PLAY_TS'], format='%d/%m/%Y %H:%M:%S')
df_filtered = df[df['PLAY_TS'].dt.strftime('%d/%m/%Y') == '10/08/2016']

# Group by CLIENT_ID and calculate the number of distinct songs
distinct_songs = df_filtered.groupby('CLIENT_ID')['SONG_ID'].nunique()

# Count the frequency of distinct play counts
result = distinct_songs.value_counts().reset_index()
result.columns = ['DISTINCT_PLAY_COUNT', 'CLIENT_COUNT']

# Sort the result by DISTINCT_PLAY_COUNT for clarity
result = result.sort_values(by='DISTINCT_PLAY_COUNT')

# Output the result
result.to_csv('output_file.csv', index=False)
print(result)
