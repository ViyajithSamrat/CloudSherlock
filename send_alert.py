import smtplib
import ssl
from email.message import EmailMessage
from pathlib import Path

# ========== CONFIGURATION ==========
SENDER = "your_email@gmail.com"
APP_PASSWORD = "your_app_password_here"  # Must be App Password, not Gmail password
RECEIVER = "your_email@gmail.com"

# Find latest anomaly report
reports_dir = Path("reports")
report_files = sorted(reports_dir.glob("anomalies_*.csv"), reverse=True)

if not report_files:
    print("❌ No anomaly report found.")
    exit()

latest_report = report_files[0]

# Compose Email
msg = EmailMessage()
msg["Subject"] = "🔍 CloudSherlock Anomaly Report"
msg["From"] = SENDER
msg["To"] = RECEIVER
msg.set_content("Hi,\n\nCloudSherlock detected anomalies in your cloud billing data.\n\nReport attached.\n\n— Team CloudSherlock")

# Attach report
msg.add_attachment(
    latest_report.read_bytes(),
    maintype="application",
    subtype="octet-stream",
    filename=latest_report.name
)

# Send email
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as server:
        server.login(SENDER, APP_PASSWORD)
        server.send_message(msg)
    print("✅ Email with report sent successfully.")
except Exception as e:
    print("❌ Failed to send email:", e)
