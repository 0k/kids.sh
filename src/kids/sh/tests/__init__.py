# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

import os

from kids.test import Test
from kids.cache import cache
from .. import wrap as w, cmd, set_env


class BaseShTest(Test):

    COMMAND = ""
    DEFAULT_ENV = {
    }

    @cache
    @property
    def cmd(self):
        return set_env(**self.DEFAULT_ENV)(cmd)

    @cache
    @property
    def w(self):
        return set_env(**self.DEFAULT_ENV)(w)
