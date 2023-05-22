import player
from player import Positions
from player import Player
import random
import yaml

def check_player_amount(players):
    # Returns boolean if there are enough players
    teams = len(players) // 6
    if len(players) >= 12:
        positions = [player.position for player in players]
        if teams > positions.count(Positions.SETTER):
            print("Not enough setters")
            return False
        elif teams > (positions.count(Positions.MIDDLE) / 2):
            print("Not enough middles")
            return False
        elif teams > (positions.count(Positions.OUTSIDE) / 2):
            print("Not enough outsides")
            return False
        elif teams > positions.count(Positions.OPPOSITE):
            print("Not enough opposites")
            return False
        else:
            return True
    else:
        print("Not enough people to have at least 2 teams")
        return False

def get_players_of_position(players, position):
    return [player for player in players if player.position == position]

def get_team_level(team):
    return round(sum([player.level for player in team]) / len(team))

def create_random_team(players):
    # Returns a list of teams
    if check_player_amount(players):
        teams = list()

        liberos = [player for player in players if player.position == Positions.LIBERO]
        random.shuffle(liberos)
        non_libs = [player for player in players if player.position not in liberos]
        random.shuffle(non_libs)

        for i in range(0, len(non_libs) // 6):
            teams.append(list())

        excess_players = len(non_libs) % 6

        for random_player in non_libs:
            # Go through random players and assign them to a team if the team needs
            # the player

            for team in teams:
                if len(team) == 6:
                    continue
                else:
                    if random_player.position == Positions.SETTER and len(get_players_of_position(team, Positions.SETTER)) < 1:
                        team.append(random_player)
                        break
                    elif random_player.position == Positions.MIDDLE and len(get_players_of_position(team, Positions.MIDDLE)) < 2:
                        team.append(random_player)
                        break
                    elif random_player.position == Positions.OUTSIDE and len(get_players_of_position(team, Positions.OUTSIDE)) < 2:
                        team.append(random_player)
                        break
                    elif random_player.position == Positions.OPPOSITE and len(get_players_of_position(team, Positions.OPPOSITE)) < 1:
                        team.append(random_player)
                        break

        for team in teams:
            for random_lib in liberos:
                random_team = random.randint(0, len(teams) - 1)
                teams[random_team].append(random_lib)

        return teams

def create_player_pool(player_pool):
    players = list()

    for player, description in player_pool.items():
        players.append(Player(player, Positions[description["position"].upper()], description["level"]))

    return players

# create players
def main():
    with open("players.yml", "r") as stream:
        try:
            players = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    
        player_pool = create_player_pool(players)
        teams = create_random_team(player_pool)

        for team in teams:
            print(
                f"Players: {[player.name for player in team]}\n"
                f"Team Level: {get_team_level(team)}"
            )


if __name__ == "__main__":
    main()