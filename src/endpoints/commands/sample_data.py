from tools.adt_sql.database import db_context

from core.organizations import organization_entities, organization_actions
from endpoints.repository import db, organization_repository


def sample_data():
    create_organizations()


def create_organizations():
    with db_context(db) as context:

        organization_repository.create(context, organization_entities.Organization(
            name = "Primera organización",
            address = "mikasa 1",
            state = "mipueblo 1",
            country = "mipais 1",
            sector = "misector 1",
            web = "www.miweb1.com",
            description = "Esto es una descripción 1",
        ))

        organization_repository.create(context, organization_entities.Organization(
            name = "Segunda organización",
            address = "mikasa 2",
            state = "mipueblo 2",
            country = "mipais 2",
            sector = "misector 2",
            web = "www.miweb2.com",
            description = "Esto es una descripción 2",
        ))

        organization_repository.create(context, organization_entities.Organization(
            name = "Tercera organización",
            address = "mikasa 3",
            state = "mipueblo 3",
            country = "mipais 3",
            sector = "misector 3",
            web = "www.miweb3.com",
            description = "Esto es una descripción 3",
        ))

