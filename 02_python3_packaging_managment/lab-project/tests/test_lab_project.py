from lab_project import __version__
import requests


def test_version():
    assert __version__ == '0.1.0'

def test_requests():
    r = requests.get('https://obscuritylabs.com')
    assert r