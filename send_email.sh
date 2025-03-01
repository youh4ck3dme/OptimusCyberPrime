#!/bin/bash

# Email settings
SENDER="h4ck3d@h4ck3d.me"
RECIPIENT="h4ck3d@h4ck3d.me"
SUBJECT="Automated Email from iSH"
BODY="Hello, this is a test email sent from iSH using msmtp."
ATTACHMENT=""  # Napr. "/path/to/file.txt" (Nechaj prázdne, ak nechceš prílohu)

# Msmtp log file
LOGFILE="$HOME/msmtp.log"

# Check if msmtp is installed
if ! command -v msmtp &> /dev/null; then
    echo "ERROR: msmtp is not installed. Install it using: apk add msmtp"
    exit 1
fi

# Create email content
EMAIL_MESSAGE="/tmp/email_message.txt"
{
    echo "From: $SENDER"
    echo "To: $RECIPIENT"
    echo "Subject: $SUBJECT"
    echo
    echo "$BODY"
} > "$EMAIL_MESSAGE"

# Attach file if specified
if [ -n "$ATTACHMENT" ]; then
    echo "Attaching file: $ATTACHMENT"
    cat "$ATTACHMENT" >> "$EMAIL_MESSAGE"
fi

# Send email
cat "$EMAIL_MESSAGE" | msmtp --debug --logfile="$LOGFILE" "$RECIPIENT"

# Cleanup
rm -f "$EMAIL_MESSAGE"

echo "✅ Email sent to $RECIPIENT. Check log: $LOGFILE"