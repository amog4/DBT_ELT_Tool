

select c.c_custkey,
        c.c_name,
        c.c_nationkey as nationkey,
        sum(o.o_totalprice) as total_orderprice
from "SNOWFLAKE_SAMPLE_DATA"."TPCH_SF001"."CUSTOMER" as c
left join
(select * from "SNOWFLAKE_SAMPLE_DATA"."TPCH_SF001"."ORDERS") as o
on (c.c_custkey = o.o_custkey)
        group by
            c.c_custkey,
            c.c_name,
            c.c_nationkey