# CheckNameAvailability

az rest --method post --uri /providers/Microsoft.Network/checkFrontDoorNameAvailability?api-version=2019-04-01 --body '
{
  "name": "sampleName",
  "type": "Microsoft.Network/frontDoors"
}
'