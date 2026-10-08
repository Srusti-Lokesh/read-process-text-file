# Final Submission Checklist

## GitHub
- [ ] Repository name: `read-process-text-file`
- [ ] Repository is Public
- [ ] README.md exists
- [ ] Source code is pushed to `main`
- [ ] requirements.txt exists
- [ ] render.yaml exists
- [ ] No `.venv`, secrets, passwords or API keys are committed
- [ ] Repository URL copied

## Local verification
- [ ] `python -m unittest discover -s tests -v` passes
- [ ] `python text_stats.py .\sample_data\sample.txt` works
- [ ] `python app.py` works
- [ ] Browser test succeeds

## Render
- [ ] Web Service created from GitHub
- [ ] Build command: `pip install -r requirements.txt`
- [ ] Start command: `gunicorn app:app`
- [ ] Health check: `/health`
- [ ] Deployment status is Live
- [ ] Upload test completed
- [ ] Live URL copied
- [ ] Deployment history screenshot captured
- [ ] Rollback evidence captured if required

## Internship portal
- [ ] GitHub URL submitted
- [ ] Render URL submitted
- [ ] Report PDF submitted
- [ ] Rollback/deployment evidence submitted
- [ ] Any required README/deployment configuration included

## LinkedIn
- [ ] Post published
- [ ] GitHub link added
- [ ] Render link added
- [ ] Task completed, features and technologies mentioned
- [ ] Internship/project hashtags included
