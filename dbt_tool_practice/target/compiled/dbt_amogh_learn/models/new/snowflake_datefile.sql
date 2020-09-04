


select *   from "SNOWFLAKE_SAMPLE_DATA"."TPCDS_SF100TCL"."DATE_DIM"
where d_date <=  current_date



  and d_date > (select max(d_date) from analytics.dbtt.snowflake_datefile)
