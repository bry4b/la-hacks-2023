using System;
using System.Drawing;
using System.Windows.Forms;

class OverlayForm : Form
{
    private Label titleLabel;
    private Label descriptionLabel;
    private PictureBox imageBox;

    public OverlayForm()
    {
        // Set form properties
        FormBorderStyle = FormBorderStyle.None;
        WindowState = FormWindowState.Maximized;
        TopMost = true;
        BackColor = Color.Black;
        Opacity = 0.8;

        // Create image box
        imageBox = new PictureBox();
        imageBox.Image = Image.FromFile(@"C:\path\to\your\image.jpg"); // replace with your image file path
        imageBox.SizeMode = PictureBoxSizeMode.Zoom;
        imageBox.Dock = DockStyle.Fill;
        Controls.Add(imageBox);

        // Create title label
        titleLabel = new Label();
        titleLabel.Text = "Title";
        titleLabel.Font = new Font("Arial", 48, FontStyle.Bold);
        titleLabel.ForeColor = Color.White;
        titleLabel.TextAlign = ContentAlignment.MiddleCenter;
        titleLabel.Dock = DockStyle.Top;
        Controls.Add(titleLabel);

        // Create description label
        descriptionLabel = new Label();
        descriptionLabel.Text = "Description";
        descriptionLabel.Font = new Font("Arial", 24, FontStyle.Regular);
        descriptionLabel.ForeColor = Color.White;
        descriptionLabel.TextAlign = ContentAlignment.MiddleCenter;
        descriptionLabel.Dock = DockStyle.Bottom;
        Controls.Add(descriptionLabel);
    }
}

class Program
{
    static void Main(string[] args)
    {
        Application.EnableVisualStyles();
        Application.SetCompatibleTextRenderingDefault(false);

        OverlayForm overlayForm = new OverlayForm();
        Application.Run(overlayForm);
    }
}