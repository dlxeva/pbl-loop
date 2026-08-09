#!/usr/bin/env python3
"""Dependency-free repository checks for Capability Loop."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "capability-loop"
SKILL_FILE = SKILL_DIR / "SKILL.md"
CASES_FILE = ROOT / "evals" / "cases.json"

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
CASE_ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
ALLOWED_CATEGORIES = {
    "trigger",
    "goal_integrity",
    "evidence",
    "state_transition",
    "transfer",
    "persistence",
    "scope",
}
ALLOWED_MODES = {"start", "checkpoint", "transfer"}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def parse_simple_frontmatter(text: str, errors: list[str]) -> dict[str, Any]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        fail(errors, "SKILL.md must start with YAML frontmatter.")
        return {}

    try:
        end = next(index for index, line in enumerate(lines[1:], start=1) if line.strip() == "---")
    except StopIteration:
        fail(errors, "SKILL.md frontmatter is missing its closing delimiter.")
        return {}

    values: dict[str, Any] = {}
    metadata: dict[str, str] = {}
    in_metadata = False

    for raw_line in lines[1:end]:
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue

        if raw_line.startswith("metadata:"):
            in_metadata = True
            values["metadata"] = metadata
            continue

        if in_metadata and raw_line.startswith("  "):
            key, sep, value = raw_line.strip().partition(":")
            if not sep:
                fail(errors, f"Invalid metadata line: {raw_line!r}")
                continue
            metadata[key.strip()] = value.strip().strip('"').strip("'")
            continue

        in_metadata = False
        key, sep, value = raw_line.partition(":")
        if not sep:
            fail(errors, f"Invalid frontmatter line: {raw_line!r}")
            continue
        values[key.strip()] = value.strip().strip('"').strip("'")

    return values


def validate_links(path: Path, errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for target in LINK_RE.findall(text):
        target = target.split("#", 1)[0]
        if not target or "://" in target or target.startswith("mailto:") or target.startswith("#"):
            continue
        resolved = (path.parent / target).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            fail(errors, f"{path.relative_to(ROOT)} links outside the repository: {target}")
            continue
        if not resolved.exists():
            fail(errors, f"{path.relative_to(ROOT)} has a broken local link: {target}")


def validate_skill(errors: list[str]) -> None:
    if not SKILL_FILE.exists():
        fail(errors, "Missing capability-loop/SKILL.md.")
        return

    text = SKILL_FILE.read_text(encoding="utf-8")
    frontmatter = parse_simple_frontmatter(text, errors)

    name = frontmatter.get("name", "")
    description = frontmatter.get("description", "")
    compatibility = frontmatter.get("compatibility", "")
    metadata = frontmatter.get("metadata", {})

    if not isinstance(name, str) or not NAME_RE.fullmatch(name):
        fail(errors, "Skill name must use lowercase letters, numbers, and single hyphens.")
    if name != SKILL_DIR.name:
        fail(errors, f"Skill name {name!r} must match directory {SKILL_DIR.name!r}.")
    if len(name) > 64:
        fail(errors, "Skill name exceeds 64 characters.")

    if not isinstance(description, str) or not description.strip():
        fail(errors, "Skill description is required.")
    elif len(description) > 1024:
        fail(errors, "Skill description exceeds 1024 characters.")

    if compatibility and len(str(compatibility)) > 500:
        fail(errors, "Skill compatibility exceeds 500 characters.")

    if not isinstance(metadata, dict):
        fail(errors, "Skill metadata must be a mapping.")
    else:
        for key in ("author", "version"):
            if not metadata.get(key):
                fail(errors, f"Skill metadata.{key} is required by this repository.")

    if len(text.splitlines()) > 500:
        fail(errors, "SKILL.md exceeds the recommended 500-line limit.")

    validate_links(SKILL_FILE, errors)


def require_string_list(case: dict[str, Any], field: str, errors: list[str]) -> None:
    value = case.get(field)
    case_id = case.get("id", "<unknown>")
    if not isinstance(value, list) or not value:
        fail(errors, f"{case_id}: {field} must be a non-empty list.")
        return
    for index, item in enumerate(value):
        if not isinstance(item, str) or not item.strip():
            fail(errors, f"{case_id}: {field}[{index}] must be a non-empty string.")


def validate_cases(errors: list[str]) -> None:
    if not CASES_FILE.exists():
        fail(errors, "Missing evals/cases.json.")
        return

    try:
        payload = json.loads(CASES_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(errors, f"evals/cases.json is invalid JSON: {exc}")
        return

    if not isinstance(payload.get("schema_version"), str):
        fail(errors, "evals/cases.json requires string schema_version.")
    if not isinstance(payload.get("skill_version"), str):
        fail(errors, "evals/cases.json requires string skill_version.")

    cases = payload.get("cases")
    if not isinstance(cases, list) or not cases:
        fail(errors, "evals/cases.json requires a non-empty cases list.")
        return

    seen: set[str] = set()
    for index, case in enumerate(cases):
        if not isinstance(case, dict):
            fail(errors, f"cases[{index}] must be an object.")
            continue

        case_id = case.get("id")
        if not isinstance(case_id, str) or not CASE_ID_RE.fullmatch(case_id):
            fail(errors, f"cases[{index}].id must use lowercase letters, numbers, and single hyphens.")
            continue
        if case_id in seen:
            fail(errors, f"Duplicate case id: {case_id}")
        seen.add(case_id)

        if case.get("category") not in ALLOWED_CATEGORIES:
            fail(errors, f"{case_id}: unsupported category {case.get('category')!r}.")
        if not isinstance(case.get("critical"), bool):
            fail(errors, f"{case_id}: critical must be boolean.")

        activation = case.get("activation")
        mode = case.get("mode")
        if activation not in {"trigger", "no-trigger"}:
            fail(errors, f"{case_id}: activation must be trigger or no-trigger.")
        elif activation == "trigger" and mode not in ALLOWED_MODES:
            fail(errors, f"{case_id}: triggered cases require a valid mode.")
        elif activation == "no-trigger" and mode is not None:
            fail(errors, f"{case_id}: no-trigger cases must use null mode.")

        prompt = case.get("prompt")
        if not isinstance(prompt, str) or not prompt.strip():
            fail(errors, f"{case_id}: prompt must be a non-empty string.")

        setup = case.get("setup")
        if setup is not None and (not isinstance(setup, str) or not setup.strip()):
            fail(errors, f"{case_id}: setup must be a non-empty string when present.")

        require_string_list(case, "assertions", errors)
        require_string_list(case, "forbidden", errors)


def validate_repository(errors: list[str]) -> None:
    required = [
        ROOT / "README.md",
        ROOT / "CHANGELOG.md",
        ROOT / "LICENSE",
        ROOT / ".github" / "workflows" / "validate.yml",
        ROOT / "capability-loop" / "references" / "evidence-ledger.md",
        ROOT / "capability-loop" / "references" / "evaluation-protocol.md",
        ROOT / "capability-loop" / "references" / "behavioral-tests.md",
        ROOT / "capability-loop" / "references" / "multi-round-example.md",
        ROOT / "evals" / "results" / "TEMPLATE.md",
    ]
    for path in required:
        if not path.exists():
            fail(errors, f"Missing required file: {path.relative_to(ROOT)}")

    for path in ROOT.rglob("*.md"):
        validate_links(path, errors)


def main() -> int:
    errors: list[str] = []
    validate_skill(errors)
    validate_cases(errors)
    validate_repository(errors)

    if errors:
        print("Validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    case_count = len(json.loads(CASES_FILE.read_text(encoding="utf-8"))["cases"])
    print(f"Validation passed: skill metadata, local links, repository structure, and {case_count} eval cases.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
