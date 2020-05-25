import wx
import logging
import os
import re
import datetime


class Window(wx.Frame):

    def check_log(self):
        log_file = 'Log.log'
        path = os.path.join(os.getcwd(), log_file)

        if os.path.exists(path) == False:
            dialog = wx.MessageDialog(self, 'Log file not found! New log will be created.', 'Check log', wx.OK)
            dialog.ShowModal()
            logging.basicConfig(file_name=log_file, level=logging.INFO)


    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(600, 400))

        self.control = wx.ListBox(self, style=wx.LB_SINGLE)
        self.statusbar = self.CreateStatusBar(2)
        self.statusbar.SetStatusWidths([-6, -4])
        self.Show(True)
        self.check_log()

        menu_file = wx.Menu()
        file_open = menu_file.Append(wx.ID_OPEN, 'Open', 'Open file')

        menu_log = wx.Menu()
        file_export = menu_log.Append(wx.ID_SAVE, 'Export', 'Export file')

        log_add = menu_log.Append(wx.ID_ADD, 'Add record to log', 'Update log')
        log_view = menu_log.Append(wx.ID_ABOUT, 'View log', 'View log file')

        menu_bar = wx.MenuBar()
        menu_bar.Append(menu_file, 'File')
        menu_bar.Append(menu_log, 'Log')

        self.SetMenuBar(menu_bar)
        self.Bind(wx.EVT_MENU, self.OnOpen, file_open)
        self.Bind(wx.EVT_MENU, self.OnExport, file_export)
        self.Bind(wx.EVT_MENU, self.AddLog, log_add)
        self.Bind(wx.EVT_MENU, self.View, log_view)


    def file_open(self, e):
        self.dir_name = " "
        open_dialog = wx.FileDialog(self, 'Choose file', self.dir_name, ' ', '*.*')
        
        if open_dialog.ShowModal() == wx.ID_OK:
            self.file_name = open_dialog.GetFilename()
            self.dir_name = open_dialog.GetDirectory()

            path = os.path.join(self.dir_name, self.file_name)
            mask = re.compile("83\d\d\d")
            
            with open(path) as file:
                date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

                self.control.Append('File ' + path + ' file processed, ' + date + ':')
                self.control.Append('')
                
                for i, line in enumerate(file):
                    for match in re.finditer(mask, line):
                        self.control.Append('String ' + str(i+1) + ', position ' + str(match.start()+1) + ' results: \'{}\''.format(line[match.start():match.end()]))

            self.control.Append('')
            self.statusbar.SetStatusText('file processed ' + path)

            size = str(os.path.getsize(path))
            size = [''.join(size[::-1][i:i+3])[::-1] for i in range(0, len(size), 3)]
            size = ' '.join(size[::-1])
            self.statusbar.SetStatusText(size + ' bytes', 1)
            
            
    def log_add(self, e):
        path = os.path.join(os.getcwd(), 'Log.log')

        with open(path, 'a') as file:
            for line in self.control.GetStrings():
                file.write(line + '\n')
                
                
    def log_view(self, e):
        dialog = wx.MessageDialog(
            self, 'Open log?', 'View log', wx.YES_NO)

        if dialog.ShowModal() == wx.ID_YES:
            self.control.Clear()
            path = os.path.join(os.getcwd(), 'Log.log')

            with open(path, 'r') as file:
                self.control.AppendItems(file.readlines())
            self.statusbar.SetStatusText('Open lof')
            self.statusbar.SetStatusText('', 1)
        else:
            dialog.Destroy()


    def file_export(self, e):
        self.dir_name = ' '
        open_dialog = wx.FileDialog(self, 'Choose file to record', self.dir_name, '', '*.*')

        if open_dialog.ShowModal() == wx.ID_OK:
            self.file_name = open_dialog.GetFilename()
            self.dir_name = open_dialog.GetDirectory()

            path = os.path.join(self.dir_name, self.file_name)

            with open(path, 'w') as file:
                for line in self.control.GetStrings():
                    file.write(line + '\n')


if __name__ == "__main__":
    application = wx.App()
    window = Window(None, 'String Search')
    application.MainLoop()