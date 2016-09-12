*************************
Feed Aggregator for Plone
*************************

.. contents:: Conteúdo
   :depth: 2

Life, the Universe, and Everything
==================================

A `Senha Web`_ é um serviço de autenticação da Prefeitura do Municipio de São Paulo.

Este pacote integra autenticação baseada na `Senha Web`_ no Plone.

.. _`Senha Web`: http://www.prefeitura.sp.gov.br/cidade/secretarias/financas/servicos/senhaweb/index.php?p=4458

Mostly Harmless
===============

.. image:: http://img.shields.io/pypi/v/collective.feedaggregator.svg
   :target: https://pypi.python.org/pypi/collective.feedaggregator

.. image:: https://img.shields.io/travis/hvelarde/collective.feedaggregator/master.svg
    :target: http://travis-ci.org/hvelarde/collective.feedaggregator

.. image:: https://img.shields.io/coveralls/hvelarde/collective.feedaggregator/master.svg
    :target: https://coveralls.io/r/hvelarde/collective.feedaggregator

Don't Panic
===========

Installation
------------

To enable this package in a buildout-based installation:

#. Edit your buildout.cfg and add add the following to it::

    [buildout]
    ...
    eggs =
        collective.feedaggregator

After updating the configuration you need to run ''bin/buildout'',
which will take care of updating your system.

Go to the 'Site Setup' page in a Plone site and click on the 'Add-ons' link.

Check the box next to ``collective.feedaggregator`` and click the 'Activate' button.

How does it work
----------------

TBA.
