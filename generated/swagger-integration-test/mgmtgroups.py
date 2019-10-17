# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------

import unittest

import azure.mgmt.xxxx
from devtools_testutils import AzureMgmtTestCase, ResourceGroupPreparer

class MgmtXxxTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtXxxTest, self).setUp()
        self.mgmt_client = self.create_mgmt_client(
            azure.mgmt.xxxx.XxxMgmtClient
        )
    
    def test_cdn(self):
        account_name = self.get_resource_name('pyarmcdn')

        output = self.mgmt_client.check_name_availability(
            name=account_name
        )
        self.assertTrue(output.name_available)


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()