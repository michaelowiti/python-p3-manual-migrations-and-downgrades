"""Renaming students to scholars

Revision ID: cab937e22468
Revises: 791279dd0760
Create Date: 2023-09-05 23:14:31.070271

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cab937e22468'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
   op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
