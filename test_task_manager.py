import pytest
import os
from task_manager import load_tasks, add_task, list_tasks, complete_task

def test_load_empty_file(tmp_path):
    """Test 1: Loads empty list if file doesn't exist."""
    test_file = tmp_path / "test_tasks.json"
    assert load_tasks(filepath=test_file) == []

def test_add_task(tmp_path):
    """Test 2: Adding a task saves it correctly."""
    test_file = tmp_path / "test_tasks.json"
    result = add_task("Buy groceries", filepath=test_file)
    
    assert "Added task" in result
    tasks = load_tasks(filepath=test_file)
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Buy groceries"
    assert tasks[0]["done"] is False

def test_list_tasks(tmp_path):
    """Test 3: Listing tasks formats them correctly."""
    test_file = tmp_path / "test_tasks.json"
    add_task("First task", filepath=test_file)
    add_task("Second task", filepath=test_file)
    
    output = list_tasks(filepath=test_file)
    assert "1. [ ] First task" in output
    assert "2. [ ] Second task" in output

def test_complete_valid_task(tmp_path):
    """Test 4: Marking a task as done updates its status."""
    test_file = tmp_path / "test_tasks.json"
    add_task("Do laundry", filepath=test_file)
    
    result = complete_task(1, filepath=test_file)
    assert "Marked task #1" in result
    
    tasks = load_tasks(filepath=test_file)
    assert tasks[0]["done"] is True

def test_complete_invalid_task(tmp_path):
    """Test 5: Edge case - completing a non-existent task gracefully fails."""
    test_file = tmp_path / "test_tasks.json"
    add_task("Only one task", filepath=test_file)
    
    result = complete_task(99, filepath=test_file)
    assert "Error: Task #99 does not exist" in result