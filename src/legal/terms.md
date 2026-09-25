# WardOps Terms of Service

Version 1.0-DRAFT · 24 September 2026

These Terms govern the rights and obligations between the business that uses the WardOps platform and the
company that operates it. The annexes to these Terms (Annex 1 Automation, Approval and Responsibility Protocol;
Annex 2 Data Processing Agreement; Annex 3 Records, Usage Data and Feedback Protocol) form an integral part of
these Terms. If an annex conflicts with this text, the annex prevails to the extent it is specific to its subject.

## 1. Parties

1.1. **Service Provider:** [COMPANY NAME], [ADDRESS], [COMPANY REGISTRATION NO.], [TAX OFFICE / NO.],
email: [EMAIL] ("Service Provider").

1.2. **Customer:** The legal entity or merchant whose details are given at sign-up or in an order form and that
accepts these Terms electronically ("Customer").

1.3. The Service is offered only to businesses acting for commercial purposes. The Customer confirms that it is
not acting as a consumer and uses the Service within its commercial or professional activity.

## 2. Definitions

Capitalised terms in these Terms have the following meanings:

- **Platform / Service:** the cloud-based software offered under the name WardOps that manages shipment files,
  containers, routes, events, documents, emails and tasks, produces alerts, prepares drafts and generates
  documents, together with its application programming interfaces (APIs), administration commands and
  documentation.
- **Authorised User:** individuals the Customer gives access to the Platform and who act on the Customer's behalf
  (employees, consultants and others authorised by the Customer).
- **Admin User:** an Authorised User who can add users, change roles, connect integrations and change company
  details and templates in the Customer account.
- **Customer Data:** all data uploaded or entered by the Customer or Authorised Users, brought into the Platform
  through Integrations, or generated in the Platform on the Customer's behalf, including shipment, container,
  party, document, email, task and log data.
- **Operational Data:** the part of Customer Data that relates to the Customer's transport and logistics
  activities (files, bills of lading, containers, arrival notices, releases, customs and ISF information, etc.).
- **Personal Data:** any information relating to an identified or identifiable natural person within the meaning
  of the Turkish Personal Data Protection Law No. 6698 ("KVKK") and, where applicable, other data protection
  laws.
- **Output:** any result the Platform produces by processing Customer Data: parsed fields, matches,
  classifications, estimated dates, stage information, alerts, tasks, statistics, reply and notification drafts,
  documents (arrival notice, delivery order, cargo release, etc.) and reports.
- **Draft:** a text or document the Platform prepares for an Authorised User to review and approve, and which is
  not sent to third parties unless approved.
- **Approved Action:** an action an Authorised User starts with an explicit step in the Platform (for example
  "Approve and send", "Download", "Save") and which may have an effect outside the Platform.
- **Automatic Action:** an action the Platform performs inside the Platform without a user step (for example
  linking an email to a file, producing an alert, preparing a Draft). An Automatic Action never communicates with
  third parties on the Customer's behalf.
- **Integration:** external services connected to the Platform with the Customer's authorisation (for example
  Microsoft 365 / Outlook, Gmail, tracking data providers, ISF providers, sign-in with Google or Apple).
- **Third-Party Service:** services not controlled by the Service Provider and used through Integrations or
  sub-processors (carrier and terminal systems, email providers, AI providers, hosting providers, etc.).
- **AI Feature:** processing performed with third-party AI models, such as reading data from documents,
  depending on the Customer's preference or account settings.
- **Template:** the Platform's ready-made templates or the Customer's own templates used to generate documents.
- **Confidential Information:** any information one Party discloses to the other that is marked confidential
  or should reasonably be treated as confidential by its nature, including Customer Data, pricing information,
  trade secrets and security information.
- **Security Incident:** an event in which Customer Data is subject to unauthorised access, disclosure,
  alteration, loss or destruction.

## 3. Formation and Electronic Acceptance

3.1. These Terms are formed when the person acting for the Customer completes sign-up by ticking the box
confirming that they have read and accept these Terms and their annexes, or when a written or electronic order
form is signed with the Service Provider.

3.2. The person accepting represents and warrants that they are authorised to bind the Customer. All
consequences of unauthorised acceptance apply jointly to that person and the Customer.

3.3. At acceptance the Platform records the accepting user, the company, the name and version of each accepted
document, a hash of the document text, the date and time, the IP address and browser information. The Parties
agree that these records are evidence of acceptance.

3.4. The current versions of these Terms and their annexes are always available in the Platform and at [WEBSITE].
The Customer can save and print them.

## 4. Description and Nature of the Service

