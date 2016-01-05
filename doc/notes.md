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

#FFM Analysis

Calculated correlations with personality for each candidate using the FFM scores calculated by Schwartz et al. (normalized by the number of words he speaks and number of debates he participates in)

Agreeableness - Positive scores imply more agreeableness (warm, kind, cooperative, unselfish, trustful, and generous)

Conscientiousness - Positive scores imply more conscientiousness (organized, responsible, practical, thorough, hardworking, and thrifty)

Extraversion - Positive scores imply more extraversion (energetic, talkative, bold, active, assertive, and adventurous)

Neuroticism - Negative scores imply more neuroticism (angry, tense, nervous, envious, unstable, discontented, and emotional)

Openness - Positive scores imply more openness (intelligent, analytical, reflective, curious, imaginative, creative, and sophisticated)

Ref to paper: Schwartz, H. Andrew, et al. "Personality, gender, and age in the language of social media: The open-vocabulary approach." PloS one 8.9 (2013): e73791.

Link to data: http://www.wwbp.org/data.html

|| Openness | Extraversion | Neuroticism | Agreeableness | Conscientiousness |
---| ---| ---| ---| ---| ---|
WEBB | -0.270848833045 | 0.0109478580712 | 0.00213067328033 | -0.0431387536812 | 0.00252315540961 |
PERRY | -0.336545410517 | 0.0104761173502 | -0.0046873125471 | -0.0491881163964 | -0.00315051198805 |
DOUGLAS | -7.33773719169 | 0.31131838863 | -0.0184353297259 | -1.35952769616 | -0.148530743165 |
RUBIO | -0.407989004258 | 0.0138333591491 | -0.000212785108805 | -0.0540468543303 | -0.00205456397093 |
KASICH | -0.302802421631 | 0.00836189569877 | 0.00017191006759 | -0.0437109657872 | -0.000694196246111 |
GRAHAM | -0.297894609228 | 0.0134336033267 | -0.00428730805496 | -0.0482527128866 | 0.00169834346083 |
GINGRICH | -0.384849187868 | 0.00496445965993 | -0.00258091049637 | -0.0565112327622 | -0.00398958219971 |
BIDEN | -0.15126481011 | 0.00800898383775 | -0.00179439251851 | -0.0254254576571 | -0.00285630668561 |
SANTORUM | -0.455198975776 | 0.00864027904291 | -0.00111054029223 | -0.0644129773225 | -0.00116502545286 |
FIORINA | -0.315926735929 | 0.00840712423511 | -0.000488656305694 | -0.0407187542217 | -0.00159437521791 |
BUSH | -0.301509742374 | 0.00652028938972 | -0.00280472026533 | -0.0438257051551 | -0.00284660823221 |
BACHMANN | -0.318589622259 | 0.00728544071053 | -0.00388301861223 | -0.0456464536851 | -0.00381270982549 |
WALKER | -0.299430571454 | 0.0212422136232 | 0.000649740658117 | -0.0379393380261 | 0.000327963360037 |
CAIN | -0.271021467599 | 0.0106724722837 | -0.00416124086191 | -0.0387157795106 | -0.0052590465434 |
JINDAL | -0.434302652837 | 0.0107686817703 | -0.0076142864724 | -0.0569100061771 | -0.00587620316542 |
LINCOLN | -9.82088885836 | 0.210882333358 | -0.1106027601 | -1.88188129014 | -0.180934593586 |
JOHNSON | -0.386505952 | 0.0115006676 | -0.00980435973333 | -0.0580014258667 | -0.0234266610667 |
KENNEDY | -1.15689574127 | 0.0115812505676 | -0.00813125621268 | -0.222647452239 | -0.0189431550042 |
CHAFEE | -0.238580246975 | 0.00135604472576 | -0.00121222608033 | -0.0294094980582 | 0.00102563663435 |
HUNTSMAN | -0.461840575677 | 0.00863437001609 | -0.00498338879181 | -0.0633098555523 | -0.00532449283759 |
ROMNEY | -0.393070840884 | 0.00835997490238 | -0.00223455212468 | -0.0550467747425 | -0.000947469739423 |
HUCKABEE | -0.377328495426 | 0.00665927715816 | -0.00393444404331 | -0.0555152311661 | -0.00350963879831 |
CRUZ | -0.318257630584 | 0.00344347034859 | -0.00274271409478 | -0.0486015178206 | -0.00583714046285 |
PAWLENTY | -0.39005549035 | 0.00766104437538 | -0.00428062899739 | -0.0587790505589 | -0.00214717070243 |
PAUL | -0.398298075932 | 0.00939846920678 | -0.00250381765826 | -0.0532555787241 | -0.00400296299807 |
NIXON | -1.20639838267 | 0.0227797304342 | -0.00508451482753 | -0.20163028421 | -0.0252388650082 |
SANDERS | -0.261314664279 | 0.00643131534741 | -5.31419599832e-05 | -0.0347991320817 | -0.00105902592328 |
CLINTON | -0.297086407851 | 0.0100737096773 | -9.56516866182e-05 | -0.0425219958516 | -0.000657081031563 |
TRUMP | -0.181794919672 | 0.00745372991605 | -0.00170248712577 | -0.0214808478136 | 0.000251793355827 |
PATAKI | -0.321873592175 | -0.00256633519992 | -0.00254302267093 | -0.0410719626179 | -0.00096050343721 |
CHRISTIE | -0.435833075354 | 0.0164556637742 | -0.00161325029698 | -0.0684546672406 | -0.00188694676873 |
RYAN | -0.164620792802 | 0.00426881477831 | -0.0019202734764 | -0.0230877926139 | -0.00201829501067 |
CARSON | -0.347751484723 | 0.00577993821569 | -0.000954795293553 | -0.0505679193724 | -0.00286093727562 |
GILMORE | -0.471439400663 | -0.0032165598422 | -0.014747362651 | -0.0656240244725 | -0.0199490887376 |
O'MALLEY | -0.297122884023 | 0.00481655920608 | 0.000983662807613 | -0.0431999637134 | -0.000269128351068 |
OBAMA | -0.386149703793 | 0.00642217253758 | -0.00354597818715 | -0.0517548114047 | -0.00289519534326 |

