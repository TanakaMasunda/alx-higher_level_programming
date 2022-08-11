-- lists cities of California that can be found in database hbtn_0d_usa.
-- states table contain only one record where name = California (different id)
-- Result sorted in ascending order by cities.id,not allowed 2 use JOIN keyword
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
