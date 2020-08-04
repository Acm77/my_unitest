#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import time
import unittest
from my_unitest.console_color import ColorWritelnDecorator


class MyTestResult(unittest.TestResult):
    separator1 = '[-------------] '
    separator2 = '[=============] '

    def __init__(self, stream=sys.stderr, descriptions=1, verbosity=1):
        unittest.TestResult.__init__(self)
        self.stream = stream
        self.showAll = verbosity > 1
        self.dots = verbosity == 1
        self.descriptions = descriptions

    def getDescription(self, test):
        if self.descriptions:
            return test.shortDescription() or str(test)
        else:
            return str(test)

    def startTest(self, test):
        self.stream.green('[-----Run-----] ')
        self.stream.write(self.getDescription(test))
        self.stream.writeln()
        unittest.TestResult.startTest(self, test)
        # if self.showAll:
        #     self.stream.write(self.getDescription(test))
        #     self.stream.write(" ... ")

    def addSuccess(self, test):
        unittest.TestResult.addSuccess(self, test)
        if self.showAll:
            self.stream.write("ok")
            self.stream.writeln()
        elif self.dots:
            self.stream.green('[-----OK------] ')
            self.stream.write(self.getDescription(test))
            self.stream.writeln()

    def addError(self, test, err):
        unittest.TestResult.addError(self, test, err)
        if self.showAll:
            self.stream.write('E')
            self.stream.writeln()
        elif self.dots:
            self.stream.red('[----ERROR----] ')
            self.stream.red(self.getDescription(test))
            self.stream.writeln()
            self.stream.write(self._exc_info_to_string(err, test))
            self.stream.writeln()

    def addFailure(self, test, err):
        unittest.TestResult.addFailure(self, test, err)
        if self.showAll:
            self.stream.write("FAIL")
            self.stream.writeln()
        elif self.dots:
            self.stream.red('[----FAILED---] ')
            self.stream.write(self.getDescription(test))
            self.stream.writeln()
            self.stream.write(self._exc_info_to_string(err, test))
            self.stream.writeln()


class MyTestRunner:
    def __init__(self, stream=sys.stderr, descriptions=1, verbosity=1):
        self.stream = ColorWritelnDecorator(stream)
        self.descriptions = descriptions
        self.verbosity = verbosity

    def run(self, test):
        result = MyTestResult(self.stream, self.descriptions, self.verbosity)
        self.stream.yellow('Note: Your Unit Tests Starts')
        self.stream.writeln()
        startTime = time.time()
        test(result)
        stopTime = time.time()
        timeTaken = stopTime - startTime
        self.stream.green(result.separator2)
        run = result.testsRun
        self.stream.write("Ran %d test%s in %.3fs" %
                          (run, run != 1 and "s" or "", timeTaken))
        self.stream.writeln()

        failed, errored = map(len, (result.failures, result.errors))

        self.stream.green("[  PASSED  ] %d tests" % (run - failed - errored))
        self.stream.writeln()

        if not result.wasSuccessful():
            errorsummary = ""
            if failed:
                self.stream.red("[  FAILED  ] %d tests, listed below:" % failed)
                self.stream.writeln()
                for failedtest, failederorr in result.failures:
                    self.stream.red("[  FAILED  ] %s" % failedtest)
                    self.stream.writeln()
            if errored:
                self.stream.red("[  ERRORED ] %d tests" % errored)
                self.stream.writeln()
                for erroredtest, erorrmsg in result.errors:
                    self.stream.red("[  ERRORED ] %s" % erroredtest)
                    self.stream.writeln()

            self.stream.writeln()
            if failed:
                self.stream.write("%d FAILED TEST" % failed)
            if errored:
                self.stream.write("%d ERRORED TEST" % errored)

        return result
