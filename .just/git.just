default:

# push all commits after ensuring the clean state
push:
    git diff --exit-code
    git diff --cached --exit-code
    git ls-files --other --exclude-standard --directory
    git push
