from core.organizations.organization_entities import Organization
from repository.organization_repository import OrganizationRepository
from tools.adt_sql.database import db_context

from repository import db

from sqlalchemy.sql import select

def test_create():
    repo = OrganizationRepository(db)
    db.create_all_tables()

    with db_context(db) as context:
        organization = Organization(
            name = "test 1",
            address = "address 1"
        )
        repo.create(context, organization)

    with db_context(db) as context:
        retrieved_org = db.retrieve_single_adt(
            context,
            Organization,
            select([db.organizations])
                .where(db.organizations.c.id == organization.id)
        )

    assert retrieved_org.id == organization.id
    assert retrieved_org.name == organization.name
    assert retrieved_org.address == organization.address

