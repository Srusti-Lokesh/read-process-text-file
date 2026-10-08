# Deployment and Submission Guide

## PowerShell commands

Run these commands from the extracted project folder:

```powershell
cd .\read_process_text_file_project
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m unittest discover -s tests -v
python text_stats.py .\sample_data\sample.txt
python app.py
```

Open `http://127.0.0.1:5000`.

Stop the local server with `Ctrl+C`.

## GitHub

If Git is not initialized:

```powershell
git init
git branch -M main
git add .
git commit -m "Initial commit - text file statistics project"
git remote add origin https://github.com/YOUR_USERNAME/read-process-text-file.git
git push -u origin main
```

If the remote already exists and you need to push later changes:

```powershell
git add .
git commit -m "Update project documentation and deployment configuration"
git push
```

## GitHub repository fields

**Repository name**
```text
read-process-text-file
```

**Description**
```text
A Python Flask text-processing application that reads UTF-8 text files and generates line, word, and character statistics, with robust file handling and Render deployment support.
```

Recommended visibility: **Public** for an internship project that asks for a public GitHub repository.

## Render

Use a Render **Web Service**, not a Static Site, because Flask runs server-side.

- Branch: `main`
- Runtime: Python
- Build: `pip install -r requirements.txt`
- Start: `gunicorn app:app`
- Health check: `/health`

After deployment, test:

1. Home page opens.
2. Upload `sample_data/sample.txt`.
3. Results appear.
4. `/health` returns status OK.
5. Save the live URL.

Render can automatically redeploy when new commits are pushed to the linked branch. Keep the successful deployment in the Deploys history for evidence.

## Submission package

Submit the following according to the internship portal instructions:

1. Public GitHub repository link
2. Live Render URL
3. Project report PDF
4. Rollback/deployment evidence if requested
5. Any portal-specific project form fields

Do not commit secrets, passwords, API keys, virtual environments, or personal files.

## LinkedIn

Use the prepared post in `LINKEDIN_POST.md`.
