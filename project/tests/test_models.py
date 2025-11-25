import os
import sys

# Ensure `project` directory is on sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models import User


def test_valid_email():
    u = User(id=1, name='Alice', email='alice@example.com')
    assert u.is_valid_email()


def test_invalid_email():
    u = User(id=2, name='Bob', email='not-an-email')
    assert not u.is_valid_email()


def test_repr_contains_id_and_name():
    u = User(id=3, name='Carol', email='c@example.com')
    r = repr(u)
    assert 'User(id=3' in r
    assert "name='Carol'" in r
