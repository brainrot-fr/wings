# Repo: security-audit
HEADER: path=/home/syed-jalal/dev/wings/research/repos/cloudflare__security-audit-skill/skills/security-audit/report-schema.json | commit=c1c8a8c1471069fb0e188eeaff69b8e8db6564a8 | license=n/a

{
  "$comment": "Top-level contract for findings.json. validate-findings.cjs interprets and checks this schema directly.",
  "type": "array",
  "items": {
    "oneOf": [
      {
        "type": "object",
        "description": "A source-grounded vulnerability that was independently demonstrated.",
        "properties": {
          "verdict": {
            "type": "string",
            "const": "confirmed"
          },
          "fingerprint": {
            "type": "string",
            "minLength": 1,
            "pattern": "^[A-Za-z0-9][A-Za-z0-9._:/@+-]*$"
          },
          "title": {
            "type": "string",
            "minLength": 1
          },
          "description": {
            "type": "string",
            "minLength": 1
          }
        }
      }
    ]
  }
}

