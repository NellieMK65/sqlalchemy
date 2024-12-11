"""add phone to users table

Revision ID: 49afaaa5158b
Revises: d2b94a2af8ce
Create Date: 2024-12-11 10:23:22.690025

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '49afaaa5158b'
down_revision: Union[str, None] = 'd2b94a2af8ce'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone', sa.Integer(), nullable=True))
    op.create_unique_constraint(None, 'users', ['phone'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'phone')
    # ### end Alembic commands ###
