# ApiManagementCreateApiOperation
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
API_NAME="myapi"
OPERATION_NAME="myoperation"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/apis/$API_NAME/operations/$OPERATION_NAME?api-version=2019-01-01 --body '
{
  "properties": {
    "displayName": "createUser2",
    "method": "POST",
    "urlTemplate": "/user1",
    "templateParameters": [],
    "description": "This can only be done by the logged in user.",
    "request": {
      "description": "Created user object",
      "queryParameters": [],
      "headers": [],
      "representations": [
        {
          "contentType": "application/json",
          "schemaId": "592f6c1d0af5840ca8897f0c",
          "typeName": "User"
        }
      ]
    },
    "responses": [
      {
        "statusCode": "200",
        "description": "successful operation",
        "representations": [
          {
            "contentType": "application/xml"
          },
          {
            "contentType": "application/json"
          }
        ],
        "headers": []
      }
    ]
  }
}
'