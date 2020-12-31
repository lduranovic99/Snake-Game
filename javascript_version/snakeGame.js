// Variables for the canvas
const gameBoard = document.getElementById("gameCanvas");
const gameBoardCtx = gameBoard.getContext("2d");

// Add a key listener - or whatever that thing is called anyway
document.addEventListener("keydown", changeDirection);

// Some color variables
const colorBlack = 'black';
const colorWhite = 'white';
const colorGreen = 'green';
const colorRed = 'red';

// Variables for the game
let gameOver = false;
const unitSize = 20;

// Variables for the snake
let xSnake = [Math.round(gameBoard.width / 2)];
let ySnake = [Math.round(gameBoard.height / 2)];
let direction = "R";
let bodyParts = 1;
let xChange = 10;
let yChange = 0;

main();

function main() {
    setTimeout(function onTick() {
        if (gameOver) 
            return;
        moveSnake();
        checkCollision();
        clearScreen();
        drawSnake();
        // We can call main() again
        main();
    }, 100);
}

function clearScreen() {
    // This is setting the color of the rectangle
    gameBoardCtx.fillStyle = colorBlack;
    // Draw a rectangle across the whole screen
    gameBoardCtx.fillRect(0, 0, gameBoard.width, gameBoard.height);
}

function drawSnake() {
    for (let i = 0; i < bodyParts; i++) {
        gameBoardCtx.fillStyle = colorGreen;
        gameBoardCtx.fillRect(xSnake[i], ySnake[i], unitSize, unitSize);
    }
}

function moveSnake() {
    // Assuming that the change is already seen
    for (let i = bodyParts - 1; i > 0; i--) {
        xSnake[i] = xSnake[i-1];
        ySnake[i] = ySnake[i-1];
    }
    xSnake[0] += xChange;
    ySnake[0] += yChange;
}

function checkCollision() {
    let xHead = xSnake[0];
    let yHead = ySnake[0];
    if (xHead < 0 || xHead > gameBoard.width - unitSize || yHead < 0 || yHead > gameBoard.width - unitSize) {
        gameOver = true;
    }
}

function changeDirection() {
    const LEFT_KEY = 37;
    const RIGHT_KEY = 39;
    const UP_KEY = 38;
    const DOWN_KEY = 40;
    const keyPressed = event.keyCode;
    
    if (keyPressed == LEFT_KEY && direction !== "R") {
        direction = "L";
        xChange = -10;
        yChange = 0;
    }

    if (keyPressed == RIGHT_KEY && direction !== "L") {
        direction = "R";
        xChange = 10;
        yChange = 0;
    }

    if (keyPressed == UP_KEY && direction !== "D") {
        direction = "U";
        xChange = 0;
        yChange = -10;
    }

    if (keyPressed == DOWN_KEY && direction !== "U") {
        direction = "D";
        xChange = 0;
        yChange = 10;
    }
}