4.1. The Platform is software that **supports the operational processes** of freight forwarders and similar
businesses in ocean transport. Its main functions are: keeping shipment file and container records; collecting
tracking data and calculating the cargo's stage; keeping the history of estimated times of arrival (ETA);
matching and classifying emails against files; reading fields from documents; producing alerts and tasks for
required documents and deadlines; tracking release and free time; preparing reply and notification Drafts;
generating documents from Templates; user and permission management; logs and reports.

4.2. **The Platform is a decision-support tool.** It does not make the Customer's operational, commercial,
legal or professional decisions for the Customer. Outputs are prepared for the Customer's own review and
judgement.

4.3. The Service Provider is **not** a carrier, NVOCC, freight forwarder, customs broker, warehouse operator,
insurer, or legal or tax adviser and does not act in any of these capacities. The Platform does not file
customs declarations, ISF, AMS or similar official filings on the Customer's behalf and does not guarantee that
such filings are accurate or made on time. Official filings are the responsibility of the Customer or third
parties authorised by the Customer.

4.4. The Platform does not calculate prices, prepare quotes or make sales. Any pricing information the Customer
records in the Platform (for example rates shared by its sales team) is a reference record only; its accuracy
and use are the Customer's responsibility.

4.5. The scope, features and interface of the Service may be developed, changed or removed over time. If an
essential function is removed, the Service Provider gives reasonable prior notice.

## 5. Account, Authorised Users and Access Security

5.1. The Customer account is opened by the person who first signs up; that person becomes the first Admin User.
Admin Users add other Authorised Users, set their roles, remove their access and manage account settings.

5.2. The Customer must verify the identity of Authorised Users, give access only to people who need it for
their work, and remove access **without delay** when a person changes role or leaves. All actions of Authorised
Users in the Platform are deemed actions of the Customer.

5.3. Sign-in is by email and password or through identity providers such as Google or Apple. The security of
identity provider accounts is the responsibility of the Authorised User and the Customer. The Customer cannot
hold the Service Provider liable for damage caused by the takeover of identity provider accounts linked to its
account, but must notify the Service Provider immediately on becoming aware of such an event.

5.4. Passwords and access details are personal and may not be shared. The Service Provider stores passwords in a
non-reversible form (as a hash) and never asks for passwords.

5.5. If unauthorised access is suspected, the Customer must deactivate the affected user, change passwords,
disconnect Integrations and notify the Service Provider at [SECURITY EMAIL].

## 6. Customer Obligations

The Customer accepts, represents and undertakes that:

6.1. **Data accuracy:** it is responsible for the data it enters or transfers being accurate, current and
complete, including customer, party, address, email and contact details. The quality of Outputs depends on the
quality of the data entered.

6.2. **Checking Outputs:** it checks Outputs against its own sources before use, especially those to be sent to
third parties or relied on for operational decisions (recipient addresses, container and bill of lading numbers,
dates, release status, delivery address, free time).

6.3. **Responsibility for approvals:** every Draft and document sent, downloaded, saved or passed to third
parties with an Authorised User's approval is the Customer's own statement and action (details in Annex 1).

6.4. **Compliance:** it uses the Service in compliance with customs, foreign trade, export control, sanctions,
data protection, e-commerce, competition and other applicable laws. Obligations under the rules of U.S. Customs
and Border Protection (CBP), the Federal Maritime Commission (FMC) and similar authorities belong to the
Customer.

6.5. **Personal data:** it is the controller of the Personal Data it brings into the Platform and has the legal
grounds needed to process that data and transfer it to the Service Provider, has provided the required privacy
notices and, where needed, obtained explicit consent (Annex 2).

6.6. **Authority over Integrations:** it is authorised over the email accounts and other Integrations it
connects, and has made the internal approvals and notices needed for the Platform to process the data in those
accounts.

6.7. **Independent records:** it does not track official obligations and critical deadlines (for example the ISF
deadline, last free day, empty return deadline) only through Platform alerts, and keeps its own internal
controls.

6.8. **Prohibited use:** it does not use the Platform to spread malware, attempt to bypass security, reverse
engineer (except where mandatory law allows), create excessive load, attempt to access other customers' data,
send misleading or unlawful content, or send spam or unsolicited commercial messages.

6.9. **Reporting errors:** it reports errors it notices in Outputs, especially those that look systematic, to
the Service Provider within a reasonable time.

## 7. Automation, Drafts and Approval

7.1. The Platform **does not send any email, message or document to third parties on the Customer's behalf
without the explicit approval of an Authorised User.** Replies and notifications are prepared as Drafts; sending
happens when an Authorised User clicks "Approve and send". The approving user and the date and time are
recorded.

