# Copyright 2016 Brocade Networks, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#

"""ml2_brcd_contract

Revision ID: 4fadb44a1e2d
Revises: 30d703af31fb
Create Date: 2016-02-09 15:30:27.535472

"""

from neutron.db.migration import cli

# revision identifiers, used by Alembic.
revision = '4fadb44a1e2d'
down_revision = 'kilo'
branch_labels = None
depends_on = None
branch_labels = (cli.CONTRACT_BRANCH,)


def upgrade():
    pass
