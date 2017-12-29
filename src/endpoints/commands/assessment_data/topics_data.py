from tools.adt_sql.database import db_context

from core.assessments.topics import topic_entities

from endpoints.repository import db, topic_repository, aspect_repository


def create_topics(assessment, stakeholders):
    create_topic_a1(assessment, stakeholders)
    create_topic_a2(assessment, stakeholders)
    create_topic_a3(assessment, stakeholders)
    create_topic_a4(assessment, stakeholders)

    create_topic_b1(assessment, stakeholders)
    create_topic_b2(assessment, stakeholders)
    # create_topic_b3(assessment, stakeholders)
    # create_topic_b4(assessment, stakeholders)
    #
    # create_topic_c1(assessment, stakeholders)
    # create_topic_c2(assessment, stakeholders)
    # create_topic_c3(assessment, stakeholders)
    # create_topic_c4(assessment, stakeholders)
    #
    # create_topic_d1(assessment, stakeholders)
    # create_topic_d2(assessment, stakeholders)
    # create_topic_d3(assessment, stakeholders)
    # create_topic_d4(assessment, stakeholders)
    #
    # create_topic_e1(assessment, stakeholders)
    # create_topic_e2(assessment, stakeholders)
    # create_topic_e3(assessment, stakeholders)
    # create_topic_e4(assessment, stakeholders)


