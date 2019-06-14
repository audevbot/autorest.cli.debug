# CosmosDBMongoCollectionCreateUpdate
RESOURCE_GROUP="myresourcegroup"
DATABASE_ACCOUNT_NAME="mydatabaseaccount"
APIS_NAME="myapis"
DATABASE_NAME="mydatabase"
COLLECTION_NAME="mycollection"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.DocumentDB/databaseAccounts/$DATABASE_ACCOUNT_NAME/apis/$APIS_NAME/databases/$DATABASE_NAME/collections/$COLLECTION_NAME --api-version 2015-04-08 --is-full-object --properties '
{
  "properties": {
    "resource": {
      "id": "testcoll",
      "indexes": [
        {
          "key": {
            "keys": [
              "testKey"
            ]
          },
          "options": {
            "expireAfterSeconds": "100",
            "unique": True
          }
        }
      ],
      "shardKey": {
        "testKey": "Hash"
      }
    },
    "options": {}
  }
}
'