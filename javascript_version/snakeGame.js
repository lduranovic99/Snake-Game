// Variables for the canvas
const snakeboard = document.getElementById("gameCanvas");
const snakeboard_ctx = snakeboard.getContext("2d");

// Variables for the game
let game_over = false;

// Variables for the snake
let x_snake = [Math.round(snakeboard.width / 2)];
let y_snake = [Math.round(snakeboard.height / 2)];
let direction = "R";
let x_change = 0;
let y_change = 0;

