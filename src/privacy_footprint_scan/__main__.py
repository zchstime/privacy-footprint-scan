import argparse, re
from collections import Counter, defaultdict
from pathlib import Path

PATTERNS={"email":re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b",re.I),"phone":re.compile(r"(?<!\d)\+?\d[\d ()-]{7,}\d(?!\d)"),"ipv4":re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b"),"api-token":re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9_-]{20,})\b"),"private-key":re.compile(r"BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY")}
TEXT={".txt",".md",".json",".jsonl",".csv",".log",".py",".js",".ts",".html",".xml",".yaml",".yml",".toml",".env"}
def scan(root):
 root=Path(root); totals=Counter(); files=[]; skipped=0
 for p in root.rglob("*"):
  if not p.is_file() or p.is_symlink(): continue
  if p.suffix.lower() not in TEXT and p.name!=".env": skipped+=1; continue
  if p.stat().st_size>1_000_000: skipped+=1; continue
  text=p.read_text(errors="replace"); counts={name:len(rx.findall(text)) for name,rx in PATTERNS.items()}; counts={k:v for k,v in counts.items() if v}
  if counts: files.append({"path":str(p),"counts":counts}); totals.update(counts)
 return {"totals":dict(totals),"files":files,"skipped":skipped}
def markdown(x):
 out=["# Privacy Footprint",f"\nFiles with findings: **{len(x['files'])}** · skipped: **{x['skipped']}**\n","## Totals"]+[f"- {k}: {v}" for k,v in sorted(x["totals"].items())]+["","## Files (values intentionally hidden)"]+[f"- `{f['path']}` — "+", ".join(f"{k}: {v}" for k,v in f["counts"].items()) for f in x["files"]]
 return "\n".join(out)+"\n"
def main(argv=None):
 p=argparse.ArgumentParser(description="Inventory personal-data hints without printing values"); p.add_argument("root"); p.add_argument("--output","-o")
 a=p.parse_args(argv); text=markdown(scan(a.root)); Path(a.output).write_text(text) if a.output else print(text)
if __name__=="__main__": main()
