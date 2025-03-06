import pynnue
pynnue.init_nnue("final.jnn")
wert = pynnue.eval_nnue("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
print("Bewertung in Centipawns:", wert)
