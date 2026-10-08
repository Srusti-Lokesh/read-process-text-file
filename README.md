# Read and Process a Text File

A Python/Flask text-processing project that reads a UTF-8 `.txt` file and generates:

- Line count
- Word count
- Character count

The application processes files line-by-line so it does not unnecessarily load the entire file into memory.

## Live deployment

Deployable on Render as a Python Web Service.

**Render build command**
```text
pip install -r requirements.txt
```

**Render start command**
```text
gunicorn app:app
```

**Health check**
```text
/health
```

The included `render.yaml` contains the same configuration.

## Features

- Upload a `.txt` file through a browser
- Line, word and character statistics
- UTF-8 validation
- Missing-file and invalid-file handling
- 10 MB upload limit
- Streaming/line-by-line processing
- CLI file-processing mode
- Automated unit tests
- Render-ready deployment configuration
- Responsive web interface

## Technologies

- Python 3
- Flask
- Gunicorn
- HTML5
- CSS3
- Git/GitHub
- Render

## Run locally on Windows PowerShell

### 1. Open the project
```powershell
cd .\read_process_text_file_project
```

### 2. Create a virtual environment
```powershell
py -m venv .venv
```

### 3. Activate it
```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies
```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Run the Flask app
```powershell
python app.py
```

Open:
```text
http://127.0.0.1:5000
```

### 6. Test the CLI processor
```powershell
python text_stats.py .\sample_data\sample.txt
```

### 7. Run unit tests
```powershell
python -m unittest discover -s tests -v
```

### 8. Test the production server locally
```powershell
gunicorn app:app
```

If `gunicorn` is not available on Windows, use the Flask development server for local testing. Render runs the Gunicorn start command on its Linux environment.

## GitHub submission

Create a **public** GitHub repository named:

`read-process-text-file`

Recommended repository description:

> A Python Flask text-processing application that reads UTF-8 text files and generates line, word, and character statistics, with robust file handling and Render deployment support.

Then, from the project folder in PowerShell:

```powershell
git init
git branch -M main
git add .
git commit -m "Initial commit - text file statistics project"
git remote add origin https://github.com/YOUR_USERNAME/read-process-text-file.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

## Render deployment

1. Sign in to Render.
2. Connect GitHub.
3. Choose **New > Web Service**.
4. Select the `read-process-text-file` repository.
5. Branch: `main`
6. Runtime/Language: Python
7. Build command:
   `pip install -r requirements.txt`
8. Start command:
   `gunicorn app:app`
9. Health check path:
   `/health`
10. Choose the required plan.
11. Create the Web Service.
12. Wait for the build and deployment to finish.
13. Open the generated `onrender.com` URL.
14. Upload `sample_data/sample.txt` and verify the statistics.
15. Keep the live URL for the internship submission form.

## Submission checklist

Before submitting, verify:

- [ ] GitHub repository is public
- [ ] README.md is present
- [ ] Source code is pushed
- [ ] requirements.txt is present
- [ ] render.yaml is present
- [ ] Render deployment is successful
- [ ] Live Render URL opens
- [ ] Text file upload works
- [ ] Statistics are displayed correctly
- [ ] `/health` returns `{"status":"ok"}`
- [ ] Report PDF is ready
- [ ] GitHub repository URL is copied
- [ ] Render live URL is copied
- [ ] GitHub link is included in LinkedIn post
- [ ] LinkedIn post is published if required by the internship
- [ ] Deployment/rollback evidence is captured as screenshots if the internship portal asks for evidence

## Rollback evidence

For the submission requirement that mentions rollback evidence, keep a simple record:

1. Note the first successful deployment/commit.
2. Make a small controlled change and push it.
3. Confirm the new deployment succeeds.
4. If required by your internship, use Render's Deploys page to redeploy a previously successful deployment.
5. Capture screenshots of the successful deployment history and the final live service.
6. Do not delete the repository or deployment history before submission.

## Project structure

```text
read_process_text_file_project/
├── app.py
├── text_stats.py
├── requirements.txt
├── render.yaml
├── Procfile
├── README.md
├── .gitignore
├── sample_data/
│   └── sample.txt
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── tests/
│   └── test_text_stats.py
└── report/
    └── Project_Report.pdf
```

## Counting rules

- **Lines:** one count for every line yielded by the text stream.
- **Words:** `line.split()` is used, so consecutive whitespace is treated as a separator.
- **Characters:** characters are counted after removing `\r` and `\n` line-ending characters.
- Empty files produce zero for all three statistics.
