import random
import tkinter as tk


CELL_SIZE = 24
GRID_WIDTH = 25
GRID_HEIGHT = 20
TICK_MS = 110


class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake")
        self.root.resizable(False, False)
        self.root.configure(bg="#151922")

        self.score_label = tk.Label(
            root,
            text="Score: 0",
            font=("Segoe UI", 16, "bold"),
            fg="#f3f4f6",
            bg="#151922",
            pady=10,
        )
        self.score_label.pack()

        self.canvas = tk.Canvas(
            root,
            width=GRID_WIDTH * CELL_SIZE,
            height=GRID_HEIGHT * CELL_SIZE,
            bg="#202631",
            highlightthickness=0,
        )
        self.canvas.pack(padx=12)

        tk.Label(
            root,
            text="Arrow keys: move    Space: pause    R: restart",
            font=("Segoe UI", 10),
            fg="#aab2c0",
            bg="#151922",
            pady=10,
        ).pack()

        self.root.bind("<Up>", lambda _event: self.change_direction((0, -1)))
        self.root.bind("<Down>", lambda _event: self.change_direction((0, 1)))
        self.root.bind("<Left>", lambda _event: self.change_direction((-1, 0)))
        self.root.bind("<Right>", lambda _event: self.change_direction((1, 0)))
        self.root.bind("<space>", self.toggle_pause)
        self.root.bind("r", self.restart)
        self.root.bind("R", self.restart)

        self.restart()
        self.root.after(TICK_MS, self.update)

    def restart(self, _event=None):
        center = (GRID_WIDTH // 2, GRID_HEIGHT // 2)
        self.snake = [center, (center[0] - 1, center[1]), (center[0] - 2, center[1])]
        self.direction = (1, 0)
        self.next_direction = self.direction
        self.score = 0
        self.paused = False
        self.game_over = False
        self.food = self.place_food()
        self.draw()

    def place_food(self):
        empty_cells = [
            (x, y)
            for x in range(GRID_WIDTH)
            for y in range(GRID_HEIGHT)
            if (x, y) not in self.snake
        ]
        return random.choice(empty_cells) if empty_cells else None

    def change_direction(self, direction):
        opposite_current = (-self.direction[0], -self.direction[1])
        opposite_next = (-self.next_direction[0], -self.next_direction[1])
        if direction != opposite_current and direction != opposite_next:
            self.next_direction = direction

    def toggle_pause(self, _event=None):
        if not self.game_over:
            self.paused = not self.paused
            self.draw()

    def update(self):
        if not self.paused and not self.game_over:
            self.move()
        self.root.after(TICK_MS, self.update)

    def move(self):
        self.direction = self.next_direction
        head_x, head_y = self.snake[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)
        eating = new_head == self.food

        if (
            new_head[0] < 0
            or new_head[0] >= GRID_WIDTH
            or new_head[1] < 0
            or new_head[1] >= GRID_HEIGHT
            or new_head in (self.snake if eating else self.snake[:-1])
        ):
            self.game_over = True
            self.draw()
            return

        self.snake.insert(0, new_head)
        if eating:
            self.score += 1
            self.food = self.place_food()
            if self.food is None:
                self.game_over = True
        else:
            self.snake.pop()

        self.draw()

    def draw_cell(self, cell, color, inset=2):
        x, y = cell
        left = x * CELL_SIZE + inset
        top = y * CELL_SIZE + inset
        self.canvas.create_rectangle(
            left,
            top,
            left + CELL_SIZE - inset * 2,
            top + CELL_SIZE - inset * 2,
            fill=color,
            outline="",
        )

    def draw(self):
        self.canvas.delete("all")
        self.score_label.configure(text=f"Score: {self.score}")

        if self.food is not None:
            self.draw_cell(self.food, "#ff6b6b", inset=4)
        for index, segment in enumerate(self.snake):
            self.draw_cell(segment, "#a3e635" if index == 0 else "#65a30d")

        if self.paused or self.game_over:
            if self.game_over:
                message = "You win!" if self.food is None else "Game over"
                detail = "Press R to play again"
            else:
                message = "Paused"
                detail = "Press Space to resume"

            center_x = GRID_WIDTH * CELL_SIZE // 2
            center_y = GRID_HEIGHT * CELL_SIZE // 2
            self.canvas.create_rectangle(
                center_x - 150,
                center_y - 48,
                center_x + 150,
                center_y + 48,
                fill="#151922",
                outline="#414b5a",
            )
            self.canvas.create_text(
                center_x,
                center_y - 12,
                text=message,
                fill="#f3f4f6",
                font=("Segoe UI", 20, "bold"),
            )
            self.canvas.create_text(
                center_x,
                center_y + 20,
                text=detail,
                fill="#aab2c0",
                font=("Segoe UI", 11),
            )


def main():
    root = tk.Tk()
    SnakeGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
