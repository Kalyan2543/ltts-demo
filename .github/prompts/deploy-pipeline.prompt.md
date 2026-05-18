---
description: "Run the full orchestrator — executes Review Gate + Pipeline 2 (Validate + Deploy to Git). Use after Pipeline 1 (Build) is complete."
agent: "agent"
argument-hint: "Type 'deploy' to validate and push, 'status' to check pipeline state, or 'full <feature>' to build + deploy"
---

# Orchestrator — Deploy Pipeline

You are the **Orchestrator Agent** executing **Pipeline 2 (Validate + Deploy)**.

## Step 0 — Read State

Read `pipeline-state.json` in the project root to understand current pipeline status.
Read `.github/agents/orchestrator-agent.md` for full architecture reference.

## Step 1 — Review Gate

Run these automated checks. ALL must pass to proceed:

### Check 1: Backend Health
```bash
# Start backend, hit health endpoint
curl http://127.0.0.1:8000/api/v1/health
# Expected: {"status": "healthy"}
```
If backend isn't running, start it with: `python -m uvicorn app.main:app --host 127.0.0.1 --port 8000`

### Check 2: Frontend Build
```bash
cd frontend && npm run build
# Expected: exit code 0, dist/ folder created
```

### Check 3: Lint Check
```bash
# Python: check for syntax errors
python -m py_compile backend/app/main.py
python -m py_compile backend/app/crud.py
python -m py_compile backend/app/models.py

# JS: check frontend builds without errors (covered by Check 2)
```

### Check 4: Tests Exist
```bash
# Verify test files exist
ls tests/e2e/*.spec.js
```

**Update `pipeline-state.json`** with review gate results (pass/fail for each check).

If ANY check fails → update state with `"status": "failed"`, report the failure, stop.
If ALL pass → proceed to Pipeline 2.

## Step 2 — Pipeline 2: Validate + Deploy

### Stage 1: Final Build
```bash
cd frontend && npm run build
```

### Stage 2: Git Init + Commit
```bash
git init  (if not already a repo)
git add .
git commit -m "feat: e-commerce app — login + home page (multi-agent pipeline)"
```

### Stage 3: Git Push
```bash
git remote add origin <REPO_URL>  (if not set)
git branch -M main
git push -u origin main
```

**IMPORTANT:** Before pushing, confirm the remote URL is set. If not, ask the user for their EY repo URL.

## Step 3 — Update State

After successful deploy, update `pipeline-state.json`:
```json
{
  "status": "completed",
  "pipeline_2": {
    "lint_format": { "status": "completed" },
    "build": { "status": "completed" },
    "git_commit": { "status": "completed" },
    "git_push": { "status": "completed" }
  }
}
```

## Rules
- Never push without user confirmation of the repo URL
- Never force-push
- Always run review gate before deploy
- Save state after every stage
