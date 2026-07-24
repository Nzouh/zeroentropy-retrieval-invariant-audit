# ZeroEntropy retrieval invariant audit

A dependency-free regression gate for synthetic retrieval results. It checks negation exclusions, multi-hop evidence coverage, duplicate IDs, and score bounds without implementing a search engine.

```bash
python audit.py example.json -o report.json
python -m unittest -v
```

The sample intentionally exits 2 because an excluded document leaked into a negated-query result. Inputs and scores are synthetic, not ZeroEntropy benchmarks.
