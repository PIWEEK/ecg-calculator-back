from anillo.http import responses

from core.assessments.topics import topic_entities, topic_actions

from tools.adt.converter import to_plain
from tools.adt_sql.database import db_context

from endpoints.repository import db

from endpoints.web.handler import BaseHandler

from endpoints.web.api.loaders_and_checkers import load_topic
from endpoints.web.api import exceptions


class AssessmentTopicsList(BaseHandler):
    def get(self, request, assessment_id):
        with db_context(db) as context:

            topics = topic_actions.list_topics(context, assessment_id)

            return responses.Ok([
                to_plain(topic)
                for topic in topics
            ])


class AssessmentTopicDetail(BaseHandler):
    def get(self, request, assessment_id, topic_id):
        with db_context(db) as context:
            topic = load_topic(context, assessment_id, topic_id)
            return responses.Ok(to_plain(
                topic,
                relationships = {
                    "aspects": {},
                }
            ))