7.2. Automatic Actions (linking emails to files, classification, reading ETAs, producing alerts and tasks,
preparing Drafts) stay inside the Platform and are presented for the Customer's review. Automatic Actions can be
wrong; unless reflected outside the Platform with an Authorised User's approval, such errors affect only records
inside the Platform.

7.3. Before approving a Draft, the Authorised User must check the recipients, subject, content, attachments and
the file referred to. **The Customer is responsible for approved content, for the choice of recipients and for
the consequences of sending.** This includes commercial losses that an email sent to the wrong recipient or with
wrong content may cause (delivery of cargo to the wrong party, disclosure of confidential information, loss of
charges, loss of reputation, etc.).

7.4. If a software error causes the Platform to communicate with third parties without an Authorised User's
approval, the Service Provider informs the Customer as soon as it learns of it, makes reasonable efforts to fix
the error, and its liability is assessed within the framework of Section 18.

7.5. Details of automation, approval and the sharing of responsibility by function are set out in Annex 1.

## 8. AI Features and Automatic Data Reading

8.1. To read fields from documents, the Platform first uses the document's own text and local optical character
recognition (OCR). If these are not enough and the AI Feature is enabled for the account, the necessary part of
the document (its text or a reduced page image) may be sent to a third-party AI provider.

8.2. Values read by AI or by rules **may be wrong, incomplete or misleading.** The Platform checks these values
with some rules (for example the container number check digit and date formats), but these checks do not
guarantee accuracy. Read values do not overwrite existing records; they only fill empty fields, and
conflicts are shown as alerts.

8.3. The Service Provider does not use Customer Data to train AI models and, in its contracts with AI providers,
requires that Customer Data is not used for model training. The providers used are listed as sub-processors in
Annex 2.

8.4. The Customer can have the AI Feature switched off for its account. In that case documents are read only
with text extraction and OCR.

## 9. Third-Party Data and Services

9.1. Information such as container movements, voyages, estimated arrival dates, terminal and release status comes
from carriers, terminals, data providers or emails. The Service Provider **does not guarantee that this
information is accurate, complete, up to date or continuously available.** Estimated dates may change by
nature.

9.2. Integrations are subject to the terms of the relevant third party. An interruption, change, access
restriction or revocation of authorisation in a third party's service is not the Service Provider's fault.

9.3. The Customer accepts that, through a connected email account, the Platform processes only emails that
appear to be operational; that filters are not perfect; and that some relevant emails may not be processed or
some unrelated emails may be processed.

## 10. Generated Documents and Templates

10.1. The Platform generates arrival notices, delivery orders, cargo releases and similar documents using the
Customer's company details and file records. **The Customer is the issuer of these documents and is responsible
for them.** The Service Provider is not a party to them.

10.2. During document generation the Platform shows missing fields and points that need attention (for example
that no release is recorded in the system). The absence of such a warning does not mean that a document is
correct or ready to use.

10.3. Documents that contain a release or delivery instruction in particular determine the party to whom cargo
is delivered. Before issuing and sending them, the Customer must **separately verify** freight and document
release, customs release, payment status and the authorised receiving party from its own sources.

10.4. The content, legal nature and compliance with third-party rights of Templates uploaded by the Customer are
the Customer's responsibility. The ready-made templates contain no prices or charges.

## 11. Service Levels, Maintenance and Backups

11.1. The Service Provider makes commercially reasonable efforts to operate the Platform with an availability
target of at least [99.5]% in each month. Planned maintenance, force majeure and outages caused by the Customer or
third parties are excluded. [An availability commitment and service credits will be set out in a separate
Service Level Annex.]

11.2. Planned maintenance is carried out outside business hours where possible and announced a reasonable time
in advance.

11.3. Customer Data is backed up regularly. Backups are for disaster recovery; restoring data the Customer
deleted by mistake is not guaranteed, but where possible the Service Provider helps for a fee.

11.4. Support requests are answered through [SUPPORT EMAIL] on business days between [09:00–18:00 (TRT)].
[SECURITY EMAIL] is used for critical security incidents.

## 12. Fees and Payment

12.1. Service fees, the subscription plan and payment terms are set out in the order form or on the Platform's
pricing page. [Pricing model to be decided.]

12.2. Unless stated otherwise, fees exclude VAT and are payable in advance. If payment is late, the Service
Provider may suspend the Service [15] days after written notice.

12.3. During trial or free periods the Service is provided "as is", and the targets in Section 11 do not apply.

## 13. Intellectual Property

