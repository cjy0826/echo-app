from collections import defaultdict
from typing import List

def dedupe_header(columns: List[str]) -> List[str]:
    seen_counts = defaultdict(int)
    result: List[str] = []

    for col in columns:
        count = seen_counts[col]
        if count == 0:
            result.append(col)
        else:
            result.append(f"{col}.{count}")
        seen_counts[col] += 1

    return result