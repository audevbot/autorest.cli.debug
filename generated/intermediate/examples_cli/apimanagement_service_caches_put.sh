# ApiManagementCreateCache
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
CACHE_NAME="mycache"
REDIS_NAME="myredis"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/caches/$CACHE_NAME --api-version 2019-01-01 --is-full-object --properties '
{
  "properties": {
    "connectionString": "contoso5.redis.cache.windows.net,ssl=true,password=...",
    "description": "Redis cache instances in West India",
    "resourceId": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Cache/Redis/" + REDIS_NAME + ""
  }
}
'