# star-archiver

## What does it do?

Given a GitHub username, this script will look up the user's starred respositories, clone each repository and compress them into a single tarball (`{username}_starred_repos_{timestamp}.tar.gz`).

## Install

    pip install stararchiver

## Usage

    stararchiver <github-username>

## (optional) Specify a GitHub user token

There is an optional parameter `-t`/`--token` that can be used to specify a GitHub user API token. Doing this will allow you to perform more successive API calls, allowing for the archive of longer GitHub user star lists.

## Build a new pip package

    ./build.sh
