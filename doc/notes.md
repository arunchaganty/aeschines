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


||Main_Colorado_Oct_2012|Main_Florida_Oct_2012|Main_NewYork_Oct_2012|Republican_Arizona_Feb_2012|Republican_California_Sep_2011|Republican_DesMoines_Dec_2011|Republican_Florida_Jan_2012|Republican_Florida_Sep_2011|Republican_Iowa_Aug_2011|Republican_Iowa_Dec_2011|Republican_Manchester_Jan_2012|Republican_Michigan_Nov_2011|Republican_MyrtleBeach_Jan_2012|Republican_Nevada_Oct_2011|Republican_NHampshire_Jan_2012|Republican_NHampshire_June_2011|Republican_NHampshire_Oct_2011|Republican_SCarolina_Jan_2012|Republican_SCarolina_Nov_2011|Republican_SCarolina_Sep_2011|Republican_Tampa_Jan_2012|Republican_Tampa_Sep_2011|Republican_Washington_Nov_2011|VP_Kentucky_Oct_2012
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---
OBAMA|9.6166666667|12.564516129|8.1627906977|||||||||||||||||||||
ROMNEY|7.0769230769|11.5652173913|6.8987341772|9.8529411765|10.85|11.1818181818|11.6285714286|11.9|12.5882352941|12.4|10.7714285714|9|14.0909090909|5.6190476191|8.5666666667|6.1923076923|7.6279069767|14.1034482759|8.2777777778|8.9230769231|7.6888888889|9.2777777778|10.5555555556|
PAUL||||14.2222222222|10.9285714286|12.1428571429|10.2222222222|6.5714285714|9.5263157895|11.2222222222|10.7647058824|8.4545454546|13.2105263158|8.8571428571|13.875|10.5|10.7|20.2142857143|6.5454545455|11.7692307692|15.6153846154|8.1578947368|13|
GINGRICH||||12.8823529412|10.75|6|8.2222222222|5.8333333333|6.0952380952|7.6923076923|6.8|	4.6315789474|5.9411764706|4.9523809524|5|7.5294117647|6.2307692308|8.8965517241|5.7368421053|9.3333333333|6|9.5|8.0952380952|
SANTORUM||||10.4242424242|14.5714285714|19.7272727273|13.9565217391|7|7.8095238095|18|9.724137931|19|8.0454545455|3.40625|7.2272727273|10.9411764706|4.5238095238|11.2692307692|12.3333333333||13.3333333333|10.6153846154|12.5|
HUNTSMAN|||||21|||15.5454545455|19|17.8|16.25|11|||14.5555555556||5.6428571429||10.5833333333|||16.4545454545|18.3571428571|
BACHMANN|||||12.1|9.45||7.25|8.0476190476|6.95||14.5||4.1428571429||7.7894736842|9.4666666667||7.9285714286|6.4210526316||5.4705882353|12.0666666667|
PERRY|||||7.2|8||6.2916666667||8.5833333333|8.1|4.4166666667|9|4|3.9230769231||8.5||6.4117647059|||6.8461538462|13.4615384615|
CAIN|||||7.1428571429|||8.625|9.4166666667|||5.5||4.3703703704||6|4.0357142857||6.2307692308|7.2352941177||7.3636363636|	7.6363636364|
JOHNSON||||||||9.2||||||||||||||||
PAWLENTY|||||||||9|||||||9.6956521739||||||||
RYAN||||||||||||||||||||||||4.2745098039
BIDEN||||||||||||||||||||||||3.9361702128
