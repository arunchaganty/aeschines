echo "http://www.cfr.org/united-states/marco-rubios-foreign-policy-vision/p36511" |
  wget -O - -i - | 
   hxnormalize -x | 
   hxselect -i "p" | 
   lynx -stdin -dump > MarcoRubio1.txt

python scraperBush.py MarcoRubio1.txt >> MarcoRubio.txt 