def create_topic_a1(assessment, stakeholders):
    """
    A1: Dignidad humana en la cadena de suministro
    """
    with db_context(db) as context:

        topic = topic_repository.create(context, topic_entities.Topic(
            assessment_id = assessment.id,
            stakeholder_id = stakeholders["providers"].id,
            slug = "providers_human_dignity",
            code = "A1",
            name = "Dignidad humana en la cadena de suministro",
            description = "Bla bla bla...",
        ))

        aspect_repository.create(context, topic_entities.Aspect(
            topic_id = topic.id,
            order = 1,
            slug = "providers_human_dignity_1",
            code = "A1.1",
            title = "Condiciones de trabajo e impacto social en la cadena de suministro",
            quick_description = "El objetivo es que la empresa se informe activamente sobre los productos y servicios que " + \
            "compra, y contribuya, gracias a las medidas adecuadas, a crear impactos positivos y condiciones " + \
            "dignas en toda su cadena de suministro.",
            valorative_questions = "<ul>" + \
            "<li>¿Qué productos y servicios compra la empresa? ¿Según qué criterios se seleccionan los proveedores?</li>" + \
            "<li>¿Cómo se evalúan los riesgos de impactos sociales negativos en la cadena de suministro?</li>" + \
            "<li>¿Cómo se detectan posibles vulneraciones de la dignidad humana en la cadena de suministro?</li>" + \
            "<li>¿Qué hace la empresa para infuir en los proveedores de tal manera que la dignidad humana esté en el centro de las relaciones con sus grupos de interés?</li>" + \
            "<li>¿Qué certifcados tienen los productos comprados?</li>" + \
            "</ul>",
            mandatory_indicators = "<ul>" + \
            "<li>Tabla de productos y servicios adquiridos y su % con respecto al gasto total de compra</li>" + \
            "<li>% de productos y servicios producidos bajo condiciones justas</li>" + \
            "</ul>",
            evaluation_levels = "" + \
            "<strong>Ejemplar</strong>" + \
            "<p>La gestión ética de los suministros es parte de la identidad empresarial y su posicionamiento de " + \
            "mercado. Procesos de compra ética se implementan de manera innovadora en todas las áreas de la empresa.</p>" + \
            "<strong>Experimentado</strong>" + \
            "<p>En la empresa existen procedimientos de compra que explican cómo se evalúan, seleccionan y apoyan los " + \
            "proveedores de acuerdo a criterios sociales, de tal manera que se cumpla con la política que contiene " + \
            "los valores de la empresa. La mayor parte de los proveedores principales tienen condiciones laborales " + \
            "por encima de la media.</p>" + \
            "<strong>Avanzado</strong>" + \
            "<p>La empresa implementa las primeras medidas para establecer condiciones laborales dignas en los " + \
            "proveedores. Además, se evalúa toda la cadena de suministro respecto a las condiciones de trabajo.</p>" + \
            "<strong>Primeros pasos</strong>" + \
            "<p>La empresa evalúa algunos de los proveedores principales respecto a las condiciones laborales y " + \
            "desarrolla estrategias y/o medidas de mejora. Se cumplen los primeros criterios excluyentes de compra.</p>" + \
            "<strong>Punto de partida</strong>" + \
            "<p>La empresa cumple con la ley respecto a las normas laborales por parte de los proveedores. A parte " + \
            "de esto, no hay más compromiso social por parte del proveedor.</p>",
            explanatory_notes = "" + \
            "<p>Las políticas de compra deben evaluarse según sus procedimientos y/o criterios " + \
            "excluyentes: cómo se identifcan los riesgos de impacto social negativo en la cadena de " + \
            "suministro, cómo se evalúan, seleccionan y fomentan los proveedores según sus " + \
            "impactos sociales.</p>" + \
            "<strong>Criterios de Evaluación:</strong>" + \
            "<ul>" + \
            "<li>Los proveedores tienen una política laboral que promueve la dignidad humana (C1).</li>" + \
            "<li>Los proveedores mismos tienen una política de compra que promueve la dignidad " + \
            "humana (ver A1).</li>" + \
            "<li>Los proveedores tienen una actitud ética respecto al uso de recursos fnancieros y sus " + \
            "clientes (ver B1 y D1) y contribuyen al Bien Común con sus productos y servicios (ver " + \
            "E1).</li>" + \
            "</ul>" + \
            "<strong>Los siguientes puntos pueden ser de ayuda a la hora de hacer la autoevaluación y/o " + \
            "para interpretar correctamente este aspecto:</strong>" + \
            "<ul>" + \
            "<li>Aquellas áreas de la cadena de suministro asociadas a altos riesgos de impacto social " + \
            "negativo son las más importantes. Cuando una empresa, en este tipo de cadenas de " + \
            "suministro, actúa muy por encima del estándar, esto puede infuir positivamente en su " + \
            "puntuación.</li>" + \
            "<li>Los impactos sociales no suelen ocurrir en los proveedores directos sino mucho antes " + \
            "en la cadena de valor. Por ejemplo, las condiciones laborales de un servicio de TIC " + \
            "probablemente sean menos críticas que las de la producción previa del hardware " + \
            "utilizado. El centro de atención deber ponerse en aquellas partes de la cadena de " + \
            "valor que tienen el impacto mayor.</li>" + \
            "<li>A la medida que la empresa crece, la política de compras se vuelve más importante y " + \
            "más compleja. De esta manera crecen los riesgos y por tanto la exigencia de políticas " + \
            "y procedimientos para garantizar una compra responsable.</li>" + \
            "<li>También se puntúa si solo algunos, muchos o todos los proveedores principales son " + \
            "evaluados o seleccionados de acuerdo a si vulneran – o no – la dignidad humana.</li>" + \
            "</ul>",
            is_negative = False,
        ))

        aspect_repository.create(context, topic_entities.Aspect(
            topic_id = topic.id,
            order = 2,
            slug = "providers_human_dignity_2",
            code = "A1.2",
            title = "Aspecto negativo: vulneración de la dignidad humana en la cadena de suministro",
            quick_description = "La producción de muchos bienes de uso diario está relacionada con graves problemas sociales. " + \
            "Debido a los procesos de producción globales y complejos, casi no hay ninguna empresa ni " + \
            "ninguna persona que pueda evitar toda vulneración de la dignidad humana en la cadena de " + \
            "suministro.",
            valorative_questions = "<ul>" + \
            "<li>¿Qué áreas de la cadena de suministro tienen riesgos importantes de vulneración " + \
            "de la dignidad humana?</li>" + \
            "<li>¿Qué medidas se toman para reducir o evitar estos impactos?</li>" + \
            "</ul>",
            mandatory_indicators = "<ul>" + \
            "<li>% de productos comprados con riesgos sociales y/o sin riesgo</li>" + \
            "</ul>",
            evaluation_levels = "<ul>" + \
            "<li><strong>Punto de partida</strong>: la empresa tiene bajos riesgos de impacto social negativo en la " + \
            "cadena de suministro o reduce los posibles impactos al mínimo.</li>" + \
            "<li><strong>20 puntos negativos</strong>: la empresa adquiere productos y servicios de sectores con " + \
            "impacto social negativo. Las medidas implementadas hasta ahora, todavía no reducen " + \
            "el impacto sufcientemente.</li>" + \
            "<li><strong>100 puntos negativos</strong>: la empresa compra productos y servicios esenciales de " + \
            "industrias con impacto social negativo y apenas muestra ninguna acción para mejorar " + \
            "su impacto.</li>" + \
            "<li><strong>200 puntos negativos</strong>: la empresa contribuye al impacto social negativo de manera " + \
            "decisiva.</li>" + \
            "</ul>",
            explanatory_notes = "" + \
            "<p>El centro de atención debe ponerse explícitamente en aquellos productos y servicios " + \
            "que tienen un alto riesgo de vulneración de la dignidad humana. Los riesgos pueden " + \
            "deberse al origen de los productos y servicios (por ejemplo, países con estándares " + \
            "laborales bajos) o al sector al que pertenecen.</p>",
            is_negative = True,
        ))


