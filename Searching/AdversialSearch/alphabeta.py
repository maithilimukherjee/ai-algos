import math

# Minimax with Alpha-Beta Pruning
def alpha_beta(node, depth, alpha, beta, maximizing_player, get_children, evaluate):
    """
    node: current state
    depth: maximum depth to search
    alpha: best value that maximizer can guarantee
    beta: best value that minimizer can guarantee
    maximizing_player: True if it's maximizer's turn, False otherwise
    get_children: function to generate child states
    evaluate: function to evaluate leaf nodes
    """
    # Base case: depth reached or terminal node
    if depth == 0 or not get_children(node):
        return evaluate(node)

    if maximizing_player:
        value = -math.inf
        for child in get_children(node):
            value = max(value, alpha_beta(child, depth-1, alpha, beta, False, get_children, evaluate))
            alpha = max(alpha, value)
            if alpha >= beta:
                break  # Beta cut-off
        return value
    else:
        value = math.inf
        for child in get_children(node):
            value = min(value, alpha_beta(child, depth-1, alpha, beta, True, get_children, evaluate))
            beta = min(beta, value)
            if beta <= alpha:
                break  # Alpha cut-off
        return value
