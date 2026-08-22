# ECC for Codex CLI

This is the repo-local ECC baseline for Codex CLI usage in this repository.

## Repo Skill

- Repo-generated Codex skill: `.agents/skills/pixelator/SKILL.md`
- Claude-facing companion skill: `.claude/skills/pixelator/SKILL.md`
- Keep user-specific credentials and private MCPs in `~/.codex/config.toml`, not in this repo.

## MCP Baseline

Treat `.codex/config.toml` as the default ECC-safe baseline for work in this repository.
The generated baseline registers GitHub, Context7, Exa, Memory, Playwright, and Sequential
Thinking. Live web search is off by default — enable it explicitly per-user in
`~/.codex/config.toml` if you need it.

## Multi-Agent Support

- Explorer: read-only evidence gathering
- Reviewer: correctness, security, and regression review
- Docs researcher: API and release-note verification

## Workflow Files

- No dedicated workflow command files were generated for this repo.