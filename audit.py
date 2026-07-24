import argparse, json, sys

def audit(data):
    findings=[]
    for case in data["cases"]:
        ids=[r["id"] for r in case["results"]]
        if len(ids)!=len(set(ids)): findings.append({"case":case["id"],"code":"DUPLICATE_RESULT"})
        excluded=set(case.get("exclude_ids",[]))
        leaked=sorted(excluded & set(ids))
        if leaked: findings.append({"case":case["id"],"code":"NEGATION_LEAK","items":leaked})
        required=set(case.get("required_evidence_ids",[]))
        missing=sorted(required-set(ids))
        if missing: findings.append({"case":case["id"],"code":"MISSING_HOP_EVIDENCE","items":missing})
        if any(r["score"]<0 or r["score"]>1 for r in case["results"]):
            findings.append({"case":case["id"],"code":"INVALID_SCORE"})
    return {"verdict":"review" if findings else "ready","findings":findings}

def main():
    p=argparse.ArgumentParser(); p.add_argument("input"); p.add_argument("-o","--output",default="report.json"); a=p.parse_args()
    r=audit(json.load(open(a.input,encoding="utf-8")))
    json.dump(r,open(a.output,"w",encoding="utf-8"),indent=2); print(json.dumps(r,indent=2))
    return 2 if r["findings"] else 0
if __name__=="__main__": sys.exit(main())
