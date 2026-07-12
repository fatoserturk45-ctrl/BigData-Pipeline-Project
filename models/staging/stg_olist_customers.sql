with source_data as (
    select * from {{ source('bronze_olist', 'raw_customers') }}
),

cleaned_customers as (
    select
        cast(customer_id as string) as customer_id,
        cast(customer_unique_id as string) as customer_unique_id,
        cast(customer_zip_code_prefix as string) as zip_code,
        lower(trim(customer_city)) as city,
        upper(trim(customer_state)) as state
    from source_data
)

select * from cleaned_customers