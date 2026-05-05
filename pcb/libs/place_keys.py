import json, pcbnew
board = pcbnew.GetBoard()
with open(r'F:\OneDrive\Desktop\Ghoost Board\libs\keyboard-layout.json') as f:
    kle = json.load(f)
switches = sorted([fp for fp in board.GetFootprints() if fp.GetReference().startswith('SW')], key=lambda f: int(f.GetReference()[2:]))
sw_idx = 0
y = 30.0
x_origin = 30.0
for row in kle:
    x = x_origin
    for key in row:
        if isinstance(key, dict):
            if 'w' in key: current_w = key['w']
            else: current_w = 1.0
        else:
            if sw_idx < len(switches):
                cx = x + (current_w * 19.05) / 2
                switches[sw_idx].SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(cx), pcbnew.FromMM(y)))
                x += current_w * 19.05
                sw_idx += 1
                current_w = 1.0
    y += 19.05
board.Save(board.GetFileName())
pcbnew.Refresh()
print("Placed", sw_idx, "switches")