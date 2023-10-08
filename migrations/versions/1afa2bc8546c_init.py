"""'Init'

Revision ID: 1afa2bc8546c
Revises: 
Create Date: 2023-10-08 21:21:27.113449

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1afa2bc8546c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contacts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('surname', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('phone_number', sa.String(length=20), nullable=True),
    sa.Column('birthday', sa.Date(), nullable=True),
    sa.Column('additional_data', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contacts')
    # ### end Alembic commands ###
