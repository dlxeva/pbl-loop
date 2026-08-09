# Changelog

All notable changes to this project are documented here.

## [0.2.0] - 2026-08-09

### Changed

- Renamed the installable skill from `pbl-loop` to `capability-loop`.
- Reframed the project as a lightweight capability-evidence loop inspired by PBL rather than a complete PBL system.
- Replaced mandatory per-turn schemas with natural conversation and on-demand ledger exposure.
- Replaced cognitive quadrants as the primary state model with `emerging`, `repeatable`, and `transfer-evidenced`.
- Scoped every state to a bounded capability, task family, and evidence set.
- Added attempt-level assistance timing and substitutive-effect rules.
- Added explicit `clean`, `partial`, `contaminated`, and `unknown` transfer isolation levels.

### Added

- Canonical evidence-ledger and transition semantics.
- Versioned machine-readable evaluation cases.
- Behavioral evaluation protocol and result template.
- Dependency-free repository validation script.
- GitHub Actions checks using the official Agent Skills reference validator.
- Agent Skills metadata for license, compatibility, author, and version.

### Validation boundary

Repository and format checks are automated. Cross-host behavior, real-user longitudinal use, authorized persistence, and clean-transfer field results remain unpublished.

## [0.1.0] - 2026-08-06

- Initial PBL Loop skill with `start`, `checkpoint`, and `transfer` modes.
- Added delivery/capability evidence separation, provenance, anti-fabrication rules, and trigger-boundary examples.
