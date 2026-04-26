# Model Card – Applied AI System

## Model Description
This system uses a rule-based AI agent to interpret natural-language pet care requests and convert them into structured tasks.

## Intended Use
The system is designed for pet task planning and scheduling assistance. It is not intended for medical or professional advice.

## Limitations and Biases
The system relies on keyword matching and may fail to interpret complex or ambiguous language. It assumes common pet care routines and may not apply to all users.

## Risks and Misuse
Users may rely on the system for critical decisions. To prevent misuse, the system avoids medical advice and focuses only on scheduling tasks.

## Evaluation
- 13/13 unit tests passed
- Evaluation script confirms correct task extraction
- Confidence scoring added for transparency

## Reflection on AI Collaboration
AI tools helped structure the system and improve modularity. However, some suggestions (like returning dictionaries instead of Task objects) caused integration issues and required correction.

## Future Improvements
- Add LLM integration
- Improve natural language understanding
- Expand knowledge base (RAG)