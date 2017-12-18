from anillo.http import responses

from core.organizations import organization_entities, organization_validators, organization_actions

from tools.adt.converter import to_plain, from_plain
from tools.adt_sql.database import db_context

from endpoints.repository import db

from endpoints.web.handler import BaseHandler
# from web.decorators import login_required

from endpoints.web.api.loaders_and_checkers import *
from endpoints.web.api import exceptions


class OrganizationsList(BaseHandler):
    def get(self, request):
        with db_context(db) as context:

            organizations = organization_actions.list_organizations(context)

            return responses.Ok([
                to_plain(organization)
                for organization in organizations
            ])

    # @login_required
    def post(self, request):
        with db_context(db) as context:

            validator = organization_validators.OrganizationForCreateValidator(request.body)
            if validator.is_valid():
                organization = organization_actions.new_organization(
                    context,
                    organization_entities.OrganizationForCreate(**validator.cleaned_data)
                )
                return responses.Ok(to_plain(organization))
            else:
                return responses.BadRequest(validator.errors)


class OrganizationDetail(BaseHandler):
    def get(self, request, organization_id):
        with db_context(db) as context:
            organization = load_organization(context, organization_id)
            return responses.Ok(to_plain(organization))

    # @login_required
    def patch(self, request, organization_id):
        with db_context(db) as context:
            organization = load_organization(context, organization_id)
            # check_user_is_owner_of_organization(context, request.user, organization)

            validator = organization_validators.OrganizationForUpdateValidator(request.body)
            if validator.is_valid():
                organization = organization_actions.edit_organization(
                    context,
                    organization,
                    organization_entities.OrganizationForUpdate(**validator.cleaned_data)
                )
                return responses.Ok(to_plain(organization))
            return responses.BadRequest(validator.errors)

    def delete(self, request):
        raise NotImplementedError("TODO")

