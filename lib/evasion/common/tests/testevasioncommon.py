# -*- coding: utf-8 -*-
"""
"""
import unittest

from evasion.common import signal


class CommonTC(unittest.TestCase):


    def testSignal(self):
        """Test the helper code provided by signal.
        """
        c = signal.CallBack(timeout=1)

        # Test the timeout waiting raises WaitTimeout
        self.assertRaises(signal.WaitTimeout, c.wait)
        self.assertEquals(c.data, None)

        c(1)
        c.wait()
        self.assertEquals(c.data, 1)


    def testNetTools(self):
        """
        """
        self.assertEquals(1,0, "Not tested: evasion.common.net")
