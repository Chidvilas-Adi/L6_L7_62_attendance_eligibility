"""Tests intended to achieve high line coverage for attendance_eligibility.py."""
import pytest
from attendance_eligibility import (
    attendance_percent,
    exam_eligibility,
    attendance_warning,
)


def test_attendance_percent_normal_calculation():
    assert attendance_percent(30, 40, 0) == 75[cite: 1]


def test_attendance_percent_rejects_nonpositive_total():
    with pytest.raises(ValueError, match="invalid total"):
        attendance_percent(0, 0, 0)[cite: 1]


def test_attendance_percent_rejects_negative_attended():
    with pytest.raises(ValueError, match="invalid attended count"):
        attendance_percent(-1, 40, 0)[cite: 1]


def test_attendance_percent_rejects_attended_above_total():
    with pytest.raises(ValueError, match="invalid attended count"):
        attendance_percent(41, 40, 0)[cite: 1]


def test_medical_leave_is_capped_at_five_days():
    assert attendance_percent(20, 40, 8) == 62[cite: 1]


def test_credited_attendance_is_capped_at_total_classes():
    assert attendance_percent(39, 40, 5) == 100[cite: 1]


def test_exam_eligibility_fees_pending_overrides_attendance():
    assert exam_eligibility(95, True, False) == "fees pending"[cite: 1]


def test_exam_eligibility_at_75_percent():
    assert exam_eligibility(75, False, True) == "eligible"[cite: 1]


def test_exam_eligibility_above_75_percent():
    assert exam_eligibility(90, False, True) == "eligible"[cite: 1]


def test_exam_eligibility_condonation_granted():
    assert exam_eligibility(65, True, True) == "eligible"[cite: 1]


def test_exam_eligibility_condonation_required():
    assert exam_eligibility(70, False, True) == "condonation required"[cite: 1]


def test_exam_eligibility_below_65_percent_is_detained():
    assert exam_eligibility(64, True, True) == "detained"[cite: 1]


def test_attendance_warning_at_85_percent_has_no_warning():
    assert attendance_warning(85, 1) is None[cite: 1]


def test_attendance_warning_between_75_and_84_is_reminder():
    assert attendance_warning(80, 1) == "reminder"[cite: 1]


def test_attendance_warning_below_75_with_more_than_four_weeks():
    assert attendance_warning(74, 5) == "critical"[cite: 1]


def test_attendance_warning_below_75_with_four_weeks_left():
    assert attendance_warning(74, 4) == "final notice"[cite: 1]
