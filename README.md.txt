# Scientia UAE Banking AML Dossier

> **Automated Corporate Bank Onboarding, KYC & UBO Verification Engine**  
> Built by **Scientia Partners** (UAE) · [hello@scientiapartners.com](mailto:hello@scientiapartners.com)  
> Permissive Open-Source Foundation: MIT Licensed

---

## Overview

Opening a corporate bank account in the UAE is notoriously slow, often taking 3 to 6 months with high rejection rates due to strict UAE Central Bank (CBUAE) and Financial Intelligence Unit (FIU) anti-money laundering (AML) controls.

`uae-banking-aml-dossier` compiles a structured, pre-validated onboarding pack containing:
1. **Ultimate Beneficial Owner (UBO) declaration** resolved down to natural persons
2. **Economic Substance verification** (lease contracts, physical presence proofs)
3. **Counterparty legitimacy dossiers** (buyer/supplier contracts and invoices)
4. **Source of Wealth & Seed Capital trail**
5. **Instant Bank Readiness Score (0-100)** to eliminate preliminary rejections

---

## Quickstart & Installation

```bash
git clone https://github.com/YOUR_USERNAME/uae-banking-aml-dossier.git
cd uae-banking-aml-dossier

pip install -r requirements.txt

# Run readiness diagnostic
python aml_dossier.py --name "Apex Meridian Technologies FZ-LLC" --license "FZ-2026-9812" --jurisdiction "ADGM" --turnover 5000000 --office --statements

Enterprise Commercial Services
Scientia Partners provides direct banking relationship management:
Turnkey Corporate Banking Concierge ($4,950 One-Time): Fast-track account opening liaison with Emirates NBD, First Abu Dhabi Bank (FAB), Mashreq, and Wio Business with completed dossier pack.
Retained Compliance Officer & AML Liaison ($1,850/Month): Ongoing transaction monitoring, annual UBO filings, and bank review representations.
Contact: hello@scientiapartners.com
Website: scientiapartners.com