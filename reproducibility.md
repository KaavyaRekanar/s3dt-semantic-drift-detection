# Anthropic 2025 case study reconstruction

This directory contains a simplified research-artifact reconstruction of the case study described in the paper. The bundled thread graph models four artifact states:

- `policy`
- `agent`
- `scripts`
- `runtime`

These correspond to the lifecycle stages discussed in the paper: model safety policy, agent interaction, generated scripts, and observed runtime activity.

## Files

- `thread_graph.json`: canonicalized artifact claims and traceability edges.
- `constraints.yaml`: semantic integrity constraints used by the case study.
- `expected_outputs/`: paper-reference drift score table for artifact comparison.

## Notes

This reconstruction is intended for academic artifact release and demonstration. It is designed to preserve the structure of the digital thread and the reported drift progression from the paper.
