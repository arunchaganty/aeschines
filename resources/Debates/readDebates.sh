for year in $(ls -d raw/*/);
do
    for file in $(ls $year);
    do
        python readDebate.py $year $file
    done
done
