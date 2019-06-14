# EventSubscriptions_ListGlobalBySubscriptionForTopicType
TOPIC_TYPE_NAME="mytopictype"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/providers/Microsoft.EventGrid/topicTypes/$TOPIC_TYPE_NAME/eventSubscriptions --api-version 2019-01-01