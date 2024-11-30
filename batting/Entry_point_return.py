import pandas as pd
import numpy as np

df = pd.read_csv("https://raw.githubusercontent.com/Aran203/cricanalytics/main/data/ipl-hawkeye-data.csv")


# function to return entry point of the batsman
def get_entry_point(over_entry):
    if over_entry <= 6.0:
        return 'powerplay'
    elif over_entry > 6.0 and over_entry <= 11.0:
        return 'mid1'
    elif over_entry > 11.0 and over_entry <= 16.0:
        return 'mid2'
    else:
        return 'death'
def get_agg_stats_by_entry_point(df, player, seasons = None, venues = None):
    df['overs'] = np.ceil(df['ball_id'])
    #filter records for the required player, season and venue
    df = df[(df['bat'] == player)]
    if seasons:
        df = df.loc[(df['season'].isin(seasons))]
    if venues:
        df = df.loc[df['ground'].isin(venues)]
    #initialize the new columns
    df['total_batsman_score'] = None
    df['entry'] = None
    df['innings_start'] = None
    #get unique matches for the player
    matches = df['p_match'].unique()
    for i in range(len(matches)):
        #get the entry over
        over_entry = df[(df['cur_bat_bf'] == 1) & (df['p_match'] == matches[i])]['overs']
        #convert to list
        lst = over_entry.to_list()
        #convert to corresponding category
        entry_point = get_entry_point(lst[0])
        #assign the value to the unique match records
        df.loc[df['p_match'] == matches[i], 'entry'] = entry_point
        #calculate total runs for every innings played
        tot_runs = df[df['p_match'] == matches[i]]['batruns'].sum()
        #assign total runs
        df.loc[df['p_match'] == matches[i], 'total_batsman_score'] = tot_runs
        #check for innings start
        df.loc[(df['p_match'] == matches[i]), 'innings_start'] = 0
        df.loc[(df['cur_bat_bf'] == 1) & (df['p_match'] == matches[i]), 'innings_start'] = 1
    #group by entry point for aggregate stats
    agg_stats = df.groupby('entry').agg(innings_played = pd.NamedAgg(column='innings_start', aggfunc='sum'),total_runs = pd.NamedAgg(column='batruns', aggfunc='sum'), balls_faced = pd.NamedAgg(column='bat', aggfunc='count'),highest_score = pd.NamedAgg(column='total_batsman_score', aggfunc='max'), lowest_score = pd.NamedAgg(column='total_batsman_score', aggfunc='min'), dismissals = pd.NamedAgg(column='out', aggfunc='sum'))
    #batting average column
    agg_stats['batting_avg'] = agg_stats['total_runs']/agg_stats['dismissals']
    #strike rate column
    agg_stats['strike_rate'] = agg_stats['total_runs']/agg_stats['balls_faced']*100
    #roundinf the values to 2 decimal points
    agg_stats['strike_rate'] = agg_stats['strike_rate'].round(2)
    return agg_stats
print(get_agg_stats_by_entry_point(df,'Virat Kohli',[2024]))