from pathlib import Path
import json

plugin_base = Path("plugins/model-thinking/skills/model-thinking")
mirrors = [["SKILL.md","SKILL.md"],["references/algorithms.md","references/algorithms.md"],["references/combinations.md","references/combinations.md"],["references/decisions.md","references/decisions.md"],["references/economics.md","references/economics.md"],["references/learning.md","references/learning.md"],["references/networks.md","references/networks.md"],["references/psychology.md","references/psychology.md"],["references/risk.md","references/risk.md"],["references/sources.md","references/sources.md"],["references/statistics.md","references/statistics.md"],["references/strategy.md","references/strategy.md"],["references/systems.md","references/systems.md"]]

errors = []
for root_rel, plugin_rel in mirrors:
    root_path = Path(root_rel)
    plugin_path = plugin_base / plugin_rel
    if not root_path.exists():
        errors.append(f"Missing root mirror: {root_path}")
        continue
    if not plugin_path.exists():
        errors.append(f"Missing packaged mirror: {plugin_path}")
        continue
    if root_path.read_bytes() != plugin_path.read_bytes():
        errors.append(f"Mirror drift: {root_path} != {plugin_path}")

for metadata in [
    Path(".agents/plugins/marketplace.json"),
    plugin_base.parent.parent / ".codex-plugin" / "plugin.json",
]:
    if not metadata.exists():
        errors.append(f"Missing plugin metadata: {metadata}")
        continue
    try:
        json.loads(metadata.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"Invalid JSON {metadata}: {exc}")

if errors:
    raise SystemExit("\n".join(errors))
print(f"Validated {len(mirrors)} mirrored files and plugin metadata.")
