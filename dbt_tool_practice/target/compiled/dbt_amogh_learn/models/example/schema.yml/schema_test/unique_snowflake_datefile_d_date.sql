



select count(*) as validation_errors
from (

    select
        d_date

    from analytics.dbtt.snowflake_datefile
    where d_date is not null
    group by d_date
    having count(*) > 1

) validation_errors

