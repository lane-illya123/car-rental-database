"""updated relationships in all models v2

Revision ID: ace69984ec3f
Revises: e3b1041a3b5e
Create Date: 2024-08-25 21:22:14.251771

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ace69984ec3f'
down_revision = 'e3b1041a3b5e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cars')
    op.drop_table('customers')
    op.drop_table('reviews')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reviews',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('description', sa.VARCHAR(), nullable=True),
    sa.Column('created_at', sa.DATETIME(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('customers',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('first_name', sa.VARCHAR(), nullable=True),
    sa.Column('last_name', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cars',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('year', sa.VARCHAR(), nullable=True),
    sa.Column('make', sa.VARCHAR(), nullable=True),
    sa.Column('model', sa.VARCHAR(), nullable=True),
    sa.Column('review_id', sa.INTEGER(), nullable=True),
    sa.Column('customer_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], name='fk_cars_customer_id_customers'),
    sa.ForeignKeyConstraint(['review_id'], ['reviews.id'], name='fk_cars_review_id_reviews'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