def create_topic_a2(assessment, stakeholders):
    """
    A2: Justicia y solidaridad en la cadena de suministro
    """
    with db_context(db) as context:

        topic = topic_repository.create(context, topic_entities.Topic(
            assessment_id = assessment.id,
            stakeholder_id = stakeholders["providers"].id,
            slug = "providers_justice_solidarity",
            code = "A2",
            name = "Justicia y solidaridad en la cadena de suministro",
            description = "Bla bla bla...",
        ))

        aspect_repository.create(context, topic_entities.Aspect(
            topic_id = topic.id,
            order = 1,
            slug = "providers_justice_solidarity_1",
            code = "A2.1",
            title = "Actitud ética con proveedores / distribuidores directos",
            quick_description = "La solidaridad y la justicia al tratar con proveedores directos se refeja especialmente en la " + \
            "organización de las relaciones comerciales en forma de precios justos, condiciones de pago y " + \
            "entrega. A parte de esto, es importante realizar un reparto justo de los ingresos dentro de la " + \
            "cadena de valor para garantizar una existencia económica de todas las partes implicadas.",
            valorative_questions = "",
            mandatory_indicators = "",
            evaluation_levels = "",
            explanatory_notes = "",
            is_negative = False,
        ))

        aspect_repository.create(context, topic_entities.Aspect(
            topic_id = topic.id,
            order = 2,
            slug = "providers_justice_solidarity_2",
            code = "A2.2",
            title = "Promoción de la justicia y la solidaridad en toda la cadena de suministro",
            quick_description = "Nulla quis lorem ut libero malesuada feugiat. Curabitur arcu erat, accumsan id imperdiet et, porttitor at sem." + \
            "Vestibulum ac diam sit amet quam vehicula elementum sed sit amet dui. Vivamus suscipit tortor eget felis porttitor volutpat." + \
            "Donec rutrum congue leo eget malesuada. Curabitur aliquet quam id dui posuere blandit." + \
            "Quisque velit nisi, pretium ut lacinia in, elementum id enim. Vivamus suscipit tortor eget felis porttitor volutpat." + \
            "Cras ultricies ligula sed magna dictum porta. Vivamus suscipit tortor eget felis porttitor volutpat.",
            valorative_questions = "",
            mandatory_indicators = "",
            evaluation_levels = "",
            explanatory_notes = "",
            is_negative = False,
        ))

        aspect_repository.create(context, topic_entities.Aspect(
            topic_id = topic.id,
            order = 3,
            slug = "providers_justice_solidarity_3",
            code = "A2.3",
            title = "Aspecto negativo: abuso de poder de mercado frente a proveedores / distribuidores",
            quick_description = "Nulla quis lorem ut libero malesuada feugiat. Curabitur arcu erat, accumsan id imperdiet et, porttitor at sem." + \
            "Vestibulum ac diam sit amet quam vehicula elementum sed sit amet dui. Vivamus suscipit tortor eget felis porttitor volutpat." + \
            "Donec rutrum congue leo eget malesuada. Curabitur aliquet quam id dui posuere blandit." + \
            "Quisque velit nisi, pretium ut lacinia in, elementum id enim. Vivamus suscipit tortor eget felis porttitor volutpat." + \
            "Cras ultricies ligula sed magna dictum porta. Vivamus suscipit tortor eget felis porttitor volutpat.",
            valorative_questions = "",
            mandatory_indicators = "",
            evaluation_levels = "",
            explanatory_notes = "",
            is_negative = True,
        ))


