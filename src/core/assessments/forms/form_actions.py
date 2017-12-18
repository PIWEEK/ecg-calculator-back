from endpoints.repository import form_repository

from . import form_entities


def list_forms(context, assessment_id):
    return form_repository.list_for_assessment(context, assessment_id)


def get_form(context, form_id):
    return form_repository.retrieve_by_id_full(context, form_id)

