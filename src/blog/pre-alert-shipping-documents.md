---
title: Pre-alert in shipping: the document checklist and an email template
meta_title: Pre-Alert in Shipping: Document Checklist and Template
description: What a pre-alert is, which documents it must include, what the destination forwarder checks when it arrives, and a copy-ready pre-alert email template.
date: 2026-09-30
slug: pre-alert-shipping-documents
---
# Pre-alert in shipping: the document checklist and an email template

A **pre-alert** is the message the origin forwarder or agent sends to the destination forwarder once cargo has
shipped. It carries the shipment's documents (house and master bill of lading, commercial invoice, packing list and,
for US imports, the ISF data) so the destination team can open its file, prepare customs clearance and plan delivery
before the vessel arrives.

A good pre-alert saves the destination team a week of back-and-forth. A thin one ("docs attached, thanks") starts it.

<figure class="diagram">
<svg viewBox="0 0 760 210" role="img" aria-labelledby="flowTitle" xmlns="http://www.w3.org/2000/svg">
<title id="flowTitle">Pre-alert flow: origin agent to destination forwarder to customs broker, trucker and consignee</title>
<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="#2B63D9"/></marker></defs>
<rect x="10" y="60" width="190" height="84" rx="14" fill="#EEF6F5" stroke="#1FB5A5" stroke-width="2"/>
<text x="105" y="96" text-anchor="middle" font-size="17" font-weight="700" fill="#10223A">Origin agent</text>
<text x="105" y="120" text-anchor="middle" font-size="13" fill="#44536A">after the vessel sails</text>
<rect x="285" y="60" width="190" height="84" rx="14" fill="#EEF3FD" stroke="#2B63D9" stroke-width="2"/>
<text x="380" y="96" text-anchor="middle" font-size="17" font-weight="700" fill="#10223A">Destination</text>
<text x="380" y="120" text-anchor="middle" font-size="13" fill="#44536A">forwarder opens the file</text>
<rect x="560" y="20" width="190" height="44" rx="12" fill="#F4F6F9" stroke="#183C8C" stroke-width="1.5"/>
<text x="655" y="47" text-anchor="middle" font-size="14" fill="#10223A">Customs broker</text>
<rect x="560" y="82" width="190" height="44" rx="12" fill="#F4F6F9" stroke="#183C8C" stroke-width="1.5"/>
<text x="655" y="109" text-anchor="middle" font-size="14" fill="#10223A">Trucker</text>
<rect x="560" y="144" width="190" height="44" rx="12" fill="#F4F6F9" stroke="#183C8C" stroke-width="1.5"/>
<text x="655" y="171" text-anchor="middle" font-size="14" fill="#10223A">Consignee</text>
<line x1="202" y1="102" x2="280" y2="102" stroke="#2B63D9" stroke-width="2.5" marker-end="url(#arrow)"/>
<text x="241" y="88" text-anchor="middle" font-size="12" fill="#2B63D9" font-weight="700">pre-alert</text>
<line x1="477" y1="96" x2="555" y2="44" stroke="#2B63D9" stroke-width="2" marker-end="url(#arrow)"/>
<line x1="477" y1="102" x2="555" y2="104" stroke="#2B63D9" stroke-width="2" marker-end="url(#arrow)"/>
<line x1="477" y1="108" x2="555" y2="164" stroke="#2B63D9" stroke-width="2" marker-end="url(#arrow)"/>
<text x="120" y="190" text-anchor="middle" font-size="12" fill="#44536A">HBL · MBL · invoice · packing list · ISF data</text>
<text x="380" y="190" text-anchor="middle" font-size="12" fill="#44536A">entry docs · delivery order · arrival notice</text>
</svg>
<figcaption>The pre-alert is the hand-off between origin and destination. Everything the destination sends later depends on it.</figcaption>
</figure>

## When should the pre-alert be sent?

As soon as the cargo is on board and the bills of lading are final or at least in draft. In practice that means on or
right after the departure date (ETD). For US imports, the ISF (10+2) data is needed even earlier: it must reach US
Customs no later than 24 hours before the container is loaded at the foreign port, so the ISF details usually travel
with the booking, and the pre-alert confirms what was filed.

The later the pre-alert, the less time the destination has to spot problems. Many teams send the arrival notice to the
consignee about a week before arrival, and that notice is built from the pre-alert.

## Pre-alert documents checklist

