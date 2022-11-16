import sqlite3
import pandas

from make_csv import write_api_csv
from queries import pitcherDataQuery

# Player IDs for Shane Carle, Jonny Venters, and Luke Jackson
playerIDs = [641438, 458924, 592426]

# write a csv file containing API data
write_api_csv()

# connect to pitchbypitch_db
try:
    connection = sqlite3.connect('database/pitchbypitch_db')
    print('Opened Database Successfully\n')
except Exception as e:
    print("Error during connection: ", e)

# column settings
pandas.set_option('display.max_columns', 2000)
pandas.set_option('display.width', 2000)

# run the query for all player IDs and add results to one table
query_loop = [pandas.read_sql_query(pitcherDataQuery.replace('$playerId', str(pid)), connection) for pid in playerIDs]
pitchByPitchData = pandas.concat(query_loop)
csvData = pandas.read_csv('csv/pitcher-data.csv')

# format data for easy comparison
pitchByPitchData.insert(0, 'From', 'Database')
csvData.insert(0, 'From', 'API')

compareData = pandas.concat([csvData, pitchByPitchData])
compareData = compareData.sort_values(by='PitcherName')
compareData = compareData.reset_index().drop('index', axis=1)
print(compareData)

# save comparison data to csv
compareData.to_csv('csv/compare-pitch-data.csv')

connection.close()
