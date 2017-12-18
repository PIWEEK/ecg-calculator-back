from core.organizations import organization_entities, organization_actions

from endpoints.web.api import exceptions


def load_organization(context, organization_id):
    organization = organization_actions.get_organization(context, organization_id)
    if not organization:
        raise exceptions.NotFound("Cannot find the organization {}".format(organization_id))
    return organization

