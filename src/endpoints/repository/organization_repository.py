from core.organizations import organization_entities

from tools.adt_sql.repository import SQLADTRepository

class OrganizationRepository(SQLADTRepository):
    adt = organization_entities.Organization
    table_name = "organizations"

