# Create or update a simple gallery image.
RESOURCE_GROUP="myresourcegroup"
GALLERY_NAME="mygallery"
IMAGE_NAME="myimage"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Compute/galleries/$GALLERY_NAME/images/$IMAGE_NAME?api-version=2019-03-01 --body '
{
  "location": "West US",
  "properties": {
    "osType": "Windows",
    "osState": "Generalized",
    "identifier": {
      "publisher": "myPublisherName",
      "offer": "myOfferName",
      "sku": "mySkuName"
    }
  }
}
'