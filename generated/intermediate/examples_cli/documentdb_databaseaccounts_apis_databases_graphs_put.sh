# CosmosDBGremlinGraphCreateUpdate
RESOURCE_GROUP="myresourcegroup"
DATABASE_ACCOUNT_NAME="mydatabaseaccount"
API_NAME="myapi"
DATABASE_NAME="mydatabase"
GRAPH_NAME="mygraph"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.DocumentDB/databaseAccounts/$DATABASE_ACCOUNT_NAME/apis/$API_NAME/databases/$DATABASE_NAME/graphs/$GRAPH_NAME?api-version=2015-04-08 --body '
{
  "properties": {
    "resource": {
      "id": "graphName",
      "indexingPolicy": {
        "indexingMode": "Consistent",
        "automatic": True,
        "includedPaths": [
          {
            "path": "/*",
            "indexes": [
              {
                "kind": "Range",
                "data_type": "String",
                "precision": "-1"
              },
              {
                "kind": "Range",
                "data_type": "Number",
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