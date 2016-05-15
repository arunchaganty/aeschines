#!/bin/bash
#
set -o nounset
set -o errexit

# Load the prerequisite environment variables
TASK_FILE="${BASH_SOURCE[0]}"
if [[ "$TASK_FILE" != /* ]]; then TASK_FILE="`pwd`/$TASK_FILE"; fi
MYDIR=$( cd "$( dirname "$TASK_FILE" )" && pwd )
ROOTDIR="$MYDIR"
source "$ROOTDIR/env/util.env"
source "$ROOTDIR/env/csv.env"
#source "$ROOTDIR/env/prereq_bash.env"
#source "$ROOTDIR/env/database.env"
source "$ROOTDIR/env/database_local.env"
MYDIR=$( cd "$( dirname "$TASK_FILE" )" && pwd )  # MYDIR gets clobbered

#set -o xtrace

# filename to load 
nargs=$#
if [[ $nargs != 2 ]]; then
  echo "Usage: $0 <dbname> <filename.gz>"
  exit 1;
fi;

dbname=$1
filename=$2;
header=`zcat $filename | get_headers`;
zcat $filename | \
    pgsql "
CREATE TABLE ${dbname}_(LIKE $dbname);
COPY ${dbname}_($header) FROM STDIN CSV HEADER DELIMITER E'\t';
-- INSERT INTO ${dbname} (SELECT DISTINCT ON (t.id) t.* FROM ${dbname}_ t);
"

# Done
wait  # Very important: wait for the jobs to actually finish...
set -o errexit
msg "DONE loading data"
msg "DONE with `basename $0`"

