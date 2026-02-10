from oracle_break.core import OracleEnumerator,OracleHardener
o=OracleEnumerator()
print("Default credentials:")
for c in o.check_default_creds(): print(f"  {c['username']}/{c['default_password']}")
print(f"\nSIDs: {o.enumerate_sids()['known_sids']}")
h=OracleHardener()
for item in h.audit_checklist(): print(f"[{item['severity']}] {item['check']}")
