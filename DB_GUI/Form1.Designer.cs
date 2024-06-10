namespace DB_GUI
{
    partial class GUI_Main
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
            Datagrid = new Panel();
            MainGrid = new DataGridView();
            Options = new Panel();
            Terminal = new Panel();
            Credits = new Panel();
            Datagrid.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)MainGrid).BeginInit();
            SuspendLayout();
            // 
            // Datagrid
            // 
            Datagrid.Controls.Add(MainGrid);
            Datagrid.Location = new Point(2, 93);
            Datagrid.Name = "Datagrid";
            Datagrid.Size = new Size(623, 323);
            Datagrid.TabIndex = 0;
            // 
            // MainGrid
            // 
            MainGrid.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            MainGrid.Dock = DockStyle.Fill;
            MainGrid.Location = new Point(0, 0);
            MainGrid.Name = "MainGrid";
            MainGrid.Size = new Size(623, 323);
            MainGrid.TabIndex = 0;
            // 
            // Options
            // 
            Options.BackColor = Color.Transparent;
            Options.Location = new Point(631, 93);
            Options.Name = "Options";
            Options.Size = new Size(213, 323);
            Options.TabIndex = 1;
            // 
            // Terminal
            // 
            Terminal.BackColor = Color.Transparent;
            Terminal.Location = new Point(2, 421);
            Terminal.Name = "Terminal";
            Terminal.Size = new Size(623, 135);
            Terminal.TabIndex = 2;
            // 
            // Credits
            // 
            Credits.BackColor = Color.Transparent;
            Credits.Location = new Point(631, 421);
            Credits.Name = "Credits";
            Credits.Size = new Size(213, 140);
            Credits.TabIndex = 3;
            // 
            // GUI_Main
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            BackgroundImage = Properties.Resources.DB_Frontend_Concept;
            BackgroundImageLayout = ImageLayout.Zoom;
            ClientSize = new Size(844, 561);
            Controls.Add(Credits);
            Controls.Add(Terminal);
            Controls.Add(Options);
            Controls.Add(Datagrid);
            FormBorderStyle = FormBorderStyle.FixedDialog;
            Name = "GUI_Main";
            Text = "Database Query Application";
            Datagrid.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)MainGrid).EndInit();
            ResumeLayout(false);
        }

        #endregion

        private Panel Datagrid;
        private DataGridView MainGrid;
        private Panel Options;
        private Panel Terminal;
        private Panel Credits;
    }
}
