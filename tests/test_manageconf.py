from unittest.mock import patch, MagicMock

import pytest

from manageconf import __version__
from manageconf import RemoteSettings
from manageconf.exceptions import (
    BotoRequestFailureError,
    RemoteConfigurationJSONDecodeError,
)
from tests.datasets import BOTO_PAYLOAD


@pytest.fixture(scope="class")
def remote_settings_class():
    rs = RemoteSettings()
    yield rs


def test_version():
    assert __version__ == "1.1.0"


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


def test__deserialise_method_returns_if_not_str(remote_settings_class):
    name = "ALLOWED_HOSTS"
    value = ["uglyurl.execute-api.us-east-1.amazonaws.com"]
    deserialised_value = remote_settings_class._deserialise(name, value)
    assert value == deserialised_value


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


@pytest.mark.parametrize(
    "value", ["\"['uglyurl.execute-api.us-east-1.amazonaws.com']\"", "text"]
)
def test__evaluate_method_captures_exception_returns_input_value(
    remote_settings_class, value
):
    name = "key"
    python_type = remote_settings_class._evaluate(name, value)
    assert isinstance(python_type, str)


@patch("boto3.client")
def test_get_remote_params_returns_response(boto_mock, remote_settings_class):
    mock_boto_payload = MagicMock(return_value=BOTO_PAYLOAD)
    boto_mock.return_value.get_parameters_by_path = mock_boto_payload
    response = remote_settings_class.get_remote_params("/portal/dev/")
    assert response == {
        "ALLOWED_HOSTS": ["uglyurl.execute-api.us-east-1.amazonaws.com"],
        "SECRET_KEY": "not-a-good-secret",
        "STATICFILES_STORAGE": "S3-storage",
    }


@patch("boto3.client", side_effect=BotoRequestFailureError)
def test_get_remote_params_boto_fails_and_raises(boto_mock, remote_settings_class):
    with pytest.raises(BotoRequestFailureError):
        remote_settings_class.get_remote_params("/portal/dev/")
