import pytest

from BaseTools.GetYaml import *


file = get_yaml("./TestFile/sit/test.yaml")


@pytest.mark.parametrize("test_data", file)
def test_yaml(test_data):
    print(test_data.get("phoneno"))

