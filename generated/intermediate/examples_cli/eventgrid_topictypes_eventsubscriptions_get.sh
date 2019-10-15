# EventSubscriptions_ListGlobalBySubscriptionForTopicType
TOPIC_TYPE_NAME="mytopictype"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/providers/Microsoft.EventGrid/topicTypes/$TOPIC_TYPE_NAME/eventSubscriptions?api-version=2019-01-01