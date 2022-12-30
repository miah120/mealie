"""add recipe_scale to shopping list item ref

Revision ID: 167eb69066ad
Revises: 1923519381ad
Create Date: 2022-11-22 03:42:45.494567

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "167eb69066ad"
down_revision = "1923519381ad"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("shopping_list_item_recipe_reference", sa.Column("recipe_scale", sa.Float(), nullable=True))
    op.execute("UPDATE shopping_list_item_recipe_reference SET recipe_scale = 1")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("shopping_list_item_recipe_reference", "recipe_scale")
    # ### end Alembic commands ###