| Document | Why the destination needs it | What to check |
|---|---|---|
| House bill of lading (HBL) | Releases cargo to the consignee; the arrival notice is built from it | Consignee and notify party, release type (original, telex release or sea waybill), container and seal numbers |
| Master bill of lading (MBL) | Carrier tracking, freight release from the carrier, terminal pickup | MBL number and carrier, whether the carrier has released it |
| Commercial invoice | Customs entry and duty | Values, currency, Incoterm, HS codes |
| Packing list | Customs entry, exams and warehouse stripping | Package count and weight match the bill of lading |
| ISF data or ISF confirmation (US imports) | Proof the Importer Security Filing was made before loading | Who filed it, that the parties match the HBL |
| Certificates when the goods need them | Certificate of origin, fumigation, phytosanitary or safety data sheet, depending on the goods | The HS code usually tells you which ones are needed |

## Data points to check in the pre-alert

Before filing the documents, compare the numbers across them. Most delivery problems start with a number that does
not match:

- **Container numbers:** four letters and seven digits, with a valid check digit. A quick way to catch typos is the
  [container check digit calculator](/tools/container-check-digit/).
- **Bill of lading numbers:** the MBL on the house bill must match the master bill
  ([master vs house bill of lading](/blog/master-vs-house-bill-of-lading/)).
- **Vessel, voyage, ETD and ETA:** the ETA drives the arrival notice and the last free day.
- **Port of loading, port of discharge and place of delivery:** inland moves need the final place, not just the port.
- **Consignee and notify party:** they must be the same on the HBL, the ISF and the invoice.
- **Release type:** original, telex release or sea waybill. It decides what the consignee has to present at
  destination; see [telex release vs express release vs sea waybill](/blog/telex-release-express-release-sea-waybill/).
- **HS codes:** at least six digits, consistent between invoice and ISF.
- **Packages and gross weight:** the same on the packing list and the bill of lading.

## What the destination does when the pre-alert arrives

- Open the shipment file and attach the documents to it, not to someone's inbox.
- Confirm the ISF was filed and matches the house bill (US imports).
- Ask the origin for everything missing in one email, not one item at a time.
- Start tracking the ETA; any change moves the arrival notice and the last free day.
- Prepare the [arrival notice](/blog/arrival-notice-shipping-sample/) for the consignee before the vessel arrives.

## Pre-alert email template

Copy this and fill in the brackets. The subject line carries the numbers the destination searches by, so the email
can be found and matched to the right file.

<pre class="template">Subject: PRE ALERT // [Shipper] TO [Port of discharge] // [1X40HC] // [Your file no] // MBL [number] // [Container no]
Hello [name],
Please find the pre-alert for the shipment below. The cargo sailed on [ETD] and is due in [port] on [ETA].
Vessel / voyage: [vessel] / [voyage]
MBL: [number] (carrier: [carrier])  HBL: [number]
Container / seal: [container] / [seal] ([type])
Packages / gross weight: [packages] / [kg]
Release type: [original / telex release / sea waybill]
ISF: filed by [party] on [date]
Attached: HBL, MBL copy, commercial invoice, packing list[, certificates]
Please confirm receipt and let us know if anything is missing.
Best regards,
[name], [company]</pre>

## Common pre-alert mistakes

- Sending the documents without the numbers in the email body or subject, so nothing can be searched.
- A draft HBL with a different consignee than the ISF.
- No release type, which leaves the destination guessing whether originals are coming.
- A container number with one wrong digit, so tracking returns nothing.
- Forwarding a pre-alert through several colleagues until the original sender is lost; reply to the origin, not to
  the person who forwarded it.

## FAQ

### What is the difference between a pre-alert and an arrival notice?

The pre-alert travels between forwarders, from origin to destination, shortly after departure. The arrival notice goes
from the destination forwarder or carrier to the consignee before arrival, with the arrival date, charges and what is
needed to release the cargo.

### Who sends the pre-alert?

The forwarder or agent at origin that booked the cargo and issued the house bill of lading. On a direct carrier booking
without a forwarder, the carrier's documentation and arrival notice take its place.

### Is a pre-alert a customs requirement?

No. It is a commercial practice between forwarders. Customs filings, such as the ISF and the customs entry in the US,
are separate and have their own deadlines.

<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
 {"@type":"Question","name":"What is the difference between a pre-alert and an arrival notice?","acceptedAnswer":{"@type":"Answer","text":"The pre-alert travels between forwarders, from origin to destination, shortly after departure. The arrival notice goes from the destination forwarder or carrier to the consignee before arrival, with the arrival date, charges and what is needed to release the cargo."}},
 {"@type":"Question","name":"Who sends the pre-alert?","acceptedAnswer":{"@type":"Answer","text":"The forwarder or agent at origin that booked the cargo and issued the house bill of lading. On a direct carrier booking without a forwarder, the carrier's documentation and arrival notice take its place."}},
 {"@type":"Question","name":"Is a pre-alert a customs requirement?","acceptedAnswer":{"@type":"Answer","text":"No. It is a commercial practice between forwarders. Customs filings, such as the ISF and the customs entry in the US, are separate and have their own deadlines."}}]}
</script>
