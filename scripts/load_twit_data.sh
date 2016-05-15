#!/bin/bash
# Script that loads the database with the tweets given the data
# collected via the scrape. 
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

nargs=$#
if [[ $nargs != 1 ]]; then
  echo "Usage: $0 <data-directory>"
  exit 1;
fi;

datadir=$1;
if [ ! -e $datadir ]; then
    error "Data directory $datadir doesn't exist";
    exit 1;
fi;

#set -o xtrace

# LOAD users
#msg "Loading users..."
#$MYDIR/load_data.sh twit_user $datadir/twit_users.tsv.gz
#pgsql "
#DELETE FROM twit_user;
#INSERT INTO twit_user (SELECT DISTINCT ON (x.id) x.* FROM twit_user_ x);
#DROP TABLE twit_user_;"
#msg "Done!"
#
## LOAD tweets
#msg "Loading tweets..."
#$MYDIR/load_data.sh load_data.sh twit_tweet $datadir/twit_tweets.tsv.gz
#pgsql "
#DELETE FROM twit_tweet;
#INSERT INTO twit_tweet (SELECT DISTINCT ON (t.id) t.* FROM twit_tweet_ t, twit_user u WHERE t.user_id = u.id);
#DROP TABLE twit_tweet_;"
#msg "Done!"

# LOAD retweets
msg "Loading retweets..."
#$MYDIR/load_data.sh twit_retweet $datadir/twit_retweets.tsv.gz
pgsql "
DELETE FROM twit_retweet;
INSERT INTO twit_retweet (SELECT DISTINCT ON (r.id) r.* FROM twit_retweet_ r, twit_tweet t WHERE r.tweet_id = t.id);
-- Update tweet counts
CREATE TEMPORARY TABLE twit_retweet_counts_ AS (SELECT tweet_id AS id, COUNT(*) AS count FROM twit_retweet GROUP BY tweet_id);
UPDATE twit_tweet t SET retweet_count = retweet_count + r.count FROM twit_retweet_counts_ r WHERE  r.id = t.id;
DROP TABLE twit_retweet_;"
msg "Done!"

# Done
wait  # Very important: wait for the jobs to actually finish...
set -o errexit
msg "DONE loading data"
msg "DONE with `basename $0`"


