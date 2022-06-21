# -*- coding: utf-8 -*-

"""Test data integrity."""

import unittest
import itertools as itt
from debio.resources import PROPERTIES, TYPEDEFS, TERMS


class TestIntegrity(unittest.TestCase):
    """Test data integrity."""

    def test_identifiers(self):
        """Test identifiers are unique."""
        resources = [
            [
                entry["identifier"]
                for entry in resource
            ]
            for resource in [PROPERTIES, TYPEDEFS, TERMS]
        ]
        for resource in resources:
            self.assertEqual(len(resource), len(set(resource)))
        for r1, r2 in itt.combinations(resources, 2):
            self.assertEqual(0, len(set(r1).intersection(r2)))
