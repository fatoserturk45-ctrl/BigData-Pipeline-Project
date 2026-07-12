with orders as (
    select * from {{ ref('stg_olist_orders') }}
),

final as (
    select
        order_id,
        customer_id,
        order_status,
        order_purchase_at,
        delivered_at
    from orders
)

select * from final