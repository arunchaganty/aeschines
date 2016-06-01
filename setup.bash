#!/bin/bash

# << set Greenplum connection parameters >>
export DB_HOST=${DB_HOST:-"localhost"}
export DB_USER=${DB_USER:-"aeschines"}
export DB_PORT=${DB_PORT:-"5432"}
export DB_DB=${DB_DB:-"aeschines"}

function pgsql() {
  query=$1;
  psql -h "$DB_HOST" \
    -p "$DB_PORT" \
    -U "$DB_USER" \
    --set ON_ERROR_STOP=on \
    "$DB_DB" \
    -c "$query"
}
