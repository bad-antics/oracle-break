import unittest,sys,os
sys.path.insert(0,os.path.join(os.path.dirname(__file__),"..","src"))
from oracle_break.core import OracleEnumerator,OracleHardener

class TestOracle(unittest.TestCase):
    def test_default_creds(self):
        o=OracleEnumerator()
        r=o.check_default_creds()
        self.assertGreater(len(r),5)
    def test_privilege(self):
        o=OracleEnumerator()
        r=o.assess_privilege(["DBA","SYSDBA","SELECT ANY TABLE"])
        self.assertEqual(r["risk"],"CRITICAL")
    def test_hardener(self):
        h=OracleHardener()
        self.assertGreater(len(h.audit_checklist()),5)

if __name__=="__main__": unittest.main()
