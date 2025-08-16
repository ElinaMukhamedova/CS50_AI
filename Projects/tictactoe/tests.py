import tictactoe


board = tictactoe.initial_state()
print(board)
print(tictactoe.player(board))
print(tictactoe.actions(board))
print(tictactoe.terminal(board))
print(tictactoe.minimax(board))