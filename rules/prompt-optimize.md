---
model: $MODEL
---

# AI Prompt Optimization

Optimize the following prompt for the specified model ($MODEL) to achieve maximum performance and reliability.
Target Content: $ARGUMENTS

Analyze and improve the input by applying these strategies:

1. **Prompt Engineering**:
   - Apply chain-of-thought reasoning where complexity requires it.
   - Add relevant few-shot examples for pattern matching.
   - Implement role-based instructions tailored to the task.
   - Use clear delimiters (e.g., XML tags, triple backticks) and structured formatting.
   - Define explicit output format specifications.

2. **Context & Token Optimization**:
   - Minimize token usage while maintaining clarity.
   - Structure information hierarchically (most important first).
   - Remove redundancy and redundant context.

3. **Model-Specific Adaptation**:
   - Leverage the specific strengths and follow the best practices of the target model ($MODEL).
   - Adjust temperature and parameters if applicable.
   - Use model-specific prompting techniques (e.g., pre-filling responses, system instructions).

4. **Production Readiness**:
   - Design for consistency across multiple runs.
   - Include error-handling instructions within the prompt.
   - Consider cost-efficiency by balancing prompt length with output quality.

Provide the optimized prompt along with a brief explanation of the structural changes made.
