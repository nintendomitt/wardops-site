# Annex 2: Data Processing Agreement

Version 1.0-DRAFT · 24 September 2026

This Data Processing Agreement ("DPA") is an integral annex to the WardOps Terms of Service. It sets out the
rights and obligations of the parties to the Terms of Service regarding the processing of Personal Data contained
in Customer Data.

## 1. Roles

1.1. The Customer is the **data controller** for the Personal Data it transfers to the Platform or processes
through the Platform. For this data, the Service Provider is the **data processor**, acting on the Customer's
behalf and on its instructions.

1.2. For the account, sign-in and log data of Authorised Users, the Service Provider is an independent data
controller; this data is covered by the Privacy Policy.

## 2. Subject, Nature and Purpose of Processing

| Element | Description |
|---|---|
| Subject | Running the Customer's ocean transport and logistics operations through the Platform |
| Nature | Recording, storing, organising, matching, classifying, reading (text, OCR, AI), generating documents, passing on with the Customer's approval, deleting |
| Purpose | Only to provide, secure and support the Service under the Terms of Service |
| Duration | For the term of the Terms of Service and the deletion periods in Section 9 of this DPA |
| Data subjects | The Customer's customers, shippers, consignees, notify parties, truckers, customs brokers, agents, carrier and terminal staff, and other people appearing in email correspondence |
| Data categories | Identity (name, surname, title), contact (email, phone, address), correspondence content and attachments, personal data appearing in shipment and document details, contact persons on customer records |
| Special categories | Not intended to be processed; the Customer must not transfer such data to the Platform |

## 3. Customer Obligations

3.1. The Customer is responsible for obtaining Personal Data lawfully, having the legal grounds needed to process
it and transfer it to the Service Provider, informing data subjects, obtaining explicit consent where needed, and
its own obligations including registration with the data controllers' registry (VERBİS) where applicable.

3.2. The Customer knows that Personal Data in the email accounts and Integrations it connects will be processed by
the Platform as part of the Service, and makes the related internal arrangements (including informing employees).

3.3. The Customer's instructions are given through this DPA, the Terms of Service and Platform settings. Additional
instructions must be in writing and within the scope of the Service.

## 4. Service Provider Obligations

4.1. The Service Provider processes Personal Data only on the Customer's documented instructions and to provide the
Service; it does not use it for its own purposes, sell it, share it for advertising or use it to train AI models.

4.2. It informs the Customer if it believes an instruction infringes the law.

4.3. It ensures that its employees and contractors with access to Personal Data are bound by confidentiality, and
limits access to the people and extent the work requires.

4.4. It applies the technical and organisational measures in Schedule A and updates them as technology evolves;
updates may not lower the level of protection.

4.5. It helps the Customer, reasonably and to the extent of the tools the Platform offers, to respond to data
subject requests under Article 11 of KVKK. It forwards requests received directly to the Customer without delay.

4.6. It provides reasonable information and documents for the Customer's obligations before the Personal Data
Protection Board and for data security assessments.

## 5. Sub-processors

5.1. The Customer gives general authorisation for the use of the sub-processors listed in Schedule B.

5.2. The Service Provider notifies the Customer in the Platform and at Admin Users' email addresses at least [30]
days before adding or replacing a sub-processor. The Customer may object within this period on reasonable data
protection grounds; if the objection cannot be resolved, the Customer may end the affected Service without
additional cost.

5.3. The Service Provider enters into contracts with sub-processors containing obligations no less protective than
those in this DPA, and is responsible to the Customer for sub-processors' actions within the framework of the
Terms of Service.

5.4. Integrations the Customer chooses to connect itself (for example its own Microsoft 365 or Gmail account) are
subject to the Customer's contract with that provider; these providers are not sub-processors of the Service
Provider.

## 6. International Transfers

6.1. Transfers to sub-processors located abroad, as indicated in Schedule B, are made in line with Article 9 of
KVKK and related secondary legislation, within the framework of standard contracts announced by the Personal Data
Protection Board or other appropriate safeguards provided by law.

6.2. The Customer can stop transfers to the related sub-processor by switching off AI document reading in the
Platform's admin screen. Documents are then read only with text extraction and local OCR.