def create_topic_a3(assessment, stakeholders):
    """
    A3: Sostenibilidad medioambiental en la cadena de suministro
    """
    with db_context(db) as context:

        topic = topic_repository.create(context, topic_entities.Topic(
            assessment_id = assessment.id,
            stakeholder_id = stakeholders["providers"].id,
            slug = "providers_sustainability",
            code = "A3",
            name = "Sostenibilidad medioambiental en la cadena de suministro",
            description = "Bla bla bla...",
        ))

        aspect_repository.create(context, topic_entities.Aspect(
            topic_id = topic.id,
            order = 1,
            slug = "providers_sustainability_1",
            code = "A3.1",
            title = "Impacto medioambiental en la cadena de suministro",
            quick_description = "Nulla quis lorem ut libero malesuada feugiat. Curabitur arcu erat, accumsan id imperdiet et, porttitor at sem." + \
            "Vestibulum ac diam sit amet quam vehicula elementum sed sit amet dui. Vivamus suscipit tortor eget felis porttitor volutpat." + \
            "Donec rutrum congue leo eget malesuada. Curabitur aliquet quam id dui posuere blandit." + \
            "Quisque velit nisi, pretium ut lacinia in, elementum id enim. Vivamus suscipit tortor eget felis porttitor volutpat." + \
            "Cras ultricies ligula sed magna dictum porta. Vivamus suscipit tortor eget felis porttitor volutpat.",
            valorative_questions = "",
            mandatory_indicators = "",
            evaluation_levels = "",
            explanatory_notes = "",
            is_negative = False,
        ))

        aspect_repository.create(context, topic_entities.Aspect(
            topic_id = topic.id,
            order = 2,
            slug = "providers_sustainability_2",
            code = "A3.2",
            title = "Aspecto negativo: impacto medioambiental desproporcionado en la cadena de suministro",
            quick_description = "Nulla quis lorem ut libero malesuada feugiat. Curabitur arcu erat, accumsan id imperdiet et, porttitor at sem." + \
            "Vestibulum ac diam sit amet quam vehicula elementum sed sit amet dui. Vivamus suscipit tortor eget felis porttitor volutpat." + \
            "Donec rutrum congue leo eget malesuada. Curabitur aliquet quam id dui posuere blandit." + \
            "Quisque velit nisi, pretium ut lacinia in, elementum id enim. Vivamus suscipit tortor eget felis porttitor volutpat." + \
            "Cras ultricies ligula sed magna dictum porta. Vivamus suscipit tortor eget felis porttitor volutpat.",
            valorative_questions = "",
            mandatory_indicators = "",
            evaluation_levels = "",
            explanatory_notes = "",
            is_negative = True,
        ))


