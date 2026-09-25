# Annex 3: Records, Usage Data and Feedback Protocol

Version 1.0-DRAFT · 24 September 2026

This Protocol is an integral annex to the WardOps Terms of Service. It sets out which records the Platform keeps,
how user experience and feedback are collected, what these records are used for, who can access them and how long
they are kept.

## 1. Purpose

1.1. Records are kept (a) to prove which action was taken by whom and when, (b) to detect and investigate security
incidents, (c) to determine the Parties' responsibility in possible disputes, and (d) to fix errors in and improve
the Service.

1.2. Records protect the Customer and the Service Provider alike: who approved an email, who generated a document
or who changed a setting is shown by these records.

## 2. Records Kept

### 2.1. Audit log

The following actions are recorded with the user who performed them, the date and time, the related record (file,
user, draft, etc.) and a summary:

- sign-in, sign-in with Google/Apple and failed sign-in attempts;
- password changes and password resets;
- company sign-up, adding users, role changes, deactivation;
- sending replies and notifications, marking them as sent manually, closing them and sending errors (including
  recipients);
- connecting and disconnecting mail accounts;
- changes to alert thresholds, tariffs, company details, logo and document templates;
- document generation and manual corrections of document fields;
- re-reading a document with AI;
- changes to customer records and pricing information;
- merges in shared master data (ports);
- acceptance of terms and policies.

**Passwords, access tokens, keys or similar secrets are never written to the audit log.**

### 2.2. Acceptance records

For acceptance of terms and policies, the accepting user, company, document name and version, a hash of the text,
the date and time, IP address and browser information are stored.

### 2.3. Operational history

The history of files (ETA changes and their sources, events, tasks opened and closed, documents read and their
validation results, the content of replies sent) is kept as part of Customer Data.

### 2.4. AI usage records

For each AI call, the date, the model used, the input type (text or image), input and output token counts, success
status and the related document are recorded. This record does not contain document content; it is kept to monitor
costs and usage limits.

### 2.5. Technical records

Server and application error logs, performance measurements and security logs are kept to fix errors and detect
attacks. Customer Data content is kept out of these logs as far as possible.

## 3. Collecting User Experience and Feedback

3.1. To improve the Service, the Service Provider may collect feedback through:

- in-Platform feedback forms and satisfaction questions;
- support requests and email correspondence;
- interviews, usability tests and surveys the Customer agrees to take part in;
- aggregated statistics on how often Platform features are used (for example the number of emails processed per
  day, the number of documents generated, the distribution of alert types).

3.2. Interviews and usability tests are recorded (audio, video or screen) **only with the participant's prior
information and consent.** The participant can ask for recording to stop at any time.

3.3. Personal data in feedback is anonymised after the feedback has been assessed or deleted within the periods in
Section 5.

3.4. The Customer's name, logo or feedback is used for references, case studies or marketing **only with the
Customer's written permission.**

3.5. The Service Provider does not use third-party advertising or tracking tools to measure product use. Usage
statistics are aggregated so that they do not identify individuals.

3.6. Feedback and usage statistics are not used as Customer Data in training AI models.

## 4. Access

| Record | Customer access | Service Provider access |
|---|---|---|
| Audit log | Company admins see it in the Platform | Only for support, security investigation or legal requirement; access is logged |
| Acceptance records | Company admins, on request | To prove acceptance and in disputes |
| Operational history | All users with permission | Only for support at the Customer's request |
| AI usage records | Company admins (summary) | Cost and capacity management |
| Technical records | — (incident summary on request) | Operations and security team |

Records cannot be changed or deleted by users. The Service Provider takes the technical measures needed to protect
their integrity.

## 5. Retention Periods

| Record | Period |
|---|---|
| Audit log | For the term and [2] years after it ends |
| Acceptance records | [10] years after the end of the Terms |
| Security and sign-in records | [2] years |
| AI usage records | [2] years |
| Technical records | [90] days |
| Interview and test recordings | Until assessed, at most [1] year |
| Support correspondence | [3] years |

Expired records are deleted or anonymised. In a legal dispute or official investigation, the related records may be
kept until it is resolved.

## 6. Evidential Value of Records

The Parties agree that the records under this Protocol may be used as evidence within the framework of Section 25 of
the Terms of Service. The Customer has the right to challenge their accuracy and submit counter-evidence.

## 7. Customer Requests

The Customer can request, through [SUPPORT EMAIL], a copy of its company's audit and acceptance records, summaries of
technical records related to an incident, and a breakdown of AI usage. Requests are handled within a reasonable time
and in a machine-readable format.
