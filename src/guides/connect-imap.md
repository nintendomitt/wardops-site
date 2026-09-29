# Connect a mailbox over IMAP

Use this for company email at your hosting provider (for example `mail.yourcompany.com`) and for Gmail, Yandex, Yahoo,
iCloud or Zoho mailboxes. WardOps reads operations emails over IMAP and sends replies over SMTP. You need the email
address and its password; most server settings fill in by themselves.

## Before you start

- **Which mailbox:** the one your team runs shipments from, for example `ops@yourcompany.com`.
- **Who can connect:** a WardOps user with the Admin or Operations role.
- **Password:** your mailbox password for company email at a hosting provider. Gmail, Yandex, Yahoo and iCloud do not
  accept your normal password here; create an **app password** first (see below).
- **Outlook, Hotmail or Microsoft 365:** use **Connect Outlook** instead. See the
  [Outlook setup guide](/guides/connect-outlook/).

## Step 1: Open the IMAP form

In WardOps, go to **Admin → Mailboxes** and select **Connect via IMAP**.

## Step 2: Enter the address and password

Type the email address. The server settings fill in from the address. For company email at a hosting provider,
WardOps suggests `mail.yourcompany.com`, port 993 (SSL) for incoming mail and port 465 (SSL) for outgoing mail.
Then enter the password or app password.

## Step 3: Check the server settings

Most mailboxes work with the suggested settings. If your provider gives different values, for example in the email
section of your hosting control panel, use theirs.

| Mailbox | Incoming (IMAP) | Outgoing (SMTP) | Password |
|---|---|---|---|
| Company email at a hosting provider | `mail.yourcompany.com`, 993 SSL | `mail.yourcompany.com`, 465 SSL | Mailbox password |
| Gmail | `imap.gmail.com`, 993 SSL | `smtp.gmail.com`, 465 SSL | App password |
| Yandex | `imap.yandex.com`, 993 SSL | `smtp.yandex.com`, 465 SSL | App password |
| Yahoo | `imap.mail.yahoo.com`, 993 SSL | `smtp.mail.yahoo.com`, 465 SSL | App password |
| iCloud | `imap.mail.me.com`, 993 SSL | `smtp.mail.me.com`, 587 STARTTLS | App-specific password |
| Zoho | `imap.zoho.com`, 993 SSL | `smtp.zoho.com`, 465 SSL | Password (IMAP must be turned on in Zoho) |

Leave **Username** empty unless your provider signs you in with something other than the email address.

## Step 4: Connect and test

Select **Connect and test**. WardOps signs in to both servers before it saves anything. If both work, you see
**Mailbox connected** and the mailbox is listed as **Connected**. The first sync reads the operations emails of the
last 14 days; after that, new emails are picked up automatically.

## Creating an app password

Menu names can differ slightly between accounts.

- **Gmail:** turn on 2-Step Verification, then open your Google Account → Security → App passwords. In company Google
  Workspace accounts your admin may have turned app passwords off; then use **Connect Gmail**.
- **Yandex:** Yandex ID → Security → App passwords → Mail.
- **Yahoo:** Account info → Account security → Generate app password.
- **iCloud:** Apple Account → Sign-In and Security → App-Specific Passwords (two-factor authentication must be on).

## What WardOps does with your mailbox

- Opens the mailbox read-only: emails are not marked as read, moved or deleted.
- Opens only emails that look like operations mail: a shipping term or a container number in the subject or the first
  lines. Newsletters and personal emails are not downloaded.
- Sends replies and notices from this mailbox within the automation settings you choose, and saves a copy in your
  Sent folder.
- Stores the password encrypted. It is never shown in the app, and it is deleted when you disconnect.

## Disconnect

In **Admin → Mailboxes**, select **Disconnect**. WardOps stops reading and sending right away and deletes the stored
password. If you used an app password, you can also delete it in your email account's security settings.

## Troubleshooting

| What you see | What to do |
|---|---|
| IMAP sign-in was refused | The password is wrong, or your provider needs an app password (see above). |
| Could not connect to the IMAP server | The server name or port is wrong. Check your provider's email settings. |
| SMTP sign-in was refused | Your provider may use different details for outgoing mail. Check the SMTP server, port and username. |
| Security must be SSL or STARTTLS | WardOps never sends a password over an unencrypted connection. Use port 993 (SSL) for IMAP and 465 (SSL) or 587 (STARTTLS) for SMTP. |
| For Outlook and Hotmail addresses, use "Connect Outlook" | Microsoft has turned off password sign-in over IMAP. Use the [Outlook setup guide](/guides/connect-outlook/). |

Questions? Write to us at [{{CONTACT_EMAIL}}](mailto:{{CONTACT_EMAIL}}).
