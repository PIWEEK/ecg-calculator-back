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
            description = "<p>Este grupo de interés incluye tanto proveedores directos como proveedores indirectos, y por " + \
            "tanto toda la cadena de suministro. Es aplicable a todo producto y servicio adquirido. Toda " + \
            "empresa es corresponsable de sus proveedores a través de sus decisiones de compra, la " + \
            "redacción formal de contratos y la posibilidad de infuir en ellos.</p>" + \
            "<p>Esta responsabilidad común depende en la práctica de las relaciones de poder en el mercado y " + \
            "de la longitud de la cadena de suministro. Es esencial cuando se compran productos y servicios " + \
            "especialmente críticos para los procesos de la cadena de suministro y conviene prestar atención " + \
            "si constituyen una gran importancia económica para la empresa o si por otro lado constituyen un " + \
            "riesgo para sus propios productos.</p>" + \
            "<p>Como guía, conviene realizar una lista de los proveedores más importantes de la empresa (que " + \
            "signifiquen aproximadamente el 80% del volumen de compra), así como de los productos y " + \
            "servicios adquiridos a estos proveedores en concreto. También deben considerarse productos y " + \
            "sectores en los que existe riesgo de impacto social y medioambiental negativo aunque el " + \
            "volumen de compra sea pequeño.</p>"
        ))

        stakeholders[stakeholder.slug] = stakeholder

        stakeholder = stakeholder_repository.create(context, stakeholder_entities.Stakeholder(
            assessment_id = assessment.id,
            name = "Propietarios y proveedores financieros",
            slug = "owners_and_financers",
            code = "B",
            description = "<p>Los propietarios de una empresa tienen derechos de utilización y decisión, pero también por eso " + \
            "mismo responsabilidad. El rol del propietario depende de la legalidad correspondiente.</p>" + \
            "<p>Los proveedores financieros aportan capital propio o externo. Los proveedores financieros son " + \
            "empresas de servicios de gestión de pagos, de seguros y de asesoramiento financiero.</p>"
        ))

        stakeholders[stakeholder.slug] = stakeholder

        stakeholder = stakeholder_repository.create(context, stakeholder_entities.Stakeholder(
            assessment_id = assessment.id,
            name = "Trabajadores",
            slug = "workers",
            code = "C",
            description = "<p>El grupo de interés C incluye a todas las personas cuya actividad es esencial para la empresa (= " + \
            "esencial para la actividad de la empresa). Forman parte del espacio y de la estructura " + \
            "organizativa y social de la empresa en uno de los siguientes ámbitos:</p>" + \
            "<ul>" + \
            "<li>Relación laboral contractual</li>" + \
            "<li>Personas que trabajan con un contrato temporal durante un período de al menos seis meses</li>" + \
            "<li>Personas que trabajan con un contrato de al menos cuatro horas por semana</li>" + \
            "<li>Personas que trabajan con un contrato por obra o servicio de forma periódica y recurrente (por " + \
            "ejemplo, en la campaña de navidad y verano)</li>" + \
            "</ul>"
        ))

        stakeholders[stakeholder.slug] = stakeholder

        stakeholder = stakeholder_repository.create(context, stakeholder_entities.Stakeholder(
            assessment_id = assessment.id,
            name = "Clientes y otras empresas del sector",
            slug = "clients_and_partners",
            code = "D",
            description = "</p>Este grupo de interés se refere al destinatario fnal de la actividad de la empresa, por ejemplo el " + \
            "consumidor de los productos y servicios, los minoristas, mayoristas y contratantes.</p>" + \
            "<p>Cuando hablamos de otras empresas nos referimos en primera instancia a las empresas que " + \
            "tienen el mismo segmento de mercado y en la misma región, pero también contemplamos el " + \
            "comportamiento y las relaciones de la empresa con otras empresas de otros sectores y regiones " + \
            "geográficas.</p>"
        ))

        stakeholders[stakeholder.slug] = stakeholder

        stakeholder = stakeholder_repository.create(context, stakeholder_entities.Stakeholder(
            assessment_id = assessment.id,
            name = "Entorno social",
            slug = "social_environment",
            code = "E",
            description = "<p>El grupo de interés E incluye todos los grupos de personas que se ven afectados indirectamente " + \
            "por la actividad de la empresa. Se consideran tantos grupos de personas como sea posible y " + \
            "tenga sentido en la práctica. Sin embargo hay diferencias dependiendo de cada valor de la " + \
            "matriz:</p>" + \
            "<ul>" + \
            "<li>E1: la humanidad como un todo común, incluidas las generaciones futuras (incluye a todas las " + \
            "personas como seres humanos racionales con valores y signifcado existencial).</li>" + \
            "<li>E2: la comunidad como un gran grupo social que comparte un espacio determinado. Éste " + \
            "puede ser físico o virtual (por ejemplo, todas las personas que viven en una región o todos los " + \
            "usuarios de internet). El grupo tiene reglas e instituciones comunes para lograr un " + \
            "entendimiento común. Una empresa puede pertenecer a varias comunidades (municipio, " + \
            "región, estado, comunidad científca, etc.).</li>" + \
            "<li>E3: entorno ecológico global, incluidos los recursos naturales de las generaciones futuras.</li>" + \
            "<li>E4: grupos de interés relevantes para la empresa, por ejemplo vecinos u ONGs como " + \
            "“defensores” de los derechos sociales.</li>" + \
            "</ul>"
        ))

        stakeholders[stakeholder.slug] = stakeholder

    return stakeholders