def create_topic_a4(assessment, stakeholders):
    """
    A4: Transparencia y participación democrática en la cadena de suministro
    """
    with db_context(db) as context:

        topic = topic_repository.create(context, topic_entities.Topic(
            assessment_id = assessment.id,
            stakeholder_id = stakeholders["providers"].id,
            slug = "providers_democracy",
            code = "A4",
            name = "Transparencia y participación democrática en la cadena de suministro",
            description = "Bla bla bla...",
        ))

        aspect_repository.create(context, topic_entities.Aspect(
            topic_id = topic.id,
            order = 1,
            slug = "providers_democracy_1",
            code = "A4.1",
            title = "Transparencia y participación democrática de los proveedores / distribuidores",
            quick_description = "Nulla quis lorem ut libero malesuada feugiat. Curabitur arcu erat, accumsan id imperdiet et, porttitor at sem." + \
            "Vestibulum ac diam sit amet quam vehicula elementum sed sit amet dui. Vivamus suscipit tortor eget felis porttitor volutpat." + \
            "Donec rutrum congue leo eget malesuada. Curabitur aliquet quam id dui posuere blandit." + \
            "Quisque velit nisi, pretium ut lacinia in, elementum id enim. Vivamus suscipit tortor eget felis porttitor volutpat." + \
            "Cras ultricies ligula sed magna dictum porta. Vivamus suscipit tortor eget felis porttitor volutpat.",
            valorative_questions = "",
            mandatory_indicators = "",
            evaluation_levels = "",
            explanatory_notes = "",
            is_negative = False,
        ))

        aspect_repository.create(context, topic_entities.Aspect(
            topic_id = topic.id,
            order = 2,
            slug = "providers_democracy_2",
            code = "A4.2",
            title = "Promoción de la transparencia y participación democrática en toda la cadena de suministro",
            quick_description = "Nulla quis lorem ut libero malesuada feugiat. Curabitur arcu erat, accumsan id imperdiet et, porttitor at sem." + \
            "Vestibulum ac diam sit amet quam vehicula elementum sed sit amet dui. Vivamus suscipit tortor eget felis porttitor volutpat." + \
            "Donec rutrum congue leo eget malesuada. Curabitur aliquet quam id dui posuere blandit." + \
            "Quisque velit nisi, pretium ut lacinia in, elementum id enim. Vivamus suscipit tortor eget felis porttitor volutpat." + \
            "Cras ultricies ligula sed magna dictum porta. Vivamus suscipit tortor eget felis porttitor volutpat.",
            valorative_questions = "",
            mandatory_indicators = "",
            evaluation_levels = "",
            explanatory_notes = "",
            is_negative = False,
        ))


def create_topic_b1(assessment, stakeholders):
    """
    B1: Actitud ética en la gestión de recursos financieros
    """
    with db_context(db) as context:

        topic = topic_repository.create(context, topic_entities.Topic(
            assessment_id = assessment.id,
            stakeholder_id = stakeholders["owners_and_financers"].id,
            slug = "owners_and_financers_human_dignity",
            code = "B1",
            name = "Actitud ética en la gestión de recursos financieros",
            description = "Bla bla bla...",
        ))

        aspect_repository.create(context, topic_entities.Aspect(
            topic_id = topic.id,
            order = 1,
            slug = "owners_and_financers_human_dignity_1",
            code = "B1.1",
            title = "Independencia financiera: autofinanciación",
            quick_description = "Nulla quis lorem ut libero malesuada feugiat. Curabitur arcu erat, accumsan id imperdiet et, porttitor at sem." + \
            "Vestibulum ac diam sit amet quam vehicula elementum sed sit amet dui. Vivamus suscipit tortor eget felis porttitor volutpat." + \
            "Donec rutrum congue leo eget malesuada. Curabitur aliquet quam id dui posuere blandit." + \
            "Quisque velit nisi, pretium ut lacinia in, elementum id enim. Vivamus suscipit tortor eget felis porttitor volutpat." + \
            "Cras ultricies ligula sed magna dictum porta. Vivamus suscipit tortor eget felis porttitor volutpat.",
            valorative_questions = "",
            mandatory_indicators = "",
            evaluation_levels = "",
            explanatory_notes = "",
            is_negative = False,
        ))

        aspect_repository.create(context, topic_entities.Aspect(
            topic_id = topic.id,
            order = 2,
            slug = "owners_and_financers_human_dignity_2",
            code = "B1.2",
            title = "Financiación externa orientada al Bien Común",
            quick_description = "Nulla quis lorem ut libero malesuada feugiat. Curabitur arcu erat, accumsan id imperdiet et, porttitor at sem." + \
            "Vestibulum ac diam sit amet quam vehicula elementum sed sit amet dui. Vivamus suscipit tortor eget felis porttitor volutpat." + \
            "Donec rutrum congue leo eget malesuada. Curabitur aliquet quam id dui posuere blandit." + \
            "Quisque velit nisi, pretium ut lacinia in, elementum id enim. Vivamus suscipit tortor eget felis porttitor volutpat." + \
            "Cras ultricies ligula sed magna dictum porta. Vivamus suscipit tortor eget felis porttitor volutpat.",
            valorative_questions = "",
            mandatory_indicators = "",
            evaluation_levels = "",
            explanatory_notes = "",
            is_negative = False,
        ))

        aspect_repository.create(context, topic_entities.Aspect(
            topic_id = topic.id,
            order = 3,
            slug = "owners_and_financers_human_dignity_3",
            code = "B1.3",
            title = "Actitud ética de los proveedores financieros",
            quick_description = "Nulla quis lorem ut libero malesuada feugiat. Curabitur arcu erat, accumsan id imperdiet et, porttitor at sem." + \
            "Vestibulum ac diam sit amet quam vehicula elementum sed sit amet dui. Vivamus suscipit tortor eget felis porttitor volutpat." + \
            "Donec rutrum congue leo eget malesuada. Curabitur aliquet quam id dui posuere blandit." + \
            "Quisque velit nisi, pretium ut lacinia in, elementum id enim. Vivamus suscipit tortor eget felis porttitor volutpat." + \
            "Cras ultricies ligula sed magna dictum porta. Vivamus suscipit tortor eget felis porttitor volutpat.",
            valorative_questions = "",
            mandatory_indicators = "",
            evaluation_levels = "",
            explanatory_notes = "",
            is_negative = False,
        ))


