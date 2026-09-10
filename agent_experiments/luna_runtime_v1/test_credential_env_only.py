import os
from pathlib import Path
from unittest.mock import patch
from agent_run import credential

with patch.dict(os.environ, {}, clear=True), patch.object(Path, 'read_text', side_effect=AssertionError('No credential files')):
    try:
        credential()
        raise AssertionError('Missing credential was accepted')
    except RuntimeError:
        pass
with patch.dict(os.environ, {'OPENROUTER_API_KEY':'synthetic-env-only'}, clear=True), patch.object(Path, 'read_text', side_effect=AssertionError('No credential files')):
    assert credential() == 'synthetic-env-only'
print('Environment-only credential, missing-key failure and no file fallback: PASS')
