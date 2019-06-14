# EventSubscriptions_ListRegionalByResourceGroupForTopicType
RESOURCE_GROUP="myresourcegroup"
LOCATION_NAME="mylocation"
TOPIC_TYPE_NAME="mytopictype"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.EventGrid/locations/$LOCATION_NAME/topicTypes/$TOPIC_TYPE_NAME/eventSubscriptions --api-version 2019-01-01