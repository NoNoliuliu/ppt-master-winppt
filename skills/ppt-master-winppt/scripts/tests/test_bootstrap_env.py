import importlib.util,unittest,sys,subprocess
from unittest.mock import patch
from pathlib import Path
p=str(Path(__file__).resolve().parents[1] / 'bootstrap_env.py')
s=importlib.util.spec_from_file_location('bootstrap',p);b=importlib.util.module_from_spec(s);s.loader.exec_module(b)
def rows(ok):return [{'requirement':r,'module':m,'ok':ok,'error':'ImportError'} for r,m in b.CORE+b.PREVIEW+b.OPTIONAL]
class Tests(unittest.TestCase):
 def test_preview_missing_does_not_block_ppt(self):
  data=rows(True)
  data[len(b.CORE)]['ok']=False
  with patch.object(b,'probe',return_value=data),patch.object(b.subprocess,'run') as run:
   self.assertEqual(b.main(['--check-only']),0);run.assert_not_called()
 def test_preview_profile_only_installs_flask(self):
  bad=[{'requirement':'flask>=3.0.0','module':'flask','ok':False,'error':'ImportError'}]
  good=[dict(bad[0],ok=True)]
  with patch.object(b,'probe',side_effect=[bad,good]),patch.object(sys,'prefix','test-venv'),patch.object(b.subprocess,'run',return_value=subprocess.CompletedProcess([],0)) as run:
   self.assertEqual(b.main(['--profile','preview']),0)
   self.assertEqual(run.call_args.args[0][-1],'flask>=3.0.0')
 def test_check_never_installs(self):
  with patch.object(b,'probe',return_value=rows(False)),patch.object(b.subprocess,'run') as run:
   self.assertEqual(b.main(['--check-only']),1);run.assert_not_called()
 def test_global_refused(self):
  with patch.object(b,'probe',return_value=rows(False)),patch.object(sys,'prefix',sys.base_prefix),patch.object(b.subprocess,'run') as run:
   self.assertEqual(b.main([]),2);run.assert_not_called()
 def test_fresh_verification(self):
  with patch.object(b,'probe',side_effect=[rows(False),rows(True)[:len(b.CORE)]]) as probe,patch.object(sys,'prefix','test-venv'),patch.object(b.subprocess,'run',return_value=subprocess.CompletedProcess([],0)) as run:
   self.assertEqual(b.main([]),0);self.assertEqual(probe.call_count,2);self.assertEqual(run.call_args.args[0][:3],[sys.executable,'-m','pip'])
 def test_pip_failure_normalized(self):
  with patch.object(b,'probe',return_value=rows(False)),patch.object(sys,'prefix','test-venv'),patch.object(b.subprocess,'run',return_value=subprocess.CompletedProcess([],17)):
   self.assertEqual(b.main([]),2)
if __name__=='__main__':unittest.main()
