# 📧 Daily Email Bot

An automated Python script that sends customized daily update emails with optional attachments — perfect for sending reports to your boss, manager, or clients.

---

## 🚀 Features

- 📬 Sends email using Gmail SMTP
- 📝 Loads email body from a customizable `.txt` template
- 🔁 Replaces placeholders with dynamic content (`{{update}}`)
- 📎 Supports optional file attachments (PDF, DOCX, etc.)
- 🔐 Uses `.env` for securing email credentials
- 🧾 Logs all events to `email_bot.log` for traceability

---

## 📁 Project Structure

```
DAILY_EMAIL_BOT/
├── .env                    # Stores EMAIL_USER and EMAIL_PASS securely
├── main.py                 # Entry point script for automation logic
├── message_template.txt    # Email message template
├── email_bot.log           # Auto-generated log file
├── README.md               # This file
```

---

## 🔧 Setup Instructions

### 1. Clone this repository

```bash
git clone https://github.com/yourusername/daily-email-bot.git
cd daily-email-bot
```

### 2. Create your `.env` file
Create a `.env` file in the root directory:

```
EMAIL_USER=yourgmail@gmail.com
EMAIL_PASS=your_app_password
```

💡 Use an **App Password** from Google (not your real password) 👉 [Generate App Password](https://support.google.com/accounts/answer/185833)

### 3. Customize the message template
Edit `message_template.txt` like this:

```
Hello Boss,

Here is today's update:

{{update}}

Regards,  
Aditya
```

### 4. Install Required Packages
Create a `requirements.txt` file with this content:

```
python-dotenv
```

Then install:

```bash
pip install -r requirements.txt
```

### 5. Run the Bot

```bash
python main.py
```

You'll be asked to:
* 📝 Enter the update message
* 📎 Enter attachment path (optional)

---

## ✅ Example Output

```
📝 Enter today's update: Fixed bug in login module
📎 Enter path to attachment (or press Enter to skip): report.pdf
📎 Attached: report.pdf
✅ Email sent successfully.
```

---

## 🧾 Logs

All email activities are logged to:

```
email_bot.log
```

Example log entries:

```
2025-06-05 19:30:00 - INFO - Email sent to manager@company.com with subject: 'Daily Report - 5 June 2025'
2025-06-05 19:30:00 - INFO - 📎 Attached: report.pdf
```

---

## 🛡️ Security Notes

* **Never** commit your `.env` file to GitHub.
* Add `.env` and logs to `.gitignore`:

```
.env
email_bot.log
```

---

## 📌 Future Ideas

* HTML email support
* Auto-scheduling via cron or Task Scheduler
* Upload logs to Notion or Google Sheets
* Slack/Discord/WhatsApp alert support

---

## 👨‍💻 Author

Made with ❤️ by **Aditya**  
📫 Connect with me on [LinkedIn](https://linkedin.com/in/yourprofile)

---

## 📜 License

This project is licensed under the MIT License.
