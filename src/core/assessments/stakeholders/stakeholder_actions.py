from endpoints.repository import stakeholder_repository

from . import stakeholder_entities


def list_stakeholders(context, assessment_id):
    return stakeholder_repository.list_for_assessment(context, assessment_id)


def get_stakeholder(context, stakeholder_id):
    return stakeholder_repository.retrieve_by_id(context, stakeholder_id)

