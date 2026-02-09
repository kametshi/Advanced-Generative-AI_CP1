from rag import retrieve

q = "How often should engine oil be replaced?"
hits = retrieve(q, top_k=3)

for h in hits:
    print("----")
    print("SOURCE:", h["source"], "PAGE:", h["page"], "DIST:", h["distance"])
    print(h["text"][:300])
