from endpoints.repository import topic_repository

from . import topic_entities


def list_topics(context, assessment_id):
    return topic_repository.list_for_assessment(context, assessment_id)


def get_topic(context, topic_id):
    return topic_repository.retrieve_by_id_full(context, topic_id)

