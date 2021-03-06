"""Add multiple organization support and add seed organization

Revision ID: b19224a5c1dd
Revises: a1ed2f75cb13
Create Date: 2016-03-18 20:41:33.024198

"""

# revision identifiers, used by Alembic.
revision = 'b19224a5c1dd'
down_revision = 'a1ed2f75cb13'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    ### commands auto generated by Alembic - please adjust! ###
    org_table = op.create_table('organization',
                                sa.Column('id', sa.Integer(), nullable=False),
                                sa.Column('name', sa.String(length=80), nullable=True),
                                sa.Column('description', sa.String(length=255), nullable=True),
                                sa.Column('parent_id', sa.Integer(), nullable=True),
                                sa.ForeignKeyConstraint(['parent_id'], ['organization.id'], ),
                                sa.PrimaryKeyConstraint('id'),
                                sa.UniqueConstraint('name')
                                )
    op.bulk_insert(org_table, [
        {'id': 1, 'name': 'betterlife', 'description': u'Betterlife'},
    ])
    op.add_column('user', sa.Column('organization_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'user', 'organization', ['organization_id'], ['id'])
    op.add_column('customer', sa.Column('organization_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'customer', 'organization', ['organization_id'], ['id'])
    op.add_column('expense', sa.Column('organization_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'expense', 'organization', ['organization_id'], ['id'])
    op.add_column('incoming', sa.Column('organization_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'incoming', 'organization', ['organization_id'], ['id'])
    op.add_column('inventory_transaction', sa.Column('organization_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'inventory_transaction', 'organization', ['organization_id'], ['id'])
    op.add_column('preference', sa.Column('organization_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'preference', 'organization', ['organization_id'], ['id'])
    op.add_column('product', sa.Column('organization_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'product', 'organization', ['organization_id'], ['id'])
    op.add_column('product_category', sa.Column('organization_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'product_category', 'organization', ['organization_id'], ['id'])
    op.add_column('purchase_order', sa.Column('organization_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'purchase_order', 'organization', ['organization_id'], ['id'])
    op.add_column('receiving', sa.Column('organization_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'receiving', 'organization', ['organization_id'], ['id'])
    op.add_column('sales_order', sa.Column('organization_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'sales_order', 'organization', ['organization_id'], ['id'])
    op.add_column('shipping', sa.Column('organization_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'shipping', 'organization', ['organization_id'], ['id'])
    op.add_column('supplier', sa.Column('organization_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'supplier', 'organization', ['organization_id'], ['id'])
    from sqlalchemy.sql import text
    op.get_bind().execute(text("UPDATE \"user\" SET organization_id = 1"))
    op.get_bind().execute(text('UPDATE customer SET organization_id = 1;'))
    op.get_bind().execute(text('UPDATE expense SET organization_id = 1;'))
    op.get_bind().execute(text('UPDATE incoming SET organization_id = 1;'))
    op.get_bind().execute(text('UPDATE inventory_transaction SET organization_id = 1;'))
    op.get_bind().execute(text('UPDATE preference SET organization_id = 1;'))
    op.get_bind().execute(text('UPDATE product SET organization_id = 1;'))
    op.get_bind().execute(text('UPDATE product_category SET organization_id = 1;'))
    op.get_bind().execute(text('UPDATE purchase_order SET organization_id = 1;'))
    op.get_bind().execute(text('UPDATE receiving SET organization_id = 1;'))
    op.get_bind().execute(text('UPDATE sales_order SET organization_id = 1;'))
    op.get_bind().execute(text('UPDATE shipping SET organization_id = 1;'))
    op.get_bind().execute(text('UPDATE supplier SET organization_id = 1;'))
    op.get_bind().execute(text("ALTER SEQUENCE organization_id_seq RESTART WITH 2;"))

    role_table = sa.table('role',
                          sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                          sa.Column('name', sa.String(length=80), nullable=True),
                          sa.Column('description', sa.String(length=255), nullable=True),
                          )
    res = op.get_bind().execute('SELECT max(id)+1 FROM role')
    results = res.fetchall()
    rm = 49
    for r in results:
        rm = r[0]
    op.bulk_insert(role_table, [
        {'id': rm, 'name': 'organization_view', 'description': 'View customers'},
        {'id': rm + 1, 'name': 'organization_create', 'description': 'Create customers'},
        {'id': rm + 2, 'name': 'organization_edit', 'description': 'Edit customers'},
        {'id': rm + 3, 'name': 'organization_delete', 'description': 'Delete customers'},
    ], multiinsert=False)
    op.get_bind().execute(text("ALTER SEQUENCE role_id_seq RESTART WITH " + str(rm + 4) + ";"))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    from sqlalchemy.sql import text
    op.get_bind().execute(text("DELETE FROM role WHERE name IN ('organization_view', 'organization_create', 'organization_edit','organization_delete')"))
    op.drop_constraint('supplier_organization_id_fkey', 'supplier', type_='foreignkey')
    op.drop_column('supplier', 'organization_id')
    op.drop_constraint('shipping_organization_id_fkey', 'shipping', type_='foreignkey')
    op.drop_column('shipping', 'organization_id')
    op.drop_constraint('sales_order_organization_id_fkey', 'sales_order', type_='foreignkey')
    op.drop_column('sales_order', 'organization_id')
    op.drop_constraint('receiving_organization_id_fkey', 'receiving', type_='foreignkey')
    op.drop_column('receiving', 'organization_id')
    op.drop_constraint('purchase_order_organization_id_fkey', 'purchase_order', type_='foreignkey')
    op.drop_column('purchase_order', 'organization_id')
    op.drop_constraint('product_category_organization_id_fkey', 'product_category', type_='foreignkey')
    op.drop_column('product_category', 'organization_id')
    op.drop_constraint('product_organization_id_fkey', 'product', type_='foreignkey')
    op.drop_column('product', 'organization_id')
    op.drop_constraint('preference_organization_id_fkey', 'preference', type_='foreignkey')
    op.drop_column('preference', 'organization_id')
    op.drop_constraint('inventory_transaction_organization_id_fkey', 'inventory_transaction', type_='foreignkey')
    op.drop_column('inventory_transaction', 'organization_id')
    op.drop_constraint('incoming_organization_id_fkey', 'incoming', type_='foreignkey')
    op.drop_column('incoming', 'organization_id')
    op.drop_constraint('expense_organization_id_fkey', 'expense', type_='foreignkey')
    op.drop_column('expense', 'organization_id')
    op.drop_constraint('customer_organization_id_fkey', 'customer', type_='foreignkey')
    op.drop_column('customer', 'organization_id')
    op.drop_constraint('user_organization_id_fkey', 'user', type_='foreignkey')
    op.drop_column('user', 'organization_id')
    op.drop_table('organization')
    ### end Alembic commands ###
