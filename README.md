Quick steps to deploy to GitHub:

1. Initialize and commit:
   git init
   git add .
   git commit -m "Initial"

2. Create a GitHub repo and add remote:
   git remote add origin git@github.com:youruser/yourrepo.git
   git branch -M main
   git push -u origin main

3. In GitHub repo → Settings → Secrets → Actions add NEWSAPI_KEY (your real key).

4. GitHub Actions will run the CI workflow on push.

Quick steps to link and push this project to your GitHub repo "bits"

1) Create a local .env (do NOT commit)
# from project root
copy .env.example .env   # Windows PowerShell/CMD
# Edit .env and replace placeholder with your real key

2) Option A — Recommended: create & push using GitHub CLI (gh)
# authenticate once:
gh auth login
# create the repo on GitHub and push the current folder as origin/main
gh repo create YOUR_GITHUB_USERNAME/bits --public --source=. --remote=origin --push

3) Option B — Manual git + existing remote
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin git@github.com:YOUR_GITHUB_USERNAME/bits.git
git push -u origin main

4) Add the NEWSAPI_KEY secret
# GitHub web UI:
# Repo → Settings → Secrets and variables → Actions → New repository secret
# Name: NEWSAPI_KEY  Value: <your_real_newsapi_key_here>

# Or with gh CLI:
gh secret set NEWSAPI_KEY --body "your_real_newsapi_key_here" --repo YOUR_GITHUB_USERNAME/bits

5) Verify CI / Actions
# After push, open the repository on GitHub → Actions → check the workflow run.
# The provided workflow sets SKIP_MODEL in CI to avoid heavy model downloads.

6) If you accidentally pushed the real key
# Rotate the key in NewsAPI dashboard immediately.
# Remove file if tracked:
git rm --cached .env.example
git commit -m "Remove secret from tracking"
git push
# For full history removal, use BFG or git-filter-repo (backup first).

Notes
- Keep .env in .gitignore (project already contains .gitignore).
- For production or local full-model use, install transformers and torch and unset SKIP_MODEL/CI.
