# Copyright 2012 by Wibowo Arindrarto.  All rights reserved.
# This code is part of the Biopython distribution and governed by its
# license.  Please see the LICENSE file that should have been included
# as part of this package.

"""Tests for SearchIO BlastIO parsers."""

# For using with statement in Python 2.5 or Jython
from __future__ import with_statement

import os
import sys
import unittest
import warnings

from Bio.SearchIO import parse, read

# test case files are in the Blast directory
TEST_DIR = 'Blast'
FMT = 'blast-tab'


def get_file(filename):
    """Returns the path of a test file."""
    return os.path.join(TEST_DIR, filename)


class BlastnTabCases(unittest.TestCase):

    def test_tab_2226_tblastn_001(self):
        "Test parsing TBLASTN 2.2.26+ tabular output (tab_2226_tblastn_001)"

        xml_file = get_file('tab_2226_tblastn_001.txt')
        qresults = parse(xml_file, FMT)
        counter = 0

        # test first qresult
        qresult = qresults.next()
        counter += 1

        self.assertEqual('gi|16080617|ref|NP_391444.1|', qresult.id)
        self.assertEqual(3, len(qresult))

        hit = qresult[0]
        self.assertEqual('gi|145479850|ref|XM_001425911.1|', hit.id)
        self.assertEqual('gi|16080617|ref|NP_391444.1|', hit.query_id)
        self.assertEqual(1, len(hit))

        hsp = hit[0]
        self.assertEqual('gi|145479850|ref|XM_001425911.1|', hsp.hit_id)
        self.assertEqual('gi|16080617|ref|NP_391444.1|', hsp.query_id)
        self.assertEqual(34.88, hsp.ident_pct)
        self.assertEqual(43, hsp.aln_span)
        self.assertEqual(28, hsp.mismatch_num)
        self.assertEqual(0, hsp.gapopen_num)
        self.assertEqual(30, hsp.query_start)
        self.assertEqual(73, hsp.query_end)
        self.assertEqual(1743, hsp.hit_start)
        self.assertEqual(1872, hsp.hit_end)
        self.assertEqual(1e-05, hsp.evalue)
        self.assertEqual(34.7, hsp.bitscore)

        hit = qresult[-1]
        self.assertEqual('gi|115975252|ref|XM_001180111.1|', hit.id)
        self.assertEqual('gi|16080617|ref|NP_391444.1|', hit.query_id)
        self.assertEqual(1, len(hit))

        hsp = hit[0]
        self.assertEqual('gi|115975252|ref|XM_001180111.1|', hsp.hit_id)
        self.assertEqual('gi|16080617|ref|NP_391444.1|', hsp.query_id)
        self.assertEqual(33.90, hsp.ident_pct)
        self.assertEqual(59, hsp.aln_span)
        self.assertEqual(31, hsp.mismatch_num)
        self.assertEqual(1, hsp.gapopen_num)
        self.assertEqual(43, hsp.query_start)
        self.assertEqual(94, hsp.query_end)
        self.assertEqual(1056, hsp.hit_start)
        self.assertEqual(1233, hsp.hit_end)
        self.assertEqual(1e-04, hsp.evalue)
        self.assertEqual(31.6, hsp.bitscore)

        # test last qresult
        qresult = qresults.next()
        counter += 1

        self.assertEqual('gi|11464971:4-101', qresult.id)
        self.assertEqual(5, len(qresult))

        hit = qresult[0]
        self.assertEqual('gi|350596019|ref|XM_003360601.2|', hit.id)
        self.assertEqual('gi|11464971:4-101', hit.query_id)
        self.assertEqual(2, len(hit))

        hsp = hit[0]
        self.assertEqual('gi|350596019|ref|XM_003360601.2|', hsp.hit_id)
        self.assertEqual('gi|11464971:4-101', hsp.query_id)
        self.assertEqual(95.92, hsp.ident_pct)
        self.assertEqual(98, hsp.aln_span)
        self.assertEqual(4, hsp.mismatch_num)
        self.assertEqual(0, hsp.gapopen_num)
        self.assertEqual(0, hsp.query_start)
        self.assertEqual(98, hsp.query_end)
        self.assertEqual(94, hsp.hit_start)
        self.assertEqual(388, hsp.hit_end)
        self.assertEqual(2e-67, hsp.evalue)
        self.assertEqual(199, hsp.bitscore)

        hsp = hit[-1]
        self.assertEqual('gi|350596019|ref|XM_003360601.2|', hsp.hit_id)
        self.assertEqual('gi|11464971:4-101', hsp.query_id)
        self.assertEqual(29.58, hsp.ident_pct)
        self.assertEqual(71, hsp.aln_span)
        self.assertEqual(46, hsp.mismatch_num)
        self.assertEqual(2, hsp.gapopen_num)
        self.assertEqual(29, hsp.query_start)
        self.assertEqual(96, hsp.query_end)
        self.assertEqual(541, hsp.hit_start)
        self.assertEqual(754, hsp.hit_end)
        self.assertEqual(4e-05, hsp.evalue)
        self.assertEqual(32.7, hsp.bitscore)

        # check if we've finished iteration over qresults
        self.assertRaises(StopIteration, qresults.next, )
        self.assertEqual(2, counter)

    def test_tab_2226_tblastn_002(self):
        "Test parsing TBLASTN 2.2.26+ tabular output (tab_2226_tblastn_002)"

        xml_file = get_file('tab_2226_tblastn_002.txt')
        qresults = parse(xml_file, FMT)

        # check if we've finished iteration over qresults
        self.assertRaises(StopIteration, qresults.next, )

    def test_tab_2226_tblastn_003(self):
        "Test parsing TBLASTN 2.2.26+ tabular output (tab_2226_tblastn_003)"

        xml_file = get_file('tab_2226_tblastn_003.txt')
        qresults = parse(xml_file, FMT)
        counter = 0

        # test first qresult
        qresult = qresults.next()
        counter += 1

        self.assertEqual('gi|16080617|ref|NP_391444.1|', qresult.id)
        self.assertEqual(3, len(qresult))

        hit = qresult[0]
        self.assertEqual('gi|145479850|ref|XM_001425911.1|', hit.id)
        self.assertEqual('gi|16080617|ref|NP_391444.1|', hit.query_id)
        self.assertEqual(1, len(hit))

        hsp = hit[0]
        self.assertEqual('gi|145479850|ref|XM_001425911.1|', hsp.hit_id)
        self.assertEqual('gi|16080617|ref|NP_391444.1|', hsp.query_id)
        self.assertEqual(34.88, hsp.ident_pct)
        self.assertEqual(43, hsp.aln_span)
        self.assertEqual(28, hsp.mismatch_num)
        self.assertEqual(0, hsp.gapopen_num)
        self.assertEqual(30, hsp.query_start)
        self.assertEqual(73, hsp.query_end)
        self.assertEqual(1743, hsp.hit_start)
        self.assertEqual(1872, hsp.hit_end)
        self.assertEqual(1e-05, hsp.evalue)
        self.assertEqual(34.7, hsp.bitscore)

        hit = qresult[-1]
        self.assertEqual('gi|115975252|ref|XM_001180111.1|', hit.id)
        self.assertEqual('gi|16080617|ref|NP_391444.1|', hit.query_id)
        self.assertEqual(1, len(hit))

        hsp = hit[0]
        self.assertEqual('gi|115975252|ref|XM_001180111.1|', hsp.hit_id)
        self.assertEqual('gi|16080617|ref|NP_391444.1|', hsp.query_id)
        self.assertEqual(33.90, hsp.ident_pct)
        self.assertEqual(59, hsp.aln_span)
        self.assertEqual(31, hsp.mismatch_num)
        self.assertEqual(1, hsp.gapopen_num)
        self.assertEqual(43, hsp.query_start)
        self.assertEqual(94, hsp.query_end)
        self.assertEqual(1056, hsp.hit_start)
        self.assertEqual(1233, hsp.hit_end)
        self.assertEqual(1e-04, hsp.evalue)
        self.assertEqual(31.6, hsp.bitscore)

        # check if we've finished iteration over qresults
        self.assertRaises(StopIteration, qresults.next, )
        self.assertEqual(1, counter)

    def test_tab_2226_tblastn_004(self):
        "Test parsing TBLASTN 2.2.26+ tabular output (tab_2226_tblastn_004)"

        xml_file = get_file('tab_2226_tblastn_004.txt')
        qresults = parse(xml_file, FMT)
        counter = 0

        qresult = qresults.next()
        counter += 1

        self.assertEqual('gi|11464971:4-101', qresult.id)
        self.assertEqual(5, len(qresult))

        hit = qresult[0]
        self.assertEqual('gi|350596019|ref|XM_003360601.2|', hit.id)
        self.assertEqual('gi|11464971:4-101', hit.query_id)
        self.assertEqual(2, len(hit))

        hsp = hit[0]
        self.assertEqual('gi|350596019|ref|XM_003360601.2|', hsp.hit_id)
        self.assertEqual('gi|11464971:4-101', hsp.query_id)
        self.assertEqual(95.92, hsp.ident_pct)
        self.assertEqual(98, hsp.aln_span)
        self.assertEqual(4, hsp.mismatch_num)
        self.assertEqual(0, hsp.gapopen_num)
        self.assertEqual(0, hsp.query_start)
        self.assertEqual(98, hsp.query_end)
        self.assertEqual(94, hsp.hit_start)
        self.assertEqual(388, hsp.hit_end)
        self.assertEqual(2e-67, hsp.evalue)
        self.assertEqual(199, hsp.bitscore)

        hsp = hit[-1]
        self.assertEqual('gi|350596019|ref|XM_003360601.2|', hsp.hit_id)
        self.assertEqual('gi|11464971:4-101', hsp.query_id)
        self.assertEqual(29.58, hsp.ident_pct)
        self.assertEqual(71, hsp.aln_span)
        self.assertEqual(46, hsp.mismatch_num)
        self.assertEqual(2, hsp.gapopen_num)
        self.assertEqual(29, hsp.query_start)
        self.assertEqual(96, hsp.query_end)
        self.assertEqual(541, hsp.hit_start)
        self.assertEqual(754, hsp.hit_end)
        self.assertEqual(4e-05, hsp.evalue)
        self.assertEqual(32.7, hsp.bitscore)

        # check if we've finished iteration over qresults
        self.assertRaises(StopIteration, qresults.next, )
        self.assertEqual(1, counter)

    def test_tab_2226_tblastn_005(self):
        "Test parsing TBLASTN 2.2.26+ tabular output with comments (tab_2226_tblastn_005)"

        xml_file = get_file('tab_2226_tblastn_005.txt')
        qresults = parse(xml_file, FMT)
        counter = 0

        # test first qresult
        qresult = qresults.next()
        counter += 1

        self.assertEqual('tblastn', qresult.program)
        self.assertEqual('db/minirefseq_mrna', qresult.target)
        self.assertEqual('2.2.26+', qresult.version)
        self.assertEqual('random_s00', qresult.id)
        self.assertEqual(0, len(qresult))

        # test second qresult
        qresult = qresults.next()
        counter += 1

        self.assertEqual('tblastn', qresult.program)
        self.assertEqual('db/minirefseq_mrna', qresult.target)
        self.assertEqual('2.2.26+', qresult.version)
        self.assertEqual('gi|16080617|ref|NP_391444.1|', qresult.id)
        self.assertEqual(3, len(qresult))

        hit = qresult[0]
        self.assertEqual('gi|145479850|ref|XM_001425911.1|', hit.id)
        self.assertEqual('gi|16080617|ref|NP_391444.1|', hit.query_id)
        self.assertEqual(1, len(hit))

        hsp = hit[0]
        self.assertEqual('gi|145479850|ref|XM_001425911.1|', hsp.hit_id)
        self.assertEqual('gi|16080617|ref|NP_391444.1|', hsp.query_id)
        self.assertEqual(34.88, hsp.ident_pct)
        self.assertEqual(43, hsp.aln_span)
        self.assertEqual(28, hsp.mismatch_num)
        self.assertEqual(0, hsp.gapopen_num)
        self.assertEqual(30, hsp.query_start)
        self.assertEqual(73, hsp.query_end)
        self.assertEqual(1743, hsp.hit_start)
        self.assertEqual(1872, hsp.hit_end)
        self.assertEqual(1e-05, hsp.evalue)
        self.assertEqual(34.7, hsp.bitscore)

        hit = qresult[-1]
        self.assertEqual('gi|115975252|ref|XM_001180111.1|', hit.id)
        self.assertEqual('gi|16080617|ref|NP_391444.1|', hit.query_id)
        self.assertEqual(1, len(hit))

        hsp = hit[0]
        self.assertEqual('gi|115975252|ref|XM_001180111.1|', hsp.hit_id)
        self.assertEqual('gi|16080617|ref|NP_391444.1|', hsp.query_id)
        self.assertEqual(33.90, hsp.ident_pct)
        self.assertEqual(59, hsp.aln_span)
        self.assertEqual(31, hsp.mismatch_num)
        self.assertEqual(1, hsp.gapopen_num)
        self.assertEqual(43, hsp.query_start)
        self.assertEqual(94, hsp.query_end)
        self.assertEqual(1056, hsp.hit_start)
        self.assertEqual(1233, hsp.hit_end)
        self.assertEqual(1e-04, hsp.evalue)
        self.assertEqual(31.6, hsp.bitscore)

        # test last qresult
        qresult = qresults.next()
        counter += 1

        self.assertEqual('tblastn', qresult.program)
        self.assertEqual('db/minirefseq_mrna', qresult.target)
        self.assertEqual('2.2.26+', qresult.version)
        self.assertEqual('gi|11464971:4-101', qresult.id)
        self.assertEqual(5, len(qresult))

        hit = qresult[0]
        self.assertEqual('gi|350596019|ref|XM_003360601.2|', hit.id)
        self.assertEqual('gi|11464971:4-101', hit.query_id)
        self.assertEqual(2, len(hit))

        hsp = hit[0]
        self.assertEqual('gi|350596019|ref|XM_003360601.2|', hsp.hit_id)
        self.assertEqual('gi|11464971:4-101', hsp.query_id)
        self.assertEqual(95.92, hsp.ident_pct)
        self.assertEqual(98, hsp.aln_span)
        self.assertEqual(4, hsp.mismatch_num)
        self.assertEqual(0, hsp.gapopen_num)
        self.assertEqual(0, hsp.query_start)
        self.assertEqual(98, hsp.query_end)
        self.assertEqual(94, hsp.hit_start)
        self.assertEqual(388, hsp.hit_end)
        self.assertEqual(2e-67, hsp.evalue)
        self.assertEqual(199, hsp.bitscore)

        hsp = hit[-1]
        self.assertEqual('gi|350596019|ref|XM_003360601.2|', hsp.hit_id)
        self.assertEqual('gi|11464971:4-101', hsp.query_id)
        self.assertEqual(29.58, hsp.ident_pct)
        self.assertEqual(71, hsp.aln_span)
        self.assertEqual(46, hsp.mismatch_num)
        self.assertEqual(2, hsp.gapopen_num)
        self.assertEqual(29, hsp.query_start)
        self.assertEqual(96, hsp.query_end)
        self.assertEqual(541, hsp.hit_start)
        self.assertEqual(754, hsp.hit_end)
        self.assertEqual(4e-05, hsp.evalue)
        self.assertEqual(32.7, hsp.bitscore)

        # check if we've finished iteration over qresults
        self.assertRaises(StopIteration, qresults.next, )
        self.assertEqual(3, counter)

    def test_tab_2226_tblastn_006(self):
        "Test parsing TBLASTN 2.2.26+ tabular output with comments (tab_2226_tblastn_006)"

        xml_file = get_file('tab_2226_tblastn_006.txt')
        qresults = parse(xml_file, FMT)
        counter = 0

        qresult = qresults.next()
        counter += 1

        self.assertEqual('tblastn', qresult.program)
        self.assertEqual('db/minirefseq_mrna', qresult.target)
        self.assertEqual('2.2.26+', qresult.version)
        self.assertEqual('random_s00', qresult.id)
        self.assertEqual(0, len(qresult))

        # check if we've finished iteration over qresults
        self.assertRaises(StopIteration, qresults.next, )
        self.assertEqual(1, counter)

    def test_tab_2226_tblastn_007(self):
        "Test parsing TBLASTN 2.2.26+ tabular output with comments (tab_2226_tblastn_007)"

        xml_file = get_file('tab_2226_tblastn_007.txt')
        qresults = parse(xml_file, FMT)
        counter = 0

        qresult = qresults.next()
        counter += 1

        self.assertEqual('tblastn', qresult.program)
        self.assertEqual('db/minirefseq_mrna', qresult.target)
        self.assertEqual('2.2.26+', qresult.version)
        self.assertEqual('gi|16080617|ref|NP_391444.1|', qresult.id)
        self.assertEqual(3, len(qresult))

        hit = qresult[0]
        self.assertEqual('gi|145479850|ref|XM_001425911.1|', hit.id)
        self.assertEqual('gi|16080617|ref|NP_391444.1|', hit.query_id)
        self.assertEqual(1, len(hit))

        hsp = hit[0]
        self.assertEqual('gi|145479850|ref|XM_001425911.1|', hsp.hit_id)
        self.assertEqual('gi|16080617|ref|NP_391444.1|', hsp.query_id)
        self.assertEqual(34.88, hsp.ident_pct)
        self.assertEqual(43, hsp.aln_span)
        self.assertEqual(28, hsp.mismatch_num)
        self.assertEqual(0, hsp.gapopen_num)
        self.assertEqual(30, hsp.query_start)
        self.assertEqual(73, hsp.query_end)
        self.assertEqual(1743, hsp.hit_start)
        self.assertEqual(1872, hsp.hit_end)
        self.assertEqual(1e-05, hsp.evalue)
        self.assertEqual(34.7, hsp.bitscore)

        hit = qresult[-1]
        self.assertEqual('gi|115975252|ref|XM_001180111.1|', hit.id)
        self.assertEqual('gi|16080617|ref|NP_391444.1|', hit.query_id)
        self.assertEqual(1, len(hit))

        hsp = hit[0]
        self.assertEqual('gi|115975252|ref|XM_001180111.1|', hsp.hit_id)
        self.assertEqual('gi|16080617|ref|NP_391444.1|', hsp.query_id)
        self.assertEqual(33.90, hsp.ident_pct)
        self.assertEqual(59, hsp.aln_span)
        self.assertEqual(31, hsp.mismatch_num)
        self.assertEqual(1, hsp.gapopen_num)
        self.assertEqual(43, hsp.query_start)
        self.assertEqual(94, hsp.query_end)
        self.assertEqual(1056, hsp.hit_start)
        self.assertEqual(1233, hsp.hit_end)
        self.assertEqual(1e-04, hsp.evalue)
        self.assertEqual(31.6, hsp.bitscore)

        # check if we've finished iteration over qresults
        self.assertRaises(StopIteration, qresults.next, )
        self.assertEqual(1, counter)

    def test_tab_2226_tblastn_008(self):
        "Test parsing TBLASTN 2.2.26+ tabular output with comments (tab_2226_tblastn_008)"

        xml_file = get_file('tab_2226_tblastn_008.txt')
        qresults = parse(xml_file, FMT)
        counter = 0

        qresult = qresults.next()
        counter += 1

        self.assertEqual('tblastn', qresult.program)
        self.assertEqual('db/minirefseq_mrna', qresult.target)
        self.assertEqual('2.2.26+', qresult.version)
        self.assertEqual('gi|11464971:4-101', qresult.id)
        self.assertEqual(5, len(qresult))

        hit = qresult[0]
        self.assertEqual('gi|350596019|ref|XM_003360601.2|', hit.id)
        self.assertEqual('gi|11464971:4-101', hit.query_id)
        self.assertEqual(2, len(hit))

        hsp = hit[0]
        self.assertEqual('gi|350596019|ref|XM_003360601.2|', hsp.hit_id)
        self.assertEqual('gi|11464971:4-101', hsp.query_id)
        self.assertEqual(95.92, hsp.ident_pct)
        self.assertEqual(98, hsp.aln_span)
        self.assertEqual(4, hsp.mismatch_num)
        self.assertEqual(0, hsp.gapopen_num)
        self.assertEqual(0, hsp.query_start)
        self.assertEqual(98, hsp.query_end)
        self.assertEqual(94, hsp.hit_start)
        self.assertEqual(388, hsp.hit_end)
        self.assertEqual(2e-67, hsp.evalue)
        self.assertEqual(199, hsp.bitscore)

        hsp = hit[-1]
        self.assertEqual('gi|350596019|ref|XM_003360601.2|', hsp.hit_id)
        self.assertEqual('gi|11464971:4-101', hsp.query_id)
        self.assertEqual(29.58, hsp.ident_pct)
        self.assertEqual(71, hsp.aln_span)
        self.assertEqual(46, hsp.mismatch_num)
        self.assertEqual(2, hsp.gapopen_num)
        self.assertEqual(29, hsp.query_start)
        self.assertEqual(96, hsp.query_end)
        self.assertEqual(541, hsp.hit_start)
        self.assertEqual(754, hsp.hit_end)
        self.assertEqual(4e-05, hsp.evalue)
        self.assertEqual(32.7, hsp.bitscore)

        # check if we've finished iteration over qresults
        self.assertRaises(StopIteration, qresults.next, )
        self.assertEqual(1, counter)

    def test_tab_2226_tblastn_009(self):
        "Test parsing TBLASTN 2.2.26+ tabular output (tab_2226_tblastn_009)"

        xml_file = get_file('tab_2226_tblastn_009.txt')
        qresults = parse(xml_file, FMT)

        # nonstandard, noncommented output should raise an error
        self.assertRaises(AssertionError, qresults.next, )

    def test_tab_2226_tblastn_010(self):
        "Test parsing TBLASTN 2.2.26+ tabular output with comments (tab_2226_tblastn_010)"

        xml_file = get_file('tab_2226_tblastn_010.txt')
        qresults = parse(xml_file, FMT)
        counter = 0

        # test first qresult
        qresult = qresults.next()
        counter += 1

        self.assertEqual('tblastn', qresult.program)
        self.assertEqual('db/minirefseq_mrna', qresult.target)
        self.assertEqual('2.2.26+', qresult.version)
        self.assertEqual('random_s00', qresult.id)
        self.assertEqual(0, len(qresult))

        # test second qresult
        qresult = qresults.next()
        counter += 1

        self.assertEqual('tblastn', qresult.program)
        self.assertEqual('db/minirefseq_mrna', qresult.target)
        self.assertEqual('2.2.26+', qresult.version)
        self.assertEqual('gi|16080617|ref|NP_391444.1|', qresult.id)
        self.assertEqual(3, len(qresult))

        hit = qresult[0]
        self.assertEqual('gi|145479850|ref|XM_001425911.1|', hit.id)
        self.assertEqual('gi|16080617|ref|NP_391444.1|', hit.query_id)
        self.assertEqual(1, len(hit))

        hsp = hit[0]
        self.assertEqual('gi|145479850|ref|XM_001425911.1|', hsp.hit_id)
        self.assertEqual('gi|16080617|ref|NP_391444.1|', hsp.query_id)
        self.assertEqual(1e-05, hsp.evalue)
        self.assertEqual(34.7, hsp.bitscore)

        hit = qresult[-1]
        self.assertEqual('gi|115975252|ref|XM_001180111.1|', hit.id)
        self.assertEqual('gi|16080617|ref|NP_391444.1|', hit.query_id)
        self.assertEqual(1, len(hit))

        hsp = hit[0]
        self.assertEqual('gi|115975252|ref|XM_001180111.1|', hsp.hit_id)
        self.assertEqual('gi|16080617|ref|NP_391444.1|', hsp.query_id)
        self.assertEqual(1e-04, hsp.evalue)
        self.assertEqual(31.6, hsp.bitscore)

        # test last qresult
        qresult = qresults.next()
        counter += 1

        self.assertEqual('tblastn', qresult.program)
        self.assertEqual('db/minirefseq_mrna', qresult.target)
        self.assertEqual('2.2.26+', qresult.version)
        self.assertEqual('gi|11464971:4-101', qresult.id)
        self.assertEqual(5, len(qresult))

        hit = qresult[0]
        self.assertEqual('gi|350596019|ref|XM_003360601.2|', hit.id)
        self.assertEqual('gi|11464971:4-101', hit.query_id)
        self.assertEqual(2, len(hit))

        hsp = hit[0]
        self.assertEqual('gi|350596019|ref|XM_003360601.2|', hsp.hit_id)
        self.assertEqual('gi|11464971:4-101', hsp.query_id)
        self.assertEqual(2e-67, hsp.evalue)
        self.assertEqual(199, hsp.bitscore)

        hsp = hit[-1]
        self.assertEqual('gi|350596019|ref|XM_003360601.2|', hsp.hit_id)
        self.assertEqual('gi|11464971:4-101', hsp.query_id)
        self.assertEqual(4e-05, hsp.evalue)
        self.assertEqual(32.7, hsp.bitscore)

        # check if we've finished iteration over qresults
        self.assertRaises(StopIteration, qresults.next, )
        self.assertEqual(3, counter)

    def test_tab_2226_tblastn_011(self):
        "Test parsing TBLASTN 2.2.26+ tabular output with comments (tab_2226_tblastn_011)"

        xml_file = get_file('tab_2226_tblastn_011.txt')
        qresults = parse(xml_file, FMT)
        counter = 0

        # test first qresult
        qresult = qresults.next()
        counter += 1

        self.assertEqual('tblastn', qresult.program)
        self.assertEqual('db/minirefseq_mrna', qresult.target)
        self.assertEqual('2.2.26+', qresult.version)
        self.assertEqual('random_s00', qresult.id)
        self.assertEqual(0, len(qresult))

        # test second qresult
        # TODO: remove after py2.5 deprecation
        if sys.version_info[:2] > (2, 5):
            with warnings.catch_warnings(record=True) as w:
                warnings.simplefilter('always')
                qresult = qresults.next()
                counter += 1
                # 1 warning for 1 unsupported column
                self.assertEqual(len(w), 1)
                self.assertTrue(issubclass(w[-1].category, UserWarning))
        else:
            qresult = qresults.next()
            counter += 1

        self.assertEqual('tblastn', qresult.program)
        self.assertEqual('db/minirefseq_mrna', qresult.target)
        self.assertEqual('2.2.26+', qresult.version)
        self.assertEqual('gi|16080617|ref|NP_391444.1|', qresult.id)
        self.assertEqual('gi|16080617|ref|NP_391444.1|', qresult.acc)
        self.assertEqual('gi|16080617|ref|NP_391444.1|', qresult.acc_ver)
        self.assertEqual('0', qresult.gi)
        self.assertEqual(102, qresult.seq_len)
        self.assertEqual(3, len(qresult))

        hit = qresult[0]
        self.assertEqual('gi|145479850|ref|XM_001425911.1|', hit.id)
        self.assertEqual('gi|145479850|ref|XM_001425911.1|', hit.id_all)
        self.assertEqual('gi|145479850|ref|XM_001425911.1|', hit.acc)
        self.assertEqual('gi|145479850|ref|XM_001425911.1|', hit.acc_ver)
        self.assertEqual('0', hit.gi)
        self.assertEqual('0', hit.gi_all)
        self.assertEqual('gi|16080617|ref|NP_391444.1|', hit.query_id)
        self.assertEqual(4632, hit.seq_len)
        self.assertEqual(1, len(hit))

        hsp = hit[0]
        self.assertEqual('gi|145479850|ref|XM_001425911.1|', hsp.hit_id)
        self.assertEqual('gi|16080617|ref|NP_391444.1|', hsp.query_id)
        self.assertEqual(34.88, hsp.ident_pct)
        self.assertEqual(43, hsp.aln_span)
        self.assertEqual(28, hsp.mismatch_num)
        self.assertEqual(0, hsp.gapopen_num)
        self.assertEqual(30, hsp.query_start)
        self.assertEqual(73, hsp.query_end)
        self.assertEqual(1743, hsp.hit_start)
        self.assertEqual(1872, hsp.hit_end)
        self.assertEqual(1e-05, hsp.evalue)
        self.assertEqual(34.7, hsp.bitscore)
        self.assertEqual('PDSNIETKEGTYVGLADTHTIEVTVDNEPVSLDITEESTSDLD', str(hsp.query.seq))
        self.assertEqual('PKTATGTKKGTIIGLLSIHTILFILTSHALSLEVKEQT*KDID', str(hsp.hit.seq))
        self.assertEqual(78, hsp.bitscore_raw)
        self.assertEqual(15, hsp.ident_num)
        self.assertEqual(26, hsp.pos_num)
        self.assertEqual(0, hsp.gap_num)
        self.assertEqual(60.47, hsp.pos_pct)
        self.assertEqual(0, hsp.query_frame)
        self.assertEqual(1, hsp.hit_frame)

        hit = qresult[-1]
        self.assertEqual('gi|115975252|ref|XM_001180111.1|', hit.id)
        self.assertEqual('gi|115975252|ref|XM_001180111.1|', hit.acc)
        self.assertEqual('gi|115975252|ref|XM_001180111.1|', hit.acc_ver)
        self.assertEqual('gi|16080617|ref|NP_391444.1|', hit.query_id)
        self.assertEqual(1, len(hit))

        hsp = hit[0]
        self.assertEqual('gi|115975252|ref|XM_001180111.1|', hsp.hit_id)
        self.assertEqual('gi|16080617|ref|NP_391444.1|', hsp.query_id)
        self.assertEqual(33.90, hsp.ident_pct)
        self.assertEqual(59, hsp.aln_span)
        self.assertEqual(31, hsp.mismatch_num)
        self.assertEqual(1, hsp.gapopen_num)
        self.assertEqual(43, hsp.query_start)
        self.assertEqual(94, hsp.query_end)
        self.assertEqual(1056, hsp.hit_start)
        self.assertEqual(1233, hsp.hit_end)
        self.assertEqual(1e-04, hsp.evalue)
        self.assertEqual(31.6, hsp.bitscore)
        self.assertEqual('GLADTHTIEVTVDNEPVSLDITEESTSDLDKFNSG--------DKVTITYEKNDEGQLL', str(hsp.query.seq))
        self.assertEqual('GLVPDHTLILPVGHYQSMLDLTEEVQTELDQFKSALRKYYLSKGKTCVIYERNFRTQHL', str(hsp.hit.seq))
        self.assertEqual(70.0, hsp.bitscore_raw)
        self.assertEqual(20, hsp.ident_num)
        self.assertEqual(29, hsp.pos_num)
        self.assertEqual(8, hsp.gap_num)
        self.assertEqual(49.15, hsp.pos_pct)
        self.assertEqual(0, hsp.query_frame)
        self.assertEqual(1, hsp.hit_frame)

        # test last qresult
        # TODO: remove after py2.5 deprecation
        if sys.version_info[:2] > (2, 5):
            with warnings.catch_warnings(record=True) as w:
                warnings.simplefilter('always')
                qresult = qresults.next()
                counter += 1
                # 1 warning for 1 unsupported column
                self.assertEqual(len(w), 1)
                self.assertTrue(issubclass(w[-1].category, UserWarning))
        else:
            qresult = qresults.next()
            counter += 1

        self.assertEqual('tblastn', qresult.program)
        self.assertEqual('db/minirefseq_mrna', qresult.target)
        self.assertEqual('2.2.26+', qresult.version)
        self.assertEqual('gi|11464971:4-101', qresult.id)
        self.assertEqual('gi|11464971:4-101', qresult.acc)
        self.assertEqual('gi|11464971:4-101', qresult.acc_ver)
        self.assertEqual('0', qresult.gi)
        self.assertEqual(98, qresult.seq_len)
        self.assertEqual(5, len(qresult))

        hit = qresult[0]
        self.assertEqual('gi|350596019|ref|XM_003360601.2|', hit.id)
        self.assertEqual('gi|350596019|ref|XM_003360601.2|', hit.id_all)
        self.assertEqual('gi|350596019|ref|XM_003360601.2|', hit.acc)
        self.assertEqual('gi|350596019|ref|XM_003360601.2|', hit.acc_ver)
        self.assertEqual('0', hit.gi)
        self.assertEqual('0', hit.gi_all)
        self.assertEqual('gi|11464971:4-101', hit.query_id)
        self.assertEqual(772, hit.seq_len)
        self.assertEqual(2, len(hit))

        hsp = hit[0]
        self.assertEqual('gi|350596019|ref|XM_003360601.2|', hsp.hit_id)
        self.assertEqual('gi|11464971:4-101', hsp.query_id)
        self.assertEqual(95.92, hsp.ident_pct)
        self.assertEqual(98, hsp.aln_span)
        self.assertEqual(4, hsp.mismatch_num)
        self.assertEqual(0, hsp.gapopen_num)
        self.assertEqual(0, hsp.query_start)
        self.assertEqual(98, hsp.query_end)
        self.assertEqual(94, hsp.hit_start)
        self.assertEqual(388, hsp.hit_end)
        self.assertEqual(2e-67, hsp.evalue)
        self.assertEqual(199, hsp.bitscore)
        self.assertEqual('KRIREGYLVKKGSVFNTWKPMWVVLLEDGIEFYKKKSDNSPKGMIPLKGSTLTSPCQDFGKRMFVLKITTTKQQDHFFQAAFLEERDAWVRDIKKAIK', str(hsp.query.seq))
        self.assertEqual('KRIREGYLVKKGSMFNTWKPMWVILLEDGIEFYKKKSDNSPKGMIPLKGSTLTSPCQDFGKRMFVFKITTTKQQDHFFQAAFLEERDGWVRDIKKAIK', str(hsp.hit.seq))
        self.assertEqual(506.0, hsp.bitscore_raw)
        self.assertEqual(94, hsp.ident_num)
        self.assertEqual(96, hsp.pos_num)
        self.assertEqual(0, hsp.gap_num)
        self.assertEqual(97.96, hsp.pos_pct)
        self.assertEqual(0, hsp.query_frame)
        self.assertEqual(2, hsp.hit_frame)

        hsp = hit[-1]
        self.assertEqual('gi|350596019|ref|XM_003360601.2|', hsp.hit_id)
        self.assertEqual('gi|11464971:4-101', hsp.query_id)
        self.assertEqual(29.58, hsp.ident_pct)
        self.assertEqual(71, hsp.aln_span)
        self.assertEqual(46, hsp.mismatch_num)
        self.assertEqual(2, hsp.gapopen_num)
        self.assertEqual(29, hsp.query_start)
        self.assertEqual(96, hsp.query_end)
        self.assertEqual(541, hsp.hit_start)
        self.assertEqual(754, hsp.hit_end)
        self.assertEqual(4e-05, hsp.evalue)
        self.assertEqual(32.7, hsp.bitscore)
        self.assertEqual('IEFYKKKSDNSPKGMIPLKGSTLTS-PCQDFGKRMFVLK---ITTTKQQDHFFQAAFLEERDAWVRDIKKA', str(hsp.query.seq))
        self.assertEqual('LHYYDPAGGEDPLGAIHLRGCVVTSVESNTDGKNGFLWERAXXITADEVHYFLQAANPKERTEWIKAIQVA', str(hsp.hit.seq))
        self.assertEqual(73.0, hsp.bitscore_raw)
        self.assertEqual(21, hsp.ident_num)
        self.assertEqual(33, hsp.pos_num)
        self.assertEqual(4, hsp.gap_num)
        self.assertEqual(46.48, hsp.pos_pct)
        self.assertEqual(0, hsp.query_frame)
        self.assertEqual(2, hsp.hit_frame)

        # check if we've finished iteration over qresults
        self.assertRaises(StopIteration, qresults.next, )
        self.assertEqual(3, counter)

    def test_tab_2226_tblastn_012(self):
        "Test parsing TBLASTN 2.2.26+ tabular output with comments (tab_2226_tblastn_012)"

        xml_file = get_file('tab_2226_tblastn_012.txt')
        qresults = parse(xml_file, FMT)
        counter = 0

        # test first qresult
        qresult = qresults.next()
        counter += 1

        self.assertEqual('tblastn', qresult.program)
        self.assertEqual('refseq_rna', qresult.target)
        self.assertEqual('2.2.26+', qresult.version)
        self.assertEqual('random_s00', qresult.id)
        self.assertEqual('X76FDCG9016', qresult.rid)
        self.assertEqual(0, len(qresult))

        # test second qresult
        qresult = qresults.next()
        counter += 1

        self.assertEqual('tblastn', qresult.program)
        self.assertEqual('refseq_rna', qresult.target)
        self.assertEqual('2.2.26+', qresult.version)
        self.assertEqual('gi|16080617|ref|NP_391444.1|', qresult.id)
        self.assertEqual('X76FDCG9016', qresult.rid)
        self.assertEqual(3, len(qresult))

        # test last qresult
        qresult = qresults.next()
        counter += 1

        self.assertEqual('tblastn', qresult.program)
        self.assertEqual('refseq_rna', qresult.target)
        self.assertEqual('2.2.26+', qresult.version)
        self.assertEqual('gi|11464971:4-101', qresult.id)
        self.assertEqual('X76FDCG9016', qresult.rid)
        self.assertEqual(5, len(qresult))

        # check if we've finished iteration over qresults
        self.assertRaises(StopIteration, qresults.next, )
        self.assertEqual(3, counter)


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity = 2)
    unittest.main(testRunner=runner)
