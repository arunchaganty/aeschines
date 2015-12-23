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

## Count of how many times a candidate speaks
      'TRUMP': 36
      'PAUL': 23
      'CHRISTIE': 18
      'RUBIO': 12
      'BUSH': 11
      'KASICH': 11
      'WALKER': 11
      'HUCKABEE': 10
      'CARSON': 9
      'CRUZ': 8


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
### Total applause count
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
### Normalized Applause Count
      'CRUZ', 1.75
      'CARSON', 1.2222222222222223
      'HUCKABEE', 0.8
      'WALKER', 0.7272727272727273
      'BUSH', 0.7272727272727273
      'RUBIO', 0.5833333333333334
      'KASICH', 0.5454545454545454
      'PAUL', 0.391304347826087
      'CHRISTIE', 0.2777777777777778
      'TRUMP', 0.25

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


# Tables for counts of use of Self-referential pronouns
|Democratic_Iowa_Nov_2015|Democratic_Nevada_Oct_2015
---|---|---
CLINTON|10.1276595745|7.8472222222
O'MALLEY|8.5|7.4888888889
SANDERS|6.5714285714|6.6229508197
CHAFEE||7.2083333333
WEBB	||6.8787878788


|Kennedy_Nixon_Oct_1960|Kennedy_Nixon_Oct2_1960|Kennedy_Nixon_Oct3_1960|Kennedy_Nixon_Sep_1960
---|---|---|---|---
KENNEDY|34.0833333333|20.2857142857|41.6363636364|23.125
NIXON|31.3333333333|27.2857142857|43.1|29.5


|Lincoln_Douglas_Alton_Oct_1858|Lincoln_Douglas_Charleston_Sep_1858|Lincoln_Douglas_Freeport_Aug_1858|Lincoln_Douglas_Galesburg_Oct_1858|Lincoln_Douglas_Jonesboro_Sep_1858|Lincoln_Douglas_Ottawa_Aug_1858|Lincoln_Douglas_Quincy_Oct_1858
---|---|---|---|---|---|---|---
LINCOLN|496|70.2|31.25|153|94.5|66.1428571429|158
DOUGLAS|98.3333333333|165.5|55.3333333333|67.3333333333|39.1666666667|48.2|121.333333333
