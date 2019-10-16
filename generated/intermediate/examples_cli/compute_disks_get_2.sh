# List all managed disks in a subscription.

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/providers/Microsoft.Compute/disks?api-version=2018-09-30