for f in *.txt; do
    python label_affect.py --lexicon ../data/Ratings_Warriner_et_al.csv --input $f --output `basename $f .txt`_affect.txt;
done;
