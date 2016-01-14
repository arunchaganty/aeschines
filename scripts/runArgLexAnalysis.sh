rm -f ../results/argLexResults.txt
for regexFile in $(ls ../resources/arglex/regex/*.tff);
do
    for partFile in $(ls ../resources/Debates/csv/*_parts.csv);
    do
        python countArglex.py $partFile $regexFile ../resources/arglex/macros/macroToRegex.tff >> ../results/argLexResults.txt
    done
done
