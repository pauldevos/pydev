## Git Tips for Trunk Based Development

### Why Trunk Based Development
- Trunk-based development is a version control management practice where developers merge small, frequent updates to a core “trunk” or main branch. Since it streamlines merging and integration phases, it helps achieve CI/CD and increases software delivery and organizational performance.
- [Google Cloud DevOps Guidelines](https://cloud.google.com/architecture/devops/technical)
- [A Guide to Git with Trunk Based Development](https://hackernoon.com/a-guide-to-git-with-trunk-based-development-93a350c)


- https://shortcut.com/developer-how-to/git-tips-for-trunk-based-development


```bash
# get list of currently available branches
$ git branch
master
* my-new-feature

# make sure your repo is up to date before you make a new branch
$ git pull -r origin master

# Another option, if you want more control over your commits is to rebase interactively:
$ git pull --rebase=interactive

# Temporarily parking your changes
# You might have started developing something new locally when somebody from the team needs you to review their pull request. In order not to lose your progress you have to make sure you store it somewhere before checking out the changes to review.

# git-stash helps you with this by stashing your changes locally.
$ git stash -u -m"Exploring a possible AI-based blockchain compiler"

# Now you can make sure your changes are stashed by doing:
$ git stash list
# stash@{0}: On ai-spike: Exploring a possible AI-based blockchain compiler 



```