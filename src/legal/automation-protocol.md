# Annex 1: Automation, Approval and Responsibility Protocol

Version 1.0-DRAFT · 24 September 2026

This Protocol is an integral annex to the WardOps Terms of Service. It sets out in detail which actions the
Platform performs on its own, which actions require an Authorised User's approval, the Customer's checking
obligations for each function, and how responsibility is shared when something goes wrong. Terms not defined
here have the meaning given in the Terms of Service.

## 1. Principles

1.1. **Every outbound action needs a person's approval.** Before sending an email, message or document to third
parties (customers, carriers, truckers, terminals, customs brokers, agents, etc.) on the Customer's behalf, the
Platform asks for the explicit approval of an Authorised User. The approval is written to the log together with
the approving user, the date, the time and the content sent.

1.2. **The Platform does not silently change existing information.** A value read from a document or email does
not overwrite a value already entered on the file; empty fields are filled and conflicts are shown as alerts and
tasks. For changing information such as the estimated time of arrival (ETA), source priority applies and every
change is kept in the history.

1.3. **An alert does not replace checking.** Alerts and tasks are based on recorded data and defined rules. The
absence of an alert does not mean there is no risk.

1.4. **Documents and communications are the Customer's statements.** The Customer is the issuer and sender of
documents and communications generated in or sent through the Platform.

1.5. **Transparency.** The Platform shows where a value came from (document, email, carrier system, manual
entry), when it was recorded and whether it was applied. The Customer weighs its decisions with this
information.

## 2. Automation and Responsibility by Function

In the table below, "Automatic" shows whether the action is done inside the Platform without a user step, and
"Reaches third parties" shows whether the action on its own reaches anyone outside.

| Function | What the Platform does | Automatic | Reaches third parties | Approval | Customer's checking obligation |
|---|---|---|---|---|---|
| Reading and matching email | Reads operational emails in the connected account, finds the file from the numbers in them, classifies them | Yes | No | Not needed | Correct emails linked to the wrong file or not linked |
| Unanswered email tracking | Opens a task when an email awaiting a reply passes the time threshold | Yes | No | Not needed | Set the threshold, follow up tasks |
| ETA from delay emails | Reads the new ETA; records it in the history with source "email"; does not apply it if a more reliable source exists | Yes | No | Not needed | Confirm important ETA changes with the carrier or terminal |
| Reading document fields (text, OCR) | Reads numbers, vessel, port and dates from bills of lading, arrival notices and similar documents | Yes | No | Not needed | Check documents sent to review and conflict alerts |
| Reading document fields (AI) | If text/OCR is not enough and the feature is on, sends the necessary part of the document to the AI provider | Yes (setting) | Data goes to a sub-processor | Account setting | Verify read values; switch the feature off if preferred |
| Tracking data | Records events from carriers, terminals or data providers and calculates the cargo's stage | Yes | No | Not needed | Check the source system for critical events |
| Alerts and tasks | Opens tasks for delays, ETA shifts, free time, document deadlines, release, ISF/AMS matching and similar | Yes | No | Not needed | Review tasks, set thresholds to fit operations |
| Demurrage/detention estimate | Calculates an estimated amount from the defined tariff | Yes | No | Not needed | Define tariffs correctly; rely on the carrier invoice for the final amount |
| Reply draft | Prepares a draft from recorded information for an email asking about status | Yes | **No** | **Required to send** | Check recipient, content and file; correct if needed |
| Proactive notification draft | Prepares a draft to the customer for ETA shifts, arrival and pickup readiness | Yes | **No** | **Required to send** | Check recipient and content |
| Sending email | Sends the approved draft from the connected account | **No** | Yes | Authorised User | Final check before approving |
| Document generation (AN, DO, release) | Produces PDF/Word from company details and file records; shows missing fields and warnings | **No** | No (the Customer passes on the downloaded document) | Authorised User | Verify the content, especially the receiving party and release status |
| Saving documents | Adds the generated document to the file's documents if requested | No | No | Authorised User | — |
| ISF record | Records ISF filing details and status; warns if not matched with AMS | Partly | Yes, if a provider is connected | Authorised User | File on time and follow the match |
| User management | Adds users, assigns roles, deactivates; ends sessions when permissions change | No | No | Admin | Keep access up to date |
| Connecting integrations | Connects email accounts etc. with the Customer's authority; stores credentials encrypted | No | No | Admin / Authorised User | Be authorised over the connected account |

## 3. How Approval Works

3.1. **Draft stage:** replies and notifications prepared by the Platform are in "draft" status. Drafts are visible
only to the Customer's Authorised Users and are not passed to any third party.

3.2. **Review:** the Authorised User sees and can edit the draft's recipients, CC recipients, subject and text.
The incoming email and file information the draft is based on are shown on the same screen.

3.3. **Approval and sending:** sending happens when the Authorised User clicks "Approve and send" and confirms
the recipients in the confirmation step. View-only users cannot send.

3.4. **Sending manually:** if the Customer sends the text from its own email program, it marks the draft as "sent
manually". This mark also counts as approval and is logged.

3.5. **Answered another way:** if another reply is detected in the same conversation through the connected
account, the pending draft is closed automatically; this does not count as a send.

3.6. **Sending error:** if the email provider rejects the send, the draft moves to "could not be sent" and the
error is shown. Retrying is the Authorised User's decision.

3.7. **Logging:** approvals, sends, manual-send marks and draft closures are logged with the user, time and
recipients. These logs are visible to the Customer's admins and cannot be changed.

## 4. Incident Scenarios and Sharing of Responsibility

This section shows, for the main incidents that can happen in operations, the Platform's preventive measures,
the Customer's measures and who is responsible. The scope and cap of liability are subject to Section 18 of the
Terms of Service.

