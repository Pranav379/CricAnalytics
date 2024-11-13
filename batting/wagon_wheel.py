def getZones(playername, df, seasons=None, venues=None):
    print(playername)
    batter = df.loc[df['bat'] == playername]  

    if seasons:
        print(seasons)
        batter = batter[batter['season'].isin(seasons)]  
    print(venues)
    if venues:
        venue_pattern = '|'.join(venues)
        print(venue_pattern)
        batter = batter[batter['ground'].str.contains(venue_pattern, case=False, na=False)]
    
    print(batter) 
    zones = [0, 0, 0, 0, 0, 0, 0, 0]

    for row in batter.itertuples(index=True, name="Row"):
        zones[int(row.wagonZone) - 1] += 1

    return zones