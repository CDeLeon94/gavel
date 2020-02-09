import gavel.crowd_bt as crowd_bt
from flask_sqlalchemy import SQLAlchemy
import gavel.settings as settings

class SerializableAlchemy(SQLAlchemy):
    def apply_driver_hacks(self, app, info, options):
        if not 'isolation_level' in options:
            # XXX is this slow? are there better ways?
            options['isolation_level'] = 'SERIALIZABLE'
        return super(SerializableAlchemy, self).apply_driver_hacks(app, info, options)
db = SerializableAlchemy()

from gavel.models.annotator import Annotator, ignore_table
from gavel.models.item import Item, view_table
from gavel.models.decision import Decision
from gavel.models.setting import Setting
from gavel.models.estimate import Estimate

from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql.expression import desc

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(settings.DB_URI)
Session = sessionmaker(bind=engine)
