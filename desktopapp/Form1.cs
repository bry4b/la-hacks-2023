using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace desktopapp
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void Form1_Load_1(object sender, EventArgs e)
        {

        }

        private void buttonSettings_Click(object sender, EventArgs e)
        {
            Settings settings = new Settings();
            settings.ShowDialog();
        }
        private void buttonStart_Click(object sender, EventArgs e)
        {
            // Hide the current form
            this.Hide();

            // Show the runWindow form
            RunWindow runWindow = new RunWindow();
            runWindow.ShowDialog();

            // Show the current form again when the runWindow form is closed
            this.Show();
        }
    }
}
