



select count(*) as validation_errors
from (

    select
        c_custkey

    from analytics.dbtt.snowflake_customer_purchases
    where c_custkey is not null
    group by c_custkey
    having count(*) > 1

) validation_errors

