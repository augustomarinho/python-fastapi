"""Update book table to adding author's name and isbn

Revision ID: 9611f57822a8
Revises: d56aa514de5f
Create Date: 2023-09-03 19:40:12.899254

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9611f57822a8'
down_revision = 'd56aa514de5f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Add the 'author' column
    op.execute("ALTER TABLE books ADD COLUMN author VARCHAR(255);")

    # Add the 'isbn' column
    op.execute("ALTER TABLE books ADD COLUMN isbn VARCHAR(13);")


def downgrade() -> None:
    # Remove the 'isbn' column using native SQL for PostgreSQL
    op.execute(f'ALTER TABLE books DROP COLUMN isbn;')

    # Remove the 'author' column using native SQL for PostgreSQL
    op.execute(f'ALTER TABLE books DROP COLUMN author;')
