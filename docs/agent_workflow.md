# Agent Workflow

All agent-like components use typed schemas.

1. InputRiskAssessmentAgent
2. IntentAgent
3. FilterBuilderAgent
4. DataRetrievalAgent
5. RetrievedContentRiskScanner
6. MetricsAgent (deterministic code)
7. SimilarityRankingAgent
8. ExplanationAgent
9. OutputVerificationAgent

## Notes
- If filter confidence is low, ask one clarifying question.
- If medium/high, parsed filters may auto-run.
- Explanations must rely on trusted structured data only.
