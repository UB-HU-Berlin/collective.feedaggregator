# -*- coding: utf-8 -*-
from collective.feedaggregator import _
from plone.supermodel import model
from zope import schema
from zope.interface import Interface


class IAddOnLayer(Interface):

    """Add-on specific layer."""


class IFeedAggregator(model.Schema):

    """A feed aggregator."""

    feeds = schema.Set(
        title=_(u'Feeds'),
        description=_(u'A list of feed URI to be processed.'),
        required=True,
        default=set(),
        value_type=schema.ASCIILine(title=_(u'URI')),
    )

    # query = schema.List(
    #     title=_(u'Search terms'),
    #     description=_(u'Define the search terms for the items you want '
    #                   u'to list by choosing what to match on. '
    #                   u'The list of results will be dynamically updated'),
    #     value_type=schema.Dict(value_type=schema.Field(),
    #                            key_type=schema.TextLine()),
    #     required=False,
    #     missing_value=''
    # )

    sort_on = schema.TextLine(
        title=_(u'label_sort_on', default=u'Sort on'),
        description=_(u'Sort the collection on this index'),
        required=False,
    )

    sort_reversed = schema.Bool(
        title=_(u'label_sort_reversed', default=u'Reversed order'),
        description=_(u'Sort the results in reversed order'),
        required=False,
    )

    limit = schema.Int(
        title=_(u'Limit'),
        description=_(u'Limit Search Results'),
        required=False,
        default=100,
    )

    item_count = schema.Int(
        title=_(u'label_item_count', default=u'Item count'),
        description=_(u'Number of items that will show up in one batch.'),
        required=False,
        default=30,
    )

    # customViewFields = schema.List(
    #     title=_(u'Table Columns'),
    #     description=_(u'Select which fields to display when '
    #                   u'"Tabular view" is selected in the display menu.'),
    #     default=['Title', 'Creator', 'Type', 'ModificationDate'],
    #     value_type=schema.Choice(
    #         vocabulary='plone.app.contenttypes.metadatafields'),
    #     required=False,
    #     )
