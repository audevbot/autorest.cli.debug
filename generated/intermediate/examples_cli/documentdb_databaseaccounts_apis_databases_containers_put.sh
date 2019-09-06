# CosmosDBSqlContainerCreateUpdate
RESOURCE_GROUP="myresourcegroup"
DATABASE_ACCOUNT_NAME="mydatabaseaccount"
API_NAME="myapi"
DATABASE_NAME="mydatabase"
CONTAINER_NAME="mycontainer"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.DocumentDB/databaseAccounts/$DATABASE_ACCOUNT_NAME/apis/$API_NAME/databases/$DATABASE_NAME/containers/$CONTAINER_NAME?api-version=2015-04-08 --body '
{
  "properties": {
    "resource": {
      "id": "containerName",
      "indexingPolicy": {
        "indexingMode": "Consistent",
        "automatic": True,
        "includedPaths": [
          {
            "path": "/*",
            "indexes": [
              {
                "kind": "Range",
                "dataType": "String",
                "precision": "-1"
              },
              {
                "kind": "Range",
                "dataType": "Number",
                "precision": "-1"
              }
            ]
          }
        ],
        "excludedPaths": []
      },
      "partitionKey": {
        "paths": [
          "/AccountNumber"
        ],
        "kind": "Hash"
      },
      "defaultTtl": "100",
      "uniqueKeyPolicy": {
        "uniqueKeys": [
          {
            "paths": [
              "/testPath"
            ]
          }
        ]
      },
      "conflictResolutionPolicy": {
        "mode": "LastWriterWins",
        "conflictResolutionPath": "/path"
      }
    },
    "options": {}
  }
}
'