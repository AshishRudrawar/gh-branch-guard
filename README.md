# GH Branch Guard

[![CI](https://github.com/AshishRudrawar/gh-branch-guard/actions/workflows/python-app.yml/badge.svg)](https://github.com/AshishRudrawar/gh-branch-guard/actions/workflows/python-app.yml)
[![Dependabot](https://github.com/AshishRudrawar/gh-branch-guard/actions/workflows/dependabot.yml/badge.svg)](https://github.com/AshishRudrawar/gh-branch-guard/actions/workflows/dependabot.yml)
[![Release](https://github.com/AshishRudrawar/gh-branch-guard/actions/workflows/release.yml/badge.svg)](https://github.com/AshishRudrawar/gh-branch-guard/actions/workflows/release.yml)

`gh-branch-guard` is an open-source CLI tool that audits and enforces branch protection policies across GitHub repositories.

## Setup

```bash
cd gh-branch-guard
python -m pip install --upgrade pip
python -m pip install -e '.[test]'
```

or with Makefile:

```bash
make install
```

## Features

- `ghguard audit --repo owner/repo`: check branch protections for required status checks, code owners, review requirements.
- `ghguard enforce --repo owner/repo`: optionally set missing protections (needs `GITHUB_TOKEN`).

## Quickstart

```bash
ghguard audit --repo octocat/Hello-World
```

## OSS health checks

- [x] Active CI: `python-app.yml`
- [x] Dependency updates: `dependabot.yml`
- [x] Release tags: `release.yml`
- [ ] Star target: 50+ (set goal)
- [ ] Contributors target: 10+ (set goal)

### Quick metrics snapshot

```bash
python scripts/oss_health.py --repo AshishRudrawar/gh-branch-guard
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT