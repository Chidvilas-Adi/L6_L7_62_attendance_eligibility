"""Tests aimed specifically at exercising both outcomes of decision branches."""
import pytest
from attendance_eligibility import (
    attendance_percent,
    exam_eligibility,
    attendance_warning,
)


@pytest.mark.parametrize("total", [0, -1])
def test_total_classes_must_be_positive(total):
    with pytest.raises(ValueError, match="invalid total"):
        attendance_percent(0, total, 0)


@pytest.mark.parametrize("attended", [-1, 11])
def test_attended_must_be_within_valid_range(attended):
    with pytest.raises(ValueError, match="invalid attended count"):
        attendance_percent(attended, 10, 0)


def test_attendance_percent_does_not_cap_leave_at_five_or_less():
    assert attendance_percent(20, 40, 5) == 62


def test_attendance_percent_caps_leave_above_five():
    assert attendance_percent(20, 40, 6) == 62


def test_attendance_percent_caps_credited_at_total():
    assert attendance_percent(39, 40, 5) == 100


def test_attendance_percent_credited_below_total():
    assert attendance_percent(20, 40, 0) == 50


def test_fees_pending_branch():
    assert exam_eligibility(80, True, False) == "fees pending"


def test_fees_paid_and_at_least_75_branch():
    assert exam_eligibility(75, False, True) == "eligible"


def test_65_to_below_75_with_condonation():
    assert exam_eligibility(65, True, True) == "eligible"


def test_65_to_below_75_without_condonation():
    assert exam_eligibility(74, False, True) == "condonation required"


def test_below_65_branch():
    assert exam_eligibility(64, True, True) == "detained"


def test_warning_at_or_above_85_returns_none():
    assert attendance_warning(85, 10) is None


def test_warning_between_75_and_84_returns_reminder():
    assert attendance_warning(75, 1) == "reminder"


def test_below_75_and_more_than_four_weeks_is_critical():
    assert attendance_warning(74, 5) == "critical"


def test_below_75_and_four_weeks_is_final_notice():
    assert attendance_warning(74, 4) == "final notice"
