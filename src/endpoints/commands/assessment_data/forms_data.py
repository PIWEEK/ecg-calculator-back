from tools.adt_sql.database import db_context

from core.assessments.forms import form_entities

from endpoints.repository import (
    db, form_repository, question_repository,
    sub_form_repository, sub_question_repository
)

from .economic_sectors import ECONOMIC_SECTORS
from .regions import REGIONS


def create_forms(assessment, stakeholders):
    create_form_a(assessment, stakeholders)
    create_form_b(assessment, stakeholders)
    create_form_c(assessment, stakeholders)
    create_form_d(assessment, stakeholders)
    create_form_e(assessment, stakeholders)


def create_form_a(assessment, stakeholders):
    """
    A: Providers
    """
    with db_context(db) as context:

        form = form_repository.create(context, form_entities.Form(
            assessment_id = assessment.id,
            stakeholder_id = stakeholders["providers"].id,
            slug = "provider_facts",
            name = "Proveedores",
            description = "Ble ble ble...",
        ))

        question_repository.create(context, form_entities.Question(
            form_id = form.id,
            order = 1,
            slug = "total_provider_expenses",
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
            slug = "providers_sectors",
            caption = "Introduzca los 5 sectores más importantes a los que realiza compras",
            description = "",
        ))

        sub_question_repository.create(context, form_entities.SubQuestion(
            sub_form_id = sub_form.id,
            order = 1,
            slug = "provider_sector",
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
            slug = "provider_description",
            title = "Descripción",
            description = "",
            data_type = "string",
            options = None
        ))

        sub_question_repository.create(context, form_entities.SubQuestion(
            sub_form_id = sub_form.id,
            order = 3,
            slug = "provider_region",
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
            slug = "provider_expenses",
            title = "Gastos",
            description = "",
            data_type = "currency",
            options = None
        ))

        question_repository.create(context, form_entities.Question(
            form_id = form.id,
            order = 3,
            slug = "other_providers_region",
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
            slug = "other_providers_expenses",
            title = "Gastos del resto de proveedores",
            quick_description = "",
            full_description = "",
            examples = "",
            data_type = "currency",
            options = None
        ))


def create_form_b(assessment, stakeholders):
    """
    B: Owners and financial providers
    """
    with db_context(db) as context:

        form = form_repository.create(context, form_entities.Form(
            assessment_id = assessment.id,
            stakeholder_id = stakeholders["owners_and_financers"].id,
            slug = "owners_and_financers_facts",
            name = "Propietarios y proveedores financieros",
            description = "Bli bli bli...",
        ))

        question_repository.create(context, form_entities.Question(
            form_id = form.id,
            order = 1,
            slug = "operating_profit",
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
            slug = "financing_cost",
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
            slug = "capital_return",
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
            slug = "assets_balance",
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
            slug = "fixed_assets_additions",
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
            slug = "financial_assets_and_cash",
            title = "Activos financieros y saldos de caja",
            quick_description = "",
            full_description = "",
            examples = "",
            data_type = "currency",
            options = None,
        ))


def create_form_c(assessment, stakeholders):
    """
    C: Workers
    """
    with db_context(db) as context:

        form = form_repository.create(context, form_entities.Form(
            assessment_id = assessment.id,
            stakeholder_id = stakeholders["workers"].id,
            slug = "workers_facts",
            name = "Trabajadores",
            description = "Blo blo blo...",
        ))

        question_repository.create(context, form_entities.Question(
            form_id = form.id,
            order = 1,
            slug = "workers_count",
            title = "Cantidad de trabajadores (equivalentes a jornada completa)",
            quick_description = "",
            full_description = "",
            examples = "",
            data_type = "integer",
            options = None,
        ))


def create_form_d(assessment, stakeholders):
    """
    D: Clients and other companies in the sector
    """
    with db_context(db) as context:

        form = form_repository.create(context, form_entities.Form(
            assessment_id = assessment.id,
            stakeholder_id = stakeholders["clients_and_partners"].id,
            slug = "clients_and_partners_facts",
            name = "Clientes y otras empresas del sector",
            description = "Blu blu blu...",
        ))

        question_repository.create(context, form_entities.Question(
            form_id = form.id,
            order = 1,
            slug = "annual_turnover",
            title = "Facturación (en euros)",
            quick_description = "",
            full_description = "",
            examples = "",
            data_type = "currency",
            options = None,
        ))


def create_form_e(assessment, stakeholders):
    """
    E: Social environment
    """
    with db_context(db) as context:

        form = form_repository.create(context, form_entities.Form(
            assessment_id = assessment.id,
            stakeholder_id = stakeholders["social_environment"].id,
            slug = "social_environment_facts",
            name = "Entorno social",
            description = "Blz blz blz...",
        ))

        question_repository.create(context, form_entities.Question(
            form_id = form.id,
            order = 1,
            slug = "company_size",
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

