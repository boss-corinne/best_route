"""
Tests for best_route using test case(s) supplied.

"""
import os
import subprocess
import pytest


HERE = os.path.abspath(os.path.dirname(__file__))
TESTDATA = os.path.abspath(os.path.join(HERE, 'testdata'))
print(TESTDATA)

class TestBestRouteExmouth():
    def setup_class(self):
        self.fpath = os.path.join(TESTDATA, 'exmouth-links.dat')
        # origin = None
        # destination = None
        # self.get_best_route = 'best_route {} {} {}'.format(fname,
        #                                                    origin,
        #                                                    destination)


    def test_neighbours(self):
        fname = self.fname
        origin = 'J1001'
        destination = 'J1002'
        get_best_route = 'best_route {} {} {}'.format(fname,
                                                      origin,
                                                      destination)
        self.best_route = subprocess.run(get_best_route)
        assert subprocess.CompletedProcess.returncode == 0
        self.output = subprocess.check_output(get_best_route,
                                              stderr=subprocess.STDOUT,
                                              shell=True)
        # TODO Run some checks on the output

    def test_bad_start_node(self):
        # TODO: This.
        pass

    def test_bad_end_node(self):
        # TODO: This.
        pass


if __name__ == '__main__':
    pytest.main()