from unittest import TestCase
import os
import doctest


class ReadMeDocTest(TestCase):
    def test__readme_doctests(self):
        readme_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "README.md")
        )
        assert os.path.exists(readme_path)
        result = doctest.testfile(readme_path, module_relative=False)
        assert result.failed == 0, "{result.failed} tests failed!"
