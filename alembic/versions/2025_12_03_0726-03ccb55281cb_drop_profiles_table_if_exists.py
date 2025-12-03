"""drop profiles table if exists

Revision ID: 03ccb55281cb
Revises: 368df87790b4
Create Date: 2025-12-03 07:26:23.221466

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "03ccb55281cb"
down_revision: Union[str, Sequence[str], None] = "368df87790b4"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Удаляем таблицу, только если она существует
    op.execute("DROP TABLE IF EXISTS profiles")


def downgrade() -> None:
    """Downgrade schema."""
    pass
