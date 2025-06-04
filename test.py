from datetime import datetime, timedelta

def generate_match_schedule(teams, match_length=10, setup_interval=5, start_time_str="09:00"):
    """
    Generate a match queue with setup start times.

    Args:
        teams (list of str): List of team names or IDs.
        match_length (int): Match duration in minutes.
        setup_interval (int): Minutes before match starts for setup.
        start_time_str (str): Day start time (24h format, e.g., "09:00").

    Returns:
        list of dict: Each dict contains match number, teams in the match, setup start time.
    """
    start_time = datetime.strptime(start_time_str, "%H:%M")
    schedule = []
    
    # Assuming 2 teams per match, queue them in order (can be adjusted)
    match_number = 1
    for i in range(0, len(teams), 2):
        if i+1 >= len(teams):
            # Odd team out: bye or practice match
            match_teams = [teams[i], "BYE"]
        else:
            match_teams = [teams[i], teams[i+1]]
        
        match_start = start_time + timedelta(minutes=(match_number - 1) * match_length)
        setup_start = match_start - timedelta(minutes=setup_interval)

        schedule.append({
            "Match": match_number,
            "Teams": match_teams,
            "Setup Start": setup_start.strftime("%H:%M"),
            "Match Start": match_start.strftime("%H:%M"),
        })

        match_number += 1
    
    return schedule

def print_schedule_for_sheets(schedule):
    print("Match\tTeam 1\tTeam 2\tSetup Start\tMatch Start")
    for item in schedule:
        print(f"{item['Match']}\t{item['Teams'][0]}\t{item['Teams'][1]}\t{item['Setup Start']}\t{item['Match Start']}")

if __name__ == "__main__":
    # Example usage:
    teams = ["Team A", "Team B", "Team C", "Team D", "Team E", "Team F", "Team G", "Team H", "Team I"]
    schedule = generate_match_schedule(teams, match_length=10, setup_interval=5, start_time_str="09:00")
    print_schedule_for_sheets(schedule)