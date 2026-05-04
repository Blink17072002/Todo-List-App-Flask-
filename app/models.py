from datetime import datetime, timedelta, timezone
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db


class Todo(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    task: so.Mapped[str] = so.mapped_column(sa.String(250), index=True)
    is_completed: so.Mapped[bool] = so.mapped_column(sa.Boolean, default=False, index=True)
    timestamp: so.Mapped[datetime] = so.mapped_column(index=True, default=lambda: datetime.now(timezone.utc))

    def date_heading(self, now=None):
        now = now or datetime.now(timezone.utc)
        today = now.date()
        task_date = self.timestamp.date()

        if task_date == today:
            return 'Today'
        if task_date == today - timedelta(days=1):
            return 'Yesterday'
        return task_date.strftime('%b %d, %Y')

    def __repr__(self) -> str:
        return self.task