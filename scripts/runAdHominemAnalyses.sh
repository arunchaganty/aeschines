rm -f ../results/adHominemResults.txt
for partFile in $(ls ../resources/Debates/csv/*_parts.csv);
do
    python adHominemBasic.py $partFile >> ../results/adHominemResults.txt
done
#python resultsTomd.py ../results/adHominemResults.txt > ../results/adHominemCounts.md
