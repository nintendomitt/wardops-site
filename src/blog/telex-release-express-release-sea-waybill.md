---
title: Telex release vs express release vs sea waybill vs original bill of lading
meta_title: Telex Release vs Express Release vs Sea Waybill
description: How telex release, express release, sea waybill and original bills of lading differ, when each is used, and the two-layer release check forwarders miss.
date: 2026-09-30
slug: telex-release-express-release-sea-waybill
---
# Telex release vs express release vs sea waybill vs original bill of lading

The **release type** decides what the consignee must hand over before the cargo is released at destination. With an
**original bill of lading**, a signed original must be surrendered. With a **telex release**, the originals were
surrendered at origin, so no paper is needed at destination. With a **sea waybill** (often called an **express
release**), no originals exist at all and the cargo goes to the named consignee.

The terms are used loosely from one office to the next, which is why the same shipment can be "telex released" in one
email and "on a sea waybill" in the next. Here is what each one means, when it is used and what to check.

## The four release types at a glance

| | Original B/L | Telex release | Express release / sea waybill |
|---|---|---|---|
| Originals printed? | Yes, usually a set of three | Yes, then handed back at origin | No |
| Document of title? | Yes, it can be endorsed and sold on | Yes, until surrendered | No, only a receipt and contract of carriage |
| What the consignee needs at destination | One signed original | Nothing on paper; the release message is enough | Proof of identity as the named consignee |
| Typical use | Letters of credit, unpaid goods, cargo sold in transit | Payment made after sailing, no time to courier originals | Trusted parties, company-to-company, prepaid or open account |
| Usual cost | Courier for the originals | A surrender or telex fee at origin in many offices | Usually none |

A telex release and an express release are not the same thing, even though many people use the words
interchangeably. With a telex release the originals existed and were surrendered; with an express release or sea
waybill they were never issued.

## Original bill of lading

The original bill of lading is a **document of title**. Whoever holds a properly endorsed original controls the
cargo, which is why banks insist on it for letters of credit and why sellers use it when the buyer has not paid.
The carrier prints a full set, usually three originals, and releases the cargo against the first one surrendered.

The risk is timing: if the originals are still in a courier bag or at the bank when the container is discharged, the
cargo cannot be released and free time keeps running.

## Telex release (surrender at origin)

The shipper hands the full set of originals back to the carrier or forwarder at origin, and the origin office sends a
release message to its destination office. The consignee then collects the cargo without any paper. The name comes
from the telex machines that once carried that message; today it is an email or a system update.

Telex releases are common when the buyer pays after the vessel sails: once payment arrives, the seller surrenders the
originals instead of couriering them. Many origin offices charge a fee for it.

## Express release and sea waybill

A **sea waybill** is not a document of title. It is a receipt for the goods and evidence of the contract of carriage,
and the carrier delivers to the consignee named on it. No originals are printed, nothing has to be surrendered, and the
release is ready from the start. Carriers and forwarders often call this an **express release** or express bill of
lading.

Use it only when the seller does not need to hold the cargo until payment, because once it is issued the named
consignee can collect.

## The check most people miss: two layers of release

When a forwarder or NVOCC is involved there are two bills of lading, and each one has its own release type:

