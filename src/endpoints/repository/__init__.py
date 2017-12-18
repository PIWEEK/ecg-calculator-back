from tools.adt_sql.database import SQLADTDatabase
from .organization_repository import OrganizationRepository

import settings

db = SQLADTDatabase(settings.DB_OPTIONS)

organization_repository = OrganizationRepository(db)

db.create_all_tables()
