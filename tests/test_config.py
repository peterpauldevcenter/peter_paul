from peter_paul import settings


def test_secrets():
    assert settings.CSRF_SESSION_KEY == 'secret'
    assert settings.SECRET_KEY == 'secret'
