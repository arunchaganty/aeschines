rm -f ../arglex/macros/macroToRegex.tff
for regexFile in $(ls ../arglex/regex/*.tff);
do
    python macroToRegex.py $regexFile ../arglex/macros/all.tff >> ../arglex/macros/macroToRegex.tff
done
