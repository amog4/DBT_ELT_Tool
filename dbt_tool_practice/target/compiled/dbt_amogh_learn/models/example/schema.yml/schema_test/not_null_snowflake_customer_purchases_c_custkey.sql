



select count(*) as validation_errors
from analytics.dbtt.snowflake_customer_purchases
where c_custkey is null

