# ApiManagementCreateSoapToRestApiUsingWsdlImport
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
APIS_NAME="myapis"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/apis/$APIS_NAME --api-version 2019-01-01 --is-full-object --properties '
{
  "properties": {
    "format": "wsdl-link",
    "value": "http://www.webservicex.net/CurrencyConvertor.asmx?WSDL",
    "path": "currency",
    "wsdlSelector": {
      "wsdlServiceName": "CurrencyConvertor",
      "wsdlEndpointName": "CurrencyConvertorSoap"
    }
  }
}
'