def create_topic_b2(assessment, stakeholders):
    """
    B2: Actitud solidaria en la gestión de recursos financieros
    """
    with db_context(db) as context:

        topic = topic_repository.create(context, topic_entities.Topic(
            assessment_id = assessment.id,
            stakeholder_id = stakeholders["owners_and_financers"].id,
            slug = "owners_and_financers_justice_solidarity",
            code = "B2",
            name = "Actitud solidaria en la gestión de recursos financieros",
            description = "Bla bla bla...",
        ))

        aspect_repository.create(context, topic_entities.Aspect(
            topic_id = topic.id,
            order = 1,
            slug = "owners_and_financers_justice_solidarity_1",
            code = "B2.1",
            title = "Gestión de los recursos financieros de forma solidaria y orientada al Bien Común",
            quick_description = "Nulla quis lorem ut libero malesuada feugiat. Curabitur arcu erat, accumsan id imperdiet et, porttitor at sem." + \
            "Vestibulum ac diam sit amet quam vehicula elementum sed sit amet dui. Vivamus suscipit tortor eget felis porttitor volutpat." + \
            "Donec rutrum congue leo eget malesuada. Curabitur aliquet quam id dui posuere blandit." + \
            "Quisque velit nisi, pretium ut lacinia in, elementum id enim. Vivamus suscipit tortor eget felis porttitor volutpat." + \
            "Cras ultricies ligula sed magna dictum porta. Vivamus suscipit tortor eget felis porttitor volutpat.",
            valorative_questions = "",
            mandatory_indicators = "",
            evaluation_levels = "",
            explanatory_notes = "",
            is_negative = False,
        ))

        aspect_repository.create(context, topic_entities.Aspect(
            topic_id = topic.id,
            order = 2,
            slug = "owners_and_financers_justice_solidarity_2",
            code = "B2.2",
            title = "Aspecto negativo: repartición injusta de los recursos financieros",
            quick_description = "Nulla quis lorem ut libero malesuada feugiat. Curabitur arcu erat, accumsan id imperdiet et, porttitor at sem." + \
            "Vestibulum ac diam sit amet quam vehicula elementum sed sit amet dui. Vivamus suscipit tortor eget felis porttitor volutpat." + \
            "Donec rutrum congue leo eget malesuada. Curabitur aliquet quam id dui posuere blandit." + \
            "Quisque velit nisi, pretium ut lacinia in, elementum id enim. Vivamus suscipit tortor eget felis porttitor volutpat." + \
            "Cras ultricies ligula sed magna dictum porta. Vivamus suscipit tortor eget felis porttitor volutpat.",
            valorative_questions = "",
            mandatory_indicators = "",
            evaluation_levels = "",
            explanatory_notes = "",
            is_negative = False,
        ))