### 4.1. Email sent to the wrong recipient or with the wrong content

- **Platform measures:** drafts are never sent without approval; recipients are shown again in the confirmation
  step; the suggested recipient comes from the sender of the incoming email or the address on the customer
  record; internal references are not added to text going to the customer; sends are logged.
- **Customer measures:** check recipients and content before approving; keep email addresses on customer records
  up to date; apply a four-eyes check for sensitive sends.
- **Responsibility:** the Customer is responsible for the content and recipients of emails sent with an
  Authorised User's approval. If a software error causes the Platform to send without approval, the Service
  Provider's liability is assessed under Section 18 of the Terms of Service.

### 4.2. Email linked to the wrong file

- **Platform measures:** a number that matches more than one file is not used for matching; if no number points
  to a single file, the email is not linked to any file and a task is opened; internal reference numbers are not
  used for matching; the number used for the match is recorded.
- **Customer measures:** correct wrong matches; do not send a draft prepared for an email linked to the wrong
  file.
- **Responsibility:** a wrong match stays inside the Platform. The Customer is responsible for the consequences of
  actions approved on the basis of that match.

### 4.3. Wrong or outdated ETA

- **Platform measures:** ETA source priority (carrier/terminal system > manual entry > email > booking >
  document) is applied; a value from a weaker source is recorded but not applied; old information does not
  overwrite newer information; an ETA from a weaker source is written as "estimated" in text going to the
  customer; after the vessel has arrived, the old ETA is not written to the customer.
- **Customer measures:** confirm the ETA with the source system for critical decisions (trucking appointments,
  customer commitments).
- **Responsibility:** an ETA is an estimate by nature. The Service Provider is not liable for damages caused by
  third-party data being wrong or late.

### 4.4. Wrong release or delivery instruction

- **Platform measures:** if no freight/document or customs release is recorded, the document screen warns; in
  that case the release document does not state a reason such as "original bill of lading surrendered"; tasks are
  opened for cargo that is released but has no delivery instruction.
- **Customer measures:** before issuing a release or delivery order, verify payment, the original bill of lading
  or telex release, customs release and the authority of the receiving party from its own sources.
- **Responsibility:** releases and delivery orders are the Customer's documents; the Service Provider is not
  responsible for damages caused by cargo being delivered to the wrong party.

### 4.5. Missing the last free day

- **Platform measures:** tasks are opened as the last free day approaches and after it passes; a critical alert is
  given if release is missing; an estimated cost is shown from the defined tariff.
- **Customer measures:** record the last free day and empty return date correctly; set alert thresholds to fit its
  operations; follow up tasks.
- **Responsibility:** demurrage, detention and storage charges are not the Service Provider's responsibility.

### 4.6. ISF filed late or not matched with AMS

- **Platform measures:** tracking of the ISF document requirement and deadline; an alert after the vessel departs
  if the ISF is filed but not matched with AMS, becoming a critical task as arrival approaches.
- **Customer measures:** file, or have the ISF filed, on time; confirm the match with the filer or broker and record
  it in the Platform.
- **Responsibility:** ISF and AMS filings and related penalties are the responsibility of the Customer and the
  filing party.

### 4.7. Data read wrongly from a document

- **Platform measures:** container number check digit and date format checks; documents with low confidence or
  conflicting with the file are sent to review and a task is opened; a read value does not overwrite an existing
  value.
- **Customer measures:** check documents sent to review and conflict alerts; verify critical fields against the
  original document.
- **Responsibility:** the Customer is responsible for the consequences of actions approved on the basis of a
  wrong reading.

### 4.8. Integration or Service outage

- **Platform measures:** integration errors are shown on the account screen and in tasks; an alert if tracking
  data stops arriving for a long time; an error in one account does not stop other accounts.
- **Customer measures:** follow critical actions in the source systems during an outage.
- **Responsibility:** third-party outages are not the Service Provider's fault; outages of the Service itself are
  covered by Section 11 of the Terms of Service.

### 4.9. Unauthorised access

- **Platform measures:** data separation by company; role-based permissions; password rules; logging of failed
  sign-ins; ending sessions when permissions or passwords change; audit log.
- **Customer measures:** remove access of departing employees immediately; protect passwords and identity provider
  accounts; report suspicious activity.
- **Responsibility:** damages caused by the takeover of the Customer's user accounts are the Customer's
  responsibility unless caused by a security vulnerability in the Platform.

### 4.10. Data loss

- **Platform measures:** regular backups in the production environment; audit log.
- **Customer measures:** also keep documents subject to legal retention obligations in its own systems.
- **Responsibility:** subject to Sections 11.3 and 18 of the Terms of Service.

## 5. Incident Reporting and Cooperation

5.1. When the Customer notices an error or incident it believes comes from the Platform, it reports the date, the
related file number, screenshots if available and the impact to [SUPPORT EMAIL]. Security incidents are reported
immediately to [SECURITY EMAIL].

5.2. On receiving a report, the Service Provider logs the incident, sets its severity and informs the Customer of
the outcome. For critical incidents (outbound communication without approval, breach of data separation,
security incident), the first response is given within [4] business hours.

5.3. The Parties cooperate reasonably to limit damage. On request, the Service Provider provides the Customer with
the logs related to the incident.

## 6. Recommended Operational Checklist for the Customer

The following checks are the recommended minimum when using the Platform:

- Review open tasks and critical alerts every day.
- Check the recipient and file number on every draft going to a customer.
- Before a release or delivery order, confirm payment, bill of lading and customs status at the source.
- Enter last free day and empty return dates on the file.
- Check documents sent to review on the same day.
- Review the user list monthly and remove access for people who have left.
- Keep email and contact details on customer records up to date.
- Set alert thresholds (free time warning, unanswered email time, stage durations) to your operation's real
  timings.
