##############################################################################
#
# Copyright (c) 2002 Zope Foundation and Contributors.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE
#
##############################################################################

import unittest

from DocumentTemplate.sequence.SortEx import SortEx
from DocumentTemplate.sequence.tests.ztestlib import wordlist
from DocumentTemplate.sequence.tests.results import (
    res1,
    res2,
    res3,
    res4,
    res5,
    res6,
    res7,
)


class TestCase(unittest.TestCase):

    def test1(self):
        assert res1 == SortEx(wordlist)

    def test2(self):
        assert res2 == SortEx(wordlist, (("key",),), mapping=1)

    def test3(self):
        assert res3 == SortEx(wordlist, (("key", "cmp"),), mapping=1)

    def test4(self):
        assert res4 == SortEx(wordlist, (("key", "cmp", "desc"),), mapping=1)

    def test5(self):
        assert res5 == SortEx(wordlist, (("weight",), ("key",)), mapping=1)

    def test6(self):
        assert res6 == SortEx(
            wordlist, (("weight",), ("key", "nocase", "desc")), mapping=1)

    def test7(self):
        def myCmp(s1, s2):
            if s1 > s2:
                return -1
            if s1 < s2:
                return 1
            return 0

        # Create namespace...
        from DocumentTemplate.DT_Util import TemplateDict
        md = TemplateDict()

        # ... and push out function onto the namespace
        md._push({"myCmp": myCmp})

        assert res7 == SortEx(
            wordlist, (("weight",), ("key", "myCmp", "desc")), md, mapping=1)