# Tables for counts of use of Self-referential pronouns

## Normalized by the number of words each speaker speaks and number of debates he participates in.

Candidate|Normalized Count|
---|---|
WEBB | 0.0784652609748 |
PERRY | 0.0692158930434 |
DOUGLAS | 0.0352332635006 |
RUBIO | 0.0751980613905 |
KASICH | 0.112248137525 |
GRAHAM | 0.0867022694958 |
GINGRICH | 0.0631779299138 |
BIDEN | 0.0721341304913 |
SANTORUM | 0.079257299736 |
FIORINA | 0.0789102918417 |
BUSH | 0.0875116767677 |
BACHMANN | 0.0792372146172 |
WALKER | 0.0884515938213 |
CAIN | 0.0743381345346 |
JINDAL | 0.0983042307623 |
LINCOLN | 0.0488179847461 |
JOHNSON | 0.0766666666667 |
KENNEDY | 0.082846841955 |
CHAFEE | 0.0958448753463 |
HUNTSMAN | 0.10392526592 |
ROMNEY | 0.0796319613483 |
HUCKABEE | 0.0885321204073 |
CRUZ | 0.0660614800831 |
PAWLENTY | 0.0811913478947 |
PAUL | 0.0862967803544 |
NIXON | 0.081795173504 |
SANDERS | 0.0826289418267 |
CLINTON | 0.095019227536 |
TRUMP | 0.108083793554 |
PATAKI | 0.0835077466304 |
CHRISTIE | 0.0758167950911 |
RYAN | 0.0830159939071 |
CARSON | 0.0819297765512 |
GILMORE | 0.0784490532011 |
O'MALLEY | 0.095297784713 |
OBAMA | 0.0867637650292 |

# Tables for Applause Counts

