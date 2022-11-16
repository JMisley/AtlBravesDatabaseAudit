# Database Auditing

## Description

- This project pulls 2018-Atlanta-Braves-pitching data from the StatsAPI provided by the MLB. It selects relevant data
  that can be used to audit the ```PITCHBYPITCH``` table (see the database in ```database/pitchbypitch_db```). It writes
  this data to a ```.csv``` file (see the file in ```csv/pitcher-data.csv```). This file is then compared to a query
  from the ```PITCHBYPITCH``` table, where a comparison table is returned with all the corresponding data side-by-side
  for easy inspection. This comparison table is also written to a ```.csv``` (see the file
  in ```csv/compare-pitch-data.csv```)

## How to Run

- Requirements
    - Python

- Installation
    - GitHub Clone
        - Open a terminal, navigate to your desired location, and
          execute ```git clone https://github.com/JMisley/DB-Audit.git```
    - Download Zip
        - Go to https://github.com/JMisley/DB-Audit.git, click the green "Code" button, and click "Download Zip"

- Install Libraries
    - Navigate to "DB-Audit" so it is your current working directory
    - Open a terminal and execute ```pip install -r reqirements.txt``` (only required for the first time running the
      project)

- Run Project From Command Line - Navigate to "DB-Audit" so it is your current working directory -
  Execute ```python main/audit_database.py``` to start the script

## Author

- John Misley
