"""
run_public.py — One-command public launcher for AI Grant & Funding Finder
---------------------------------------------------------------------------
Starts:
  1. bob_bridge.py  (FastAPI backend on port 8000)
  2. Streamlit app  (app.py on port 8501)
  3. ngrok tunnel   (exposes port 8501 as a public HTTPS URL)

Usage:
  python run_public.py
  python run_public.py --token YOUR_NGROK_AUTHTOKEN   (first time only)
"""

import argparse
import subprocess
import sys
import time
import threading

# ── 1. Parse optional ngrok auth token ──────────────────────────────────────
parser = argparse.ArgumentParser(description="Launch app with a public ngrok URL")
parser.add_argument("--token", help="Your ngrok authtoken (only needed once)", default=None)
args = parser.parse_args()

# ── 2. Save authtoken if provided ────────────────────────────────────────────
if args.token:
    from pyngrok import ngrok
    ngrok.set_auth_token(args.token)
    print(f"[✔] ngrok authtoken saved.")

# ── 3. Helper: stream subprocess output to terminal ──────────────────────────
def stream(proc, label):
    for line in iter(proc.stdout.readline, b""):
        print(f"[{label}] {line.decode(errors='replace').rstrip()}")

# ── 4. Start bob_bridge.py (FastAPI backend) ─────────────────────────────────
print("[→] Starting bob_bridge.py on port 8000...")
bridge_proc = subprocess.Popen(
    [sys.executable, "bob_bridge.py"],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
)
threading.Thread(target=stream, args=(bridge_proc, "bridge"), daemon=True).start()
time.sleep(2)  # give FastAPI a moment to boot

# ── 5. Start Streamlit app ───────────────────────────────────────────────────
print("[→] Starting Streamlit on port 8501...")
streamlit_proc = subprocess.Popen(
    [sys.executable, "-m", "streamlit", "run", "app.py",
     "--server.port", "8501",
     "--server.headless", "true"],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
)
threading.Thread(target=stream, args=(streamlit_proc, "streamlit"), daemon=True).start()
time.sleep(4)  # give Streamlit a moment to boot

# ── 6. Open ngrok tunnel on port 8501 ────────────────────────────────────────
from pyngrok import ngrok, exception as ngrok_ex

try:
    tunnel = ngrok.connect(8501, "http")
    public_url = tunnel.public_url
    # ngrok gives http:// — upgrade to https://
    if public_url.startswith("http://"):
        public_url = public_url.replace("http://", "https://", 1)

    print("\n" + "=" * 60)
    print("  🌐  PUBLIC URL READY")
    print(f"  👉  {public_url}")
    print("=" * 60)
    print("\n  Share this link with anyone — it's live right now.")
    print("  Press Ctrl+C to stop everything.\n")

except ngrok_ex.PyngrokNgrokError as e:
    print(f"\n[✖] ngrok error: {e}")
    print("    If you see 'authtoken', run:")
    print("    python run_public.py --token YOUR_NGROK_AUTHTOKEN")
    print("    Get a free token at: https://dashboard.ngrok.com/get-started/your-authtoken\n")
    bridge_proc.terminate()
    streamlit_proc.terminate()
    sys.exit(1)

# ── 7. Keep running until Ctrl+C ─────────────────────────────────────────────
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\n[→] Shutting down...")
    ngrok.disconnect(tunnel.public_url)
    ngrok.kill()
    bridge_proc.terminate()
    streamlit_proc.terminate()
    print("[✔] All processes stopped.")
