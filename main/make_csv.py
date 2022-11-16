import requests
import csv
import json
import sys

# specify where to find requests to avoid command-line issues
sys.path.append('../venv/Lib/site-packages/requests')


# get data from endpoint
response = requests.get(
    'https://statsapi.mlb.com/api/v1/stats?stats=season&group=pitching&playerPool=all&season=2018&teamId=144')
data = json.loads(response.text)


# get data that can be used to validate the PITCHBYPITCH table
def get_data(count):
    playerDict = data['stats'][0]['splits'][count]['player']
    statDict = data['stats'][0]['splits'][count]['stat']

    name = f"{playerDict['lastName']}, {playerDict['firstName']}"
    pitcherID = playerDict['id']

    gamesPitched = statDict['gamesPitched']
    battersFaced = statDict['battersFaced']
    strikeOuts = statDict['strikeOuts']
    pitchesThrown = statDict['numberOfPitches']
    outs = statDict['outs']

    # singles is not given but can be calculated as below
    doubles = statDict['doubles']
    triples = statDict['triples']
    homeRuns = statDict['homeRuns']
    hits = statDict['hits']
    singles = hits - homeRuns - triples - doubles

    # return dictionary of chosen values
    return {
        'PitcherName': name, 'PitcherID': pitcherID, 'GamesPitched': gamesPitched, 'BattersFaced': battersFaced,
        'StrikeOuts': strikeOuts, 'PitchesThrown': pitchesThrown, 'Outs': outs, 'Singles': singles,
        'Doubles': doubles, 'Triples': triples, 'HomeRuns': homeRuns, 'Hits': hits
    }


def write_api_csv():
    with open('csv/pitcher-data.csv', 'w', newline='') as file:
        fieldnames = [
            'PitcherName', 'PitcherID', 'GamesPitched', 'BattersFaced', 'StrikeOuts',
            'PitchesThrown', 'Outs', 'Singles', 'Doubles', 'Triples', 'HomeRuns', 'Hits'
        ]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        # Player IDs for Shane Carle, Jonny Venters, and Luke Jackson
        playerIDs = [641438, 458924, 592426]
        iteration = 0
        for x in range(len(data['stats'][0]['splits'])):
            currentID = data['stats'][0]['splits'][iteration]['player']['id']
            if currentID in playerIDs:
                writer.writerow(get_data(iteration))
            iteration += 1
