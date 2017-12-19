from tools.adt_sql.database import db_context

from core.assessments import assessment_entities
from endpoints.repository import db, assessment_repository

from .forms_data import create_forms


def assessment_data():
    with db_context(db) as context:
        db.truncate_table(context, db.assessments)
        db.truncate_table(context, db.forms)
        db.truncate_table(context, db.questions)
        db.truncate_table(context, db.sub_forms)
        db.truncate_table(context, db.sub_questions)

    assessment_id = create_assessments()
    create_forms(assessment_id)


def create_assessments():
    with db_context(db) as context:

        assessment = assessment_repository.create(context, assessment_entities.Assessment(
            name = "Balance del Bien Común",
            version = "5.02",
            year = "2017",
            description = "Bla bla bla...",
        ))

        return assessment

