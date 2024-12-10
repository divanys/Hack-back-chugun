"""update courses table

Revision ID: 856ef56a09b2
Revises: c00401af4d6e
Create Date: 2024-12-10 22:22:43.771354

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "856ef56a09b2"
down_revision: Union[str, None] = "c00401af4d6e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("Courses", sa.Column("description_course", sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("Courses", "description_course")
    # ### end Alembic commands ###