<figure class="diagram">
<svg viewBox="0 0 760 230" role="img" aria-labelledby="layersTitle" xmlns="http://www.w3.org/2000/svg">
<title id="layersTitle">Two layers of release: the carrier releases to the destination forwarder under the master bill; the forwarder releases to the consignee under the house bill</title>
<defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="#2B63D9"/></marker></defs>
<rect x="10" y="70" width="200" height="80" rx="14" fill="#F4F6F9" stroke="#183C8C" stroke-width="2"/>
<text x="110" y="104" text-anchor="middle" font-size="17" font-weight="700" fill="#10223A">Ocean carrier</text>
<text x="110" y="126" text-anchor="middle" font-size="13" fill="#44536A">holds the cargo</text>
<rect x="280" y="70" width="200" height="80" rx="14" fill="#EEF3FD" stroke="#2B63D9" stroke-width="2"/>
<text x="380" y="104" text-anchor="middle" font-size="17" font-weight="700" fill="#10223A">Destination forwarder</text>
<text x="380" y="126" text-anchor="middle" font-size="13" fill="#44536A">agent of the NVOCC</text>
<rect x="550" y="70" width="200" height="80" rx="14" fill="#EEF6F5" stroke="#1FB5A5" stroke-width="2"/>
<text x="650" y="104" text-anchor="middle" font-size="17" font-weight="700" fill="#10223A">Consignee</text>
<text x="650" y="126" text-anchor="middle" font-size="13" fill="#44536A">the actual buyer</text>
<line x1="212" y1="110" x2="275" y2="110" stroke="#2B63D9" stroke-width="2.5" marker-end="url(#arr)"/>
<line x1="482" y1="110" x2="545" y2="110" stroke="#2B63D9" stroke-width="2.5" marker-end="url(#arr)"/>
<text x="243" y="54" text-anchor="middle" font-size="13" font-weight="700" fill="#2B63D9">Layer 1: master B/L</text>
<text x="243" y="178" text-anchor="middle" font-size="12" fill="#44536A">original, telex or waybill</text>
<text x="513" y="54" text-anchor="middle" font-size="13" font-weight="700" fill="#1B8F84">Layer 2: house B/L</text>
<text x="513" y="178" text-anchor="middle" font-size="12" fill="#44536A">original, telex or waybill</text>
<text x="380" y="214" text-anchor="middle" font-size="12" fill="#44536A">Both layers must be released before the container can leave the terminal.</text>
</svg>
<figcaption>The carrier releases to the forwarder under the master bill; the forwarder releases to the consignee under the house bill. Each layer has its own release type.</figcaption>
</figure>

The two layers do not have to match. A common case: the house bill is telex released to the consignee, but the master
bill was issued as an original and the carrier still wants it surrendered. The consignee has paid and expects the
cargo, yet the carrier will not release the container. Before promising a release date, confirm both:

- **Master bill:** has the carrier released the container to you (original surrendered, telex release received, or
  waybill)?
- **House bill:** have you released it to the consignee (original surrendered to you, telex release from your origin
  agent, or waybill)?
- **Freight and charges:** most carriers and forwarders also hold the release until freight and local charges are paid.
- **Customs:** the freight release is separate from the customs release; both are needed before pickup.

## How to spot the release type on the documents

Look for these words on the bill of lading or in the pre-alert:

- "Original", "3/3 originals" or "Number of original B/Ls: THREE" means an original bill.
- "Telex release", "Surrendered", "OBL surrendered at origin" or a surrender stamp means a telex release.
- "Sea waybill", "SWB", "Non-negotiable waybill" or "Express B/L" means a waybill or express release.

If none of these appears, ask the origin before arrival. A missing release type is one of the most common gaps in a
[pre-alert](/blog/pre-alert-shipping-documents/).

## FAQ

### Is a telex release the same as a sea waybill?

No. With a telex release the originals were printed and then surrendered at origin; with a sea waybill no originals
were ever issued and the document is not a document of title. In both cases the consignee does not need paper at
destination.

### Can a telex release be cancelled?

Once the carrier or forwarder has sent the release to destination and the cargo has been collected, it cannot be
undone. Before that point the origin office can usually hold the release, which is why sellers wait for payment before
surrendering the originals.

### Who pays the telex release fee?

It is set by the carrier or forwarder that performs the surrender, usually at origin, and is billed to whoever the
parties agree on, typically the shipper.

<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
 {"@type":"Question","name":"Is a telex release the same as a sea waybill?","acceptedAnswer":{"@type":"Answer","text":"No. With a telex release the originals were printed and then surrendered at origin; with a sea waybill no originals were ever issued and the document is not a document of title. In both cases the consignee does not need paper at destination."}},
 {"@type":"Question","name":"Can a telex release be cancelled?","acceptedAnswer":{"@type":"Answer","text":"Once the carrier or forwarder has sent the release to destination and the cargo has been collected, it cannot be undone. Before that point the origin office can usually hold the release, which is why sellers wait for payment before surrendering the originals."}},
 {"@type":"Question","name":"Who pays the telex release fee?","acceptedAnswer":{"@type":"Answer","text":"It is set by the carrier or forwarder that performs the surrender, usually at origin, and is billed to whoever the parties agree on, typically the shipper."}}]}
</script>
