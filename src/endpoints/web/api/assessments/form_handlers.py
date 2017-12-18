from anillo.http import responses

from core.assessments.forms import form_entities, form_actions

from tools.adt.converter import to_plain
from tools.adt_sql.database import db_context

from endpoints.repository import db

from endpoints.web.handler import BaseHandler

from endpoints.web.api.loaders_and_checkers import load_form
from endpoints.web.api import exceptions


class AssessmentFormsList(BaseHandler):
    def get(self, request, assessment_id):
        with db_context(db) as context:

            forms = form_actions.list_forms(context, assessment_id)

            return responses.Ok([
                to_plain(form)
                for form in forms
            ])


class AssessmentFormDetail(BaseHandler):
    def get(self, request, assessment_id, form_id):
        with db_context(db) as context:
            form = load_form(context, assessment_id, form_id)
            return responses.Ok(to_plain(
                form,
                relationships = {
                    "questions": {},
                    "sub_forms": {
                        "relationships": {
                            "sub_questions": {}
                        }
                    }
                }
            ))

