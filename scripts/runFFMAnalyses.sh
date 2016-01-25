resultsFile=../results/FFMAnalyses.txt
rm -f $resultsFile
for partFile in $(ls ../resources/Debates/csv/*_parts.csv);
do
    for weightFile in $(ls ../resources/UngarFFM/*.csv)
    do
        python FFMAnalysis.py $partFile $weightFile >> $resultsFile
    done
done
python aggregateFFMAnalysis.py $resultsFile > ../results/aggFFMAnalysis.md