13.1. All intellectual and industrial property rights in the Platform, software, interface, ready-made templates,
documentation, brands and logos, and their developments, belong to the Service Provider or its licensors. The
Customer receives a non-transferable, non-exclusive right to use them for its own internal business purposes
during the term.

13.2. Customer Data belongs to the Customer. The Customer permits Customer Data to be processed to the extent
necessary to provide the Service, keep it secure, fix errors and meet legal obligations.

13.3. The Service Provider may use anonymised and aggregated usage statistics that do not identify the Customer
or individuals (for example the number of documents processed or the frequency of alert types) to improve the
Service.

13.4. Suggestions and feedback from the Customer or Authorised Users may be used to improve the Service without
any fee or obligation. Parts of feedback that contain personal data are processed under Annex 3.

## 14. Confidentiality

14.1. Each Party uses the other's Confidential Information only for the purpose of these Terms, protects it with
no less care than its own confidential information, and shares it only with employees, sub-processors and
advisers who need to know it and are under equivalent confidentiality obligations.

14.2. Disclosure may be made at the request of legally authorised authorities; in that case, where legally
possible, the other Party is informed in advance.

14.3. Confidentiality obligations continue for [5] years after the end of these Terms, and indefinitely for trade
secrets and Personal Data.

## 15. Personal Data Protection

15.1. For Personal Data in Customer Data, **the Customer is the data controller and the Service Provider is the
data processor.** The Parties' rights and obligations in this respect are set out in Annex 2, the Data
Processing Agreement.

15.2. For the account, sign-in and contact details of Authorised Users, the Service Provider is the data
controller. Information about this processing is given in the Privacy Policy.

## 16. Information Security

16.1. The Service Provider applies the technical and organisational measures summarised in Annex 2 to protect
Customer Data, including separation of data by company, role-based permissions, storing passwords as hashes,
storing integration credentials encrypted, logs, and ending sessions when permissions change.

16.2. The Customer is responsible for the security of its own devices, networks, email and identity provider
accounts, and for Authorised Users using the Platform securely.

16.3. When the Service Provider becomes aware of a Security Incident affecting Customer Data, it informs the
Customer within the time set out in Annex 2 and takes reasonable measures to limit its effects.

## 17. Disclaimer of Warranties

17.1. Except as expressly stated in these Terms, the Service is provided **"as is" and "as available".** The
Service Provider does not warrant that the Service will be uninterrupted or error-free, that Outputs will be
accurate, complete or current, that the Service will be fit for a particular purpose, that all errors will be
corrected, or that the Service will meet all of the Customer's operational needs.

17.2. Alerts and tasks are based on recorded data and defined rules. **The absence of an alert does not mean the
related risk does not exist.** Rule thresholds (for example the free time warning day or stage time limits) can
be adjusted by the Customer and are the Customer's responsibility.

17.3. This section applies to the maximum extent permitted by mandatory law.

## 18. Limitation of Liability

18.1. **Indirect damages:** neither Party is liable to the other for loss of profit, loss of revenue, loss of
business, loss of customers, loss of reputation, indirect damages arising from data loss, indirect damages
arising from third-party claims, or unforeseeable damages, even if advised of their possibility.

18.2. **Operational damages:** the Service Provider is not liable for the following, even if connected with the
use of the Service:

- demurrage, detention, storage, warehousing, port and terminal charges;
- administrative fines, liquidated damages, late penalties and seizures related to customs, ISF, AMS, export
  declarations and other official filings;
- delivery of cargo to the wrong party, late delivery, non-delivery, loss of or damage to cargo;
- damages arising from wrong emails, documents or notifications, or ones sent to the wrong recipient, with an
  Authorised User's approval;
- damages arising from third-party data (tracking, voyage, terminal, carrier information) being wrong,
  incomplete or late;
- damages arising from wrong data entered or transferred by the Customer, from Templates uploaded by the
  Customer, or from the Customer not performing its checking obligations.

18.3. **Cap:** the Service Provider's total liability arising from these Terms or the Service, on whatever legal
basis, is limited to **the Service fees actually paid by the Customer to the Service Provider in the [12] months
before the event giving rise to the damage.** [During free use, maximum liability is limited to [AMOUNT].]

18.4. **Exceptions:** the limitations in this section do not apply to intent and gross negligence, damage to
life and physical integrity, intentional breach of confidentiality, and liabilities that cannot be limited
under mandatory law.

18.5. The Customer cannot claim compensation from the Service Provider to the extent its own fault caused or
increased the damage (for example not performing its checking obligation, ignoring alerts or not removing
access in time).

18.6. Claims not notified in writing within [30] days of becoming aware of the damage are, to the extent
permitted by mandatory law, not heard. [Subject to legal review.]

