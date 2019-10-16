# CosmosDBDatabaseAccountCheckNameExists
DATABASE_ACCOUNT_NAME_NAME="mydatabaseaccount"

az rest --method head --uri /providers/Microsoft.DocumentDB/databaseAccountNames/$DATABASE_ACCOUNT_NAME_NAME?api-version=2015-04-08