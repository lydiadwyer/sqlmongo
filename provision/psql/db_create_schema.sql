-- Postgres Cheatsheet
-- https://gist.github.com/apolloclark/ea5466d5929e63043dcf

-- Destroy the schema
DROP SCHEMA IF EXISTS sqlmongo CASCADE;

-- Setup database schema:
CREATE SCHEMA IF NOT EXISTS sqlmongo AUTHORIZATION sqldb;
GRANT ALL ON SCHEMA sqlmongo TO sqldb;



DROP TABLE IF EXISTS countries CASCADE;
CREATE TABLE countries(
    country_id         SERIAL PRIMARY KEY,
    country_name       VARCHAR(128),
    country_abrev      VARCHAR(128)
);
ALTER TABLE countries OWNER TO sqldb;


-- Setup trigger, to auto-set the created and updated time
CREATE OR REPLACE FUNCTION set_country_created()
RETURNS TRIGGER AS $$
BEGIN
   NEW.country_created = now();
   RETURN NEW;
END;
$$ language 'plpgsql';
ALTER FUNCTION set_country_created() OWNER TO sqldb;

CREATE TRIGGER set_country_created_trigger BEFORE INSERT
    ON countries FOR EACH ROW EXECUTE PROCEDURE
    set_country_created();




ALTER DATABASE sqlmongo OWNER TO sqldb;
