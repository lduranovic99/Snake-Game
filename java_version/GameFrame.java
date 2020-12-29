import javax.swing.JFrame;

// This class will essentially be the window that we see on the screen
public class GameFrame extends JFrame {

    public GameFrame() {

        this.add(new GamePanel());
        this.setTitle("Snake Game");
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setResizable(false);
        this.pack();
        this.setVisible(true);
        this.setLocationRelativeTo(null);

    }

}
