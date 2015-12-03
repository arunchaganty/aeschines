# Observations of the debates.

Currently, we are looking at the first 2016 Republican debate that took place on August 7th, 2015.

# Republican Debate: August 7th, 2015.


## The secondary candidates

A list of how often each candidate spoke. Note the last two are moderators.

      1 UNKNOWN
      7 SANTORUM
      8 GILMORE
      9 GRAHAM
      9 JINDAL
      9 PERRY
     10 FIORINA
     10 PATAKI
     43 MacCALLUM
     60 HEMMER

How many words each candidate spoke.


# Republican Debate: August 6th, 2015.

## PARTICIPANTS:
Former Governor Jeb Bush (FL);
Ben Carson;
Governor Chris Christie (NJ);
Senator Ted Cruz (TX);
Former Governor Mike Huckabee (AR);
Governor John Kasich (OH);
Senator Rand Paul (KY);
Senator Marco Rubio (FL);
Donald Trump;
Governor Scott Walker (WI);
## MODERATORS:
Bret Baier (Fox News);
Megyn Kelly (Fox News); and 
Chris Wallace (Fox News)


## Count of how often each candidate used a personal pronoun. (normalized by number of times each person speaks)

      'BUSH', 15.363636363636363
      'KASICH', 13.727272727272727
      'CARSON', 12.777777777777779
      'WALKER', 11.181818181818182
      'RUBIO', 11.166666666666666
      'CRUZ', 11.0
      'HUCKABEE', 10.1
      'CHRISTIE', 7.166666666666667
      'TRUMP', 6.222222222222222
      'PAUL', 4.173913043478261

## Popularity of Candidates (based on applause count for each)

      'CRUZ': 14
      'CARSON': 11
      'TRUMP': 9
      'PAUL': 9
      'HUCKABEE': 8
      'BUSH': 8
      'WALKER': 8
      'RUBIO': 7
      'KASICH': 6
      'CHRISTIE': 5

## Ad Hominem Attacks (Basic approach)
Methods used:
* How often a candidate speaks immediately after another without a moderator in between
* How often a candidate says another candidates' name
```
      'kasich': [13, {'ted': 6, 'trump': 2, 'donald': 2, 'christie': 1, 'jeb': 1, 'chris': 1}]
      'trump': [9, {'chris': 4, 'ted': 3, 'jeb': 2}]
      'walker': [8, {'ted': 6, 'chris': 2}]
      'huckabee': [6, {'ted': 3, 'chris': 1, 'ben': 1, 'donald': 1}]
      'christie': [6, {'ted': 2, 'paul': 2, 'carson': 1, 'bush': 1}]
      'bush': [6, {'ted': 5, 'trump': 1}]
      'rubio': [6, {'ted': 4, 'chris': 1, 'kasich': 1}]
      'paul': [5, {'john': 2, 'ted': 2, 'ben': 1}]
      'cruz': [3, {'chris': 3}]
      'carson': [2, {'ted': 2}]
```
