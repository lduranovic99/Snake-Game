import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.Random;

// This class will hold all the action
public class GamePanel extends JPanel implements ActionListener {

    // Global constant
    static final int SCREEN_WIDTH = 600;
    static final int SCREEN_HEIGHT = 600;
    static final int UNIT_SIZE = 25;
    static final int GAME_UNITS = (SCREEN_WIDTH * SCREEN_HEIGHT) / UNIT_SIZE;
    static final int DELAY = 75;

    // Variables for the snake
    final int[] x = new int[GAME_UNITS];
    final int[] y = new int[GAME_UNITS];
    int bodyParts = 6;
    char direction = 'R';

    // Variables for the apple
    int applesEaten = 0;
    int appleX;
    int appleY;

    // Gameplay variables
    boolean running = false;
    Timer timer;
    Random random;

    public GamePanel() {
        random = new Random();
        this.setPreferredSize(new Dimension(SCREEN_WIDTH, SCREEN_HEIGHT));
        this.setBackground(Color.BLACK);
        this.setFocusable(true);
        this.addKeyListener(new MyKeyAdapter());
        startGame();
    }

    public void startGame() {

        // Adjust the initial position of the snake
        x[0] = 7 * UNIT_SIZE;
        y[0] = 5 * UNIT_SIZE;
        for (int i = 1; i < bodyParts; i++) {
            x[i] = x[i-1] - 1;
            y[i] = y[i-1];
        }

        newApple();
        running = true;
        timer = new Timer(DELAY, this);
        timer.start();
    }

    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        draw(g);
    }

    public void draw(Graphics g) {
        if (running) {

            // Draw the apple
            g.setColor(Color.RED);
            g.fillOval(appleX, appleY, UNIT_SIZE, UNIT_SIZE);
            
            // Draw the snake
            for (int i = 0; i < bodyParts; i++) {
                if (i == 0) {
                    g.setColor(Color.GREEN);
                    g.fillRect(x[i], y[i], UNIT_SIZE, UNIT_SIZE);
                } else {
                    int first, second, third;
                    first = random.nextInt(255);
                    second = random.nextInt(255);
                    third = random.nextInt(255);
                    g.setColor(new Color(first, second, third));
                    g.fillRect(x[i], y[i], UNIT_SIZE, UNIT_SIZE);
                }
            }

            // Score
            g.setColor(Color.RED);
            g.setFont( new Font("Ink Free", Font.PLAIN, 40 ) );
            FontMetrics metrics = getFontMetrics(g.getFont());
            g.drawString("Score: " + applesEaten, (SCREEN_WIDTH - metrics.stringWidth("Score: " + applesEaten))/2, g.getFont().getSize());

        } else {
            gameOver(g);
        }
    }

    public void newApple() {
        // Generate coordinates for the apple
        appleX = random.nextInt((int) (SCREEN_WIDTH / UNIT_SIZE)) * UNIT_SIZE;
        appleY = random.nextInt((int) (SCREEN_HEIGHT / UNIT_SIZE)) * UNIT_SIZE;
    }

    public void move() {
        for (int i = bodyParts; i > 0; i--) {
            x[i] = x[i-1];
            y[i] = y[i-1];
        }
        switch (direction) {
            case 'U':
                y[0] -= UNIT_SIZE;
                break;
            case 'D':
                y[0] += UNIT_SIZE;
                break;
            case 'L':
                x[0] -= UNIT_SIZE;
                break;
            case 'R':
                x[0] += UNIT_SIZE;
                break;
        }
    }

    public void checkApple() {
        if (x[0] == appleX && y[0] == appleY) {
            bodyParts++;
            applesEaten++;
            newApple();
        }
    }

    public void checkCollisions() {
        // Check if the snake has a collision with itself
        for (int i = bodyParts; i > 0; i --) {
            if (x[0] == x[i] && y[0] == y[i]) {
                running = false;
            }
        }

        // Handle the left border
        if (x[0] < 0) {
            running = false;
        }

        // Handle the right border
        if (x[0] > SCREEN_WIDTH - UNIT_SIZE) {
            running = false;
        }

        // Handle the upper border
        if (y[0] < 0) {
            running = false;
        }

        // Handle the lower border
        if (y[0] > SCREEN_HEIGHT - UNIT_SIZE) {
            running = false;
        }

        if (!running) {
            timer.stop();
        }
    }

    public void gameOver(Graphics g) {
        
        // Display Game Over
        g.setColor(Color.RED);
        g.setFont( new Font("MONOSPACED", Font.BOLD, 75) );
        FontMetrics metrics1 = getFontMetrics(g.getFont());
        g.drawString("Game Over", (SCREEN_WIDTH - metrics1.stringWidth("Game Over"))/2, SCREEN_HEIGHT / 2);

        // Score
        g.setColor(Color.RED);
        g.setFont( new Font("Ink Free", Font.PLAIN, 40 ) );
        FontMetrics metrics2 = getFontMetrics(g.getFont());
        g.drawString("Score: " + applesEaten, (SCREEN_WIDTH - metrics2.stringWidth("Score: " + applesEaten))/2, g.getFont().getSize());

    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (running) {
            move();
            checkApple();
            checkCollisions();
        }
        repaint();
    }

    public class MyKeyAdapter extends KeyAdapter {
        @Override
        public void keyPressed(KeyEvent e) {
            switch(e.getKeyCode()) {
                case KeyEvent.VK_LEFT:
                    if (direction != 'R') {
                        direction = 'L';
                    }
                    break;
                case KeyEvent.VK_RIGHT:
                    if (direction != 'L') {
                        direction = 'R';
                    }
                    break;
                case KeyEvent.VK_UP:
                    if (direction != 'D') {
                        direction = 'U';
                    }
                    break;
                case KeyEvent.VK_DOWN:
                    if (direction != 'U') {
                        direction = 'D';
                    }
                    break;
            }
        }
    }

}
