from sqlalchemy.sql import select


class SQLADTRepository:

    adt = None
    table_name = None

    def __init__(self, db):
        self.db = db
        self.db.add_adt_table(self.adt, self.table_name)

    def create(self, context, instance):
        return self.db.insert_adt(
            context,
            getattr(self.db, self.table_name),
            instance
        )

    def list(self, context, order_by = None):
        return self.db.retrieve_adts(
            context,
            self.adt,
            select([getattr(self.db, self.table_name)])
                .order_by(order_by)
        )

    def retrieve_by_id(self, context, instance_id):
        db_table = getattr(self.db, self.table_name)
        return self.db.retrieve_single_adt(
            context,
            self.adt,
            select([db_table])
                .where(db_table.c.id == instance_id)
        )

    def update(self, context, instance):
        return self.db.update_adt(
            context,
            getattr(self.db, self.table_name),
            instance
        )

