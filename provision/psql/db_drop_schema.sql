-- Close any open connections to the database
SELECT pg_terminate_backend(pid) from pg_stat_activity where datname='sqlmongo';



-- Drop the database (schema and tables),
-- Create the initial user, set their password:
DROP DATABASE IF EXISTS sqlmongo;
DROP USER IF EXISTS sqldb;
CREATE USER sqldb WITH PASSWORD 'sqldb';

-- Create the database:
CREATE DATABASE sqlmongo WITH OWNER sqldb;
GRANT ALL PRIVILEGES ON DATABASE "sqlmongo" TO sqldb;
