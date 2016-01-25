rm -f ../results/applauseResults.txt
for partFile in $(ls ../resources/Debates/csv/*_parts.csv);
do
    python countApplause.py $partFile >> ../results/applauseResults.txt
done
python resultsTomd.py ../results/applauseResults.txt > ../results/applauseCounts.md
