"""
Tests for best_route using test case(s) supplied.

"""
import os
import subprocess
import pytest


HERE = os.path.abspath(os.path.dirname(__file__))
TESTDATA = os.path.abspath(os.path.dirname(os.path.join(HERE,
                                                        'testdata')))

class TestBestRouteExmouth():
    def setup_class(self):
        fname = os.path.join(TESTDATA, 'exmouth-links.dat')
        origin = TBC  # TODO Complete this
        destination = TBC  # TODO Complete this
        self.get_best_route = 'best_route {} {} {}'.format(fname,
                                                           origin,
                                                           destination)


    def test_nodaA_nodeB(self):
        self.best_route = subprocess.run([self.get_best_route])
        assert subprocess.CompletedProcess.returncode == 0
        self.output = subprocess.check_output(get_envs,
                                              stderr=subprocess.STDOUT,
                                              shell=True)
        # TODO Run some checks on the output


if __name__ == '__main__':
    pytest.main()