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
            quick_description = "",
            full_description = "El objetivo es que la empresa se informe activamente sobre los productos y servicios que " + \
            "compra, y contribuya, gracias a las medidas adecuadas, a crear impactos positivos y condiciones " + \
            "dignas en toda su cadena de suministro.",
            examples = "",
            is_negative = False,
        ))

        aspect_repository.create(context, topic_entities.Aspect(
            topic_id = topic.id,
            order = 2,
            slug = "providers_human_dignity_2",
            code = "A1.2",
            title = "Aspecto negativo: vulneración de la dignidad humana en la cadena de suministro",
            quick_description = "",
            full_description = "La producción de muchos bienes de uso diario está relacionada con graves problemas sociales. " + \
            "Debido a los procesos de producción globales y complejos, casi no hay ninguna empresa ni " + \
            "ninguna persona que pueda evitar toda vulneración de la dignidad humana en la cadena de " + \
            "suministro.",
            examples = "",
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
            quick_description = "",
            full_description = "La solidaridad y la justicia al tratar con proveedores directos se refeja especialmente en la " + \
            "organización de las relaciones comerciales en forma de precios justos, condiciones de pago y " + \
            "entrega. A parte de esto, es importante realizar un reparto justo de los ingresos dentro de la " + \
            "cadena de valor para garantizar una existencia económica de todas las partes implicadas.",
            examples = "",
            is_negative = False,
        ))

        aspect_repository.create(context, topic_entities.Aspect(
            topic_id = topic.id,
            order = 2,
            slug = "providers_justice_solidarity_2",
            code = "A2.2",
            title = "Promoción de la justicia y la solidaridad en toda la cadena de suministro",
            quick_description = "",
            full_description = "Nulla quis lorem ut libero malesuada feugiat. Curabitur arcu erat, accumsan id imperdiet et, porttitor at sem." + \
            "Vestibulum ac diam sit amet quam vehicula elementum sed sit amet dui. Vivamus suscipit tortor eget felis porttitor volutpat." + \
            "Donec rutrum congue leo eget malesuada. Curabitur aliquet quam id dui posuere blandit." + \
            "Quisque velit nisi, pretium ut lacinia in, elementum id enim. Vivamus suscipit tortor eget felis porttitor volutpat." + \
            "Cras ultricies ligula sed magna dictum porta. Vivamus suscipit tortor eget felis porttitor volutpat.",
            examples = "",
            is_negative = False,
        ))

        aspect_repository.create(context, topic_entities.Aspect(
            topic_id = topic.id,
            order = 3,
            slug = "providers_justice_solidarity_3",
            code = "A2.3",
            title = "Aspecto negativo: abuso de poder de mercado frente a proveedores / distribuidores",
            quick_description = "",
            full_description = "Nulla quis lorem ut libero malesuada feugiat. Curabitur arcu erat, accumsan id imperdiet et, porttitor at sem." + \
            "Vestibulum ac diam sit amet quam vehicula elementum sed sit amet dui. Vivamus suscipit tortor eget felis porttitor volutpat." + \
            "Donec rutrum congue leo eget malesuada. Curabitur aliquet quam id dui posuere blandit." + \
            "Quisque velit nisi, pretium ut lacinia in, elementum id enim. Vivamus suscipit tortor eget felis porttitor volutpat." + \
            "Cras ultricies ligula sed magna dictum porta. Vivamus suscipit tortor eget felis porttitor volutpat.",
            examples = "",
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
            quick_description = "",
            full_description = "Nulla quis lorem ut libero malesuada feugiat. Curabitur arcu erat, accumsan id imperdiet et, porttitor at sem." + \
            "Vestibulum ac diam sit amet quam vehicula elementum sed sit amet dui. Vivamus suscipit tortor eget felis porttitor volutpat." + \
            "Donec rutrum congue leo eget malesuada. Curabitur aliquet quam id dui posuere blandit." + \
            "Quisque velit nisi, pretium ut lacinia in, elementum id enim. Vivamus suscipit tortor eget felis porttitor volutpat." + \
            "Cras ultricies ligula sed magna dictum porta. Vivamus suscipit tortor eget felis porttitor volutpat.",
            examples = "",
            is_negative = False,
        ))

        aspect_repository.create(context, topic_entities.Aspect(
            topic_id = topic.id,
            order = 2,
            slug = "providers_sustainability_2",
            code = "A3.2",
            title = "Aspecto negativo: impacto medioambiental desproporcionado en la cadena de suministro",
            quick_description = "",
            full_description = "Nulla quis lorem ut libero malesuada feugiat. Curabitur arcu erat, accumsan id imperdiet et, porttitor at sem." + \
            "Vestibulum ac diam sit amet quam vehicula elementum sed sit amet dui. Vivamus suscipit tortor eget felis porttitor volutpat." + \
            "Donec rutrum congue leo eget malesuada. Curabitur aliquet quam id dui posuere blandit." + \
            "Quisque velit nisi, pretium ut lacinia in, elementum id enim. Vivamus suscipit tortor eget felis porttitor volutpat." + \
            "Cras ultricies ligula sed magna dictum porta. Vivamus suscipit tortor eget felis porttitor volutpat.",
            examples = "",
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
            quick_description = "",
            full_description = "Nulla quis lorem ut libero malesuada feugiat. Curabitur arcu erat, accumsan id imperdiet et, porttitor at sem." + \
            "Vestibulum ac diam sit amet quam vehicula elementum sed sit amet dui. Vivamus suscipit tortor eget felis porttitor volutpat." + \
            "Donec rutrum congue leo eget malesuada. Curabitur aliquet quam id dui posuere blandit." + \
            "Quisque velit nisi, pretium ut lacinia in, elementum id enim. Vivamus suscipit tortor eget felis porttitor volutpat." + \
            "Cras ultricies ligula sed magna dictum porta. Vivamus suscipit tortor eget felis porttitor volutpat.",
            examples = "",
            is_negative = False,
        ))

        aspect_repository.create(context, topic_entities.Aspect(
            topic_id = topic.id,
            order = 2,
            slug = "providers_democracy_2",
            code = "A4.2",
            title = "Promoción de la transparencia y participación democrática en toda la cadena de suministro",
            quick_description = "",
            full_description = "Nulla quis lorem ut libero malesuada feugiat. Curabitur arcu erat, accumsan id imperdiet et, porttitor at sem." + \
            "Vestibulum ac diam sit amet quam vehicula elementum sed sit amet dui. Vivamus suscipit tortor eget felis porttitor volutpat." + \
            "Donec rutrum congue leo eget malesuada. Curabitur aliquet quam id dui posuere blandit." + \
            "Quisque velit nisi, pretium ut lacinia in, elementum id enim. Vivamus suscipit tortor eget felis porttitor volutpat." + \
            "Cras ultricies ligula sed magna dictum porta. Vivamus suscipit tortor eget felis porttitor volutpat.",
            examples = "",
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
            quick_description = "",
            full_description = "Nulla quis lorem ut libero malesuada feugiat. Curabitur arcu erat, accumsan id imperdiet et, porttitor at sem." + \
            "Vestibulum ac diam sit amet quam vehicula elementum sed sit amet dui. Vivamus suscipit tortor eget felis porttitor volutpat." + \
            "Donec rutrum congue leo eget malesuada. Curabitur aliquet quam id dui posuere blandit." + \
            "Quisque velit nisi, pretium ut lacinia in, elementum id enim. Vivamus suscipit tortor eget felis porttitor volutpat." + \
            "Cras ultricies ligula sed magna dictum porta. Vivamus suscipit tortor eget felis porttitor volutpat.",
            examples = "",
            is_negative = False,
        ))

        aspect_repository.create(context, topic_entities.Aspect(
            topic_id = topic.id,
            order = 2,
            slug = "owners_and_financers_human_dignity_2",
            code = "B1.2",
            title = "Financiación externa orientada al Bien Común",
            quick_description = "",
            full_description = "Nulla quis lorem ut libero malesuada feugiat. Curabitur arcu erat, accumsan id imperdiet et, porttitor at sem." + \
            "Vestibulum ac diam sit amet quam vehicula elementum sed sit amet dui. Vivamus suscipit tortor eget felis porttitor volutpat." + \
            "Donec rutrum congue leo eget malesuada. Curabitur aliquet quam id dui posuere blandit." + \
            "Quisque velit nisi, pretium ut lacinia in, elementum id enim. Vivamus suscipit tortor eget felis porttitor volutpat." + \
            "Cras ultricies ligula sed magna dictum porta. Vivamus suscipit tortor eget felis porttitor volutpat.",
            examples = "",
            is_negative = False,
        ))

        aspect_repository.create(context, topic_entities.Aspect(
            topic_id = topic.id,
            order = 3,
            slug = "owners_and_financers_human_dignity_3",
            code = "B1.3",
            title = "Actitud ética de los proveedores financieros",
            quick_description = "",
            full_description = "Nulla quis lorem ut libero malesuada feugiat. Curabitur arcu erat, accumsan id imperdiet et, porttitor at sem." + \
            "Vestibulum ac diam sit amet quam vehicula elementum sed sit amet dui. Vivamus suscipit tortor eget felis porttitor volutpat." + \
            "Donec rutrum congue leo eget malesuada. Curabitur aliquet quam id dui posuere blandit." + \
            "Quisque velit nisi, pretium ut lacinia in, elementum id enim. Vivamus suscipit tortor eget felis porttitor volutpat." + \
            "Cras ultricies ligula sed magna dictum porta. Vivamus suscipit tortor eget felis porttitor volutpat.",
            examples = "",
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
            quick_description = "",
            full_description = "Nulla quis lorem ut libero malesuada feugiat. Curabitur arcu erat, accumsan id imperdiet et, porttitor at sem." + \
            "Vestibulum ac diam sit amet quam vehicula elementum sed sit amet dui. Vivamus suscipit tortor eget felis porttitor volutpat." + \
            "Donec rutrum congue leo eget malesuada. Curabitur aliquet quam id dui posuere blandit." + \
            "Quisque velit nisi, pretium ut lacinia in, elementum id enim. Vivamus suscipit tortor eget felis porttitor volutpat." + \
            "Cras ultricies ligula sed magna dictum porta. Vivamus suscipit tortor eget felis porttitor volutpat.",
            examples = "",
            is_negative = False,
        ))

        aspect_repository.create(context, topic_entities.Aspect(
            topic_id = topic.id,
            order = 2,
            slug = "owners_and_financers_justice_solidarity_2",
            code = "B2.2",
            title = "Aspecto negativo: repartición injusta de los recursos financieros",
            quick_description = "",
            full_description = "Nulla quis lorem ut libero malesuada feugiat. Curabitur arcu erat, accumsan id imperdiet et, porttitor at sem." + \
            "Vestibulum ac diam sit amet quam vehicula elementum sed sit amet dui. Vivamus suscipit tortor eget felis porttitor volutpat." + \
            "Donec rutrum congue leo eget malesuada. Curabitur aliquet quam id dui posuere blandit." + \
            "Quisque velit nisi, pretium ut lacinia in, elementum id enim. Vivamus suscipit tortor eget felis porttitor volutpat." + \
            "Cras ultricies ligula sed magna dictum porta. Vivamus suscipit tortor eget felis porttitor volutpat.",
            examples = "",
            is_negative = False,
        ))

