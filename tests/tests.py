import builtins
from unittest import mock
from unittest.mock import patch
import io

from program.main import pin_inquiry, run
import program.main
from io import StringIO


def test_correct_pin_inquiry(monkeypatch):
    with mock.patch.object(builtins, 'input', lambda _: '1234'):
        assert pin_inquiry() == True


def test_incorrect_pin_inquiry(monkeypatch):
    with mock.patch.object(builtins, 'input', lambda _: '1111'):
        assert pin_inquiry() == False


@patch('sys.stdout', new_callable=io.StringIO)
def test_run_insufficient(mock_stdout, monkeypatch):
    def mock_pin_inquiry():
        return True
    monkeypatch.setattr(program.main, "pin_inquiry", mock_pin_inquiry)
    with mock.patch.object(builtins, 'input', lambda _: '111'):
        run()
        assert mock_stdout.getvalue() == 'Insufficient funds.\nThank you for using Simple ATM.\n'


@patch('sys.stdout', new_callable=io.StringIO)
def test_run_3_incorrect_pin(mock_stdout, monkeypatch):
    def mock_pin_inquiry():
        return False
    monkeypatch.setattr(program.main, "pin_inquiry", mock_pin_inquiry)
    incorrect_message = 'The pin is incorrect. '
    attempt_2 = 'You have 2 more attempts.\n'
    attempt_1 = 'You have 1 more attempts.\n'
    attempt_0 = 'You have 0 more attempts.\n'
    lock_message = 'Your account has been locked.\n'
    full_message = incorrect_message + attempt_2 + incorrect_message + attempt_1 + incorrect_message + attempt_0 + lock_message
    run()
    assert mock_stdout.getvalue() == full_message


@patch('sys.stdout', new_callable=io.StringIO)
def test_run_correct(mock_stdout, monkeypatch):
    def mock_pin_inquiry():
        return True
    monkeypatch.setattr(program.main, "pin_inquiry", mock_pin_inquiry)
    with mock.patch.object(builtins, 'input', lambda _: '5'):
        run()
        assert mock_stdout.getvalue() == 'Withdrawal successful. Your balance is 95.\nThank you for using Simple ATM.\n'

