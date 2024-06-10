namespace DB_GUI
{
    partial class DBGUI
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
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
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            Terminal = new Panel();
            Options = new Panel();
            Signature = new Panel();
            Datagrid = new Panel();
            SuspendLayout();
            // 
            // Terminal
            // 
            Terminal.BackColor = Color.Transparent;
            Terminal.Location = new Point(4, 420);
            Terminal.Name = "Terminal";
            Terminal.Size = new Size(623, 140);
            Terminal.TabIndex = 0;
            // 
            // Options
            // 
            Options.BackColor = Color.Transparent;
            Options.Location = new Point(631, 93);
            Options.Name = "Options";
            Options.Size = new Size(213, 323);
            Options.TabIndex = 1;
            // 
            // Signature
            // 
            Signature.BackColor = Color.Transparent;
            Signature.Location = new Point(631, 420);
            Signature.Name = "Signature";
            Signature.Size = new Size(213, 140);
            Signature.TabIndex = 2;
            // 
            // Datagrid
            // 
            Datagrid.BackColor = Color.Transparent;
            Datagrid.Location = new Point(1, 93);
            Datagrid.Name = "Datagrid";
            Datagrid.Size = new Size(626, 323);
            Datagrid.TabIndex = 3;
            // 
            // DBGUI
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            BackgroundImage = Properties.Resources.DB_Frontend_Concept;
            BackgroundImageLayout = ImageLayout.Zoom;
            ClientSize = new Size(844, 561);
            Controls.Add(Datagrid);
            Controls.Add(Signature);
            Controls.Add(Options);
            Controls.Add(Terminal);
            FormBorderStyle = FormBorderStyle.FixedDialog;
            Name = "DBGUI";
            Text = "Database Query Application";
            TopMost = true;
            Load += DB_Load;
            ResumeLayout(false);
        }

        #endregion

        private Panel Terminal;
        private Panel Options;
        private Panel Signature;
        private Panel Datagrid;
    }
}
