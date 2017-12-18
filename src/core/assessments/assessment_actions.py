from endpoints.repository import assessment_repository

from . import assessment_entities


def list_assessments(context):
    return assessment_repository.list(context)


def get_assessment(context, assessment_id):
    return assessment_repository.retrieve_by_id(context, assessment_id)

