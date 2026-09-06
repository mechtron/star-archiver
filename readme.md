# stararchiver

Current version: `1.0.0`

## What does it do?

Given a GitHub username, `stararchiver` looks up every repository that user has starred via the [GitHub REST API](https://docs.github.com/en/rest), clones them all to disk, and optionally compresses them into a single zip file.

```text
stararchiver_<username>_<timestamp>/
  author1-repo1/
  author1-repo2/
  ...
  author2-repo3/
```

## Requirements

- Python 3.9+
- [`git`](https://git-scm.com/) (required)
- Internet access to `api.github.com`

Python's built-in `zipfile` module is used for compression, so no external `zip` binary is needed.

## Install

```sh
pip install stararchiver
```

## Usage

```
stararchiver <github-username>
```

### Clone over SSH

By default repositories are cloned over HTTPS, which works without any extra setup.
To clone over SSH (requires an SSH key registered with GitHub):

```sh
stararchiver <github-username> --ssh
```

### Compress repositories into a single zip file

```sh
stararchiver <github-username> -c
```

Optionally delete the cloned data afterwards (the zip is kept):

```sh
stararchiver <github-username> -c -d
```

### Specify the output directory

```sh
stararchiver <github-username> -o ~/starred_repos
```

### Provide a GitHub token

The unauthenticated GitHub API allows 60 requests/hour. Starred-list pagination
consumes roughly one request per 100 stars, so long star lists hit that ceiling
quickly. Passing a token raises the limit to 5,000 requests/hour.

Either pass it explicitly or export it in your environment (recommended, so it
never ends up in your shell history):

```sh
export GITHUB_TOKEN=ghp_xxx
stararchiver <github-username>
# equivalent:
stararchiver <github-username> -t ghp_xxx
```

Both fine-grained and classic personal access tokens are supported. Tokens only
need `public` read access; no scopes beyond public data are required.

### Other options

| Flag | Description |
| --- | --- |
| `-j, --jobs N` | Clone up to N repositories concurrently (default 4) |
| `--shallow` | Shallow-clone each repo (`--depth 1`) to save space and time |
| `--no-wiki` | Don't clone each repository's wiki |
| `--metadata` | Write a `starred_repos.json` manifest describing every repo |
| `--max-repos N` | Only archive the first N starred repos (handy for testing) |
| `--dry-run` | Print the starred repos without cloning anything |
| `-v, --version` | Show the version and exit |

Full details are always available via `stararchiver -h`.

## pip packaging

View the `stararchiver` package on [PyPI](https://pypi.org/project/stararchiver/).

#### Build a new pip package

```sh
./build.sh
```

#### Upload a new package to PyPI

```sh
./update-pip.sh
```

## Development

Run straight from a checkout (no install needed):

```sh
./stararchiver <github-username> --dry-run
```
