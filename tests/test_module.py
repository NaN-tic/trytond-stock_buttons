
# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.tests.test_tryton import ModuleTestCase
import trytond.tools as tools
import os
from trytond.modules.company.tests import CompanyTestMixin
OPJ = os.path.join
MODULES_PATH = os.path.abspath(__file__)
# MODULES_PATH = os.path.abspath('../..')


class StockButtonsTestCase(CompanyTestMixin, ModuleTestCase):
    'Test StockButtons module'
    module = 'stock_buttons'
    extras = []
    for extra_depend in ('stock_split', 'stock_lot', 'stock_valued',
            'purchase', 'sale'):
        try:
            tools.file_open(os.path.join(extra_depend, 'tryton.cfg'))
            extras.append(extra_depend)
        except IOError:
            pass


del ModuleTestCase
