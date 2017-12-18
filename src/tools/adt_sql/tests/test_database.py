import pytest
from contextlib import contextmanager

from tools.adt.types import ADT_WITH_ID, Field, IntField, StrField
from tools.adt.relationships import Relationship1N, RoleSingle, RoleMulti, Context
from sqlalchemy.sql import select, outerjoin

from tools.adt_sql.database import SQLADTDatabase, db_context


class Card(ADT_WITH_ID):
    deck_id = IntField()
    title = StrField()
    strength = IntField()
    defense = IntField()


class Deck(ADT_WITH_ID):
    name = StrField()


class DeckHasCards(Relationship1N):
    role_1 = RoleSingle(role_class=Deck, role_name="deck")
    role_n = RoleMulti(role_class=Card, role_name="cards", role_fk="deck_id", required=False)


def test_sql_persistence():
    db = SQLADTDatabase({
        "DB_NAME": "test",
        "ECHO": False
    })

    db.add_adt_table(Card, "cards")
    db.add_adt_table(Deck, "decks")
    db.create_all_tables()

    with db_context(db) as context:

        db.truncate_all_tables(context)

        deck = db.insert_adt(context,
            db.decks,
            Deck(
                name="Test deck"
            )
        )

        card_1 = db.insert_adt(context,
            db.cards,
            Card(
                deck_id=deck.id,
                title="Test card #1",
                strength=10,
                defense=1,
            )
        )

        card_2 = db.insert_adt(context,
            db.cards,
            Card(
                deck_id=deck.id,
                title="Test card #2",
                strength=8,
                defense=7,
            )
        )

    with db_context(db) as context:
        r_deck = db.retrieve_single_adt(context,
            Deck,
            select([db.decks])
                .where(db.decks.c.id == deck.id)
        )

    assert r_deck.id == deck.id
    assert r_deck.name == deck.name

    with db_context(db) as context:
        r_cards = db.retrieve_adts(context,
            Card,
            select([db.cards])
        )

    assert len(r_cards) == 2
    assert card_1.id in [card.id for card in r_cards]
    assert card_2.id in [card.id for card in r_cards]

    with db_context(db) as context:
        r_decks = db.retrieve_joined_adts(context,
            Deck, {"decks": Deck, "cards": Card},
            select([db.decks, db.cards], use_labels=True)
                .select_from(outerjoin(
                    db.decks, db.cards, db.decks.c.id == db.cards.c.deck_id
                ))
                .where(db.decks.c.id == deck.id)
        )

    assert len(r_decks) == 1

    r_deck = r_decks[0]
    assert r_deck.id == deck.id
    assert r_deck.name == deck.name

    assert len(context.cards(r_deck)) == 2
    assert card_1.id in [card.id for card in context.cards(r_deck)]
    assert card_2.id in [card.id for card in context.cards(r_deck)]

