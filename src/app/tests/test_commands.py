from unittest.mock import patch

from django.core.management import call_command
from django.db.utils import OperationalError


def test_wait_for_db_ready():
    """test waiting for db when db is available"""
    with patch("django.core.management.base.BaseCommand.check") as check:
        check.return_value = True

        call_command("wait_for_db")  # act

        assert check.call_count == 1


@patch("time.sleep", return_value=True)
def test_wait_for_db_not_ready(mock_sleep):
    """test waiting for db until it's available"""
    with patch("django.core.management.base.BaseCommand.check") as check:
        check.side_effect = [OperationalError] * 5 + [True]

        call_command("wait_for_db")  # act

        assert check.call_count == 6
