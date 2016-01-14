rm -f ../Results/*.txt
for partFile in $(ls ../Debates/csv/*_parts.csv);
do
    python countPronouns.py $partFile >> ../Results/pronounsResults.txt
    python countApplause.py $partFile >> ../Results/applauseResults.txt
    python adHominemBasic.py $partFile >> ../Results/adHominemResults.txt
done

for partFile in $(ls ../Debates/csv/*_parts.csv);
do
    python countArglex.py $partFile ../arglex/macros/macroToRegex.tff >> ../Results/argLexResults1.txt
done
