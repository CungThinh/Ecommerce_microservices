"""Initial migration

Revision ID: f321542f71d9
Revises: 
Create Date: 2025-02-15 09:28:27.564622

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f321542f71d9'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('addresses',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('street', sa.String(length=100), nullable=False),
    sa.Column('ward', sa.String(length=50), nullable=False),
    sa.Column('district', sa.String(length=50), nullable=False),
    sa.Column('city', sa.Enum('HANOI', 'HOCHIMINH', 'DANANG', name='city'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('profiles',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=True),
    sa.Column('full_name', sa.String(length=100), nullable=False),
    sa.Column('phone', sa.String(length=15), nullable=False),
    sa.Column('address_id', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['address_id'], ['addresses.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_profiles_user_id'), 'profiles', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_profiles_user_id'), table_name='profiles')
    op.drop_table('profiles')
    op.drop_table('addresses')
    # ### end Alembic commands ###
