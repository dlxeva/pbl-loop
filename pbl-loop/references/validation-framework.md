# PBL Loop Validation Framework

## Purpose

This document defines lightweight validation criteria for testing whether PBL Loop improves capability evidence tracking without confusing delivery progress with learning progress.

## Validation dimensions

### 1. Trigger accuracy

Expected behavior:

- Trigger only for explicit learning, reflection, transfer, or capability-development requests.
- Do not activate for normal project management requests.

Evidence:

- Positive examples where the loop activates.
- Negative examples where the loop remains inactive.

### 2. Evidence separation

Expected behavior:

- Delivery evidence describes shipped artifacts, outcomes, or acceptance signals.
- Capability evidence describes repeatability, reasoning, transfer, or teachability.

Failure signals:

- A completed project is treated as proof of mastery.
- AI assistance is hidden in capability claims.

### 3. Provenance integrity

Expected behavior:

Every important claim identifies whether it came from:

- human input
- AI reasoning
- AI tool output
- external evidence

Failure signals:

- Proposed suggestions become recorded facts.
- Missing information is replaced with invented metrics.

### 4. Transfer quality

Expected behavior:

A transfer exercise tests whether capability can move to an adjacent problem.

Review:

- adaptability
- explanation quality
- reuse of method

## Suggested test cases

| Case | Expected mode |
| --- | --- |
| "Help me reflect on what I learned from this project" | checkpoint |
| "Teach me how to repeat this capability elsewhere" | transfer |
| "Help me plan tomorrow's tasks" | no trigger |
| "Track my project completion status" | no trigger |

## Versioning rule

Validation results should update alongside skill changes. A passing conversation test does not establish general capability validation across all hosts or users.
