from tools.adt_sql.database import db_context

from core.assessments import assessment_entities
from core.assessments.forms import form_entities

from endpoints.repository import (
    db, assessment_repository,
    form_repository, question_repository,
    sub_form_repository, sub_question_repository
)


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


def create_forms(assessment):
    create_form_a(assessment)
    create_form_b(assessment)
    create_form_c(assessment)
    create_form_d(assessment)
    create_form_e(assessment)


def create_form_a(assessment):
    with db_context(db) as context:

        form = form_repository.create(context, form_entities.Form(
            assessment_id = assessment.id,
            code = "A",
            name = "Proveedores",
            description = "Ble ble ble...",
        ))

        question_repository.create(context, form_entities.Question(
            form_id = form.id,
            order = 1,
            title = "Gastos totales en proveedores (en Euros)",
            quick_description = "",
            full_description = "",
            examples = "",
            data_type = "currency",
            options = None,
        ))

        sub_form = sub_form_repository.create(context, form_entities.SubForm(
            form_id = form.id,
            order = 2,
            caption = "Introduzca los 5 sectores más importantes a los que realiza compras",
            description = "",
        ))

        sub_question_repository.create(context, form_entities.SubQuestion(
            sub_form_id = sub_form.id,
            title = "Sector",
            description = "",
            data_type = "select",
            options = {
                "caption": "Seleccione del catálogo",
                "choices": [
                    "A - Agricultura, silvicultura y pesca",
                    "B - Explotación de minas y canteras",
                    "C - Industrias manufactureras",
                ]
            }
        ))

        question_repository.create(context, form_entities.Question(
            form_id = form.id,
            order = 3,
            title = "Región de origen principal del resto de proveedores",
            quick_description = "",
            full_description = "",
            examples = "",
            data_type = "select",
            options = {
                "caption": "Seleccione del catálogo",
                "choices": [
                    "A - Agricultura, silvicultura y pesca",
                    "B - Explotación de minas y canteras",
                    "C - Industrias manufactureras",
                ]
            }
        ))


def create_form_b(assessment):
    with db_context(db) as context:

        form = form_repository.create(context, form_entities.Form(
            assessment_id = assessment.id,
            code = "B",
            name = "Propietarios y proveedores financieros",
            description = "Bli bli bli...",
        ))

        question_repository.create(context, form_entities.Question(
            form_id = form.id,
            order = 1,
            title = "Beneficios (EBIT)",
            quick_description = "",
            full_description = "",
            examples = "",
            data_type = "currency",
            options = None,
        ))

        question_repository.create(context, form_entities.Question(
            form_id = form.id,
            order = 2,
            title = "Costes financieros",
            quick_description = "",
            full_description = "",
            examples = "",
            data_type = "currency",
            options = None,
        ))

        question_repository.create(context, form_entities.Question(
            form_id = form.id,
            order = 3,
            title = "Rendimientos de capital",
            quick_description = "",
            full_description = "",
            examples = "",
            data_type = "currency",
            options = None,
        ))

        question_repository.create(context, form_entities.Question(
            form_id = form.id,
            order = 4,
            title = "Activo (balance financiero)",
            quick_description = "",
            full_description = "",
            examples = "",
            data_type = "currency",
            options = None,
        ))

        question_repository.create(context, form_entities.Question(
            form_id = form.id,
            order = 5,
            title = "Altas de activos fijos",
            quick_description = "",
            full_description = "",
            examples = "",
            data_type = "currency",
            options = None,
        ))

        question_repository.create(context, form_entities.Question(
            form_id = form.id,
            order = 6,
            title = "Activos financieros y saldos de caja",
            quick_description = "",
            full_description = "",
            examples = "",
            data_type = "currency",
            options = None,
        ))


def create_form_c(assessment):
    pass


def create_form_d(assessment):
    pass


def create_form_e(assessment):
    pass

