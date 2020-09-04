

      create or replace transient table analytics.dbtt.my_second_dbt_model  as
      (-- Use the `ref` function to select from other models

select *
from analytics.dbtt.first_model
where id = 1
      );
    