#!/usr/bin/env python3
"""
Scientia UAE Banking AML Dossier Generator (v1.3.0)
Automated Corporate Bank Onboarding, KYC & UBO Verification Engine.
Repurposed from open-source PDF & form generation engines (ReportLab / FastAPI).

Scientia Partners · Independent Advisory & Engineering Hub · UAE
hello@scientiapartners.com
"""

import argparse
import json
import sys
from typing import Dict, Any, List


class UAEBankingAMLDossier:
    def __init__(self, legal_name: str, trade_license_no: str, jurisdiction: str):
        self.legal_name = legal_name
        self.trade_license_no = trade_license_no
        self.jurisdiction = jurisdiction

    def assess_readiness(
        self,
        ubo_shareholders: List[Dict[str, Any]],
        projected_turnover_aed: float,
        has_physical_office: bool,
        has_supplier_invoices: bool,
        has_client_contracts: bool,
        has_six_months_bank_statements: bool
    ) -> Dict[str, Any]:
        """
        Calculates AML compliance readiness according to UAE Central Bank (CBUAE) standards.
        """
        score = 0
        missing_critical: List[str] = []
        actionable_steps: List[str] = []

        # 1. Physical Substance Check
        if has_physical_office:
            score += 25
        else:
            missing_critical.append("Physical Tenancy Contract (Ejari or Free Zone lease agreement)")
            actionable_steps.append("Tier-1 UAE banks (ENBD, FAB, Wio Business) routinely reject flexi-desk applications for high-turnover trading or tech companies. Secure physical desk/office lease.")

        # 2. Counterparty Proofs
        if has_client_contracts and has_supplier_invoices:
            score += 30
        else:
            score += 10
            missing_critical.append("Executed counterparty agreements or validated Letters of Intent (LOIs)")
            actionable_steps.append("Provide at least 3 supplier invoices and 3 signed customer service agreements with detailed payment terms.")

        # 3. Financial Track Record
        if has_six_months_bank_statements:
            score += 25
        else:
            missing_critical.append("6-Month personal or parent entity bank statements")
            actionable_steps.append("Assemble 6 consecutive months of stamped bank statements proving origin of seed capital.")

        # 4. UBO Structure Validation
        total_ownership = sum(s.get("ownership_pct", 0) for s in ubo_shareholders)
        ubo_compliant = abs(total_ownership - 100.0) < 0.01

        high_risk_jurisdictions = {"iran", "north korea", "syria", "russia", "myanmar"}
        has_high_risk_ubo = any(
            s.get("nationality", "").lower() in high_risk_jurisdictions
            for s in ubo_shareholders
        )

        if ubo_compliant:
            score += 20
        else:
            missing_critical.append("UBO register does not resolve to 100% ultimate natural persons")

        if has_high_risk_ubo:
            score -= 20
            actionable_steps.append("Enhanced Due Diligence (EDD) required: Provide apostilled source of wealth documentation and certified UAE residency proofs for all sanctioned-adjacent nationalities.")

        score = max(10, min(100, score))
        readiness_status = "FAST-TRACK READY (Tier-1 Bank Feasible)" if score >= 85 else "MODERATE READINESS (Requires Document Remediation)" if score >= 60 else "HIGH REJECTION RISK (Do Not Submit Until Resolved)"

        return {
            "entity": {
                "legal_name": self.legal_name,
                "trade_license_no": self.trade_license_no,
                "jurisdiction": self.jurisdiction,
                "projected_annual_turnover_aed": projected_turnover_aed,
            },
            "aml_readiness_score": score,
            "readiness_status": readiness_status,
            "ubo_structure": {
                "total_ownership_accounted": total_ownership,
                "compliant_natural_persons": ubo_compliant,
                "shareholders_count": len(ubo_shareholders),
            },
            "missing_critical_documents": missing_critical,
            "fast_track_recommendations": actionable_steps,
        }


def main():
    parser = argparse.ArgumentParser(description="Scientia UAE Banking AML Dossier CLI")
    parser.add_argument("--name", default="Apex Meridian Technologies FZ-LLC", help="Legal Company Name")
    parser.add_argument("--license", default="FZ-2026-9812", help="Trade License Number")
    parser.add_argument("--jurisdiction", default="ADGM", help="Jurisdiction")
    parser.add_argument("--turnover", type=float, default=5000000.0, help="Projected Turnover in AED")
    parser.add_argument("--office", action="store_true", default=True, help="Has physical office lease")
    parser.add_argument("--statements", action="store_true", default=True, help="Has 6mo bank statements")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")

    args = parser.parse_args()

    sample_ubos = [
        {"name": "Elena Rostova", "nationality": "Germany", "ownership_pct": 60.0},
        {"name": "Tariq Al-Mansoor", "nationality": "UAE", "ownership_pct": 40.0},
    ]

    engine = UAEBankingAMLDossier(
        legal_name=args.name,
        trade_license_no=args.license,
        jurisdiction=args.jurisdiction
    )

    result = engine.assess_readiness(
        ubo_shareholders=sample_ubos,
        projected_turnover_aed=args.turnover,
        has_physical_office=args.office,
        has_supplier_invoices=True,
        has_client_contracts=True,
        has_six_months_bank_statements=args.statements,
    )

    if args.json:
        print(json.dumps(result, indent=2))
        return

    print("=" * 72)
    print("  SCIENTIA PARTNERS · UAE BANKING AML DOSSIER READINESS ENGINE")
    print("=" * 72)
    print(f"Legal Entity:        {result['entity']['legal_name']}")
    print(f"Jurisdiction:        {result['entity']['jurisdiction']} (License: {result['entity']['trade_license_no']})")
    print(f"Readiness Score:     {result['aml_readiness_score']}/100")
    print(f"Status:              {result['readiness_status']}")
    print("-" * 72)
    if result['missing_critical_documents']:
        print("Missing Documentation:")
        for doc in result['missing_critical_documents']:
            print(f"  • {doc}")
    else:
        print("All core CBUAE mandatory documentation categories verified.")
    print("-" * 72)
    if result['fast_track_recommendations']:
        print("Recommendations:")
        for rec in result['fast_track_recommendations']:
            print(f"  → {rec}")
    print("=" * 72)


if __name__ == "__main__":
    main()