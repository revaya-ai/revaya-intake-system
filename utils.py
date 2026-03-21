"""
Utility functions for email (Resend), Slack, and Google Drive integration
"""

import os
import json
from typing import Optional, Dict, Any
from datetime import datetime
import requests
from config import EMAIL_CONFIG, SLACK_CONFIG, GOOGLE_DRIVE_CONFIG


# ============================================================================
# EMAIL FUNCTIONS (Resend)
# ============================================================================

def send_email(
    content_text: str,
    subject: str,
    recipient: Optional[str] = None,
    content_type: str = "text/html"
) -> dict:
    """
    Send email via Resend API

    Args:
        content_text: Email body (supports HTML)
        subject: Email subject line
        recipient: Email recipient (defaults to config)
        content_type: "text/plain" or "text/html"

    Returns:
        dict with success status and details
    """
    try:
        api_key = os.getenv("RESEND_API_KEY")
        if not api_key:
            return {
                "success": False,
                "error": "RESEND_API_KEY not configured",
                "message": "Email not sent - API key missing"
            }

        from_email = os.getenv("FROM_EMAIL", EMAIL_CONFIG["from_email"])
        to_email = recipient or os.getenv("TO_EMAIL", EMAIL_CONFIG["recipient"])

        html_content = markdown_to_html(content_text) if content_type == "text/html" else content_text

        response = requests.post(
            "https://api.resend.com/emails",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json={
                "from": f"Revaya AI <{from_email}>",
                "to": [to_email],
                "subject": subject,
                "html": html_content,
            },
            timeout=15,
        )

        if response.status_code in (200, 201):
            return {
                "success": True,
                "status_code": response.status_code,
                "message": f"Email sent to {to_email}",
                "recipient": to_email
            }
        else:
            return {
                "success": False,
                "status_code": response.status_code,
                "error": response.text,
                "message": f"Resend API returned {response.status_code}"
            }

    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "message": f"Failed to send email: {str(e)}"
        }


