# Annex 1: Automation and Responsibility Protocol

Version 1.7-DRAFT · 29 September 2026

This Protocol is an integral annex to the WardOps Terms of Service. It sets out in detail which actions the
Platform performs on its own, which messages it sends automatically, which actions need an Authorised User, the
Customer's checking
obligations for each function, and how responsibility is shared when something goes wrong. Terms not defined
here have the meaning given in the Terms of Service.

## 1. Principles

1.1. **Automatic sending is limited to a defined scope.** On the Customer's behalf and from the Customer's
connected email account, the Platform sends only the messages listed in Section 3 (replies to status questions;
answers to the customer's out-of-routine questions; notices for an ETA change, vessel arrival and cargo ready for pickup; the customs document pack to the
customer's customs broker; the payment request to a customer on prepayment terms; the missing-information request on a file opened from email) without waiting for an Authorised
User's approval. These messages are built by rules and only from information recorded on the file; no AI writes
the text. Every other email, message or document to third parties is sent by an Authorised User's action. The
Customer can switch automatic sending off in the company settings; while it is off, messages wait and are sent
by an Authorised User. Every send is logged with the sender (the Platform or a user), the date, the time, the
recipients and the content.

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

| Function | What the Platform does | Automatic | Reaches third parties | User action | Customer's checking obligation |
|---|---|---|---|---|---|
| Reading and matching email | Reads operational emails in the connected account, finds the file from the numbers in them, classifies them | Yes | No | Not needed | Correct emails linked to the wrong file or not linked |
| Unanswered email tracking | Opens a task when an email awaiting a reply passes the time threshold | Yes | No | Not needed | Set the threshold, follow up tasks |
| Opening files from email | Opens a new file from a bill of lading, arrival notice or booking confirmation in an unmatched email (or from a pre-alert's text); does not open one if any number points to an existing file | Yes (can be switched off) | No | Not needed | Check the opened file, the customer and the parties |
| ETA from delay emails | Reads the new ETA; records it in the history with source "email"; does not apply it if a more reliable source exists | Yes | No | Not needed | Confirm important ETA changes with the carrier or terminal |
| Reading document fields (text, OCR) | Reads numbers, vessel, port and dates from bills of lading, arrival notices and similar documents | Yes | No | Not needed | Check documents sent to review and conflict alerts |
| Reading document fields (AI) | If text/OCR is not enough and the feature is on, sends the necessary part of the document to the AI provider | Yes (setting) | Data goes to a sub-processor | Account setting | Verify read values; switch the feature off if preferred |
| Understanding email and documents (Jev) | Decides the email's type and the customer's out-of-routine questions (saved to the customer memory); chooses the type of a document the rules cannot recognise and which field each document value belongs to. Chooses only among values found in the document and writes no text. Rules run first; if Jev does not answer, rules decide the same topics | On (the company can switch it off) | Data goes to a sub-processor | Not needed | Review fields filled by Jev and the customer memory; switch the feature off if wanted |
| Tracking data | Records events from carriers, terminals or data providers and calculates the cargo's stage | Yes | No | Not needed | Check the source system for critical events |
| Alerts and tasks | Opens tasks for delays, ETA shifts, free time, document deadlines, release, ISF/AMS matching and similar | Yes | No | Not needed | Review tasks, set thresholds to fit operations |
| Demurrage/detention estimate | Calculates an estimated amount from the defined tariff | Yes | No | Not needed | Define tariffs correctly; rely on the carrier invoice for the final amount |
| Reply to a status question | Builds a reply from recorded information for an email linked to a file and, if it passes the brakes in Section 3, sends it from the connected account | Yes | **Yes** | Not needed (can be switched off) | Keep file records (ETA, release, parties) correct and current; review sent replies |
| Answer to the customer's out-of-routine question | For an email from the file's customer asking to pay and pick up before the last free day, about terminal charges, or for charges or a document, writes an answer from the file's records (invoice status, last free day, release status); attaches the issued invoices and the requested document (only the house B/L and documents the Platform generated; never the master B/L or the carrier's arrival notice); does not estimate a charge whose exact amount is unknown. For a complaint, an HS code difference or an out-of-routine instruction it sends only an acknowledgement. It always opens a task for the team and sends with the same brakes | Yes | **Yes** | Not needed (can be switched off) | Keep customer email addresses, invoices and document types on the file correct; follow up the tasks and the topics that need a decision (complaint, HS difference, instruction) |
| Missing-information request | For a file opened from an email, asks the party that sent the document (for a forwarded email, the original sender) for the information still blank on the file (shipper, consignee, notify, vessel/voyage, dates, container and cargo details, B/L release type, commercial invoice and packing list) in one email, once per file and with the same brakes | Yes | **Yes** | Not needed (can be switched off) | Check the parties read from the document or taken from its layout; watch that the request goes to the right party |
| Proactive notice | Builds and sends a notice to the customer for an ETA change, vessel arrival and pickup readiness, with the same brakes | Yes | **Yes** | Not needed (can be switched off) | Keep email addresses on customer records up to date |
| Customs documents to the broker | When the customer's broker handles clearance, sends the Platform-generated arrival notice, the commercial invoice and the packing list to the broker in one email once all are on the file, with the same brakes (once per file) | Yes | **Yes** | Not needed (can be switched off) | Check the broker's email address, the clearance choice on the file and the attached documents |
| Payment request | For a customer marked as prepayment (no credit) on its record, sends the unpaid invoices and debit notes issued on the file as a payment request, 7 days before arrival or once the vessel arrives, with the same brakes | Yes | **Yes** | Not needed (can be switched off) | Keep the customer's payment terms and issued invoices correct; mark an invoice as paid when payment arrives |
| Draft comparison | Compares the House B/L and Master B/L drafts; if they differ, prepares a correction email to the origin agent but does not send it | Yes | No | Authorised User sends | Check that the differences are real and edit the text if needed |
| Manual email sending | Sends a message that could not go automatically, or that waits because automatic sending is off | **No** | Yes | Authorised User | Check recipient and content before sending |
| Charges and accounting documents | Issues invoices, debit notes and credit notes from entered charges, numbers them, produces PDFs and statements; never suggests amounts | **No** | No (the Customer passes on the document) | Authorised User | Verify charges, amounts, the billed party and tax obligations; an issued document does not change, corrections are made with a credit note |
| Document generation (AN, DO, release, POD) | Produces PDF/Word from company details and file records; shows missing fields and warnings | **No** | No (the Customer passes on the downloaded document) | Authorised User | Verify the content, especially the receiving party and release status |
| Saving documents | Adds the generated document to the file's documents if requested | No | No | Authorised User | — |
| ISF record | Records ISF filing details and status; warns if not matched with AMS | Partly | Yes, if a provider is connected | Authorised User | File on time and follow the match |
| User management | Adds users, assigns roles, deactivates; ends sessions when permissions change | No | No | Admin | Keep access up to date |
| Connecting integrations | Connects email accounts etc. with the Customer's authority; stores credentials encrypted | No | No | Admin / Authorised User | Be authorised over the connected account |

## 3. How Automatic Sending Works, and Its Brakes

3.1. **Scope:** the Platform sends automatically only (a) replies to emails that ask about status and are linked
unambiguously to one file, and (b) notices when the ETA moves from the value last told to the customer by the
company threshold, when the vessel arrives (imports) and when the cargo is ready for pickup, and (c) for imports
cleared by the customer's customs broker, the Platform-generated arrival notice with the commercial invoice and the
packing list to the broker in one email once all are on the file, and (d) for a customer marked as prepayment on its
record, a payment request with the unpaid invoices issued on the file attached, 7 days before arrival or once the
vessel arrives, and (e) answers to an out-of-routine question in an email from the file's customer (the sender must
match the customer record or the customer's company domain): paying to pick up before the last free day, terminal
charges, charges and document requests, and an acknowledgement for a complaint, an HS code difference or an
instruction, and (f) for a file opened from an email, a request for the information still missing on the file
to the party that sent the document (the original sender of a forwarded email), once per file and without
attachments. Amounts, invoices and documents are never sent to a sender other than the customer. The Platform does
not give the freight release by itself. The draft correction email to the origin agent
is not sent automatically; an Authorised User sends it. Other emails are not answered; those waiting for a reply come back to the team as tasks after the time threshold.

3.2. **Content:** a message contains only information recorded on the file; information that is not recorded is
not added. An ETA from a weaker source is written as "estimated". Internal reference numbers are not added to
text going to the customer. The signature and company identity come from the Customer's record.

3.3. **Brakes:** a message is not sent, and waits on the Replies screen where an Authorised User can send it,
when: automatic sending is switched off for the company; no email account is connected; a recipient is on the
Customer's own domain (internal correspondence); the email being answered has been answered another way; a
status reply went to the same recipient for the same file in the last 12 hours; or the message was prepared
more than 2 days ago. Auto-replies, out-of-office messages and delivery failure notices are treated as not
waiting for a reply, and no reply is prepared for them.

3.4. **Manual sending:** an Authorised User can review, edit and send waiting messages, or send the text from
their own email program and mark it "sent manually". Users with the viewer role cannot send.

3.5. **Answered another way:** if another reply is detected on the same conversation through a connected
account, the waiting message is closed automatically; this does not count as a send.

3.6. **Sending errors:** if the email provider rejects a send, the message moves to "failed" and the error is
shown. The Platform does not retry on its own; retrying is the Authorised User's decision.

3.7. **Logging:** every automatic and manual send, closure and mark is logged with the sender (the Platform or a
user), the time, the recipients and the content. Company admins can see these logs and they cannot be changed.

3.8. **Switching off:** the Customer can switch automatic sending off in the company settings at any time. It
applies from the next sending cycle and does not affect messages already sent.

## 4. Incident Scenarios and Sharing of Responsibility

This section shows, for the main incidents that can happen in operations, the Platform's preventive measures,
the Customer's measures and who is responsible. The scope and cap of liability are subject to Section 18 of the
Terms of Service.

### 4.1. Email sent to the wrong recipient or with the wrong content

- **Platform measures:** automatic messages are built only from recorded information; the recipient is the
  sender of the incoming email or the address on the customer record and is never guessed; nothing is sent to
  internal recipients or auto-responders; the same recipient is not written to again within a short time;
  internal references are not added to text going to the customer; every send is logged; the Customer can switch
  automatic sending off.
- **Customer measures:** keep file records (ETA, release, parties) and customer email addresses correct and
  current; review email matches and sent messages regularly; switch automatic sending off for customers or
  periods where it does not fit; check recipient and content on manual sends.
- **Responsibility:** an automatic message is built from information the Customer entered or the Platform
  recorded on the Customer's behalf; the Customer is responsible for the accuracy of that information and for
  the decision to keep automatic sending on. The Customer is responsible for the content and recipients of
  manual sends. If a software error causes the Platform to send outside the scope or brakes defined in this
  Protocol, the Service Provider's liability is assessed under Section 18 of the Terms of Service.

### 4.2. Email linked to the wrong file

- **Platform measures:** a number that matches more than one file is not used for matching; if no number points
  to a single file, the email is not linked to any file and a task is opened; internal reference numbers are not
  used for matching; the number used for the match is recorded.
- **Customer measures:** correct wrong matches; if an automatic reply went out for an email linked to the wrong
  file, send the customer a correction.
- **Responsibility:** a wrong match can lead to an automatic reply built from the matched file. If the match
  followed the rules in this section, the Customer is responsible for the consequences; if it results from a
  software error against these rules, the Service Provider is responsible within Section 18 of the Terms of
  Service.

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
- **Responsibility:** the Customer is responsible for the consequences of actions (including automatic messages)
  based on a wrong reading that stayed on the file without the Customer's review.

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
the outcome. For critical incidents (outbound communication outside the defined scope or brakes, breach of data separation,
security incident), the first response is given within [4] business hours.

5.3. The Parties cooperate reasonably to limit damage. On request, the Service Provider provides the Customer with
the logs related to the incident.

## 6. Recommended Operational Checklist for the Customer

The following checks are the recommended minimum when using the Platform:

- Review open tasks and critical alerts every day.
- Review automatically sent messages and those waiting on the Replies screen; keep customer email addresses
  up to date.
- Check charges and the billed party before issuing accounting documents; meet official invoicing and tax
  obligations in your own accounting system.
- Before a release or delivery order, confirm payment, bill of lading and customs status at the source.
- Enter last free day and empty return dates on the file.
- Check documents sent to review on the same day.
- Review the user list monthly and remove access for people who have left.
- Keep email and contact details on customer records up to date.
- Set alert thresholds (free time warning, unanswered email time, stage durations) to your operation's real
  timings.
