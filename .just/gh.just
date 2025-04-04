mod git

issue-id := "git branch --show-current | cut -d- -f1"
issue-title := "GH_PAGER=cat gh issue view {{issue-id}} --json title -t '{{{{.title}}'"
repo-name := "git config --get remote.origin.url | sed 's|.*/\\(.*/.*\\)\\.git$|\\1|'"


default:

# get issue id of current GitHub branch
issue-id:
    @{{issue-id}}

# get issue title of current GitHub branch
issue-title:
    @{{issue-title}}

# create GitHub pull request
pr-create:
    just git::push
    gh pr create --web -t "$({{issue-title}})"

# create GitHub release
release-create tag:
    #!/usr/bin/env sh
    set -eu
    if [ "$(git branch --show-current)" != "main" ]; then
        echo "Can release from main branch only"
        exit 1
    fi
    git push origin tag "{{tag}}"
    gh release create --draft -t "{{tag}} — $(date -Idate)" --generate-notes "{{tag}}"

# get "org/name" of current GitHub repository
repo-name:
    @{{repo-name}}

# update GitHub repository metadata from pyproject.toml
repo-update:
    #!/usr/bin/env sh
    set -eu
    # update description
    gh repo edit -d "$(yq .project.description pyproject.toml)"
    # update homepage
    homepage="$(yq .project.urls.Documentation pyproject.toml)"
    if [[ $homepage != "https://github.com"* ]]; then
      gh repo edit -h "$homepage"
    fi
    # delete old topics
    old_topics="$(GH_PAGER=cat gh api repos/$("{{repo-name}}") | yq -r '.topics | join(" ")')"
    if [ -n "$old_topics" ]; then
      gh repo edit $(sed 's/ / --remove-topic /g' <<<" $old_topics")
    fi
    # add new topics
    new_topics="$(yq -r '.project.keywords | join(" ")' pyproject.toml)"
    gh repo edit $(sed 's/ / --add-topic /g' <<<" $new_topics")
    # provide community support
    gh label create "code of conduct" --force -c D73A4A -d "Code of Conduct issues"
