using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Python.Runtime;
using System.Windows;
using System.Windows.Input;
using NonInvasiveKeyboardHookLibrary;


namespace desktopapp
{
    public partial class RunWindow : Form
    {

        public RunWindow()
        {
            var kbhook = new KeyboardHookManager();
            kbhook.Start();

            InitializeComponent();
            PythonEngine.PythonHome = @"F:\anaconda3";
            PythonEngine.Initialize();
            this.TopMost = true;

            kbhook.RegisterHotkey(0x18, () =>
            {
                this.Close();
            });

        }
        private void Form1_Load(object sender, EventArgs e)
        {
        }

        /*private bool isRecording = false;
        private void Record()
        {
            MessageBox.Show("yes");

            using (Py.GIL())
            {
                MessageBox.Show("yeet");
                try
                {
                    dynamic module = Py.Import(@"..\..\..\src\microphone.py");
                }
                catch (Exception ex) 
                {
                    MessageBox.Show("error: " + ex.Message);
                }
*/
/*                dynamic module = Py.Import("..\\..\\..\\src\\microphone.py");
                dynamic recorder = module.Recorder();*/
/*                if (!isRecording)
                {
                    isRecording = true;
                    recorder.start_recording();
                    MessageBox.Show("started recording");

                }
                else
                {
                    isRecording = false;
                    recorder.stop_recording("audio.wav");
                    MessageBox.Show("stopped recording");

                }*/
     /*       }
        }*/
    }
}
