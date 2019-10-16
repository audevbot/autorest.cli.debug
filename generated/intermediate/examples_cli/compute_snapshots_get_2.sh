# List all snapshots in a subscription.

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/providers/Microsoft.Compute/snapshots?api-version=2018-09-30