## 19. Indemnity

19.1. The Customer pays the Service Provider, and holds it harmless from, damages and reasonable legal fees
arising from claims, lawsuits and administrative sanctions brought against the Service Provider by third parties
because of (a) Customer Data being unlawful or infringing third-party rights, (b) communications and documents
sent with the approval of Authorised Users, (c) use of the Service contrary to these Terms or the law, or (d)
the Customer not meeting its obligations as data controller.

19.2. For claims against the Customer alleging that the Platform infringes third-party intellectual property
rights, the Service Provider defends the Customer and covers finally awarded damages, provided that the Customer
notifies the claim promptly and cooperates reasonably. This obligation does not cover claims arising from
Customer Data, Customer Templates, or modified use or use of the Platform outside its purpose.

## 20. Term, Suspension and Termination

20.1. These Terms take effect on acceptance and remain in force for the subscription period. They renew for the
same period unless a Party gives notice [30] days before the end of the period.

20.2. The Service Provider may suspend the Service in whole or in part, immediately and for as long as necessary,
in case of a security threat, unlawful use, late payment or misuse affecting other customers. Suspension is
notified to the Customer as soon as possible.

20.3. Either Party may terminate these Terms if the other Party materially breaches an obligation and the breach
is not remedied within [30] days of written notice.

20.4. The Customer may terminate at any time by paying the fees up to the end of the period. [Partial refund
terms to be decided.]

## 21. Return and Deletion of Data at the End of the Term

21.1. For [30] days after the end of these Terms, the Customer can obtain Customer Data in a machine-readable
format through the Platform's export tools or by request to the Service Provider.

21.2. After this period, Customer Data is deleted from live systems, subject to legal retention obligations, and
from backups within the normal backup cycle and no later than [90] days. Logs are subject to the periods in
Annex 3.

21.3. Integration credentials (for example email account access tokens) are invalidated and deleted immediately
when these Terms end or the connection is removed.

## 22. Force Majeure

Failure or delay in performing obligations due to events beyond the Parties' reasonable control (natural
disasters, epidemics, war, terrorism, strikes, cyber attacks, decisions of public authorities, energy or
internet infrastructure outages, widespread outages of third-party providers) is not a breach. If force
majeure lasts more than [60] days, either Party may terminate these Terms.

## 23. Changes to These Terms

23.1. The Service Provider may update these Terms and their annexes. Material changes are notified in the
Platform and to Admin Users' email addresses at least [30] days before they take effect.

23.2. The updated text is shown to Authorised Users when they sign in, and the Platform cannot be used further
until it is accepted. If the Customer does not accept a change, it may terminate these Terms without additional
cost before the change takes effect.

## 24. Notices

Notices under these Terms are sent to the email address in Section 1.1 for the Service Provider, and for the
Customer to the email addresses given at sign-up and set for Admin Users. In-Platform notices are also valid.
Until a change of address is notified, notices sent to the old address are valid.

## 25. Evidence

The Parties agree that, in disputes arising from these Terms, the commercial books and records of the Service
Provider and the Customer, the Platform's logs (acceptance records, approval records, sending records), email
correspondence and electronic records constitute evidence under Article 193 of the Turkish Code of Civil
Procedure No. 6100. This does not remove the right to submit counter-evidence.

## 26. Governing Law and Disputes

26.1. These Terms are governed by the laws of the Republic of Türkiye. [A separate choice of law for customers
outside Türkiye will be considered.]

26.2. The courts and enforcement offices of [ISTANBUL (ÇAĞLAYAN)] have jurisdiction. [An arbitration option will
be considered.]

## 27. Miscellaneous

27.1. **Severability:** if a provision is invalid, the other provisions are not affected; the invalid provision is
deemed replaced by the valid provision closest to its purpose.

27.2. **Assignment:** the Customer may not assign these Terms without the Service Provider's written consent. The
Service Provider may assign them by notice in case of merger, acquisition or transfer of assets.

27.3. **Waiver:** not exercising a right is not a waiver of it.

27.4. **Entire agreement:** these Terms and their annexes are the entire agreement between the Parties and
replace prior oral or written agreements. The Customer's purchase orders or general terms do not apply unless
accepted in writing by the Service Provider.

27.5. **Independent parties:** there is no partnership, agency, representation or employment relationship
between the Parties.

27.6. **Language:** this English text is a translation of a draft prepared in Turkish. [The controlling language
will be decided after legal review.]

27.7. **Survival:** Sections 13, 14, 17, 18, 19, 21, 25, 26 and other provisions that by their nature should
continue remain in force after these Terms end.
