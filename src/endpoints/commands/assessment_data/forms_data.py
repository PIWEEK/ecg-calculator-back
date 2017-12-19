from tools.adt_sql.database import db_context

from core.assessments.forms import form_entities

from endpoints.repository import (
    db, form_repository, question_repository,
    sub_form_repository, sub_question_repository
)

from .economic_sectors import ECONOMIC_SECTORS
from .regions import REGIONS


def create_forms(assessment):
    create_form_a(assessment)
    create_form_b(assessment)
    create_form_c(assessment)
    create_form_d(assessment)
    create_form_e(assessment)


def create_form_a(assessment):
    """
    A: Providers
    """
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
            order = 1,
            title = "Sector",
            description = "",
            data_type = "select",
            options = {
                "caption": "Seleccione del catálogo",
                "choices": ECONOMIC_SECTORS
            }
        ))

        sub_question_repository.create(context, form_entities.SubQuestion(
            sub_form_id = sub_form.id,
            order = 2,
            title = "Descripción",
            description = "",
            data_type = "string",
            options = None
        ))

        sub_question_repository.create(context, form_entities.SubQuestion(
            sub_form_id = sub_form.id,
            order = 3,
            title = "Región de origen",
            description = "",
            data_type = "select",
            options = {
                "caption": "Seleccione del catálogo",
                "choices": REGIONS
            }
        ))

        sub_question_repository.create(context, form_entities.SubQuestion(
            sub_form_id = sub_form.id,
            order = 4,
            title = "Gastos",
            description = "",
            data_type = "currency",
            options = None
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
                "choices": REGIONS
            }
        ))

        question_repository.create(context, form_entities.Question(
            form_id = form.id,
            order = 4,
            title = "Gastos del resto de proveedores",
            quick_description = "",
            full_description = "",
            examples = "",
            data_type = "currency",
            options = None
        ))


def create_form_b(assessment):
    """
    B: Owners and financial providers
    """
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
    """
    C: Workers
    """
    with db_context(db) as context:

        form = form_repository.create(context, form_entities.Form(
            assessment_id = assessment.id,
            code = "C",
            name = "Trabajadores",
            description = "Blo blo blo...",
        ))

        question_repository.create(context, form_entities.Question(
            form_id = form.id,
            order = 1,
            title = "Cantidad de trabajadores (equivalentes a jornada completa)",
            quick_description = "",
            full_description = "",
            examples = "",
            data_type = "integer",
            options = None,
        ))


def create_form_d(assessment):
    """
    D: Clients and other companies in the sector
    """
    with db_context(db) as context:

        form = form_repository.create(context, form_entities.Form(
            assessment_id = assessment.id,
            code = "D",
            name = "Clientes y otras empresas del sector",
            description = "Blu blu blu...",
        ))

        question_repository.create(context, form_entities.Question(
            form_id = form.id,
            order = 1,
            title = "Facturación (en euros)",
            quick_description = "",
            full_description = "",
            examples = "",
            data_type = "currency",
            options = None,
        ))


def create_form_e(assessment):
    """
    E: Social environment
    """
    with db_context(db) as context:

        form = form_repository.create(context, form_entities.Form(
            assessment_id = assessment.id,
            code = "E",
            name = "Entorno social",
            description = "Blz blz blz...",
        ))

        question_repository.create(context, form_entities.Question(
            form_id = form.id,
            order = 1,
            title = "Tamaño de la empresa",
            quick_description = "",
            full_description = "",
            examples = "",
            data_type = "select",
            options = {
                "caption": "Seleccione una opción",
                "choices": [
                    ("micropyme", "micropyme"),
                    ("pyme", "pyme"),
                    ("gran empresa", "gran empresa"),
                ]
            }
        ))

