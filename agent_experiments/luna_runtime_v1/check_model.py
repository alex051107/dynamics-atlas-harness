"""Read-only balance precheck; no paid test invocation at import or startup."""
import json
from agent_run import credential,balance_precheck
if __name__=='__main__':
    print(json.dumps({'available_balance_usd':balance_precheck(credential()),'paid_model_calls':0}))
