def is_available(candidate, current_row):
  current_col = len(candidate)
  for queen_col in range(current_col):
    if candidate[queen_col]==current_row or abs(candidate[queen_col]-current_row) == current_col - queen_col:
      return False
  return True

def DFS(N, current_col, current_candidate, final_result):
  if len(current_candidate)==N:
    final_result.append(current_candidate[:])
    return

  for candidate_row in range(N):
    if is_available(current_candidate, candidate_row):
      current_candidate.append(candidate_row)
      DFS(N, current_col+1, current_candidate, final_result)
      current_candidate.pop()

def solve_n_queens(N):
  final_result = []
  DFS(N, 0, [], final_result)
  return(final_result)
print(solve_n_queens(4))