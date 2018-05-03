#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
The MetadataWizard(pymdwizard) software was developed by the
U.S. Geological Survey Fort Collins Science Center.
See: https://github.com/usgs/fort-pymdwizard for current project source code
See: https://usgs.github.io/fort-pymdwizard/ for current user documentation
See: https://github.com/usgs/fort-pymdwizard/tree/master/examples
    for examples of use in other scripts

License:            Creative Commons Attribution 4.0 International (CC BY 4.0)
                    http://creativecommons.org/licenses/by/4.0/

PURPOSE
------------------------------------------------------------------------------
Contains a


SCRIPT DEPENDENCIES
------------------------------------------------------------------------------
    This script is part of the pymdwizard package and is not intented to be
    used independently.  All pymdwizard package requirements are needed.

    See imports section for external packages used in this script as well as
    inter-package dependencies


U.S. GEOLOGICAL SURVEY DISCLAIMER
------------------------------------------------------------------------------
This software has been approved for release by the U.S. Geological Survey (USGS).
Although the software has been subjected to rigorous review,
the USGS reserves the right to update the software as needed pursuant to
further analysis and review. No warranty, expressed or implied, is made by
the USGS or the U.S. Government as to the functionality of the software and
related material nor shall the fact of release constitute any such warranty.
Furthermore, the software is released on condition that neither the USGS nor
the U.S. Government shall be held liable for any damages resulting from
its authorized or unauthorized use.

Any use of trade, product or firm names is for descriptive purposes only and
does not imply endorsement by the U.S. Geological Survey.

Although this information product, for the most part, is in the public domain,
it also contains copyrighted material as noted in the text. Permission to
reproduce copyrighted items for other than personal use must be secured from
the copyright owner.
------------------------------------------------------------------------------
"""

from PyQt5 import QtCore, QtGui
import re

from pymdwizard.core import utils


def load_words():

    fname = utils.get_resource_path("spelling/words.txt")
    global word_set
    try:
        word_set = set(line.strip() for line in open(fname, 'r'))
    except UnicodeDecodeError:
        word_set = set(line.strip() for line in open(fname, 'r', encoding='latin-1'))

    return word_set

word_set = load_words()


class Highlighter(QtGui.QSyntaxHighlighter):
    """
    An implementation of a custom syntax highlighter that highlights
    misspelled words
    """
    def __init__(self, parent):
        super(Highlighter, self).__init__(parent)
        self.sectionFormat = QtGui.QTextCharFormat()
        self.sectionFormat.setForeground(QtCore.Qt.blue)
        self.errorFormat = QtGui.QTextCharFormat()
        self.errorFormat.setForeground(QtCore.Qt.red)
        self.errorFormat.setBackground(QtCore.Qt.yellow)

        # Only hightlight when the hightlighter is enabled
        self.enabled = True

    def highlightBlock(self, text):
        """

        Parameters
        ----------
        text

        Returns
        -------

        """
        if not self.enabled:
            return None

        words = re.findall(r"[\w]+", text)

        for word in words:
            if word.lower() not in word_set and \
                    re.search('[a-zA-Z]', word) is not None:
                clean = ' ' + re.sub(r"[^a-zA-Z]", " ", text) + ' '
                try:
                    self.setFormat(clean.index(" {} ".format(word)), len(word),
                                       self.errorFormat)
                except ValueError:
                    pass
