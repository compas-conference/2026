import json

input_file = "index.json"
output_file = "index.md"

with open(input_file, "r", encoding="utf-8") as f:
    submissions = json.load(f)

with open(output_file, "w", encoding="utf-8") as f:
    for sub in submissions:
        number = sub.get("pid", "???")
        title = sub.get("title", "").strip()
        abstract = sub.get("abstract", "").strip()

        # Process authors → extract "First Last (Affiliation)"
        authors = []
        for a in sub.get("authors", []):
            name = f"{a.get('first', '')} {a.get('last', '')}".strip()
            affiliation = a.get("affiliation", "").strip()
            if affiliation:
                authors.append(f"{name} ({affiliation})")
            else:
                authors.append(name)
        authors_md = "\n".join(f"- {author}" for author in authors)

        # Topics
        topics = sub.get("topics", [])
        topics_md = "\n".join(f"- {topic}" for topic in topics)

        # Format
        format_ = sub.get("format", "").strip()

        f.write(f"# Submission #{number}\n\n")
        f.write(f"## Titre\n\n{title}\n\n")
        f.write(f"## Résumé\n\n{abstract}\n\n")
        f.write(f"## Auteurs\n\n{authors_md}\n\n")
        f.write(f"## Sujet\n\n{topics_md}\n\n")
        f.write(f"## Type de présentation\n\n{format_}\n\n")
        f.write("---\n\n")