def markdown_to_html(markdown_text: str) -> str:
    """
    Convert markdown to HTML for email
    Converts markdown headings to bold text, uses Montserrat font size 11
    """
    import re

    content = markdown_text

    content = re.sub(r'^### (.+)$', r'<p style="margin-top: 20px; margin-bottom: 8px;"><strong>\1</strong></p>', content, flags=re.MULTILINE)
    content = re.sub(r'^## (.+)$', r'<p style="margin-top: 28px; margin-bottom: 10px;"><strong style="font-size: 13px;">\1</strong></p>', content, flags=re.MULTILINE)
    content = re.sub(r'^# (.+)$', r'<p style="margin-top: 32px; margin-bottom: 12px;"><strong style="font-size: 15px;">\1</strong></p>', content, flags=re.MULTILINE)
    content = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', content)
    content = re.sub(r'\*(.+?)\*', r'<em>\1</em>', content)
    content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" style="color: #028090;">\1</a>', content)
    content = re.sub(r'^- (.+)$', r'<p style="margin: 4px 0 4px 20px;">• \1</p>', content, flags=re.MULTILINE)
    content = re.sub(r'^(\d+)\. (.+)$', r'<p style="margin: 4px 0 4px 20px;">\1. \2</p>', content, flags=re.MULTILINE)
    content = re.sub(r'^---+$', r'<hr style="border: none; border-top: 1px solid #ddd; margin: 20px 0;">', content, flags=re.MULTILINE)
    content = content.replace('\n\n', '</p><p style="margin: 8px 0;">')
    content = content.replace('\n', '<br>')

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body {{
                font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                font-size: 11px;
                line-height: 1.6;
                color: #333;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
            }}
            p {{ margin: 8px 0; }}
            strong {{ font-weight: 600; color: #0d1a4a; }}
            a {{ color: #028090; text-decoration: none; }}
            a:hover {{ text-decoration: underline; }}
            .footer {{
                margin-top: 40px;
                padding-top: 20px;
                border-top: 1px solid #ecf0f1;
                font-size: 10px;
                color: #7f8c8d;
            }}
        </style>
    </head>
    <body>
        <div>{content}</div>
        <div class="footer">
            <p>
                <strong>Revaya AI</strong><br>
                Email: shannon@revaya.ai<br>
                Web: <a href="https://www.revaya.ai">www.revaya.ai</a>
            </p>
        </div>
    </body>
    </html>
    """
    return html


# ============================================================================
# SLACK FUNCTIONS
# ============================================================================

def notify_slack(message: str, channel: Optional[str] = None) -> dict:
    """
    Send notification to Slack via webhook
    """
    try:
        webhook_url = os.getenv("SLACK_WEBHOOK_URL")
        if not webhook_url or webhook_url == "ENV_VAR":
            return {
                "success": False,
                "error": "SLACK_WEBHOOK_URL not configured",
                "message": "Slack notification skipped - webhook not configured"
            }

        payload = {
            "text": message,
            "username": "Revaya AI",
            "icon_emoji": ":brain:"
        }

        if channel:
            payload["channel"] = channel

        response = requests.post(
            webhook_url,
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=10
        )

        if response.status_code == 200:
            return {"success": True, "message": "Slack notification sent"}
        else:
            return {
                "success": False,
                "error": f"Slack API returned {response.status_code}",
                "message": f"Failed to send Slack notification: {response.text}"
            }

    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "message": f"Failed to send Slack notification: {str(e)}"
        }


def send_slack_lead_notification(lead_data: dict, agent_results: dict = None) -> dict:
    """
    Send formatted lead notification to Slack
    """
    company = lead_data.get("company_name", "Unknown Company")
    name = f"{lead_data.get('first_name', '')} {lead_data.get('last_name', '')}".strip()
    interested_in = lead_data.get("interested_in", "General Inquiry")
    linkedin_url = lead_data.get("linkedin_url", "")

    dossier_status = ""
    if agent_results and "dossier" in agent_results:
        dossier_content = agent_results.get("dossier", "")
        if dossier_content and "Error" not in dossier_content:
            headline_info = ""
            if "**Title:**" in dossier_content:
                for line in dossier_content.split("\n"):
                    if "**Title:**" in line:
                        title = line.replace("**Title:**", "").strip()
                        if title:
                            headline_info = f" - {title}"
                        break
            dossier_status = f"\n*DOSSIER generated for {name}*{headline_info}"

    message = f"""
*New AIOS Inquiry: {company}*

*Contact:* {name}
*Email:* {lead_data.get('email', 'N/A')}
*LinkedIn:* {linkedin_url if linkedin_url else 'Not provided'}
*Interested In:* {interested_in}
*Pain Points:* {lead_data.get('pain_points', 'Not specified')}{dossier_status}

Call prep brief has been generated and emailed.
"""

    return notify_slack(message)


def send_slack_proposal_notification(client_info: dict) -> dict:
    """
    Send formatted proposal notification to Slack
    """
    company = client_info.get("company_name", "Unknown Company")

    message = f"""
*Proposal Generated: {company}*

A new Business AI OS proposal has been created and sent for review.
Check your email for the complete proposal.
"""

    return notify_slack(message)


# ============================================================================
# GOOGLE DRIVE FUNCTIONS
# ============================================================================

def save_to_drive(content: str, filename: str) -> dict:
    """
    Save content to Google Drive
    """
    try:
        from google.oauth2 import service_account
        from googleapiclient.discovery import build
        import io
        from googleapiclient.http import MediaIoBaseUpload

        creds_path = os.getenv("GOOGLE_DRIVE_CREDENTIALS_PATH", "credentials.json")

        if not os.path.exists(creds_path):
            return {
                "success": True,
                "drive_link": None,
                "message": "Google Drive credentials not configured - file not saved to Drive",
                "local_fallback": save_to_local(content, filename)
            }

        creds = service_account.Credentials.from_service_account_file(
            creds_path,
            scopes=['https://www.googleapis.com/auth/drive.file']
        )

        service = build('drive', 'v3', credentials=creds)

        folder_name = os.getenv("GOOGLE_DRIVE_FOLDER_NAME", GOOGLE_DRIVE_CONFIG["folder_name"])
        folder_id = get_or_create_folder(service, folder_name)

        file_metadata = {
            'name': filename,
            'parents': [folder_id] if folder_id else [],
            'mimeType': 'text/markdown'
        }

        media = MediaIoBaseUpload(
            io.BytesIO(content.encode('utf-8')),
            mimetype='text/markdown',
            resumable=True
        )

        file = service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id, webViewLink'
        ).execute()

        permission = {'type': 'anyone', 'role': 'reader'}
        service.permissions().create(fileId=file.get('id'), body=permission).execute()

        return {
            "success": True,
            "drive_link": file.get('webViewLink'),
            "file_id": file.get('id'),
            "message": f"File saved to Google Drive: {filename}"
        }

    except Exception as e:
        local_path = save_to_local(content, filename)
        return {
            "success": True,
            "drive_link": None,
            "error": str(e),
            "message": f"Could not save to Drive, saved locally: {local_path}",
            "local_path": local_path
        }


def get_or_create_folder(service, folder_name: str) -> Optional[str]:
    """Get existing folder or create new one in Google Drive"""
    try:
        query = f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder' and trashed=false"
        results = service.files().list(q=query, fields="files(id, name)").execute()
        folders = results.get('files', [])

        if folders:
            return folders[0]['id']

        file_metadata = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        folder = service.files().create(body=file_metadata, fields='id').execute()
        return folder.get('id')

    except Exception as e:
        print(f"Error with folder: {e}")
        return None


def save_to_local(content: str, filename: str) -> str:
    """Fallback: Save file locally if Drive is not available"""
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base, ext = os.path.splitext(filename)
    filename_with_timestamp = f"{base}_{timestamp}{ext}"

    filepath = os.path.join(output_dir, filename_with_timestamp)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    return filepath


# ============================================================================
# CALL PREP BRIEF COMPILER
# ============================================================================

def compile_call_prep_brief(agent_results: dict, lead_data: dict) -> str:
    """
    Compile all Phase 1 research into a formatted call prep brief
    """
    company = lead_data.get("company_name", "Prospect")
    contact = f"{lead_data.get('first_name', '')} {lead_data.get('last_name', '')}".strip()

    linkedin = lead_data.get('linkedin_url', '')
    linkedin_display = f"**LinkedIn:** {linkedin}\n" if linkedin else ""

    brief = f"""
# CALL PREP BRIEF: {company}

**Contact:** {contact}
**Email:** {lead_data.get('email', 'N/A')}
**Phone:** {lead_data.get('phone', 'N/A')}
{linkedin_display}**Interested In:** {lead_data.get('interested_in', 'N/A')}

**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M")}

---

"""

    sections = [
        ("dossier", "COMPREHENSIVE DOSSIER"),
        ("contact_profile", "CONTACT RESEARCH"),
        ("company_profile", "COMPANY RESEARCH — AIOS FIT"),
        ("competitive_context", "COMPETITIVE INTELLIGENCE"),
        ("operations_analysis", "OPERATIONS ANALYSIS — AIOS LAYER MAP"),
        ("digital_footprint", "DIGITAL FOOTPRINT"),
        ("project_history", "PROJECT HISTORY"),
        ("network_intelligence", "NETWORK INTELLIGENCE"),
        ("discovery_questions", "DISCOVERY QUESTIONS"),
        ("objection_handling", "OBJECTION HANDLING")
    ]

    for key, title in sections:
        if key in agent_results:
            brief += f"""
## {title}

{agent_results[key]}

---

"""

    brief += f"""
## CALL PREPARATION CHECKLIST

- [ ] Review AIOS fit score from Company Research
- [ ] Note which AIOS layers are weakest (Operations Analysis)
- [ ] Review conversation hooks from Dossier (personal + professional)
- [ ] Prepare layer-specific discovery questions
- [ ] Flag which known objections to expect
- [ ] Have Audit ($3K) + Setup range ready to discuss
- [ ] Confirm calendar availability for follow-up

---

*Prepared by Revaya AI*
*Contact: shannon@revaya.ai*
"""

    return brief


if __name__ == "__main__":
    print("Testing utility functions...")
    result = notify_slack("Test message from Revaya AI system")
    print(f"Slack test: {result}")

    test_content = "# Test Document\n\nThis is a test."
    result = save_to_local(test_content, "test.md")
    print(f"Local save test: {result}")

    print("\nUtilities loaded successfully!")
