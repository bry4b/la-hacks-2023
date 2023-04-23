using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace desktopapp
{
    public partial class Settings : Form
    {
        public string FieldText { get; set; }

        public Settings()
        {
            InitializeComponent();
        }

        private void txtField_TextChanged(object sender, EventArgs e)
        {

        }

        private void btnSave_Click(object sender, EventArgs e)
        {
            FieldText = txtField.Text;

            // Save the contents of the text field to a file
            string path = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "settings.txt");
            File.WriteAllText(path, FieldText);

            this.DialogResult = DialogResult.OK;
            this.Close();

        }

        private void btnCancel_Click(object sender, EventArgs e)
        {

        }
    }
}
