# GH Branch Guard

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

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT