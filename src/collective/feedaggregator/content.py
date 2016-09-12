# -*- coding: utf-8 -*-
from collective.feedaggregator.interfaces import IFeedAggregator
from plone.app.contenttypes.interfaces import ICollection
from plone.dexterity.content import Item
from zope.interface import implementer


@implementer(IFeedAggregator, ICollection)
class FeedAggregator(Item):

    """A feed aggregator."""

    @property
    def query(self):
        return ''

    @property
    def customViewFields(self):
        return ['Title', 'Creator', 'Type', 'ModificationDate']

    def selectedViewFields(self):
        return self.customViewFields

    def results(
        self,
        batch=True,
        b_start=0,
        b_size=None,
        sort_on=None,
        limit=None,
        brains=False,
        custom_query=None,
    ):
        return []
