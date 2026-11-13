<!-- repo: natolitech/security-skill | path: .claude/commands/threat-model.md | lines: 160-205 | commit: 3bdb1dc1922902a8907821ea663f0bbbfea79728 | license: MIT (LICENSE) -->
<!-- SOURCE BODY -->
# Threat Model: [System Name]

**Date:** [Date]
**Scope:** [What was analyzed]
**Data Sensitivity:** [Highest classification of data handled]

## System Overview
[Brief description based on actual code analysis, not assumptions]

## Data Classification
| Data Type | Classification | Storage | Encryption |
|-----------|---------------|---------|------------|
| [Actual data from code] | [Level] | [Where stored] | [At rest / in transit status] |

## Attack Surface
[Entry point table from Step 2]

## Trust Boundaries
[Describe actual boundaries identified in the architecture]

## Data-Flow Diagram
[The mermaid DFD from Step 2, with trust zones and numbered boundary crossings]

## Threats

### Critical/High Risk
[Only threats rated critical or high — each with an ID (TM-NNN) and specific references to code]

### Medium Risk
[Medium-rated threats — each with an ID (TM-NNN)]

### Low Risk
[Low-rated threats — brief descriptions sufficient, still with IDs]

## Attack Paths (Top Risks)
[For the top 2-3 risks only: kill chains — preconditions, initial access, pivot, impact — referencing components, boundary crossing IDs, and enabling findings]

## Existing Security Controls
[What's already in place — this matters for accurate risk assessment]

## Recommended Mitigations
[Ordered by risk reduction value, with implementation guidance]

## Regulatory Considerations
[Only if applicable — note if the data types trigger HIPAA, GDPR, PCI-DSS, FERPA, or SOC 2 requirements, and which specific requirements are relevant to the identified threats]
```
