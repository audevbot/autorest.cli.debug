# ApiManagementCreateApiDiagnostic
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
API_NAME="myapi"
DIAGNOSTIC_NAME="mydiagnostic"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/apis/$API_NAME/diagnostics/$DIAGNOSTIC_NAME?api-version=2019-01-01 --body '
{
  "properties": {
    "alwaysLog": "allErrors",
    "loggerId": "/loggers/applicationinsights",
    "sampling": {
      "samplingType": "fixed",
      "percentage": "50"
    },
    "frontend": {
      "request": {
        "headers": [
          "Content-type"
        ],
        "body": {
          "bytes": "512"
        }
      },
      "response": {
        "headers": [
          "Content-type"
        ],
        "body": {
          "bytes": "512"
        }
      }
    },
    "backend": {
      "request": {
        "headers": [
          "Content-type"
        ],
        "body": {
          "bytes": "512"
        }
      },
      "response": {
        "headers": [
          "Content-type"
        ],
        "body": {
          "bytes": "512"
        }
      }
    }
  }
}
'