from anillo.http import responses

from core.assessments import assessment_entities, assessment_actions
from core.assessments.stakeholders import stakeholder_entities, stakeholder_actions

from tools.adt.converter import to_plain
from tools.adt_sql.database import db_context

from endpoints.repository import db

from endpoints.web.handler import BaseHandler

from endpoints.web.api.loaders_and_checkers import load_assessment


class AssessmentsList(BaseHandler):
    def get(self, request):
        with db_context(db) as context:

            assessments = assessment_actions.list_assessments(context)

            return responses.Ok([
                to_plain(assessment)
                for assessment in assessments
            ])


class AssessmentDetail(BaseHandler):
    def get(self, request, assessment_id):
        with db_context(db) as context:
            assessment = load_assessment(context, assessment_id)
            return responses.Ok(to_plain(assessment))


class AssessmentStakeholdersList(BaseHandler):
    def get(self, request, assessment_id):
        with db_context(db) as context:

            stakeholders = stakeholder_actions.list_stakeholders(context, assessment_id)

            return responses.Ok([
                to_plain(stakeholder)
                for stakeholder in stakeholders
            ])

