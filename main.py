import pygame

pygame.init()

WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

# Define colors
Cream = (255,253,208)
Green = (107,142,35)


# Board settings
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

def draw_board(win):
    win.fill(Cream)
    for row in range(ROWS):
        for col in range(row % 2, COLS, 2):
            pygame.draw.rect(win, Green, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))







def main():
    import pygame

    pygame.init()

    WIDTH, HEIGHT = 500, 500
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chess")

    # Define colors
    Cream = (255, 253, 208)
    Green = (107, 142, 35)

    # Board settings
    ROWS, COLS = 8, 8
    SQUARE_SIZE = WIDTH // COLS

    # Load images once outside the loop for performance
    PIECES = {
        "wp": pygame.image.load("wp.png"),
        "wr": pygame.image.load("wR.png"),
        "wn": pygame.image.load("wN.png"),
        "wb": pygame.image.load("wB.png"),
        "wq": pygame.image.load("wQ.png"),
        "wk": pygame.image.load("wK.png"),
        "bp": pygame.image.load("bp.png"),
        "br": pygame.image.load("bR.png"),
        "bn": pygame.image.load("bN.png"),
        "bb": pygame.image.load("bB.png"),
        "bq": pygame.image.load("bQ.png"),
        "bk": pygame.image.load("bK.png"),
    }

    board = [
        ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
        ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
        ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"],
    ]

    def draw_board(win):
        win.fill(Cream)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, Green, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw_pieces(win, board):
        for row in range(8):
            for col in range(8):
                piece = board[row][col]
                if piece != "--":  # If the square is not empty
                    win.blit(PIECES[piece], (col * SQUARE_SIZE, row * SQUARE_SIZE))

    def get_row_col_from_mouse(pos):
        x, y = pos
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE
        return row, col

    def main():
        run = True
        clock = pygame.time.Clock()

        selected_piece = None
        selected_pos = None

        while run:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)

                    if selected_piece:
                        # Move the piece to the new position
                        if board[row][col] == "--":  # Allow only empty square moves for now
                            board[row][col] = selected_piece
                            board[selected_pos[0]][selected_pos[1]] = "--"
                            selected_piece = None
                            selected_pos = None
                        else:
                            selected_piece = None  # Deselect if click on a non-empty square
                    else:
                        # Select a piece if there's one at the clicked square
                        if board[row][col] != "--":
                            selected_piece = board[row][col]
                            selected_pos = (row, col)

            draw_board(WIN)
            draw_pieces(WIN, board)
            pygame.display.update()

        pygame.quit()

    main()


main()
