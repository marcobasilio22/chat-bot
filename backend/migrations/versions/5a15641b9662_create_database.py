"""create_database

Revision ID: 5a15641b9662
Revises: 
Create Date: 2024-10-02 10:57:33.675366

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5a15641b9662'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'contacts',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('number', sa.String(20), nullable=False),
        sa.Column('creation_date', sa.DateTime, server_default=sa.func.now())
    )

    # Criação da tabela conversations
    op.create_table(
        'conversations',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('customer_id', sa.Integer, nullable=False),
        sa.Column('message', sa.Text, nullable=False),
        sa.Column('type_message', sa.String(50), nullable=False),
        sa.Column('date_message', sa.DateTime, server_default=sa.func.now())
    )


def downgrade() -> None:
    op.drop_table('conversations')
    op.drop_table('contacts')
