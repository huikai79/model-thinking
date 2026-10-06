[繁體中文完整說明](README.zh-Hant.md)

# Model Thinking

**A practical AI agent skill for looking at the same problem through multiple useful models before committing to a conclusion.**

Model Thinking helps users generate alternative explanations and options, test the conditions under which each perspective applies, and identify information that would materially change a decision.

It is intended as a practical reasoning aid rather than a claim that one model can explain every situation.

## What this project demonstrates

- Multi-model problem framing across ten practical domains.
- Explicit attention to assumptions and applicability conditions.
- Separation between formal models, empirical findings, and heuristics.
- Reusable agent instructions packaged as an installable skill.
- Worked decision, systems, risk, learning, strategy, and statistical examples.
- Cross-platform packaging for supported AI-agent environments.

## Core idea

When a problem looks obvious, ask whether another model reveals something the first view misses.

The workflow is:

**Problem → candidate perspectives → assumptions → applicability checks → alternatives → decision-relevant next step**

A second model is useful only if it changes what can be seen, tested, or decided.

## Intellectual provenance

This independent project is inspired by Charlie Munger's latticework-of-mental-models idea and Scott E. Page's many-model perspective. It is not affiliated with or endorsed by those authors or publishers.

The repository distinguishes formal models from broader heuristics and records source references in the detailed documentation.

## Installation

For supported Claude, ChatGPT/Codex, and coding-agent installation routes, see the [full Traditional Chinese guide](README.zh-Hant.md#安裝).

For Skills CLI:

```sh
npx skills@latest add https://github.com/kcchien/model-thinking
```

## Example use

Instead of asking only, “Which option is better?”, use Model Thinking to ask:

- What other explanations fit the same observations?
- Which constraints or incentives change the answer?
- What assumptions must hold for each option?
- Which missing fact would most change the decision?

## License

[MIT](LICENSE)
