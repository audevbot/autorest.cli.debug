# RegionsListBySku
SKU_NAME="mysku"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/providers/Microsoft.ServiceBus/sku/$SKU_NAME/regions?api-version=2017-04-01