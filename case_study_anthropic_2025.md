{
  "case_id": "anthropic_2025",
  "title": "Anthropic 2025 AI-orchestrated cyber-espionage case study",
  "artifacts": [
    {
      "id": "policy",
      "meta": {"name": "Model Safety Policy", "stage": "policy"},
      "claims": [
        {
          "s": "ClaudeCode",
          "p": "allowed_activity",
          "o": "benign_assistance_only",
          "q": {"scope": "cyber"},
          "gamma": 0.98,
          "evidence": ["policy:1"]
        },
        {
          "s": "ClaudeCode",
          "p": "prohibited_activity",
          "o": "credential_harvesting_and_exfiltration",
          "q": {"scope": "cyber"},
          "gamma": 0.99,
          "evidence": ["policy:2"]
        }
      ]
    },
    {
      "id": "agent",
      "meta": {"name": "Agent Interaction", "stage": "agent"},
      "claims": [
        {
          "s": "ClaudeCode",
          "p": "allowed_activity",
          "o": "task_orchestration",
          "q": {"scope": "cyber"},
          "gamma": 0.92,
          "evidence": ["agent:1"]
        },
        {
          "s": "AgentWorkflow",
          "p": "objective",
          "o": "automated_target_enumeration",
          "q": {"stage": "planning"},
          "gamma": 0.90,
          "evidence": ["agent:2"]
        }
      ]
    },
    {
      "id": "scripts",
      "meta": {"name": "Generated Scripts", "stage": "scripts"},
      "claims": [
        {
          "s": "GeneratedScripts",
          "p": "capability",
          "o": "reconnaissance_and_vulnerability_discovery",
          "q": {"stage": "execution_prep"},
          "gamma": 0.96,
          "evidence": ["scripts:1"]
        },
        {
          "s": "GeneratedScripts",
          "p": "objective",
          "o": "credential_collection_pathways",
          "q": {"stage": "execution_prep"},
          "gamma": 0.95,
          "evidence": ["scripts:2"]
        }
      ]
    },
    {
      "id": "runtime",
      "meta": {"name": "Runtime Activity", "stage": "runtime"},
      "claims": [
        {
          "s": "ObservedRuntime",
          "p": "activity",
          "o": "credential_harvesting",
          "q": {"stage": "runtime"},
          "gamma": 0.99,
          "evidence": ["runtime:1"]
        },
        {
          "s": "ObservedRuntime",
          "p": "activity",
          "o": "data_exfiltration",
          "q": {"stage": "runtime"},
          "gamma": 0.99,
          "evidence": ["runtime:2"]
        },
        {
          "s": "ObservedRuntime",
          "p": "activity",
          "o": "backdoor_creation",
          "q": {"stage": "runtime"},
          "gamma": 0.97,
          "evidence": ["runtime:3"]
        }
      ]
    }
  ],
  "edges": [
    {
      "source": "policy",
      "target": "agent",
      "meta": {"type": "traceability", "description": "policy to agent invocation"}
    },
    {
      "source": "agent",
      "target": "scripts",
      "meta": {"type": "traceability", "description": "agent to generated scripts"}
    },
    {
      "source": "scripts",
      "target": "runtime",
      "meta": {"type": "traceability", "description": "generated scripts to runtime activity"}
    }
  ]
}
