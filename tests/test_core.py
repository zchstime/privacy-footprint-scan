import tempfile, unittest
from pathlib import Path
from privacy_footprint_scan.__main__ import markdown, scan
class Tests(unittest.TestCase):
 def test_counts_without_values(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d); (p/"notes.txt").write_text("Contact ada@example.com from 192.168.1.2"); result=scan(p); report=markdown(result)
   self.assertEqual(result["totals"],{"email":1,"ipv4":1}); self.assertNotIn("ada@example.com",report)
if __name__=="__main__": unittest.main()
