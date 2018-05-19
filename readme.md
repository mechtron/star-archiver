# star-archiver

## What does it do?

Given a GitHub username, this script will look up the user's starred respositories, clone each repository and (optionally) compress them into a single tarball (`{username}_starred_repos_{timestamp}.tar.gz`).

## (optional) Dependencies

    zip

## Install

    pip install stararchiver

## Usage

    stararchiver <github-username>

## Compress repositories into a tarball

    stararchiver <github-username> -c

## Specify the output directory

    stararchiver <github-username> -o ~/starred_repos

## (optional) Specify a GitHub user token

There is an optional parameter `-t`/`--token` that can be used to specify a GitHub user API token. Doing this will allow you to perform more successive API calls, allowing for the archive of longer GitHub user star lists.

## Build a new pip package

    ./build.sh
