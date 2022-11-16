# Database Auditing

## Description

This project pulls 2018-Atlanta-Braves-pitching data from the StatsAPI provided by the MLB. It selects relevant data that can be used to audit the ```PITCHBYPITCH``` table (see the database in ```database/pitchbypitch_db```). It writes this data to a ```.csv``` file (see the file in ```csv/pitcher-data.csv```). This file is then compared to a query from the ```PITCHBYPITCH``` table, where a comparison table is returned with all the corresponding data side-by-side for easy inspection. This comparison table is also written to a ```.csv``` (see the file in ```csv/compare-pitch-data.csv```)

## How to Run

### Requirements

Python (3.9.6) and required libraries (see [install libraries](#install-libraries) for more details).

### Setup

#### Get the Code

Clone (`git clone https://github.com/JMisley/DB-Audit.git`) or [download a zip file](https://github.com/JMisley/DB-Audit/archive/refs/heads/master.zip).

#### Install Libraries

Open a terminal in the root directory of the project and execute: 

```bash
pip install -r reqirements.txt
```

## Run 

Opena terminal in the root directory of the project and execute:

```bash
python main/audit_database.py
```

## Author

| [<img src="https://avatars.githubusercontent.com/u/89669123?v=4" width="100"><br><sub>@JMisley</sub>](https://github.com/JMisley) |
|:----:|
