# 💼 AI Grant & Funding Finder

An AI-powered startup grant evaluation dashboard built with Streamlit and IBM Bob Engine.

## 🚀 Deploy on Streamlit Community Cloud (Free Public URL)

### Step 1 — Push to GitHub
1. Go to [https://github.com/new](https://github.com/new) and create a **new public repository**
2. Open PowerShell in this project folder and run:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

### Step 2 — Deploy on Streamlit Cloud
1. Go to [https://share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Click **"New app"**
4. Select your repository, branch `main`, and set **Main file path** to `app.py`
5. Click **Deploy** — your public URL is live in ~60 seconds!

Your URL will look like:
```
https://YOUR_USERNAME-YOUR_REPO_NAME-app-xxxx.streamlit.app
```

## 🖥️ Run Locally
```bash
python -m streamlit run app.py
```

## 📁 Project Files
| File | Purpose |
|------|---------|
| `app.py` | Streamlit frontend + IBM Bob validation engine |
| `bob_bridge.py` | Standalone FastAPI backend (local use only) |
| `requirements.txt` | Python dependencies |
| `.streamlit/config.toml` | Streamlit server configuration |
