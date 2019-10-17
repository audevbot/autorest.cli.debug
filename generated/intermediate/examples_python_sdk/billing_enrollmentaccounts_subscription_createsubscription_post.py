# createSubscription
#
# This script expects that the following environment vars are set:
#
# AZURE_TENANT: your Azure Active Directory tenant id or domain
# AZURE_CLIENT_ID: your Azure Active Directory Application Client ID
# AZURE_SECRET: your Azure Active Directory Application Secret
# AZURE_SUBSCRIPTION_ID: your Azure Subscription Id

import os
import traceback
from azure.common.credentials import ServicePrincipalCredentials
from msrestazure.azure_exceptions import CloudError
from msrestazure.azure_configuration import AzureConfiguration
from msrest.service_client import ServiceClient
from msrest.polling import LROPoller
from msrestazure.polling.arm_polling import ARMPolling
from msrest.pipeline import ClientRawResponse
from azure.mgmt.subscriptions import Subscription
import uuid

SUBSCRIPTION_ID = os.environ['AZURE_SUBSCRIPTION_ID']
ENROLLMENT_ACCOUNT_NAME = "myenrollmentaccount"

BODY = {
  "offer_type": "MS-AZR-0017P",
  "display_name": "Test Ea Azure Sub",
  "owners": [
    {
      "object_id": "973034ff-acb7-409c-b731-e789672c7b31"
    },
    {
      "object_id": "67439a9e-8519-4016-a630-f5f805eba567"
    }
  ],
  "additional_parameters": {
    "custom_data": {
      "key1": "value1",
      "key2": True
    }
  }
}

def get_credentials():
    credentials = ServicePrincipalCredentials(
        client_id=os.environ['AZURE_CLIENT_ID'],
        secret=os.environ['AZURE_SECRET'],
        tenant=os.environ['AZURE_TENANT']
    )
    return credentials


def run_example():
    credentials = get_credentials()
    mgmt_client = Subscription(credentials, os.environ['AZURE_SUBSCRIPTION_ID'])
    response = mgmt_client.subscription_factory.create_subscription_in_enrollment_account(ENROLLMENT_ACCOUNT_NAME, , BODY)
    if isinstance(response, LROPoller):
        while not response.done():
            response.wait(timeout=30)
        response = response.result()
    print(str(response))


if __name__ == "__main__":
    run_example()