"""Add external_id to product, sales_order and supplier for 3rd party system integration

Revision ID: 38571f2c12fc
Revises: 428a1c2e88b2
Create Date: 2015-09-05 18:56:58.031184

"""

# revision identifiers, used by Alembic.
revision = '38571f2c12fc'
down_revision = '428a1c2e88b2'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('external_id', sa.String(), nullable=True, unique=True))
    op.add_column('sales_order', sa.Column('external_id', sa.String(), nullable=True, unique=True))
    op.add_column('supplier', sa.Column('external_id', sa.String(), nullable=True, unique=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('supplier', 'external_id')
    op.drop_column('sales_order', 'external_id')
    op.drop_column('product', 'external_id')
    ### end Alembic commands ###