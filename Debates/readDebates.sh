for year in $(ls -d raw/*/);
do
    echo $year
    for file in $(ls $year);
    do
        python readDebate.py $year $file
        echo $file
    done
done
