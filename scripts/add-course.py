#!/usr/bin/env python3
"""Create a confirmed Semester 3 course division and register it in the workspace."""

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("slug", help="lowercase folder slug, e.g. behavioral-economics")
    parser.add_argument("title", help="official course title")
    parser.add_argument("--role", default="course subject expert", help="coaching perspective")
    args = parser.parse_args()
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", args.slug):
        parser.error("slug must contain lowercase letters, digits, and internal hyphens only")
    course = ROOT / args.slug
    if course.exists():
        parser.error(f"course already exists: {course}")
    dashboard = ROOT / "learning-system" / "review-dashboard.md"
    readme = ROOT / "README.md"
    dashboard_text = dashboard.read_text(encoding="utf-8")
    readme_text = readme.read_text(encoding="utf-8")
    anchor = "\n\n## Review queue\n"
    if anchor not in dashboard_text:
        parser.error("dashboard is missing the course-list insertion anchor")

    (course / "raw").mkdir(parents=True)
    (course / "wiki").mkdir()
    (course / "raw" / ".gitkeep").touch()
    (course / "AGENTS.md").write_text(
        f"# {args.title} study coach\n\n"
        "Follow `../AGENTS.md` for ingestion, notes, context, graphs, recall, and scheduling.\n\n"
        f"Act as a rigorous {args.role} for {args.title}. Read "
        "`wiki/_course-logistics.md` before prioritizing or coaching. "
        "Preserve only verified course-specific facts there.\n",
        encoding="utf-8",
    )
    (course / "wiki" / "_course-logistics.md").write_text(
        f"# {args.title} course logistics\n\n"
        "No syllabus, assessment details, or schedule verified yet. "
        "Add only facts from supplied course materials or the user.\n",
        encoding="utf-8",
    )
    (course / "wiki" / "_course-knowledge-graph.md").write_text(
        f"# {args.title} course knowledge graph\n\n"
        "No topic notes ingested yet. Add the first Mermaid graph and node/edge tables after processing a source.\n",
        encoding="utf-8",
    )
    row = f"| {args.title} | Unconfirmed | Unconfirmed | Await course material; do not infer exam priorities. |\n"
    dashboard.write_text(dashboard_text.replace(anchor, "\n" + row + "\n## Review queue\n", 1), encoding="utf-8")
    readme.write_text(readme_text.replace("- [Game Theory](game-theory/)\n", "- [Game Theory](game-theory/)\n" + f"- [{args.title}]({args.slug}/)\n", 1), encoding="utf-8")
    print(f"Created and registered {course}")
    print("Add source files and refresh the weekly calendar when material arrives.")


if __name__ == "__main__":
    main()
