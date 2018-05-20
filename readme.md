# star-archiver

Current version: `0.0.8`

## What does it do?

Given a GitHub username, this script will look up the user's starred respositories, clone each repository and (optionally) compress them into a single zip file with the filename format `{username}_{repo-owner}-{repo-name}_{timestamp}.zip`.

## Dependencies

### Required

    git

### Optional

    zip

## Install

    pip install stararchiver

## Usage

    stararchiver <github-username>

#### Compress repositories into a single zip file

    stararchiver <github-username> -c

#### Specify the output directory

    stararchiver <github-username> -o ~/starred_repos

#### (optional) Specify a GitHub user token

There is an optional parameter `-t`/`--token` that can be used to specify a GitHub user API token. Doing this will allow you to perform more successive API calls, allowing for the archive of longer GitHub user star lists.

    stararchiver <github-username> -t <github-api-token>

## pip packaging

View the `stararchiver` package on [PyPi](https://pypi.org/project/stararchiver/).

#### Build a new pip package

    ./build.sh

#### Upload a new package to PyPi

    ./update-pip.sh