## Normalized by the number of words each speaker speaks and number of debates he participates in.

Candidate|Normalized Count|
---|---|
WEBB | 0.0 |
PERRY | 0.00222939181577 |
DOUGLAS | 0.0 |
RUBIO | 0.00246114169087 |
KASICH | 0.00263565895375 |
GRAHAM | 0.0017175117154 |
GINGRICH | 0.00369242471924 |
BIDEN | 0.0 |
SANTORUM | 0.00178760156376 |
FIORINA | 0.00219577098478 |
BUSH | 0.00267898813111 |
BACHMANN | 0.00219547220727 |
WALKER | 0.00419835068202 |
CAIN | 0.00289483107519 |
JINDAL | 0.00176540881154 |
LINCOLN | 7.61223298821e-05 |
JOHNSON | 0.01 |
KENNEDY | 0.0 |
CHAFEE | 0.0016620498615 |
HUNTSMAN | 0.0017298217053 |
ROMNEY | 0.00211552563221 |
HUCKABEE | 0.00309103207622 |
CRUZ | 0.00429751434307 |
PAWLENTY | 0.0 |
PAUL | 0.00377359593789 |
NIXON | 0.0 |
SANDERS | 0.00423832650969 |
CLINTON | 0.00318789934564 |
TRUMP | 0.00299749000003 |
PATAKI | 0.00123302817733 |
CHRISTIE | 0.00334569947189 |
RYAN | 0.0 |
CARSON | 0.00421903157438 |
GILMORE | 0.0 |
O'MALLEY | 0.001894578897 |
OBAMA | 0.0 |

# Table for number of times each speaker speaks in each debate

