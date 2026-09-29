# Connect your Outlook or Microsoft 365 mailbox

WardOps reads the operations emails in your mailbox and sends replies from it. Connecting takes about two minutes.
For a company mailbox on Microsoft 365, your IT admin may need to approve WardOps once.

## Before you start

- **Which mailbox:** the one your team runs shipments from, for example `ops@yourcompany.com`. You sign in as that
  mailbox, so you need its password and your usual sign-in check, such as an authenticator app.
- **Who can connect:** a WardOps user with the Admin or Operations role.
- **Personal or company account:** Outlook.com and Hotmail addresses connect directly. Microsoft 365 mailboxes connect
  the same way, unless your company only lets apps approved by its IT admin read email (see Step 4).

## Step 1: Open Mailboxes in WardOps

In WardOps, go to **Admin → Mailboxes** and select **Connect Outlook**.

## Step 2: Sign in with Microsoft

Microsoft's sign-in page opens. Choose the mailbox account, or select **Use another account**, and sign in.

## Step 3: Review and accept the permissions

Microsoft lists what WardOps asks for. Select **Accept**.

| Permission | Why WardOps needs it |
|---|---|
| Read your mail | To read operations emails and their attachments |
| Send mail as you | To send replies and notices from this mailbox |
| Maintain access to data you have given it access to | To keep reading new emails without asking you to sign in again |
| Sign you in and read your profile | To learn the mailbox address |

Microsoft may show the app as **unverified**. This label is about how the app publisher is registered with
Microsoft; it does not change what WardOps can access.

## Step 4: If you see "Need admin approval"

Many companies let only apps approved by their IT admin read email. Microsoft then shows **Need admin approval**
instead of the permissions.

- In WardOps, under **Admin → Mailboxes**, select **Copy admin approval link** and send the link to your IT admin.
- Your admin opens the link, signs in with an admin account (for example Global Administrator, Cloud Application
  Administrator or Application Administrator), reviews the permissions and selects **Accept**. This approves WardOps
  for your company; each person still connects only their own mailbox.
- Back in WardOps, select **Connect Outlook** again.

If WardOps is already listed in your company's app list, your admin can also approve it in the Microsoft Entra admin
center: **Entra ID → Enterprise apps → All applications → WardOps → Permissions → Grant admin consent**.

## Step 5: Check the connection

Back in WardOps you see **Mailbox connected**, and the mailbox is listed as **Connected**. The first sync reads the
operations emails of the last 14 days; after that, new emails are picked up automatically.

## What WardOps does with your mailbox

- Opens only emails that look like operations mail: a shipping term or a container number in the subject or the first
  lines. Newsletters and personal emails are not opened, and their attachments are not downloaded.
- Does not mark emails as read, move them or delete them.
- Sends replies and notices from this mailbox within the automation settings you choose. Sent emails appear in your
  Sent Items.
- Keeps the access it receives from Microsoft encrypted. It is never shown in the app.

## Disconnect

In **Admin → Mailboxes**, select **Disconnect**. WardOps stops reading and sending right away and deletes the stored
access. Your IT admin can also remove WardOps from your company's apps in the Microsoft Entra admin center.

## Troubleshooting

| What you see | What to do |
|---|---|
| Need admin approval | Send your IT admin the approval link (Step 4). |
| The mailbox was not connected (permission not given) | The permissions screen was closed or declined. Select **Connect Outlook** again and accept. |
| The mailbox shows an error after a password change | Microsoft ended the access. Select **Connect Outlook** again. |
| Emails are read but replies are not sent | The permission to send mail was not approved. Ask your admin to approve with the link (Step 4), then connect again. |
| Your team works from a shared mailbox without its own sign-in | Shared mailboxes cannot be connected yet. Connect a user mailbox, or redirect the shared mailbox's email to one. |
| Your email is with a hosting company, Yandex, Yahoo or iCloud | Use **Connect via IMAP** in the same screen instead. See the [IMAP setup guide](/guides/connect-imap/). |

Questions? Write to us at [{{CONTACT_EMAIL}}](mailto:{{CONTACT_EMAIL}}).
