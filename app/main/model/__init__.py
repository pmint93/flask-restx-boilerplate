from flask import current_app as app
import datetime

from app.main import db

__all__ = (
    'demo',
)

class BaseDocument(db.Document):
    meta = {
        'abstract': True,
        'strict': False
    }

    created_at          = db.DateTimeField(default=None)
    updated_at          = db.DateTimeField(default=None)

    def is_persisted(self):
        return bool(self.id and self.__class__.objects(id=self.id))

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.datetime.utcnow()
        self.updated_at = datetime.datetime.utcnow()
        return super(BaseDocument, self).save(*args, **kwargs)
