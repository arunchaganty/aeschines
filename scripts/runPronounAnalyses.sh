rm -f ../results/pronounsResults.txt
for partFile in $(ls ../resources/Debates/csv/*_parts.csv);
do
    python countPronouns.py $partFile >> ../results/pronounsResults.txt
done
python resultsTomd.py ../results/pronounsResults.txt > ../results/pronounCounts.md
