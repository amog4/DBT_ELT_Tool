




with all_values as (

    select distinct
        id as value_field

    from analytics.dbtt.first_model

),

validation_errors as (

    select
        value_field

    from all_values
    where value_field not in (
        1,2
    )
)

select count(*) as validation_errors
from validation_errors

