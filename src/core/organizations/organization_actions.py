from endpoints.repository import organization_repository

from . import organization_entities

def new_organization(context, organization_for_create):
    organization = organization_entities.Organization(
        name = organization_for_create.name,
        address = "",
        state = "",
        country = "",
        sector = "",
        web = "",
        description = "",
    )

    return organization_repository.create(context, organization)


def list_organizations(context):
    return organization_repository.list(context)


def get_organization(context, organization_id):
    return organization_repository.retrieve_by_id(context, organization_id)


def edit_organization(context, organization, organization_for_update):
    organization.edit(organization_for_update)
    return organization_repository.update(organization)

