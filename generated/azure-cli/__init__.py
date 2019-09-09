# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core import AzCommandsLoader

from azext_vmwarecs._help import helps  # pylint: disable=unused-import


class VMwareCloudSimpleCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType
        from azext_vmwarecs._client_factory import cf_vmwarecs
        vmwarecs_custom = CliCommandType(
            operations_tmpl='azext_vmwarecs.custom#{}',
            client_factory=cf_vmwarecs)
        super( VMwareCloudSimpleCommandsLoader, self).__init__(cli_ctx=cli_ctx,
                                                       custom_command_type=vmwarecs_custom)

    def load_command_table(self, args):
        from azext_vmwarecs.commands import load_command_table
        load_command_table(self, args)
        return self.command_table

    def load_arguments(self, command):
        from azext_vmwarecs._params import load_arguments
        load_arguments(self, command)


COMMAND_LOADER_CLS =  VMwareCloudSimpleCommandsLoader