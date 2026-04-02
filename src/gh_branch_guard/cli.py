import os
import sys
import click
import requests

API = "https://api.github.com"


def _get_json(url, token=None):
    headers = {"Accept": "application/vnd.github.v3+json"}
    if token:
        headers["Authorization"] = f"token {token}"
    resp = requests.get(url, headers=headers, timeout=15)
    resp.raise_for_status()
    return resp.json()


def _patch_json(url, body, token):
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {token}"
    }
    resp = requests.patch(url, json=body, headers=headers, timeout=15)
    resp.raise_for_status()
    return resp.json()


@click.group()
def cli():
    """GH Branch Guard: audit/enforce GitHub branch protection."""
    pass


@cli.command()
@click.option("--repo", required=True, help="Repository slug e.g. owner/repo")
def audit(repo):
    """Audit branch protection for default branch."""
    token = os.getenv("GITHUB_TOKEN")
    owner, name = repo.split("/", 1)
    repo_data = _get_json(f"{API}/repos/{owner}/{name}", token=token)
    branch = repo_data["default_branch"]
    try:
        protection = _get_json(f"{API}/repos/{owner}/{name}/branches/{branch}/protection", token=token)
    except requests.HTTPError as err:
        click.echo(f"No branch protection found on default branch '{branch}': {err}")
        sys.exit(1)

    checks = protection.get("required_status_checks")
    required_reviews = protection.get("required_pull_request_reviews")
    enforce_admins = protection.get("enforce_admins", {}).get("enabled")

    click.echo(f"Repo: {repo}, branch: {branch}")
    click.echo(f"Required checks enabled: {bool(checks)}")
    click.echo(f"Required reviews: {bool(required_reviews)}")
    click.echo(f"Enforce admins: {enforce_admins}")


@cli.command()
@click.option("--repo", required=True, help="Repository slug e.g. owner/repo")
@click.option("--require-status-checks", is_flag=True, help="Enable required status checks")
@click.option("--require-review", is_flag=True, help="Enable required pull request reviews")
def enforce(repo, require_status_checks, require_review):
    """Enforce branch protection policy on default branch."""
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        click.echo("Error: GITHUB_TOKEN is required for enforce", err=True)
        sys.exit(1)

    owner, name = repo.split("/", 1)
    repo_data = _get_json(f"{API}/repos/{owner}/{name}", token=token)
    branch = repo_data["default_branch"]

    body = {
        "required_status_checks": None,
        "enforce_admins": True,
        "required_pull_request_reviews": None,
        "restrictions": None
    }

    if require_status_checks:
        body["required_status_checks"] = {"strict": True, "contexts": []}
    if require_review:
        body["required_pull_request_reviews"] = {"required_approving_review_count": 1}

    _patch_json(f"{API}/repos/{owner}/{name}/branches/{branch}/protection", body, token)
    click.echo(f"Applied policy on {repo}:{branch}")


def main():
    cli()


if __name__ == "__main__":
    main()
