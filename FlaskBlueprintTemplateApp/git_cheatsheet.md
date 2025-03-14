# Remove the wrong tracking branch
git branch --unset-upstream

# Set the new upstream branch for sync in project
git branch --set-upstream-to=origin/feature/database feature/database
