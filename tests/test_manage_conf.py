import pytest

from manage_conf import __version__
from manage_conf import RemoteSettings, RemoteConfigurationJSONDecodeError


@pytest.fixture(scope="class")
def remote_settings_class():
    rs = RemoteSettings()
    yield rs


def test_version():
    assert __version__ == "0.1.0"


def test__deserialise_method_json_loads(remote_settings_class):
    name = "ALLOWED_HOSTS"
    value = "\"['uglyurl.execute-api.us-east-1.amazonaws.com']\""
    assert isinstance(value, str)
    deserialised_value = remote_settings_class._deserialise(name, value)
    assert isinstance(deserialised_value, str)
    assert deserialised_value == "['uglyurl.execute-api.us-east-1.amazonaws.com']"


def test__deserialise_method_raises_if_invalid_json(remote_settings_class):
    with pytest.raises(RemoteConfigurationJSONDecodeError):
        name = "ALLOWED_HOSTS"
        value = "'['uglyurl.execute-api.us-east-1.amazonaws.com']'"
        remote_settings_class._deserialise(name, value)


@pytest.mark.parametrize(
    "value",
    [
        "['uglyurl.execute-api.us-east-1.amazonaws.com']",
        ["uglyurl.execute-api.us-east-1.amazonaws.com"],
    ],
)
def test__evaluate_method_returns_python_type(remote_settings_class, value):
    name = "ALLOWED_HOSTS"
    python_type = remote_settings_class._evaluate(name, value)
    assert isinstance(python_type, list)
