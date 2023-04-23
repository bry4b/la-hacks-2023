using System;
using System.Drawing;
using System.Runtime.InteropServices;
using System.Windows.Forms;
using System.Diagnostics;

namespace desktopapp
{
    partial class RunWindow
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            // 
            // label
            // 
            this.label = new System.Windows.Forms.Label();
            this.SuspendLayout();
            this.label.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.label.Font = new System.Drawing.Font("Comic Sans MS", 10F);
            this.label.ForeColor = System.Drawing.Color.White;
            this.label.Size = new System.Drawing.Size(526, 40);
            this.label.Name = "label";
            this.label.Dock = DockStyle.Bottom;
            this.label.TabIndex = 0;
            this.label.Text = "speechImage is currently running! Press esc to exit.";
            this.label.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            this.Resize += (sender, e) =>
            {
                this.label.Left = this.ClientSize.Width - this.label.Width;
            };
            // 
            // RunWindow
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            // transparency
            this.BackColor = Color.Black;
            this.TransparencyKey = Color.Black;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.TopMost = true;
            this.Controls.Add(label);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Name = "RunWindow";
            this.Text = "runWindow";
            this.WindowState = System.Windows.Forms.FormWindowState.Maximized;
            this.KeyDown += new System.Windows.Forms.KeyEventHandler(this.RunWindow_KeyDown);
            this.ResumeLayout(false);
        }

        #endregion
        private void RunWindow_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Escape)
            {
                this.Close();
            }
        }
        private Label label;


    }
}