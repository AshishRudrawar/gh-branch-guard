import pytest
from click.testing import CliRunner
from gh_branch_guard import cli


def test_audit_missing_repo():
    runner = CliRunner()
    result = runner.invoke(cli.cli, ["audit"])
    assert result.exit_code != 0


def test_enforce_requires_token(monkeypatch):
    runner = CliRunner()
    monkeypatch.delenv("GITHUB_TOKEN", raising=False)
    result = runner.invoke(cli.cli, ["enforce", "--repo", "owner/repo"])
    assert result.exit_code == 1
    assert "GITHUB_TOKEN is required" in result.output
