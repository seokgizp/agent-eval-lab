# agent-eval-lab

Keyword-based eval runner with latency tracking

Small but I use it weekly.

## How to use

```bash
python evals.py
# edit cases.json, point run() at your agent
```

## Highlights

- Exit code usable as a CI gate
- Swap in any agent function via one line
- Cases defined in plain JSON
- Keyword scoring + latency per case

## Getting started

```bash
# stdlib only, nothing to install
```

## Project structure

```text
├── .github/
│   └── workflows/
│       └── ci.yml
├── docs/
│   ├── configuration.md
│   ├── faq.md
│   └── usage.md
├── examples/
│   └── quickstart.md
├── .gitignore
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── SECURITY.md
├── cases.json
└── evals.py
```

## Development

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## 说明

个人练习项目, 谨慎用于生产环境。
