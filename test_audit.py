import unittest
from audit import audit
class TestAudit(unittest.TestCase):
    def test_ready(self):
        d={"cases":[{"id":"x","required_evidence_ids":["a"],"results":[{"id":"a","score":.8}]}]}
        self.assertEqual(audit(d)["verdict"],"ready")
    def test_negation_leak(self):
        d={"cases":[{"id":"x","exclude_ids":["a"],"results":[{"id":"a","score":.8}]}]}
        self.assertEqual(audit(d)["findings"][0]["code"],"NEGATION_LEAK")
if __name__=="__main__": unittest.main()
