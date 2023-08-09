#!/bin/sh

python docker/scripts/setup_db_tables.py
python docker/scripts/run_api_server.py

exec "$@"