## 7. Security Incidents

7.1. The Service Provider informs the Customer without undue delay, and in any case **within [48] hours**, after
becoming aware of a Security Incident affecting Personal Data in Customer Data. This period is set so that the
Customer can meet its obligation to notify the Board (72 hours under the Board's decision).

7.2. The notice includes, as far as available: the nature of the incident, the categories of data and approximate
number of people affected, likely consequences, measures taken and proposed, and a contact person. If the
information is not yet complete, notice is given in stages.

7.3. The Service Provider takes reasonable measures to limit the effects of the incident and prevent it happening
again; notifying the Board and data subjects is the Customer's obligation, and the Service Provider provides
reasonable support.

## 8. Audit

8.1. The Customer may, at most once a year, with at least [30] days' written notice and at its own cost, reasonably
audit compliance with this DPA or have an independent auditor do so. The audit does not cover access to other
customers' data or confidential information of the Service Provider and may not unreasonably disrupt its
business.

8.2. Instead of an audit, the Service Provider may provide independent security reports, certifications or
completed security questionnaires.

## 9. Return and Deletion at the End of the Term

9.1. Within [30] days of the end of the Terms of Service, the Customer can export Customer Data.

9.2. After this period, the Service Provider deletes Personal Data in Customer Data from live systems, subject to
legal retention obligations, and from backups within the normal cycle and no later than [90] days. On request, it
confirms the deletion in writing.

## 10. Liability

Liability arising from this DPA is subject, to the extent permitted by mandatory law, to Section 18 of the Terms of
Service. For administrative fines imposed on the Customer by the Board, the Party whose fault caused the breach is
taken as the basis.

## Schedule A: Technical and Organisational Measures

| Area | Measure |
|---|---|
| Company separation | Every query on operational data is restricted by company; users of one company cannot access another company's records. Master data shared by all companies (ports, terminals) can be changed only by the platform administrator. |
| Authentication | Passwords are stored as non-reversible hashes (bcrypt); a minimum password rule applies; users signing in with a temporary password cannot act until they change it; for Google/Apple sign-in, the identity token's signature, audience, issuer and expiry are verified. |
| Session security | Session tokens are time-limited and signed; when a role changes, a user is deactivated or a password changes, the user's open sessions are invalidated. |
| Authorisation | Role-based permissions (admin, operations, view-only); the view-only role cannot change data or send. |
| Integration credentials | Email account access tokens are stored encrypted in the database (AES-based authenticated encryption), never returned in API responses, and deleted when the connection is removed. |
| Transport security | All connections in the production environment are encrypted with TLS. |
| Audit log | Sign-ins, failed sign-ins, user management, outbound sends, setting and template changes and document generation are logged; logs are visible to company admins and cannot be changed by users. Secrets such as passwords or tokens are never written to logs. |
| Outbound control | No email or document is sent on the Customer's behalf without an Authorised User's approval. |
| Data minimisation | Through the email integration, only the content and attachments of messages that appear operational are downloaded; the body of unrelated messages is not opened. Only the necessary page or text is sent to AI. |
| Backups | Regular backups are taken in production and stored encrypted. [Backup frequency and retention to be set after deployment.] |
| Access management | Service Provider staff access to production data is limited on a least-privilege basis and logged. |
| Development | Real Customer Data is not used in test environments; tests do not connect to real email accounts or the AI provider. |

## Schedule B: Sub-processors

| Sub-processor | Service | Location | When |
|---|---|---|---|
| [HOSTING PROVIDER] | Servers, database and file storage | [COUNTRY] | Always |
| Anthropic PBC | AI reading of documents that text and OCR cannot read | USA | Unless the Customer switches the feature off, and only when needed |
| Google LLC | Sign in with Google (authentication) | USA | If the user chooses Google sign-in |
| Apple Inc. | Sign in with Apple (authentication) | USA | If the user chooses Apple sign-in |
| [EMAIL DELIVERY PROVIDER] | System notifications (if any) | [COUNTRY] | [To be decided] |

The Microsoft 365 / Outlook and Gmail accounts the Customer connects itself are subject to the Customer's contract
with the relevant provider (Section 5.4).
