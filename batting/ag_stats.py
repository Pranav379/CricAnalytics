



def player_agg_stats(df, playername):

    #filter the data to include only records for the specified player
    playerdata = df[df['bat'] == playername]
    
    #calculate total runs scored
    sum_runs = playerdata['batruns'].sum()
    
    #count total dismissals
    total_dismissals = playerdata['out'].sum() 
    
    #calculate dot % 
    total_balls_faced = playerdata.shape[0]
    dot_balls = playerdata[playerdata['batruns'] == 0].shape[0]
    dot_percentage = (dot_balls / total_balls_faced) * 100
    
    #calculate boundary % (from 4s and 6s)
    boundaries = playerdata[playerdata['batruns'].isin([4, 6])].shape[0]
    boundary_percentage = (boundaries / total_balls_faced) * 100
    
    #gets the stats 
    stats = {
        "Runs": sum_runs,
        "Dismissals": total_dismissals,
        "Dot %": dot_percentage,
        "Boundary %": boundary_percentage
    }
    
    return stats