# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core import AzCommandsLoader

from azext_vmwarecs operation-result._help import helps  # pylint: disable=unused-import


class VMwareCloudSimpleCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType
        from azext_vmwarecs operation-result._client_factory import cf_vmwarecs operation-result
        vmwarecs operation-result_custom = CliCommandType(
            operations_tmpl='azext_vmwarecs operation-result.custom#{}',
            client_factory=cf_vmwarecs operation-result)
        super( VMwareCloudSimpleCommandsLoader, self).__init__(cli_ctx=cli_ctx,
                                                       custom_command_type=vmwarecs operation-result_custom)

    def load_command_table(self, args):
        from azext_vmwarecs operation-result.commands import load_command_table
        load_command_table(self, args)
        return self.command_table

    def load_arguments(self, command):
        from azext_vmwarecs operation-result._params import load_arguments
        load_arguments(self, command)


COMMAND_LOADER_CLS =  VMwareCloudSimpleCommandsLoader