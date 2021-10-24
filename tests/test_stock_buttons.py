# This file is part of the stock_buttons module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase
import trytond.tools as tools
import os

OPJ = os.path.join
MODULES_PATH = os.path.abspath(__file__)
# MODULES_PATH = os.path.abspath('../..')


class StockButtonsTestCase(ModuleTestCase):
    'Test Stock Buttons module'
    module = 'stock_buttons'
    extras = []
    for extra_depend in ('product_manufacturer', 'stock_split',
            'stock_lot', 'stock_valued'):
        try:
            tools.file_open(os.path.join(extra_depend, 'tryton.cfg'))
            extras.append(extra_depend)
        except IOError:
            pass

def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        StockButtonsTestCase))
    return suite
