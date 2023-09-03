"""create book table

Revision ID: d56aa514de5f
Revises: 
Create Date: 2023-09-03 17:16:43.762731

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd56aa514de5f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(
        """
        CREATE TABLE books (
            id bigserial NOT NULL,
            name character varying(50) NOT NULL,
            created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
            updated_at timestamp with time zone,
            CONSTRAINT book_pk PRIMARY KEY (id),
            CONSTRAINT idx_name_unique UNIQUE (name)
        );
        """
    )


def downgrade() -> None:
    op.execute("DROP TABLE books;")