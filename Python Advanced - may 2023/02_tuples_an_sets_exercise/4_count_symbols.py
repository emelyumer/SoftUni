symbols = input()
counted_symbols = {sym:symbols.count(sym) for sym in symbols}
for k,v in sorted(counted_symbols.items()):
    print(f"{k}:{v} time/s")