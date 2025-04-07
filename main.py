def main():
  team_data = []

  # Read pitching data
  with open("MLB_Pitching.csv", 'r') as pitching:
   for line in pitching:
    info = line.split(",")
    name = info[0]
    runs_allowed = info[3]
    wins = info[4]
    losses = info[5]
    era = info[7]

  team_data.append([name, "", runs_allowed, wins, losses, era])

    # Read hitting data
  with open("MLB_Hitting.csv", 'r') as hitting:
   teamCount = 0
   for line in hitting:
    info = line.split(",")
    runs_scored = info[3]
    print(runs_scored)
    team_data[teamCount][1] = runs_scored
    print(team_data[teamCount])

    teamCount += 1

    # Write output to file
  with open("mlb_output.csv", 'w') as outFile:
    for team in team_data:
      output = ",".join(team) + "\n"
      outFile.write(output)

if __name__ == '__main__':
    main()