|| CLINTON | O'MALLEY | SANDERS | CHAFEE | WEBB | KENNEDY | NIXON | LINCOLN | DOUGLAS | OBAMA | ROMNEY | PAUL | GINGRICH | SANTORUM | HUNTSMAN | BACHMANN | PERRY | CAIN | KASICH | HUCKABEE | CHRISTIE | RUBIO | CARSON | WALKER | CRUZ | BUSH | TRUMP | FIORINA | JOHNSON | PAWLENTY | JINDAL | PATAKI | GRAHAM | GILMORE | RYAN | BIDEN |
---| ---| ---| ---| ---| ---| ---| ---| ---| ---| ---| ---| ---| ---| ---| ---| ---| ---| ---| ---| ---| ---| ---| ---| ---| ---| ---| ---| ---| ---| ---| ---| ---| ---| ---| ---| ---|
Lincoln_Douglas_Alton_Oct_1858 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
Lincoln_Douglas_Charleston_Sep_1858 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
Lincoln_Douglas_Freeport_Aug_1858 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
Lincoln_Douglas_Galesburg_Oct_1858 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
Lincoln_Douglas_Jonesboro_Sep_1858 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
Lincoln_Douglas_Ottawa_Aug_1858 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
Lincoln_Douglas_Quincy_Oct_1858 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
Kennedy_Nixon_Oct2_1960 | 0 | 0 | 0 | 0 | 0 | 14 | 14 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
Kennedy_Nixon_Oct3_1960 | 0 | 0 | 0 | 0 | 0 | 11 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
Kennedy_Nixon_Oct_1960 | 0 | 0 | 0 | 0 | 0 | 12 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
Kennedy_Nixon_Sep_1960 | 0 | 0 | 0 | 0 | 0 | 16 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
Republican_California_Sep_2011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 20 | 14 | 8 | 7 | 11 | 10 | 25 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
Republican_DesMoines_Dec_2011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 33 | 14 | 30 | 11 | 0 | 20 | 19 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
Republican_Florida_Sep_2011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 20 | 7 | 12 | 20 | 11 | 12 | 24 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
Republican_Iowa_Aug_2011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 17 | 19 | 21 | 21 | 10 | 21 | 0 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 15 | 0 | 0 | 0 | 0 | 0 | 0 |
Republican_Iowa_Dec_2011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 20 | 18 | 26 | 8 | 10 | 20 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
Republican_Michigan_Nov_2011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 27 | 11 | 19 | 6 | 14 | 8 | 12 | 14 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
Republican_NHampshire_June_2011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 26 | 18 | 17 | 17 | 0 | 19 | 0 | 24 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 23 | 0 | 0 | 0 | 0 | 0 | 0 |
Republican_NHampshire_Oct_2011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 43 | 10 | 13 | 21 | 14 | 15 | 14 | 28 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
Republican_Nevada_Oct_2011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 63 | 21 | 21 | 32 | 0 | 28 | 34 | 27 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
Republican_SCarolina_Nov_2011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 18 | 11 | 19 | 12 | 12 | 14 | 17 | 13 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
Republican_SCarolina_Sep_2011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 13 | 13 | 12 | 0 | 0 | 19 | 0 | 17 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
Republican_Tampa_Sep_2011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 18 | 19 | 12 | 13 | 11 | 17 | 26 | 11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
Republican_Washington_Nov_2011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 18 | 15 | 21 | 12 | 14 | 15 | 13 | 11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
Main_Colorado_Oct_2012 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 60 | 78 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
Main_Florida_Oct_2012 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 62 | 69 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
Main_NewYork_Oct_2012 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 86 | 79 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
Republican_Arizona_Feb_2012 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 34 | 18 | 17 | 33 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
Republican_Florida_Jan_2012 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 35 | 18 | 36 | 23 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
Republican_Manchester_Jan_2012 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 35 | 17 | 15 | 29 | 12 | 0 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
Republican_MyrtleBeach_Jan_2012 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 33 | 19 | 17 | 22 | 0 | 0 | 13 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
Republican_NHampshire_Jan_2012 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 30 | 8 | 19 | 22 | 9 | 0 | 13 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
Republican_SCarolina_Jan_2012 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 29 | 14 | 29 | 26 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
Republican_Tampa_Jan_2012 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 45 | 13 | 41 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
VP_Kentucky_Oct_2012 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 153 | 141 |
Democratic_Iowa_Nov_2015 | 47 | 38 | 56 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
Democratic_Nevada_Oct_2015 | 72 | 45 | 61 | 24 | 33 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
RepUC_California_Sep_2015 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 46 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 32 | 34 | 64 | 0 | 0 | 0 |
RepUC_Colorado_Oct_2015 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 18 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 18 | 31 | 24 | 0 | 0 | 0 |
RepUC_Nevada_Dec_2015 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 30 | 0 | 0 | 0 | 0 | 0 | 22 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 28 | 41 | 0 | 0 | 0 |
RepUC_Ohio_Aug_2015 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 0 | 0 | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 0 | 0 | 9 | 10 | 9 | 8 | 0 | 0 |
RepUC_Wisconsin_Nov_2015 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 15 | 0 | 0 | 0 | 0 | 0 | 14 | 15 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 18 | 0 | 0 | 0 | 0 | 0 |
Republican_California_Sep_2015 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 35 | 0 | 0 | 0 | 0 | 0 | 0 | 33 | 19 | 28 | 30 | 28 | 30 | 25 | 64 | 106 | 52 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
Republican_Colorado_Oct_2015 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 13 | 0 | 0 | 0 | 0 | 0 | 0 | 22 | 27 | 13 | 29 | 17 | 0 | 24 | 22 | 29 | 24 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
Republican_Nevada_Dec_2015 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 16 | 0 | 0 | 0 | 0 | 0 | 0 | 12 | 0 | 10 | 24 | 14 | 0 | 34 | 26 | 44 | 20 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
Republican_Ohio_Aug_2015 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 23 | 0 | 0 | 0 | 0 | 0 | 0 | 11 | 10 | 18 | 12 | 9 | 11 | 8 | 11 | 36 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
Republican_Wisconsin_Nov_2015 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 25 | 0 | 0 | 0 | 0 | 0 | 0 | 27 | 0 | 0 | 15 | 10 | 0 | 21 | 16 | 28 | 18 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
