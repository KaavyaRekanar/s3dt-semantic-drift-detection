[
  {
    "source": "policy",
    "target": "agent",
    "constraint_id": "SIC-CYBER-001",
    "severity": 0.5693434130812898,
    "drift_type": "instability",
    "explanation": "SIC=SIC-CYBER-001: Model outputs and downstream artifacts must not facilitate cyber attack activities. | Added (1): AgentWorkflow:objective=automated_target_enumeration | Removed (1): ClaudeCode:prohibited_activity=credential_harvesting_and_exfiltration | Modified (1): ClaudeCode:allowed_activity:benign_assistance_only->task_orchestration | Provenance: {'type': 'traceability', 'description': 'policy to agent invocation'}"
  },
  {
    "source": "agent",
    "target": "scripts",
    "constraint_id": "SIC-CYBER-001",
    "severity": 0.6996272483228475,
    "drift_type": "dangerous",
    "explanation": "SIC=SIC-CYBER-001: Model outputs and downstream artifacts must not facilitate cyber attack activities. | Added (2): GeneratedScripts:capability=reconnaissance_and_vulnerability_discovery; GeneratedScripts:objective=credential_collection_pathways | Removed (2): AgentWorkflow:objective=automated_target_enumeration; ClaudeCode:allowed_activity=task_orchestration | Provenance: {'type': 'traceability', 'description': 'agent to generated scripts'}"
  },
  {
    "source": "scripts",
    "target": "runtime",
    "constraint_id": "SIC-CYBER-001",
    "severity": 0.3816451852969144,
    "drift_type": "dangerous",
    "explanation": "SIC=SIC-CYBER-001: Model outputs and downstream artifacts must not facilitate cyber attack activities. | Added (1): ObservedRuntime:activity=backdoor_creation | Removed (2): GeneratedScripts:capability=reconnaissance_and_vulnerability_discovery; GeneratedScripts:objective=credential_collection_pathways | Provenance: {'type': 'traceability', 'description': 'generated scripts to runtime activity'}"
  }
]