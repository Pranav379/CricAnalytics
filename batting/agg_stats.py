
def player_agg_stats(df, player_name):

    #filter the data to include only records for the specified player
    player_data = df[df['bat'] == player_name]
    
    #calculate total runs scored
    total_runs = player_data['batruns'].sum()
    
    #count total dismissals
    total_dismissals = player_data['out'].sum()  #'out' is 1 if dismissed, 0 otherwise
    
    # Calculate Dot % (percentage of dot balls faced)
    #do not include balls with extras from balls faced
    valid_balls = player_data[(player_data['byes'] == 0) & 
                              (player_data['legbyes'] == 0) & 
                              (player_data['noballs'] == 0) & 
                              (player_data['wides'] == 0)]
    total_balls_faced = valid_balls.shape[0]
    
    #count dot balls only from valid balls (excluding extras)
    dot_balls = valid_balls[valid_balls['batruns'] == 0].shape[0]
    dot_percentage = (dot_balls / total_balls_faced) * 100 if total_balls_faced > 0 else 0
    
    #calculate Boundary % (percentage of boundaries, 4s or 6s)
    boundaries = valid_balls[valid_balls['batruns'].isin([4, 6])].shape[0]
    boundary_percentage = (boundaries / total_balls_faced) * 100 if total_balls_faced > 0 else 0
    
    #store results in a dictionary
    stats = {
        "Runs": total_runs,
        "Dismissals": total_dismissals,
        "Dot %": dot_percentage,
        "Boundary %": boundary_percentage
    }
    
    return stats

