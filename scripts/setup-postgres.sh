#!/bin/bash

# Create the database users expected along with databases
sudo -u postgres psql postgres -c "CREATE USER $DATABASE_USER WITH PASSWORD '$DATABASE_PASSWORD' CREATEDB;"
sudo -u postgres psql postgres -c "CREATE DATABASE $DATABASE_NAME OWNER $DATABASE_USER;"
sudo -u postgres psql postgres -c "ALTER ROLE $DATABASE_USER SET client_encoding TO 'utf8';"
sudo -u postgres psql postgres -c "ALTER ROLE $DATABASE_USER SET default_transaction_isolation TO 'read committed';"
sudo -u postgres psql postgres -c "ALTER ROLE $DATABASE_USER SET timezone TO 'UTC';"
sudo -u postgres psql postgres -c "GRANT ALL PRIVILEGES ON DATABASE $DATABASE_PASSWORD TO $DATABASE_USER;"

echo "Confirm database is running: pg_isready"
pg_isready -d "$DATABASE_NAME" -U "$DATABASE_USER" -t 5