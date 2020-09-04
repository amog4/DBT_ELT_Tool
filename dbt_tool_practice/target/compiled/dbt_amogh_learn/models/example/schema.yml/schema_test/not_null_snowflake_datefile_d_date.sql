



select count(*) as validation_errors
from analytics.dbtt.snowflake_datefile
where d_date is null

