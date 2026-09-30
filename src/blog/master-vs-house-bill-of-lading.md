---
title: Master vs house bill of lading: what each one is and why both matter
meta_title: Master vs House Bill of Lading: A Forwarder's Guide
description: The difference between a master and a house bill of lading, who issues each, which number to track with, and the mismatches that hold up cargo at destination.
date: 2026-09-30
slug: master-vs-house-bill-of-lading
---
# Master vs house bill of lading: what each one is and why both matter

A **master bill of lading (MBL)** is issued by the ocean carrier to the forwarder or NVOCC that booked the space. A
**house bill of lading (HBL)** is issued by that forwarder or NVOCC to the actual shipper, naming the real buyer as
consignee. One container moving through a forwarder therefore travels on two bills: the carrier only knows the master
bill, and the buyer usually only sees the house bill.

## Two bills, two contracts

<figure class="diagram">
<svg viewBox="0 0 760 250" role="img" aria-labelledby="mbhbTitle" xmlns="http://www.w3.org/2000/svg">
<title id="mbhbTitle">The master bill connects the carrier with the origin forwarder and its destination agent; the house bill connects the forwarder with the actual shipper and consignee</title>
<rect x="250" y="14" width="260" height="56" rx="12" fill="#F4F6F9" stroke="#183C8C" stroke-width="2"/>
<text x="380" y="40" text-anchor="middle" font-size="16" font-weight="700" fill="#10223A">Ocean carrier</text>
<text x="380" y="60" text-anchor="middle" font-size="12" fill="#44536A">issues the master bill</text>
<rect x="30" y="104" width="230" height="56" rx="12" fill="#EEF3FD" stroke="#2B63D9" stroke-width="2"/>
<text x="145" y="130" text-anchor="middle" font-size="15" font-weight="700" fill="#10223A">Origin forwarder / NVOCC</text>
<text x="145" y="150" text-anchor="middle" font-size="12" fill="#44536A">MBL shipper · HBL issuer</text>
<rect x="500" y="104" width="230" height="56" rx="12" fill="#EEF3FD" stroke="#2B63D9" stroke-width="2"/>
<text x="615" y="130" text-anchor="middle" font-size="15" font-weight="700" fill="#10223A">Destination agent</text>
<text x="615" y="150" text-anchor="middle" font-size="12" fill="#44536A">MBL consignee</text>
<rect x="30" y="186" width="230" height="52" rx="12" fill="#EEF6F5" stroke="#1FB5A5" stroke-width="2"/>
<text x="145" y="217" text-anchor="middle" font-size="15" font-weight="700" fill="#10223A">Actual shipper</text>
<rect x="500" y="186" width="230" height="52" rx="12" fill="#EEF6F5" stroke="#1FB5A5" stroke-width="2"/>
<text x="615" y="217" text-anchor="middle" font-size="15" font-weight="700" fill="#10223A">Actual consignee</text>
<path d="M260 118 Q380 60 500 118" fill="none" stroke="#183C8C" stroke-width="2.5"/>
<text x="380" y="100" text-anchor="middle" font-size="13" font-weight="700" fill="#183C8C">master B/L</text>
<line x1="260" y1="212" x2="500" y2="212" stroke="#1B8F84" stroke-width="2.5" stroke-dasharray="7 5"/>
<text x="380" y="204" text-anchor="middle" font-size="13" font-weight="700" fill="#1B8F84">house B/L</text>
</svg>
<figcaption>The carrier's contract is with the forwarders (master bill); the forwarder's contract is with the actual shipper and consignee (house bill).</figcaption>
</figure>

| | Master bill of lading | House bill of lading |
|---|---|---|
| Issued by | The ocean carrier | The forwarder or NVOCC |
| Shipper | The origin forwarder or NVOCC | The actual exporter |
| Consignee | The destination agent of the forwarder | The actual buyer, or "to order" |
| Number looks like | Usually starts with the carrier's code (for example MEDU, ONEY, COSU, ZIMU, CMDU) | The forwarder's own numbering |
| Tracked on | The carrier's website, by MBL, booking or container number | The forwarder's own system only |
| Released by | The carrier, to the destination agent | The destination agent, to the consignee |

## Which number do you track with?

Carrier websites know the **master bill**, the booking number and the container numbers. They do not know house bill
numbers, so tracking by an HBL on a carrier site returns nothing. When a customer sends only a house bill number, look
up the master bill and container on the forwarder's file, or ask the origin agent for them.

The container number is the most reliable key of all: it is the same on both bills and on every terminal system. Check
its digit with the [container check digit calculator](/tools/container-check-digit/) before using it.

## Where master and house bills go wrong

- **Different release types.** The house bill is telex released to the consignee while the master bill is still an
  original held by the carrier. The consignee is ready; the carrier is not. See
  [telex release vs express release vs sea waybill](/blog/telex-release-express-release-sea-waybill/).
- **Numbers mixed up.** The house bill often prints the master bill number too ("MBL#"). Reading the wrong one into
  the file means tracking and matching fail.
- **Consignee mismatch.** The house bill, the invoice and, for US imports, the ISF must name the same consignee.
- **Different cargo details.** Package count, weight or description differ between the bills; customs and the
  terminal work from different figures.
- **A missing house bill.** The pre-alert carries only the master bill, so the destination cannot issue the arrival
  notice to the consignee.

## Master and house bills in US import filings

For US imports the two bills show up in different filings. The carrier manifests the master bill, and the NVOCC
manifests its house bills. The importer's ISF is filed against the lowest-level bill, which on an NVOCC shipment is
the house bill, so the house bill number and parties on the ISF must match the house bill that is actually issued.

## When is there only one bill?

When the shipper books directly with the carrier, without a forwarder or NVOCC in between, the carrier's bill of
lading names the real shipper and consignee and there is no house bill. It is common for large shippers and rare for
small ones.

## FAQ

### Can the consignee get the master bill of lading?

Usually not. The master bill is between the carrier and the forwarders; the consignee receives the house bill and the
arrival notice. The destination agent handles the master bill release with the carrier.

### Is the house bill of lading a document of title?

It can be. An original house bill works like any original bill of lading: it must be surrendered to the destination
agent unless it was telex released or issued as a waybill.

### Why does my tracking number not work on the carrier's website?

You probably have a house bill number. Carriers track by master bill, booking or container number.

<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
 {"@type":"Question","name":"Can the consignee get the master bill of lading?","acceptedAnswer":{"@type":"Answer","text":"Usually not. The master bill is between the carrier and the forwarders; the consignee receives the house bill and the arrival notice. The destination agent handles the master bill release with the carrier."}},
 {"@type":"Question","name":"Is the house bill of lading a document of title?","acceptedAnswer":{"@type":"Answer","text":"It can be. An original house bill works like any original bill of lading: it must be surrendered to the destination agent unless it was telex released or issued as a waybill."}},
 {"@type":"Question","name":"Why does my tracking number not work on the carrier's website?","acceptedAnswer":{"@type":"Answer","text":"You probably have a house bill number. Carriers track by master bill, booking or container number."}}]}
</script>
