# TopicTypes_ListEventTypes
TOPIC_TYPE_NAME="mytopictype"

az rest --method get --uri /providers/Microsoft.EventGrid/topicTypes/$TOPIC_TYPE_NAME/eventTypes?api-version=2019-01-01