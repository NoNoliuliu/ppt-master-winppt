#!/usr/bin/env python3
"""Behavioral tests for ppt-master-winppt local image and configuration compatibility."""
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

SCRIPTS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPTS))
import config
import image_gen

class WinCompatibilityTests(unittest.TestCase):
    def test_explicit_config_does_not_fall_through_to_other_skill(self):
        with tempfile.TemporaryDirectory() as tmp:
            expected = (Path(tmp) / 'selected.env').resolve()
            with patch.dict(os.environ, {'WIN_PPT_ENV_FILE': str(expected)}, clear=True):
                self.assertEqual(config.get_env_candidates(), [expected])
                self.assertEqual(config.resolve_env_path(), expected)

    def test_legacy_root_is_preserved_without_global_ppt_master_config(self):
        with patch.dict(os.environ, {}, clear=True):
            self.assertEqual(config.get_env_candidates(), [config.REPO_ROOT / '.env'])

    def test_negative_prompt_reaches_backend_without_network(self):
        backend = MagicMock()
        with patch.object(sys, 'argv', ['image_gen.py', 'hospital cover', '-n', 'illegible text']), \
             patch.object(image_gen, '_load_image_env_file'), \
             patch.object(image_gen, '_validate_runtime_config'), \
             patch.object(image_gen, '_resolve_backend', return_value=(backend, 'openai')):
            image_gen.main()
        kwargs = backend.generate.call_args.kwargs
        self.assertEqual(kwargs['prompt'], 'hospital cover\n\nAvoid the following: illegible text')
