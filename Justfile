mod gh '.just/gh.just'

docker := if `command -v docker || true` == "" { "podman" } else { "docker" }

# list commands
default:
    @just --list

#
# --- Seed ---
#

# run once on project creation
[group('0-seed')]
seed:
    echo -e "#!/usr/bin/env sh\njust pre-commit" > .git/hooks/pre-commit

#
# --- Develop ---
#

# init dev environment
[group('1-develop')]
init:
    chmod ug+x .git/hooks/*
    brew install gh git uv yq

# build python package
[group('1-develop')]
build: sync
    make requirements build

# build docs
[group('1-develop')]
docs: sync
    make docs

# add changelog news entry
[group('1-develop')]
news:
    uv run scriv create

# sunchronize dependencies
[group('1-develop')]
sync:
    uv lock
    uv sync --all-extras --all-groups --frozen

# update dev environment
[group('1-develop')]
upgrade:
    uv sync --all-extras --all-groups --upgrade
    uvx copier update --trust --vcs-ref main

# run linters
[group('1-develop')]
lint:
    uv run mypy .
    uv run ruff check
    uv run ruff format --diff

# run tests
[group('1-develop')]
test *toxargs: build
    #!/usr/bin/env sh
    set -eu
    PKG="$(find dist/pkg -name '*.whl')"
    mkdir -p .tox
    find .tox -name '.pass-*' -delete
    if [ "{{toxargs}}" = "" ]; then
        {{docker}} compose run --rm tox run --notest --skip-pkg-install
        {{docker}} compose run --rm tox run-parallel --installpkg="$PKG"
    else
        {{docker}} compose run --rm tox run --installpkg="$PKG" {{toxargs}}
    fi
    make sources

# enter testing docker container
[group('1-develop')]
shell service='tox':
    {{docker}} compose run --rm --entrypoint bash {{service}}

# remove all temporary files
[group('1-develop')]
clean:
    rm -rf .tmp .tox .venv dist .coverage
    find . -name __pycache__ -delete

#
# --- Release helpers ---
#

# display manual action confirmation
[private]
manual msg:
    @printf "\n{{msg}}, then press enter " && read

# bump project version
[private]
version-bump:
    #!/usr/bin/env bash
    set -eu
    uv run bump-my-version show-bump
    printf 'Choose version part: '
    read PART
    uv run bump-my-version bump -- "$PART"
    uv lock

# collect changelog entries
[private]
changelog-collect:
    uv run scriv collect
    sed -e's/^### \(.*\)$/***\1***/; s/\([a-z]\)\*\*\*$/\1***/' -i '' CHANGELOG.md

# publish package on PyPI
[private]
pypi-publish: build
    uv publish

#
# --- Manage ---
#

# run pre-commit hook
[group('2-manage')]
pre-commit:
    just lint
    make docs sources

# run pre-merge
[group('2-manage')]
pre-merge:
    just lint
    just test
    make docs sources

# merge
[group('2-manage')]
merge:
    just pre-merge
    just gh::pr-create
    just manual "Merge pull request"
    git switch main
    git fetch
    git pull

# release
[group('2-manage')]
release:
    just pre-merge
    just version-bump
    just changelog-collect
    make sources
    just confirm "Proofread the changelog and commit changes"
    just merge
    just gh::repo-update
    just gh::release-create
    just confirm "Update release notes and publish GitHub release"
    just pypi-publish
