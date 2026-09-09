import sys
import json
from client import SIMDVectorEngine

simd = SIMDVectorEngine()

def handle_call(name, arguments):
    if name == "fma":
        a = arguments["a"]
        b = arguments["b"]
        c = arguments["c"]
        mask = arguments.get("mask")
        res = simd.fma(a, b, c, mask)
        return {"result": res, "horizontal_sum": simd.horizontal_add(res)}
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_call(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"id": req.get("id"), "result": res}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
