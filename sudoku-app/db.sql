DROP TABLE IF EXISTS sudoku_pattern;

CREATE TABLE sudoku_pattern (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  pattern VARCHAR(90) UNIQUE NOT NULL
);

INSERT INTO sudoku_pattern(pattern) values("4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......");
INSERT INTO sudoku_pattern(pattern) values("..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..");
INSERT INTO sudoku_pattern(pattern) values("2...8.3...6..7..84.3.5..2.9...1.54.8.........4.27.6...3.1..7.4.72..4..6...4.1...3");

