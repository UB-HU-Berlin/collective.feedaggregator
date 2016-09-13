# -*- coding: utf-8 -*-
from collective.feedaggregator.logger import logger
from plone.memoize import ram
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from time import time


def _feedaggregator_cachekey(method, self):
    """Cache Feed Aggregators for 15 minutes; invalidate on changes."""
    TTL = time() // (60 * 15)
    cachekey = (self.context.absolute_url(), self.context.modified(), TTL)
    logger.debug(cachekey)
    return cachekey


class ListingView(BrowserView):

    """Default view, a listing of feed entries."""

    index = ViewPageTemplateFile('feedaggregator.pt')

    def __call__(self):
        return self.index()

    @property
    @ram.cache(_feedaggregator_cachekey)
    def results(self):
        return self.context.results

    @property
    def show_byline(self):
        return True
