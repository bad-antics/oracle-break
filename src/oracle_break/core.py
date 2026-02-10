"""Oracle Security Testing"""
import json,hashlib

class OracleEnumerator:
    DEFAULT_CREDS={
        "SYS":"change_on_install","SYSTEM":"manager","SCOTT":"tiger",
        "HR":"hr","DBSNMP":"dbsnmp","OUTLN":"outln","MDSYS":"mdsys",
    }
    KNOWN_SIDS=["ORCL","XE","PROD","DEV","TEST","DB1","ORACLE","PLSExtProc"]
    
    def check_default_creds(self):
        return [{"username":u,"default_password":p,"severity":"CRITICAL",
                 "fix":f"ALTER USER {u} IDENTIFIED BY <strong_password>"}
                for u,p in self.DEFAULT_CREDS.items()]
    
    def enumerate_sids(self):
        return {"known_sids":self.KNOWN_SIDS,"note":"Use tnscmd or odat for live enumeration"}
    
    def assess_privilege(self,user_privs):
        dangerous=["DBA","SYSDBA","SYSOPER","CREATE ANY PROCEDURE","EXECUTE ANY PROCEDURE",
                    "ALTER SYSTEM","CREATE LIBRARY","JAVA_ADMIN"]
        found=[p for p in user_privs if p.upper() in dangerous]
        return {"dangerous_privs":found,"count":len(found),
                "risk":"CRITICAL" if len(found)>2 else "HIGH" if found else "LOW"}

class OracleHardener:
    def audit_checklist(self):
        return [
            {"check":"Change all default passwords","severity":"CRITICAL"},
            {"check":"Remove sample schemas (SCOTT, HR)","severity":"HIGH"},
            {"check":"Disable Oracle listener external procedures","severity":"HIGH"},
            {"check":"Enable audit trail","severity":"HIGH"},
            {"check":"Apply latest CPU patches","severity":"CRITICAL"},
            {"check":"Restrict TNS listener admin","severity":"MEDIUM"},
            {"check":"Disable unnecessary database features","severity":"MEDIUM"},
            {"check":"Implement password complexity","severity":"HIGH"},
        ]
