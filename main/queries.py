pitcherDataQuery = """
SELECT PitcherName,
       t1.PitcherID AS PitcherID,
       GamesPitched,
       BattersFaced,
       StrikeOuts,
       PitchesThrown,
       Outs,
       Singles,
       Doubles,
       Triples,
       HomeRuns,
       Hits
FROM (SELECT PitcherName,
             PitcherID,
             COUNT(DISTINCT GameDate) AS GamesPitched,
             SUM(IS_STRIKEOUT)        AS StrikeOuts,
             COUNT(*)                 AS PitchesThrown,
             SUM(IS_SINGLE)           AS Singles,
             SUM(IS_DOUBLE)           AS Doubles,
             SUM(IS_TRIPLE)           AS Triples,
             SUM(IS_HOMERUN)          AS HomeRuns,
             SUM(IS_HIT)              AS Hits,
             SUM(IS_OUT)              AS Outs
      FROM PITCHBYPITCH
      WHERE PitcherID = $playerId) t1
         INNER JOIN (SELECT PitcherID, COUNT(PA_OF_INNING) AS BattersFaced
                     FROM (SELECT DISTINCT PitcherName, PitcherID, GameDate, INNING, PA_OF_INNING
                           FROM PITCHBYPITCH
                           WHERE PitcherID = $playerId)) t2 ON t1.PitcherID = t2.PitcherID;
"""
