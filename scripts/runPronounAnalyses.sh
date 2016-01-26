rm -f ../results/pronounsSingularResults.txt
rm -f ../results/pronounsPluralResults.txt
for partFile in $(ls ../resources/Debates/csv/*_parts.csv);
do
    python countPronouns.py $partFile 1 >> ../results/pronounsSingularResults.txt
    python countPronouns.py $partFile 0 >> ../results/pronounsPluralResults.txt
done
python resultsTomd.py ../results/pronounsSingularResults.txt > ../results/pronounSingularCounts.md
python resultsTomd.py ../results/pronounsPluralResults.txt > ../results/pronounPluralCounts.md
