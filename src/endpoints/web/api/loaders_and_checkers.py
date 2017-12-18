from core.assessments import assessment_entities, assessment_actions
from core.assessments.forms import form_entities, form_actions
from core.organizations import organization_entities, organization_actions

from endpoints.web.api import exceptions


def load_assessment(context, assessment_id):
    assessment = assessment_actions.get_assessment(context, assessment_id)
    if not assessment:
        raise exceptions.NotFound("Cannot find the assessment {}".format(assessment_id))
    return assessment


def load_form(context, assessment_id, form_id):
    form = form_actions.get_form(context, form_id)
    if not form:
        raise exceptions.NotFound("Cannot find the form {}".format(form_id))
    if form.assessment_id != int(assessment_id):
        raise exceptions.NotFound("Invalid assessment {} for the form {}".format(assessment_id, form_id))
    return form


def load_organization(context, organization_id):
    organization = organization_actions.get_organization(context, organization_id)
    if not organization:
        raise exceptions.NotFound("Cannot find the organization {}".format(organization_id))
    return organization

