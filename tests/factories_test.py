"""Test factories for database models."""

import factory
from faker import Faker

fake = Faker()


class MessageFactory(factory.Factory):
    """Factory for creating test Message instances."""

    class Meta:
        """Factory configuration."""

        model = dict

    id = factory.Sequence(lambda n: n)
    sender = factory.LazyFunction(fake.phone_number)
    recipient = factory.LazyFunction(fake.phone_number)
    content = factory.LazyFunction(fake.text)
    timestamp = factory.LazyFunction(fake.date_time)


# Renaming file to factories_test.py
