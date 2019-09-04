
import numpy as np

import pytest


class TestCaseNormal:

    @pytest.fixture
    def normal(self):
        return np.random.normal(10, 2, 100)

    def test_mean(self, normal):
        np.testing.assert_almost_equal(normal.mean(), 10., 0)

    def test_std(self, normal):
        np.testing.assert_almost_equal(normal.std(), 2., 0)



class TestCaseUniform:

    def setup_method(self, method):
        self.uniform = np.random.uniform(10, 20, 100)

    def teardown_method(self, method):
        print("Finishing")

    def test_min(self):
        assert self.uniform.min() >= 10

    def test_max(self):
        assert self.uniform.min() <= 20
