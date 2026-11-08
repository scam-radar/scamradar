import hashlib, sys, pathlib
def canon_hash(path: str) -> str:
    raw = pathlib.Path(path).read_bytes().decode("utf-8-sig", errors="replace")
    norm = raw.replace("\r\n", "\n").replace("\r", "\n").strip()
    return hashlib.sha256(norm.encode("utf-8")).hexdigest()
if __name__ == "__main__":
    p = sys.argv[1] if len(sys.argv) > 1 else "scam_radar.py"
    print(canon_hash(p))
