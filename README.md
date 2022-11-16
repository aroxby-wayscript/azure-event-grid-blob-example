# azure-event-grid-blob-example
Example service that receives blob events from event grid using cloud events

```
SUBSCRIPTION_NAME=azure-event-grid-blob-example
ENDPOINT='[YOUR-DEPLOYMENT_HERE]/hook?secret=fictional-spoon-crispy-waffle'
STORAGE_ACCOUNT_NAME=[YOUR-STORAGE-ACCOUNT-NAME]
RESOURCE_GROUP=[YOUR-RESOURCE-GROUP]

STORAGE_ACCOUNT_ID=$(
    az storage account show --name $STORAGE_ACCOUNT_NAME --resource-group $RESOURCE_GROUP --query id --output tsv
)


az eventgrid event-subscription create \
    --source-resource-id $STORAGE_ACCOUNT_ID \
    --name $SUBSCRIPTION_NAME \
    --endpoint $ENDPOINT \
    --event-delivery-schema cloudeventschemav1_0
```
