from tools.adt_sql.database import db_context

from core.assessments import assessment_entities
from core.assessments.stakeholders import stakeholder_entities

from endpoints.repository import db, assessment_repository, stakeholder_repository

from .forms_data import create_forms
from .topics_data import create_topics


def assessment_data():
    with db_context(db) as context:
        db.truncate_table(context, db.assessments)
        db.truncate_table(context, db.stakeholders)
        db.truncate_table(context, db.forms)
        db.truncate_table(context, db.questions)
        db.truncate_table(context, db.sub_forms)
        db.truncate_table(context, db.sub_questions)
        db.truncate_table(context, db.topics)
        db.truncate_table(context, db.aspects)

    assessment = create_assessments()
    stakeholders = create_stakeholders(assessment)
    create_forms(assessment, stakeholders)
    create_topics(assessment, stakeholders)


def create_assessments():
    with db_context(db) as context:

        assessment = assessment_repository.create(context, assessment_entities.Assessment(
            name = "Balance del Bien Común",
            slug = "ecg_balance_5_0_2",
            version = "5.02",
            year = "2017",
            description = "Bla bla bla...",
        ))

        return assessment


def create_stakeholders(assessment):
    stakeholders = {}

    with db_context(db) as context:

        stakeholder = stakeholder_repository.create(context, stakeholder_entities.Stakeholder(
            assessment_id = assessment.id,
            name = "Proveedores",
            slug = "providers",
            code = "A",
            description = "Bla bla bla...",
        ))

        stakeholders[stakeholder.slug] = stakeholder

        stakeholder = stakeholder_repository.create(context, stakeholder_entities.Stakeholder(
            assessment_id = assessment.id,
            name = "Propietarios y proveedores financieros",
            slug = "owners_and_financers",
            code = "B",
            description = "Bla bla bla...",
        ))

        stakeholders[stakeholder.slug] = stakeholder

        stakeholder = stakeholder_repository.create(context, stakeholder_entities.Stakeholder(
            assessment_id = assessment.id,
            name = "Trabajadores",
            slug = "workers",
            code = "C",
            description = "Bla bla bla...",
        ))

        stakeholders[stakeholder.slug] = stakeholder

        stakeholder = stakeholder_repository.create(context, stakeholder_entities.Stakeholder(
            assessment_id = assessment.id,
            name = "Clientes y otras empresas del sector",
            slug = "clients_and_partners",
            code = "D",
            description = "Bla bla bla...",
        ))

        stakeholders[stakeholder.slug] = stakeholder

        stakeholder = stakeholder_repository.create(context, stakeholder_entities.Stakeholder(
            assessment_id = assessment.id,
            name = "Entorno social",
            slug = "social_environment",
            code = "E",
            description = "Bla bla bla...",
        ))

        stakeholders[stakeholder.slug] = stakeholder

    return stakeholders
