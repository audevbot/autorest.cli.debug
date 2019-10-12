# EventSubscriptions_ListRegionalBySubscriptionForTopicType
LOCATION_NAME="mylocation"
TOPIC_TYPE_NAME="mytopictype"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/providers/Microsoft.EventGrid/locations/$LOCATION_NAME/topicTypes/$TOPIC_TYPE_NAME/eventSubscriptions?api-version=2019-01-01