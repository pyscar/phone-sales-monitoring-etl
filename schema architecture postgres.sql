-- creating schema ,its professional aproach instead of keeping everything in the public.
CREATE SCHEMA IF NOT EXISTS analytics;

-- verfiying that sales is created after the db connection to vs
SELECT *
FROM analytics.sales
LIMIT 10;

SELECT COUNT(*)
FROM analytics.sales;




-- reserting database
DROP TABLE IF EXISTS analytics.audit_reconciliation CASCADE;

DROP TABLE IF EXISTS analytics.sales CASCADE;

DROP TABLE IF EXISTS analytics.master_loans CASCADE;

DROP TABLE IF EXISTS analytics.sales_reconciliation CASCADE;

DROP TABLE IF EXISTS analytics.sales_not_in_loans CASCADE;

DROP TABLE IF EXISTS analytics.loans_not_in_sales CASCADE;


SELECT table_name
FROM information_schema.tables
WHERE table_schema='analytics'
ORDER BY table_name;
------------------

SELECT table_name
FROM information_schema.tables
WHERE table_schema='analytics';

SELECT *
FROM analytics.audit_reconciliation;


